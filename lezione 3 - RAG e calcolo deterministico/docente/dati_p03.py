"""Diari della P03 (gennaio-giugno 2026): conversione, versione Excel e calcoli di riferimento.

I diari originali dello zip `backup/fonti/Diari_pressa_gennaio_giugno_2026.zip` riportano la
macchina come «P-01»: qui diventano «P03» senza toccare impaginazione e dati.

Uso per il docente (stampa i valori di riferimento della guida, gli stessi che il generatore
inserisce in GUIDA_DOCENTE al posto dei segnaposto {{nome}}):
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
ALARM_GUIDE = HERE / 'backup' / 'fonti' / '02_GUIDA_ALLARMI_P03.md'
FIRST_QUARTER = ('Gennaio', 'Febbraio', 'Marzo')
SUMMED = ('giornate', 'ore', 'pezzi_teorici', 'fault', 'fermo_min', 'fermo_min_fino_ripristino', 'pezzi_persi')
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


def machine_parts(path: Path = ALARM_GUIDE) -> dict[str, str]:
    """Tipo di allarme -> parte della macchina, dalla tabella del paragrafo 2 della guida IO-P03-07."""
    section = re.search(r'^## 2\..*?\n(.*?)^## ', path.read_text(encoding='utf-8'), re.M | re.S).group(1)
    rows = [line.strip().strip('|').split('|') for line in section.splitlines() if line.startswith('|')]
    parts = {}
    for part, alarms in rows[2:]:
        for alarm in alarms.split('·'):
            parts[alarm.strip()] = part.strip()
    if not parts:
        raise RuntimeError(f'{path.name}: tabella delle parti della macchina non trovata')
    return parts


def it_number(value: float, decimals: int = 0) -> str:
    """Numero all'italiana: punto per le migliaia, virgola per i decimali."""
    return f'{value:,.{decimals}f}'.replace(',', ' ').replace('.', ',').replace(' ', '.')


def slug(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', text.lower()).strip('_')


def md_table(header: list[str], rows: list[list[str]]) -> str:
    lines = [header, ['---'] * len(header), *rows]
    return '\n'.join('| ' + ' | '.join(row) + ' |' for row in lines)


def reference_values(months: list[Month]) -> dict[str, str]:
    """Valori di riferimento della guida docente, già formattati: tabelle Markdown e numeri citati nel testo.

    Si ferma se un riepilogo stampato non torna con i dati o se un tipo di fault manca nella guida agli allarmi.
    """
    monthly = [(month, indicators(month)) for month in months]
    problems = [problem for month, values in monthly for problem in check_summary(month, values)]
    if problems:
        raise RuntimeError('Riepiloghi dei diari non coerenti: ' + '; '.join(problems))
    if tuple(month.name for month in months[:3]) != FIRST_QUARTER:
        raise RuntimeError('Mesi non in ordine da gennaio a giugno')
    parts = machine_parts()
    totals = {key: sum(values[key] for _, values in monthly) for key in SUMMED}
    by_type: dict[str, list] = defaultdict(lambda: [0, 0.0, 0.0])
    by_part: dict[str, list] = defaultdict(lambda: [0, 0.0, 0.0, 0, 0])
    for month, values in monthly:
        for fault in values['dettaglio_fault']:
            if fault['tipo'] not in parts:
                raise RuntimeError(f"Tipo di fault assente dalla guida IO-P03-07: {fault['tipo']}")
            for entry in (by_type[fault['tipo']], by_part[parts[fault['tipo']]]):
                entry[0] += 1
                entry[1] += fault['minuti_fino_avvio']
                entry[2] += fault['pezzi_persi']
            by_part[parts[fault['tipo']]][3 if month.name in FIRST_QUARTER else 4] += 1

    def summary_row(label: str, v: dict) -> list[str]:
        return [label, str(v['giornate']), it_number(v['ore'], 1), it_number(v['pezzi_teorici']), str(v['fault']),
                it_number(v['fermo_min']), it_number(v['pezzi_persi'])]

    values = {
        'tabella_riepiloghi': md_table(
            ['Mese', 'Giornate', 'Ore di produzione', 'Pezzi teorici', 'Fault', 'Fermo per fault (min)', 'Pezzi teorici persi'],
            [summary_row(month.name, v) for month, v in monthly] + [[f'**{cell}**' for cell in summary_row('Totale', totals)]]),
        'righe_eventi': it_number(sum(len(month.events) for month in months)),
        'fault_totali': str(totals['fault']),
        'fermo_totale': it_number(totals['fermo_min']),
        'fermo_totale_ripristino': it_number(totals['fermo_min_fino_ripristino']),
        'fermo_ripristino_mesi': ', '.join(it_number(v['fermo_min_fino_ripristino']) for _, v in monthly),
        'fault_mese_min': str(min(v['fault'] for _, v in monthly)),
        'fault_mese_max': str(max(v['fault'] for _, v in monthly)),
    }
    ranked_types = sorted(by_type.items(), key=lambda item: -item[1][1])
    values['tabella_tipi'] = md_table(
        ['Tipo di fault', 'N.', 'Minuti di fermo', 'Pezzi teorici persi'],
        [[name, str(n), it_number(minutes), it_number(lost)] for name, (n, minutes, lost) in ranked_types])
    for place, (name, (n, minutes, lost)) in enumerate(ranked_types, start=1):
        key = slug(name)
        values.update({f'n_{key}': str(n), f'min_{key}': it_number(minutes), f'persi_{key}': it_number(lost), f'posto_min_{key}': str(place)})
    ranked_parts = sorted(by_part.items(), key=lambda item: -item[1][1])
    values['tabella_parti'] = md_table(
        ['Parte della macchina', 'N.', 'Minuti di fermo', 'Pezzi teorici persi', 'Fault gennaio–marzo', 'Fault aprile–giugno'],
        [[name, str(n), it_number(minutes), it_number(lost), str(q1), str(q2)] for name, (n, minutes, lost, q1, q2) in ranked_parts])
    for name, (n, minutes, lost, q1, q2) in ranked_parts:
        key = slug(name)
        values.update({f'n_{key}': str(n), f'trim1_{key}': str(q1), f'trim2_{key}': str(q2)})
    return values


def fill(text: str, values: dict[str, str]) -> str:
    """Sostituisce i segnaposto {{nome}}; un nome sconosciuto ferma la generazione."""
    def value(match: re.Match) -> str:
        if match.group(1) not in values:
            raise KeyError(f'Segnaposto senza valore: {match.group(0)}')
        return values[match.group(1)]
    return re.sub(r'\{\{(\w+)\}\}', value, text)


def report(months: list[Month]) -> str:
    values = reference_values(months)
    tables = [values[key] for key in ('tabella_riepiloghi', 'tabella_tipi', 'tabella_parti')]
    inline = [f'{key}: {value}' for key, value in values.items() if not key.startswith('tabella_')]
    return '\n\n'.join(tables + ['\n'.join(inline), 'Controllo dei riepiloghi stampati: tutti coerenti'])


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
