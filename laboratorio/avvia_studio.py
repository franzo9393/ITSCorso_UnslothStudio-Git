"""Avvia Studio con recupero dei passaggi: nessuna installazione o configurazione globale."""

import argparse
import os
import shutil
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8888)
    parser.add_argument("--models-dir", type=Path, help="Cartella GGUF già popolata dal docente")
    parser.add_argument("--offline", action="store_true", help="Disabilita accessi Hub/Transformers; risorse già in cache")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port deve essere compresa fra 1 e 65535")
    executable = shutil.which("unsloth")
    if not executable:
        parser.exit(1, "Unsloth non disponibile nel PATH: completare la Golden Image prima della lezione.\n")
    command = [executable, "studio", "-p", str(args.port)]
    if args.models_dir:
        directory = args.models_dir.expanduser().resolve()
        if not directory.is_dir():
            parser.error("--models-dir deve indicare una cartella già esistente")
        command.extend(["--models-dir", str(directory)])
    environment = os.environ.copy()
    # Controllo upstream dipendente dalla release: il docente deve osservare il recupero effettivo.
    environment["RAG_THREAD_WHOLE_DOC"] = "0"
    if args.offline:
        environment["HF_HUB_OFFLINE"] = "1"
        environment["TRANSFORMERS_OFFLINE"] = "1"
    print(f"Studio locale: http://localhost:{args.port}", flush=True)
    print("RAG_THREAD_WHOLE_DOC=0 nel solo processo avviato; tool RAG non disabilitati.", flush=True)
    print("Controllare passaggi recuperati: la variabile non certifica il comportamento di ogni release.", flush=True)
    if args.offline:
        print("Modalità Hub/Transformers offline. Non è un firewall: disattivare web search e provider remoti.", flush=True)
    try:
        return subprocess.call(command, env=environment)
    except OSError as exc:
        parser.exit(1, f"Avvio non riuscito: {exc}\n")
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
