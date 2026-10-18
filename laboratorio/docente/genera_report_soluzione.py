"""Soluzione docente: aggiunge un filtro di lettura senza cambiare gli esiti registrati."""

import argparse
import csv
import sys
from pathlib import Path

# Eseguire dal kit completo: riusa lo stesso lettore CSV e gli stessi criteri del report base.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "starter"))
from genera_report import load_results, render_report


FILTER = """<section aria-label="Filtro di lettura" class="riepilogo">
<label><input type="checkbox" id="solo-da-rivedere"> Solo da rivedere</label>
<p id="visibili" aria-live="polite"></p>
</section>
<main id="casi">"""
SCRIPT = """<script>
const filtro = document.getElementById('solo-da-rivedere');
const casi = [...document.querySelectorAll('.caso')];
function aggiornaFiltro() {
  let visibili = 0;
  for (const caso of casi) {
    caso.hidden = filtro.checked && caso.dataset.daRivedere !== 'true';
    if (!caso.hidden) visibili++;
  }
  document.getElementById('visibili').textContent = `${visibili} di ${casi.length} casi visibili. Il riepilogo comprende sempre tutti i casi.`;
}
filtro.addEventListener('change', aggiornaFiltro);
aggiornaFiltro();
</script>
</body>"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("risultati.csv"))
    parser.add_argument("--output", type=Path, default=Path("report.html"))
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve():
        parser.exit(1, "Input e output devono essere file diversi.\n")
    try:
        document = render_report(load_results(args.input))
        # Due punti d'inserimento del template base; nessuna interpretazione dei contenuti del CSV.
        if document.count('<main id="casi">') != 1 or document.count("</body>") != 1:
            raise ValueError("Template base cambiato: aggiornare i due punti d'inserimento della soluzione.")
        document = document.replace('<main id="casi">', FILTER, 1).replace("</body>", SCRIPT, 1)
        args.output.write_text(document, encoding="utf-8")
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        parser.exit(1, f"Report non generato: {exc}\n")
    print(f"Report con filtro generato: {args.output.resolve()}")


if __name__ == "__main__":
    main()
