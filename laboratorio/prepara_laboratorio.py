"""Copia soltanto il materiale studente in una cartella nuova; nessuna installazione."""

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
STARTER_FILES = ("genera_report.py", "risultati.csv")


def prepare(destination):
    destination = destination.expanduser().resolve()
    if destination.exists():
        raise ValueError(f"La destinazione esiste già: {destination}. Scegli una cartella nuova.")
    for name in STARTER_FILES:
        if not (ROOT / "starter" / name).is_file():
            raise ValueError(f"Starter incompleto: manca {name}.")
    corpus = sorted((ROOT / "corpus").glob("*.md"))
    if len(corpus) != 5:
        raise ValueError("Il corpus iniziale deve contenere i cinque documenti didattici.")
    destination.mkdir(parents=True)
    try:
        for name in STARTER_FILES:
            shutil.copyfile(ROOT / "starter" / name, destination / name)
        (destination / "corpus").mkdir()
        for source in corpus:
            shutil.copyfile(source, destination / "corpus" / source.name)
    except OSError:
        shutil.rmtree(destination)
        raise
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", required=True, type=Path, help="Cartella personale non ancora esistente")
    args = parser.parse_args()
    try:
        destination = prepare(args.dest)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Preparazione non riuscita: {exc}\n")
    print(f"Materiale studente copiato in: {destination}")
    print("Nessuna soluzione docente copiata; nessuna configurazione Git modificata.")
    print("Studio e modello devono essere pronti prima di B1; segui la dispensa.")
    print("Git si introduce in B5 sui risultati e sul corpus, con identità locale.")
    print("Il report iniziale si genera con: python genera_report.py")


if __name__ == "__main__":
    main()
