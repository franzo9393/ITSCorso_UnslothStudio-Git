"""Genera un report HTML offline da una valutazione umana, non giudica le risposte AI."""

import argparse
import csv
from collections import Counter
from html import escape
from pathlib import Path


FIELDS = [
    "id", "domanda", "documenti_recuperati", "risposta", "citazioni",
    "esito_recupero", "esito_risposta", "note",
]
STATUSES = ("OK", "ERRORE", "NON_ESEGUITO")
REQUIRED_IDS = {f"T{number:02d}" for number in range(1, 7)}


def load_results(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream, delimiter=";")
        if reader.fieldnames != FIELDS:
            raise ValueError("Intestazione CSV non valida: " + ";".join(FIELDS))
        rows = []
        seen = set()
        for number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Riga {number}: numero di colonne errato; quota i testi con ; o a capo.")
            row = {key: value.strip() for key, value in row.items()}
            case_id = row["id"]
            if not case_id or case_id in seen:
                raise ValueError(f"Riga {number}: ID vuoto o duplicato.")
            if not row["domanda"]:
                raise ValueError(f"Riga {number}: domanda mancante.")
            for key in ("esito_recupero", "esito_risposta"):
                if row[key] not in STATUSES:
                    raise ValueError(f"Riga {number}: {key} deve essere OK, ERRORE o NON_ESEGUITO.")
            if row["esito_risposta"] == "OK" and not row["risposta"]:
                raise ValueError(f"Riga {number}: non segnare OK una risposta non registrata.")
            seen.add(case_id)
            rows.append(row)
        missing = REQUIRED_IDS - seen
        if missing:
            raise ValueError("Mancano casi obbligatori: " + ", ".join(sorted(missing)))
    return rows


def render_report(rows):
    retrieval = Counter(row["esito_recupero"] for row in rows)
    answers = Counter(row["esito_risposta"] for row in rows)
    summary = "".join(
        f"<tr><th scope='row'>{status}</th><td>{retrieval[status]}</td><td>{answers[status]}</td></tr>"
        for status in STATUSES
    )
    cases = []
    for row in rows:
        needs_review = row["esito_recupero"] != "OK" or row["esito_risposta"] != "OK"
        details = "".join(
            f"<dt>{label}</dt><dd>{escape(row[key]) if row[key] else 'Non registrato'}</dd>"
            for key, label in (
                ("documenti_recuperati", "Documenti e passaggi recuperati"),
                ("risposta", "Risposta osservata"), ("citazioni", "Citazioni da controllare"),
                ("note", "Note del collaudatore"),
            )
        )
        cases.append(
            f"<article class='caso' data-da-rivedere='{str(needs_review).lower()}'>"
            f"<h2>{escape(row['id'])}: {escape(row['domanda'])}</h2>"
            f"<p><strong>Recupero:</strong> {row['esito_recupero']} · "
            f"<strong>Risposta:</strong> {row['esito_risposta']}</p><dl>{details}</dl></article>"
        )
    untouched = all(row["esito_risposta"] == "NON_ESEGUITO" for row in rows)
    notice = (
        "Prove non eseguite: questo report non contiene risultati di un modello."
        if untouched else "Esiti assegnati dal collaudatore: il programma non verifica automaticamente le risposte."
    )
    return """<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Collaudo RAG — Officina Scuola</title>
<style>
body { max-width: 64rem; margin: 2rem auto; padding: 0 1rem; font: 1rem/1.55 system-ui, sans-serif; color: #172033; background: #f5f7fb; }
header, article, .riepilogo { background: white; border: 1px solid #aab8cb; padding: 1.2rem; margin-bottom: 1rem; border-radius: .5rem; }
h1 { font-size: 1.8rem; } h2 { font-size: 1.15rem; }
.avviso { padding: .8rem; border-left: .3rem solid #805b00; background: #fff8df; }
table { border-collapse: collapse; width: 100%; } th, td { border: 1px solid #aab8cb; padding: .5rem; text-align: left; }
dt { font-weight: bold; } dd { margin: 0 0 .8rem; white-space: pre-wrap; overflow-wrap: anywhere; }
button { min-height: 44px; padding: .6rem; cursor: pointer; }
@media print { body { background: white; margin: 0; } article { break-inside: avoid; } button { display: none; } }
</style></head><body>
<header><h1>Collaudo RAG — Officina Scuola</h1>
<p>Documenti sintetici, nessun uso operativo su macchinari. Recupero e generazione sono valutati separatamente.</p>
<p class="avviso">""" + notice + """</p></header>
<section class="riepilogo" aria-labelledby="riepilogo"><h2 id="riepilogo">Valutazione umana</h2>
<table><thead><tr><th>Esito</th><th>Recupero</th><th>Risposta</th></tr></thead><tbody>""" + summary + """</tbody></table>
<p>OK non significa certificazione: controllare identificativo macchina, revisione e sostegno effettivo delle citazioni. T05 richiede il riconoscimento del dato assente.</p></section>
<main id="casi">""" + "".join(cases) + """</main>
<footer><p>Fonte: risultati.csv compilato dal gruppo. Le righe NON_ESEGUITO non sono prove superate.</p></footer>
</body></html>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("risultati.csv"))
    parser.add_argument("--output", type=Path, default=Path("report.html"))
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.exit(1, "Input e output devono essere file diversi.\n")
    try:
        rows = load_results(args.input)
        document = render_report(rows)
        args.output.write_text(document, encoding="utf-8")
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        parser.exit(1, f"Report non generato: {exc}\n")
    print(f"Report generato: {args.output.resolve()}")
    print("Esiti umani, nessuna chiamata AI o rete. Apri il file nel browser.")


if __name__ == "__main__":
    main()
