"""Registra prerequisiti CLI e impronte del corpus, senza avviare o scaricare modelli."""

import argparse
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ANSI = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")


def invoke(name, arguments):
    executable = shutil.which(name)
    if not executable:
        return {"ok": False, "errore": f"{name} non disponibile nel PATH"}
    try:
        result = subprocess.run(
            [executable, *arguments], capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "errore": str(exc)}
    text = ANSI.sub("", result.stdout + result.stderr).strip()
    return {"ok": result.returncode == 0, "output": text}


def inspect_environment():
    versions = {name: invoke(name, ["--version"]) for name in ("git", "unsloth", "opencode")}
    contracts = {}
    checks = (
        ("studio", ["studio", "--help"], ("--port", "--models-dir")),
        ("run", ["run", "--help"], ("--host", "--disable-tools")),
        ("opencode", ["start", "opencode", "--help"], ()),
    )
    for name, args, flags in checks:
        check = invoke("unsloth", args)
        missing = [flag for flag in flags if flag not in check.get("output", "")]
        contracts[name] = {"ok": check["ok"] and not missing, "flag_mancanti": missing}
        if not check["ok"]:
            contracts[name]["errore"] = check.get("errore", check.get("output", ""))
    corpus = sorted((ROOT / "corpus").glob("*.md"))
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in corpus}
    cli_ok = (
        sys.version_info >= (3, 10)
        and len(corpus) == 5
        and all(value["ok"] for value in versions.values())
        and all(value["ok"] for value in contracts.values())
    )
    return {
        "data_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "piattaforma": platform.platform(),
        "versioni_cli": versions, "contratti_cli": contracts, "corpus_sha256": hashes,
        "prerequisiti_cli_ok": cli_ok,
        "verifica": "CLI_E_CORPUS_SOLTANTO",
        "collaudi_manuali_obbligatori": [
            "Registrare modello/quantizzazione, revisioni e impostazioni effettivamente usati.",
            "Verificare embedding multilingue, tokenizer e runtime già presenti offline.",
            "Indicizzare solo corpus/ in una knowledge base e osservare il recupero dei passaggi.",
            "Eseguire le sei domande e verificare fonti e astensione con la griglia docente.",
            "Provare avvio senza rete e carico concorrente sull'infrastruttura dell'aula.",
            "Provare creazione e modifica di un file tramite OpenCode, non soltanto testo in chat.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("ambiente.json"))
    args = parser.parse_args()
    if args.output.exists():
        parser.exit(1, "Il manifesto esiste già: usa un nuovo --output per conservare il precedente.\n")
    report = inspect_environment()
    try:
        with args.output.open("x", encoding="utf-8") as stream:
            json.dump(report, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
    except OSError as exc:
        parser.exit(1, f"Impossibile salvare il manifesto: {exc}\n")
    print(f"Manifesto salvato in: {args.output.resolve()}")
    print("Prerequisiti CLI: " + ("OK" if report["prerequisiti_cli_ok"] else "NON COMPLETI"))
    print("Non certifica inferenza, RAG, offline o capacità dell'aula: seguire SOLUZIONI.md.")
    return 0 if report["prerequisiti_cli_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
