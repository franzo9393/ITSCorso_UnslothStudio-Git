"""Misura Unsloth Studio nella VM: memoria, tempi di risposta e indicizzazione dei documenti.

Uso (nella VM, dopo aver installato Unsloth Studio e scaricato il modello):
    python misura_vm.py --modello unsloth/Qwen3.5-2B-GGUF --variante UD-Q4_K_XL --rag

Avvia `unsloth studio run` su una porta separata, invia tre richieste fisse, facoltativamente
indicizza il corpus del laboratorio e salva tutto in un file JSON. Non addestra modelli.
Funziona su Windows e Linux; richiede `psutil` (già presente nell'ambiente di Unsloth Studio).
"""

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

import psutil

CORPUS_PREDEFINITO = Path(__file__).resolve().parents[4] / "laboratorio" / "corpus"
ISTRUZIONI = ("Sei l'assistente di reparto della pressa P03. Rispondi in italiano, in modo breve. "
              "Usa solo i documenti forniti. Se un dato non c'è, scrivi 'dato assente'.")
MB = 2**20


def esegui(comando):
    try:
        r = subprocess.run(comando, capture_output=True, text=True, timeout=60,
                           encoding="utf-8", errors="replace")
        return (r.stdout + r.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as exc:
        return f"non disponibile: {exc}"


def nome_processore():
    if sys.platform.startswith("linux"):
        for riga in Path("/proc/cpuinfo").read_text().splitlines():
            if riga.startswith("model name"):
                return riga.split(":", 1)[1].strip()
    if sys.platform == "win32":
        return esegui(["powershell", "-NoProfile", "-Command",
                       "(Get-CimInstance Win32_Processor).Name"])
    return platform.processor()


def sistema():
    memoria = psutil.virtual_memory()
    disco = shutil.disk_usage(Path.home())
    nvidia = shutil.which("nvidia-smi")
    return {
        "sistema_operativo": platform.platform(),
        "processore": nome_processore(),
        "processori_logici": psutil.cpu_count(),
        "ram_totale_mb": round(memoria.total / MB),
        "ram_disponibile_mb": round(memoria.available / MB),
        "disco_libero_gb": round(disco.free / 2**30, 1),
        "nvidia_smi": esegui([nvidia, "-L"]) if nvidia else "assente",
        "unsloth": esegui(["unsloth", "--version"]),
    }


class Memoria:
    """Campiona ogni 0,25 s la RAM del sistema e quella dei processi di Studio."""

    def __init__(self, radice):
        self.radice = radice

    def processi(self):
        try:
            return [self.radice, *self.radice.children(recursive=True)]
        except psutil.Error:
            return []

    def studio_mb(self):
        totale = 0
        for p in self.processi():
            try:
                totale += p.memory_info().rss
            except psutil.Error:
                pass
        return round(totale / MB)

    def adesso(self):
        m = psutil.virtual_memory()
        return {"studio_mb": self.studio_mb(), "sistema_usata_mb": round((m.total - m.available) / MB),
                "sistema_disponibile_mb": round(m.available / MB)}

    def dettaglio(self):
        """Memoria di ogni processo di Studio: server Python, llama-server per il modello, ecc."""
        voci = []
        for p in self.processi():
            try:
                voci.append({"processo": p.name(), "mb": round(p.memory_info().rss / MB),
                             "comando": " ".join(p.cmdline()[1:4])[:120]})
            except psutil.Error:
                pass
        return sorted(voci, key=lambda v: -v["mb"])[:6]

    def __enter__(self):
        self.fine, self.picco_studio, self.minimo_disponibile = False, 0, 10**12

        def ciclo():
            while not self.fine:
                stato = self.adesso()
                self.picco_studio = max(self.picco_studio, stato["studio_mb"])
                self.minimo_disponibile = min(self.minimo_disponibile, stato["sistema_disponibile_mb"])
                time.sleep(0.25)

        self.filo = threading.Thread(target=ciclo, daemon=True)
        self.filo.start()
        return self

    def __exit__(self, *_):
        self.fine = True
        self.filo.join()

    def picchi(self):
        return {"picco_studio_mb": self.picco_studio, "minimo_disponibile_mb": self.minimo_disponibile}


class Studio:
    def __init__(self, args):
        self.base = f"http://127.0.0.1:{args.porta}"
        self.chiave = None
        self.righe = []
        ambiente = os.environ.copy()
        ambiente["RAG_THREAD_WHOLE_DOC"] = "0"
        ambiente["PYTHONIOENCODING"] = "utf-8"
        if args.offline:
            ambiente["HF_HUB_OFFLINE"] = "1"
            ambiente["TRANSFORMERS_OFFLINE"] = "1"
        comando = ["unsloth", "studio", "run", "--model", args.modello, "--api-only",
                   "--port", str(args.porta), "--disable-tools", "--parallel", "1"]
        if args.variante:
            comando += ["--gguf-variant", args.variante]
        if args.contesto:
            comando += ["--context-length", str(args.contesto)]
        eseguibile = shutil.which("unsloth")
        if not eseguibile:
            sys.exit("Comando unsloth non trovato: installare Unsloth Studio nella VM.")
        comando[0] = eseguibile
        self.inizio = time.time()
        self.proc = subprocess.Popen(comando, env=ambiente, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                                     errors="replace")
        self.radice = psutil.Process(self.proc.pid)
        threading.Thread(target=self._leggi, daemon=True).start()

    def _leggi(self):
        for riga in self.proc.stdout:
            self.righe.append(riga.rstrip())
            trovata = re.search(r"API Key:\s+(\S+)", riga)
            if trovata:
                self.chiave = trovata.group(1)

    def attendi(self, limite_s):
        while self.chiave is None:
            if self.proc.poll() is not None:
                raise RuntimeError("Studio si è chiuso durante il caricamento:\n" + "\n".join(self.righe[-30:]))
            if time.time() - self.inizio > limite_s:
                raise RuntimeError("Caricamento oltre il limite di tempo:\n" + "\n".join(self.righe[-30:]))
            time.sleep(0.5)
        return round(time.time() - self.inizio, 1)

    def richiesta(self, metodo, percorso, corpo=None, grezzo=None, intestazioni=None):
        h = {"Authorization": f"Bearer {self.chiave}", **(intestazioni or {})}
        dati = grezzo
        if corpo is not None:
            dati = json.dumps(corpo).encode()
            h["Content-Type"] = "application/json"
        req = urllib.request.Request(self.base + percorso, data=dati, headers=h, method=metodo)
        with urllib.request.urlopen(req, timeout=3600) as r:
            return json.loads(r.read() or b"{}")

    def chiudi(self):
        for p in reversed(self.radice.children(recursive=True) if self.proc.poll() is None else []):
            try:
                p.terminate()
            except psutil.Error:
                pass
        self.proc.terminate()
        try:
            self.proc.wait(30)
        except subprocess.TimeoutExpired:
            self.proc.kill()


def prove_chat(studio, corpus):
    documenti = {p.name: p.read_text(encoding="utf-8") for p in sorted(corpus.glob("*.md"))}
    tutti = "\n\n".join(documenti.values())
    scheda = documenti.get("01_scheda_P03.md", "") + "\n\n" + documenti.get("02_rapporto_fermo_P03.md", "")
    return [
        ("risposta_breve", None,
         "Spiega in tre frasi che cos'è un fermo macchina in un reparto di stampaggio."),
        ("estrazione_due_documenti", ISTRUZIONI,
         f"Documenti:\n{scheda}\n\nEstrai in una tabella: macchina, data, ora di inizio e fine del fermo, "
         "durata, causa, ricambio usato."),
        ("cinque_documenti", ISTRUZIONI,
         f"Documenti:\n{tutti}\n\nQuale codice ricambio serve per la P03 e quanti pezzi sono arrivati "
         "con la bolla? Indica la fonte."),
    ]


def indicizza(studio, corpus, memoria, registra):
    kb = studio.richiesta("POST", "/api/rag/knowledge-bases", {"name": f"prova-vm-{uuid.uuid4().hex[:6]}"})
    prima = memoria.adesso()
    nomi_prima = {p.pid for p in memoria.processi()}
    with Memoria(studio.radice) as picco:
        inizio = time.time()
        lavori = []
        for f in sorted(corpus.glob("*.md")):
            confine = uuid.uuid4().hex
            grezzo = (f"--{confine}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{f.name}\"\r\n"
                      "Content-Type: text/markdown\r\n\r\n").encode() + f.read_bytes() + f"\r\n--{confine}--\r\n".encode()
            lavori.append(studio.richiesta("POST", f"/api/rag/knowledge-bases/{kb['id']}/documents", grezzo=grezzo,
                                           intestazioni={"Content-Type": f"multipart/form-data; boundary={confine}"}))
        esiti = []
        for lavoro in lavori:
            while True:
                stato = studio.richiesta("GET", f"/api/rag/jobs/{lavoro['jobId']}")
                if stato["status"] in ("completed", "failed", "cancelled"):
                    esiti.append({"file": lavoro["filename"], "stato": stato["status"],
                                  "blocchi": stato["numChunks"], "errore": stato["error"]})
                    break
                time.sleep(1)
        durata = round(time.time() - inizio, 1)
    nuovi = []
    for p in memoria.processi():
        if p.pid not in nomi_prima:
            try:
                nuovi.append(" ".join(p.cmdline())[:200])
            except psutil.Error:
                pass
    registra(prova="indicizzazione_corpus", secondi=durata, documenti=esiti, prima=prima,
             dopo=memoria.adesso(), processi_nuovi=nuovi, **picco.picchi())
    for modo in ("lexical", "hybrid"):
        with Memoria(studio.radice) as picco:
            inizio = time.time()
            try:
                risultato = studio.richiesta("POST", "/api/rag/search", {
                    "query": "codice ricambio P03 bolla di consegna", "kb_id": kb["id"], "top_k": 2, "mode": modo})
            except urllib.error.HTTPError as exc:
                risultato = {"errore": f"HTTP {exc.code}", "dettaglio": exc.read().decode(errors="replace")[:300]}
        registra(prova=f"ricerca_{modo}", secondi=round(time.time() - inizio, 2),
                 risultato=json.dumps(risultato, ensure_ascii=False)[:800], **picco.picchi())
    studio.richiesta("DELETE", f"/api/rag/knowledge-bases/{kb['id']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--modello", required=True, help="Repository Hugging Face o percorso del file GGUF")
    parser.add_argument("--variante", help="Variante GGUF, per esempio UD-Q4_K_XL")
    parser.add_argument("--contesto", type=int, default=8192, help="Lunghezza del contesto in token (0 = predefinita)")
    parser.add_argument("--porta", type=int, default=8899)
    parser.add_argument("--rag", action="store_true", help="Indicizza anche il corpus del laboratorio")
    parser.add_argument("--offline", action="store_true", help="Nessun accesso a Hugging Face: modello già scaricato")
    parser.add_argument("--corpus", type=Path, default=CORPUS_PREDEFINITO)
    parser.add_argument("--uscita", type=Path, help="File JSON dei risultati")
    parser.add_argument("--etichetta", default=platform.node())
    args = parser.parse_args()
    if args.rag and not args.corpus.is_dir():
        parser.error(f"Cartella del corpus non trovata: {args.corpus}")
    uscita = args.uscita or Path(f"misure_{args.etichetta}_{time.strftime('%Y%m%d_%H%M%S')}.json")
    if uscita.exists():
        parser.error(f"Il file {uscita} esiste già: indicare un nuovo --uscita.")

    risultati = {"etichetta": args.etichetta, "data": time.strftime("%Y-%m-%d %H:%M:%S"),
                 "modello": args.modello, "variante": args.variante, "contesto": args.contesto,
                 "sistema": sistema(), "prove": []}

    def registra(**voce):
        risultati["prove"].append(voce)
        print(json.dumps(voce, ensure_ascii=False)[:700], flush=True)

    ram_prima = psutil.virtual_memory()
    risultati["ram_disponibile_prima_mb"] = round(ram_prima.available / MB)
    studio = Studio(args)
    memoria = Memoria(studio.radice)
    try:
        with Memoria(studio.radice) as picco:
            caricamento = studio.attendi(limite_s=1800)
        hardware = [r for r in studio.righe if "Hardware detected" in r or "GPU" in r][:5]
        time.sleep(5)
        registra(prova="caricamento", secondi=caricamento, hardware=hardware, processi=memoria.dettaglio(),
                 **memoria.adesso(), **picco.picchi())
        for nome, istruzioni, testo in prove_chat(studio, args.corpus):
            messaggi = ([{"role": "system", "content": istruzioni}] if istruzioni else []) + \
                       [{"role": "user", "content": testo}]
            corpo = {"messages": messaggi, "max_tokens": 400, "temperature": 0.2, "stream": False,
                     "enable_thinking": False}
            with Memoria(studio.radice) as picco:
                inizio = time.time()
                r = studio.richiesta("POST", "/v1/chat/completions", corpo)
                durata = round(time.time() - inizio, 1)
            uso, tempi = r.get("usage", {}), r.get("timings", {})
            messaggio = r["choices"][0]["message"]
            registra(prova=nome, secondi=durata, token_richiesta=uso.get("prompt_tokens"),
                     token_risposta=uso.get("completion_tokens"),
                     token_risposta_al_secondo=round((uso.get("completion_tokens") or 0) / durata, 1),
                     lettura_token_s=tempi.get("prompt_per_second"),
                     scrittura_token_s=tempi.get("predicted_per_second"),
                     ragionamento_presente=bool(messaggio.get("reasoning_content")),
                     risposta=messaggio.get("content"), **picco.picchi())
        if args.rag:
            indicizza(studio, args.corpus, memoria, registra)
    except (RuntimeError, urllib.error.URLError, KeyError) as exc:
        registra(prova="errore", messaggio=str(exc)[:3000])
    finally:
        studio.chiudi()
        uscita.write_text(json.dumps(risultati, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Risultati salvati in {uscita.resolve()}")


if __name__ == "__main__":
    main()
