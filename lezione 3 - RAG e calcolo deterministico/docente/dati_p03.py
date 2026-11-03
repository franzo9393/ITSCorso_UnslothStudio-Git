"""Diari della P03 (gennaio-giugno 2026): conversione, versione Excel e calcoli di riferimento.

I diari originali dello zip `backup/fonti/Diari_pressa_gennaio_giugno_2026.zip` riportano la
macchina come «P-01»: qui diventano «P03» senza toccare impaginazione e dati.

Uso per il docente (stampa i valori di riferimento della guida):
    python dati_p03.py
"""
from __future__ import annotations

import io
import math
import re
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE_ZIP = HERE / 'backup' / 'fonti' / 'Diari_pressa_gennaio_giugno_2026.zip'
MACHINE_OLD, MACHINE = 'P-01', 'P03'
EVENT_COLUMNS = ('Data / ora', 'Evento', 'Pz/ora', 'Dettaglio evento')
STOP_EVENTS = ('ARRESTO', 'FAULT')


@dataclass(frozen=True)
class Event:
    when: datetime
    kind: str
    rate: int | None
    detail: str


@dataclass
class Month:
    name: str
    title: str
    subtitle: str
    summary: dict[str, str]
    note: str
    events: list[Event]


def diary_name(source_name: str) -> str:
    """`Diario_pressa_01_Gennaio_2026.docx` -> `Diario_P03_01_Gennaio_2026.docx`."""
    return source_name.replace('Diario_pressa_', f'Diario_{MACHINE}_')


def convert_diaries(target: Path) -> list[Path]:
    """Scrive i sei diari Word con la macchina P03, conservando ogni altra parte del file."""
    target.mkdir(parents=True, exist_ok=True)
    written = []
    with zipfile.ZipFile(SOURCE_ZIP) as archive:
        for name in sorted(archive.namelist()):
            source = zipfile.ZipFile(io.BytesIO(archive.read(name)))
            month = re.search(r'_\d\d_(\w+)_2026', name).group(1)
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as out:
                for item in source.infolist():
                    data = source.read(item.filename)
                    if item.filename.endswith('.xml'):
                        text = data.decode('utf-8').replace(MACHINE_OLD, MACHINE)
                        if item.filename == 'docProps/core.xml':
                            text = re.sub(r'<dc:title\s*/>|<dc:title>[^<]*</dc:title>', '', text)
                            text = text.replace('</cp:coreProperties>', f'<dc:title>Diario di produzione {MACHINE} · {month} 2026</dc:title></cp:coreProperties>')
                            text = re.sub(r'<dc:description>[^<]*</dc:description>', '', text)
                        data = text.encode('utf-8')
                    out.writestr(item, data)
            path = target / diary_name(name)
            path.write_bytes(buffer.getvalue())
            if MACHINE_OLD.encode() in path.read_bytes():
                raise RuntimeError(f'{path.name}: resta un riferimento a {MACHINE_OLD}')
            written.append(path)
    if len(written) != 6:
        raise RuntimeError(f'Attesi 6 diari, trovati {len(written)}')
    return written


def read_month(path: Path) -> Month:
    from docx import Document

    doc = Document(path)
    lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    title, subtitle, summary_line, note = lines[0], lines[1], lines[2], lines[3]
    summary = dict(re.findall(r'([A-Za-zà ]+?):\s*([\d.,]+(?: h| min)?)', summary_line))
    summary = {key.strip(): value for key, value in summary.items()}
    table = doc.tables[0]
    header = tuple(cell.text.strip() for cell in table.rows[0].cells)
    if header != EVENT_COLUMNS:
        raise ValueError(f'{path.name}: intestazione inattesa {header}')
    events = []
    for row in table.rows[1:]:
        when, kind, rate, detail = (cell.text.strip() for cell in row.cells)
        events.append(Event(datetime.strptime(when, '%d/%m/%Y %H:%M'), kind, None if rate == '—' else int(rate), detail))
    name = re.search(r'\| (\w+) 2026', title).group(1)
    return Month(name, title, subtitle, summary, note, events)


def read_months(folder: Path) -> list[Month]:
    paths = sorted(folder.glob(f'Diario_{MACHINE}_*_2026.docx'))
    if len(paths) != 6:
        raise RuntimeError(f'Attesi 6 diari P03 in {folder}, trovati {len(paths)}')
    return [read_month(path) for path in paths]


def fault_type(event: Event) -> str:
    return event.detail.split(';')[0].strip()


def indicators(month: Month) -> dict:
    """Applica le regole del documento «Regole di calcolo degli indicatori della P03»."""
    events = month.events
    hours = pieces = 0.0
    running: Event | None = None
    faults = []
    for index, event in enumerate(events):
        if event.kind == 'AVVIO':
            running = event
        elif event.kind in STOP_EVENTS and running is not None:
            span = (event.when - running.when).total_seconds() / 3600
            hours += span
            pieces += span * running.rate
            running = None
        if event.kind == 'FAULT':
            restart = next(e for e in events[index + 1:] if e.kind == 'AVVIO')
            reset = next(e for e in events[index + 1:] if e.kind == 'RIPRISTINO')
            active = next(e for e in reversed(events[:index]) if e.kind == 'AVVIO')
            minutes = (restart.when - event.when).total_seconds() / 60
            faults.append({
                'quando': event.when,
                'tipo': fault_type(event),
                'minuti_fino_avvio': minutes,
                'minuti_fino_ripristino': (reset.when - event.when).total_seconds() / 60,
                'cadenza': active.rate,
                'pezzi_persi': minutes * active.rate / 60,
            })
    days = {event.when.date() for event in events if event.kind == 'AVVIO'}
    return {
        'giornate': len(days),
        'ore': hours,
        'pezzi_teorici': pieces,
        'fault': len(faults),
        'fermo_min': sum(f['minuti_fino_avvio'] for f in faults),
        'fermo_min_fino_ripristino': sum(f['minuti_fino_ripristino'] for f in faults),
        'pezzi_persi': sum(f['pezzi_persi'] for f in faults),
        'dettaglio_fault': faults,
    }


def check_summary(month: Month, values: dict) -> list[str]:
    """Confronta i calcoli con il riepilogo stampato in testa al diario."""
    expected = {
        'Giornate lavorative': (values['giornate'], lambda v: int(v)),
        'Ore di produzione': (round(values['ore'], 1), lambda v: float(v.replace(' h', ''))),
        'Pezzi teorici': (round(values['pezzi_teorici']), lambda v: int(v.replace('.', ''))),
        'Fault': (values['fault'], lambda v: int(v)),
        'Fermo per fault': (round(values['fermo_min']), lambda v: int(v.replace(' min', ''))),
    }
    problems = []
    for key, (computed, parse) in expected.items():
        printed = parse(month.summary[key])
        if printed != computed:
            problems.append(f'{month.name} · {key}: stampato {printed}, calcolato {computed}')
    return problems


def write_workbook(months: list[Month], target: Path) -> Path:
    """Una cartella Excel con un foglio per mese, impaginata come il diario Word."""
    import xlsxwriter

    target.parent.mkdir(parents=True, exist_ok=True)
    book = xlsxwriter.Workbook(target)
    book.set_properties({'title': f'Diari di produzione {MACHINE} · gennaio-giugno 2026', 'author': 'ITS MAKER Bologna', 'comments': 'Dati simulati per l\'esercitazione'})
    bold = book.add_format({'bold': True})
    title_format = book.add_format({'bold': True, 'font_size': 14, 'font_color': '#1064A0'})
    head = book.add_format({'bold': True, 'bg_color': '#EAF0F6', 'border': 1})
    stamp = book.add_format({'num_format': 'dd/mm/yyyy hh:mm', 'border': 1})
    cell = book.add_format({'border': 1})
    for month in months:
        sheet = book.add_worksheet(month.name)
        sheet.write(0, 0, month.title, title_format)
        sheet.write(1, 0, month.subtitle)
        row = 3
        for key, value in month.summary.items():
            sheet.write(row, 0, key, bold)
            sheet.write(row, 1, value)
            row += 1
        sheet.write(row, 0, month.note)
        row += 2
        for col, name in enumerate(EVENT_COLUMNS):
            sheet.write(row, col, name, head)
        for event in month.events:
            row += 1
            sheet.write_datetime(row, 0, event.when, stamp)
            sheet.write(row, 1, event.kind, cell)
            if event.rate is None:
                sheet.write(row, 2, '—', cell)
            else:
                sheet.write_number(row, 2, event.rate, cell)
            sheet.write(row, 3, event.detail, cell)
        sheet.set_column(0, 0, 21)
        sheet.set_column(1, 1, 18)
        sheet.set_column(2, 2, 9)
        sheet.set_column(3, 3, 95)
    book.close()
    return target


def report(months: list[Month]) -> str:
    lines = ['Mese | Giornate | Ore | Pezzi teorici | Fault | Fermo (fino ad AVVIO) | Fermo (fino a RIPRISTINO) | Pezzi teorici persi']
    by_type: dict[str, list] = defaultdict(lambda: [0, 0.0, 0.0, []])
    totals = defaultdict(float)
    problems = []
    for month in months:
        values = indicators(month)
        problems += check_summary(month, values)
        lines.append(f"{month.name} | {values['giornate']} | {values['ore']:.1f} | {values['pezzi_teorici']:.0f} | {values['fault']} | {values['fermo_min']:.0f} | {values['fermo_min_fino_ripristino']:.0f} | {values['pezzi_persi']:.0f}")
        for key in ('giornate', 'ore', 'pezzi_teorici', 'fault', 'fermo_min', 'fermo_min_fino_ripristino', 'pezzi_persi'):
            totals[key] += values[key]
        for fault in values['dettaglio_fault']:
            entry = by_type[fault['tipo']]
            entry[0] += 1
            entry[1] += fault['minuti_fino_avvio']
            entry[2] += fault['pezzi_persi']
            entry[3].append(month.name[:3])
    lines.append(f"Totale | {totals['giornate']:.0f} | {totals['ore']:.1f} | {totals['pezzi_teorici']:.0f} | {totals['fault']:.0f} | {totals['fermo_min']:.0f} | {totals['fermo_min_fino_ripristino']:.0f} | {totals['pezzi_persi']:.0f}")
    lines += ['', 'Tipo di fault | N. | Minuti di fermo | Pezzi teorici persi | Mesi']
    for name, (count, minutes, lost, when) in sorted(by_type.items(), key=lambda item: -item[1][1]):
        lines.append(f'{name} | {count} | {minutes:.0f} | {lost:.0f} | {", ".join(when)}')
    lines += ['', 'Controllo dei riepiloghi stampati: ' + ('tutti coerenti' if not problems else '; '.join(problems))]
    return '\n'.join(lines)


if __name__ == '__main__':
    import sys
    import tempfile

    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if folder is None:
        with tempfile.TemporaryDirectory() as temp:
            convert_diaries(Path(temp))
            print(report(read_months(Path(temp))))
    else:
        print(report(read_months(folder)))
