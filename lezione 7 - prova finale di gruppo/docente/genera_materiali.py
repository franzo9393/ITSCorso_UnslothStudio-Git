"""Genera i materiali della lezione 7 (prova finale di gruppo).

Uso:
    python genera_materiali.py

Prima parte, i cinque casi: legge i moduli `casi/caso_*.py` (dati inventati,
controlli di coerenza e valori calcolati dagli eventi), controlla lunghezze e
ordine, e scrive:
- `studenti/casi/<caso>/` con registro, regole, guida e i tre numeri in testo
  semplice, da stampare o incollare in Copilot;
- `docente/da_consegnare_a_parte/<caso>/Riservato_<caso>.txt` per i casi con un testo
  riservato a sé, da consegnare a parte (le vecchie cartelle
  `studenti/casi/<caso>/da_consegnare_a_parte` vengono rimosse);
- `docente/backup/VALORI_DI_RIFERIMENTO_CASI.md`, riservato al docente.

Seconda parte, i documenti, dai sorgenti Markdown (se un sorgente manca lo
segnala e prosegue con gli altri):
- `docente/backup/SLIDE_LEZIONE7.md` -> PowerPoint nella cartella della lezione
  (dal modello ufficiale `MODELLO_ITS_MAKER.pptx`), HTML e PDF in `docente/backup/`;
- `studenti/backup/ATTIVITA_LEZIONE7.md` -> `studenti/ATTIVITA_LEZIONE7.docx`;
- `studenti/backup/FOGLIO_DEL_GRUPPO.md` e `studenti/backup/FOGLIO_DEL_COLLAUDO.md` ->
  `studenti/FOGLIO_DEL_GRUPPO.docx` e `studenti/FOGLIO_DEL_COLLAUDO.docx` (da stampare);
- `docente/backup/TEST_LEZIONE7.md` -> `studenti/da_pubblicare_alla_fine/TEST_LEZIONE7.docx`,
  PDF in `docente/backup/` (i vecchi `studenti/TEST_LEZIONE7.docx` e
  `studenti/backup/TEST_LEZIONE7.md/.pdf`, se esistono, vengono rimossi);
- `docente/backup/GUIDA_DOCENTE.md` -> `docente/GUIDA_DOCENTE.docx`, con i segnaposto
  `{{TRE_NUMERI_<caso>}}` e `{{VALORI_<caso>}}` sostituiti dai valori calcolati;
- i PDF dei Word in `studenti/backup/` e in `docente/backup/`.

Nelle slide di sezione il numero segue l'ordine (01, 02, ...); si può forzarlo con
`<!-- section: 3 -->` nel corpo della slide.

Richiede i pacchetti Markdown, python-docx, python-pptx, Pillow, PyMuPDF, lxml e
LibreOffice (solo per chi rigenera i materiali; gli studenti non installano nulla).
Non legge file di altre lezioni: il modello PowerPoint è `MODELLO_ITS_MAKER.pptx`,
accanto a questo file.
"""
from __future__ import annotations

import argparse
import base64
import copy
import html
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from functools import lru_cache
from pathlib import Path

import markdown
import pymupdf
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_ROW_HEIGHT_RULE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches as DocInches
from docx.shared import Pt as DocPt
from docx.shared import RGBColor as DocColor
from lxml import html as lxml_html
from PIL import Image, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
LESSON = HERE.parent
CASES_DIR = HERE / 'casi'
STUDENTS = LESSON / 'studenti'
STUDENTS_CASES = STUDENTS / 'casi'
RESERVED_DIR = HERE / 'da_consegnare_a_parte'
STUDENTS_BACKUP = STUDENTS / 'backup'
TEACHER_BACKUP = HERE / 'backup'
REFERENCE = TEACHER_BACKUP / 'VALORI_DI_RIFERIMENTO_CASI.md'

# Copilot riceve in un solo messaggio orchestratore e tre testi: limiti in caratteri.
LIMITS = {'registro': 6500, 'regole': 2800, 'guida': 2800}
ORDER = ('sicurezza', 'manutenzione', 'stampanti', 'prenotazioni', 'attrezzi')
# Casi in cui il dato riservato è un testo a sé e si consegna ai gruppi a parte;
# negli altri tre casi il dato riservato è il registro stesso.
RESERVED_WITH_DATA = {'sicurezza', 'prenotazioni'}
# I tre numeri che ogni gruppo ricava a mano dal registro stampato prima di aprire Copilot:
# (domanda per gli studenti, voce di valori() con la risposta, solo per la guida docente).
TRE_NUMERI = {
    'sicurezza': [
        ('Quante segnalazioni hanno la priorità immediata?', 'Segnalazioni per priorità'),
        ('Quante segnalazioni, secondo le regole, aspettano il riepilogo del venerdì?', 'Inoltrate e in attesa del riepilogo'),
        ('Quante volte è stato segnalato il trapano a colonna?', 'Oggetto segnalato più volte'),
    ],
    'manutenzione': [
        ('Quanti interventi risultano scaduti il 2 dicembre 2026?', 'Stati degli interventi'),
        ('Quale intervento di quale macchina scade proprio il 2 dicembre 2026?', 'Scade oggi'),
        ('Quante volte è stato fatto lo scarico della condensa?', 'Scarichi della condensa'),
    ],
    'stampanti': [
        ('Quanti minuti in tutto sono state fuori uso le stampanti?', 'Minuti fuori uso'),
        ('Quante stampe sono fallite?', 'Stampe fallite'),
        ('Quanti grammi di filo sono andati persi?', 'Filo perso'),
    ],
    'prenotazioni': [
        ('Quante prenotazioni sono attive?', 'Prenotazioni attive'),
        ('Quante fasce sono occupate su 30?', 'Fasce occupate e libere'),
        ('Quale laboratorio ha più prenotazioni attive, e quante?', 'Prenotazioni attive per laboratorio'),
    ],
    'attrezzi': [
        ('Quanti attrezzi sono in prestito oggi?', 'Prestiti aperti oggi'),
        ('Quanti prestiti aperti sono in ritardo?', 'Prestiti aperti in ritardo'),
        ('Per il multimetro 9, qual è la data prevista di rientro dopo la proroga?', 'Prestito con proroga'),
    ],
}
MONTHS = ('gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto',
          'settembre', 'ottobre', 'novembre', 'dicembre')

# Documenti da Markdown.
SLIDES_SOURCE = TEACHER_BACKUP / 'SLIDE_LEZIONE7.md'
DECK_NAME = 'Lezione7_Prova_finale_di_gruppo_ITS_MAKER'
DECK_DIR = LESSON  # il PowerPoint sta nella cartella della lezione; HTML e PDF in docente/backup/
MODEL = HERE / 'MODELLO_ITS_MAKER.pptx'
TITLE = 'Lezione 7 — Prova finale di gruppo'
SUBJECT = 'Prova finale di gruppo: un agente in Microsoft Copilot'
FOOTER = 'ITS MAKER Bologna · Lezione 7 · '
LAYOUTS = ('COPERTINA', 'CONTENUTO', 'SEZIONE', 'CHIUSURA')
PROGRAM = ('UNSLOTH STUDIO', 'COPILOT')  # il modello riporta ancora il programma della lezione 1: si sostituisce al caricamento
BLUE, INK, MUTED, PALE = '1064A0', '17344D', '4B6275', 'EAF0F6'
FONT = 'Arial'
BODY_SIZE, BODY_GAP = 26, 0.16  # punti e pollici: testo delle slide di contenuto e spazio fra i paragrafi
FONT_FILES: dict[bool, str] = {}


def load(slug: str):
    path = CASES_DIR / f'caso_{slug}.py'
    if not path.exists():
        raise SystemExit(f'Manca {path.name}')
    spec = importlib.util.spec_from_file_location(f'caso_{slug}', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def italian_date(iso: str) -> str:
    day = date.fromisoformat(iso)
    return f'{day.day:02d}/{day.month:02d}/{day.year}'


def registro_testo(case) -> str:
    parts = [case.INTESTAZIONE.strip(), '']
    for event in case.EVENTI:
        parts.append(f"{italian_date(event['data'])} · {event['ora']}")
        parts.append('')
        parts.append(event['testo'].strip())
        parts.append('')
    return '\n'.join(parts).rstrip() + '\n'


def check_case(case) -> list[str]:
    errors = [f'controlli(): {e}' for e in case.controlli()]
    keys = [(e['data'], e['ora']) for e in case.EVENTI]
    if keys != sorted(keys):
        errors.append('eventi non in ordine di data e ora')
    if len(case.EVENTI) < 18:
        errors.append(f'eventi: {len(case.EVENTI)}, ne servono almeno 18')
    if len(case.LAVORI) != 3:
        errors.append('i lavori devono essere tre')
    if sum(1 for l in case.LAVORI if l.get('dipende_da')) < 1:
        errors.append('nessun lavoro dichiara una dipendenza')
    texts = {'registro': registro_testo(case), 'regole': case.REGOLE, 'guida': case.GUIDA}
    for name, text in texts.items():
        if len(text) > LIMITS[name]:
            errors.append(f'{name}: {len(text)} caratteri, limite {LIMITS[name]}')
    missing = case.INFORMAZIONE_ASSENTE.strip().lower()
    if missing and any(missing in t.lower() for t in texts.values()):
        errors.append('INFORMAZIONE_ASSENTE compare tra i testi per gli studenti')
    if len(case.valori()) < 6:
        errors.append('valori(): servono almeno 6 voci')
    for _, key in TRE_NUMERI[case.SLUG]:
        if key not in case.valori():
            errors.append(f'TRE_NUMERI: manca in valori() la voce «{key}»')
    return errors


def write_students(case) -> None:
    folder = STUDENTS_CASES / case.SLUG
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f'Registro_{case.SLUG}.txt').write_text(registro_testo(case), encoding='utf-8')
    (folder / f'Regole_{case.SLUG}.txt').write_text(case.REGOLE.strip() + '\n', encoding='utf-8')
    (folder / f'Guida_{case.SLUG}.txt').write_text(case.GUIDA.strip() + '\n', encoding='utf-8')
    old_apart = folder / 'da_consegnare_a_parte'  # posizione precedente dei testi riservati
    if old_apart.is_dir():
        shutil.rmtree(old_apart)
    if case.SLUG in RESERVED_WITH_DATA:
        apart = RESERVED_DIR / case.SLUG
        apart.mkdir(parents=True, exist_ok=True)
        (apart / f'Riservato_{case.SLUG}.txt').write_text(case.RISERVATO.strip() + '\n', encoding='utf-8')
    questions = '\n'.join(f'{n}. {q}' for n, (q, _) in enumerate(TRE_NUMERI[case.SLUG], 1))
    (folder / f'I_tre_numeri_{case.SLUG}.txt').write_text(questions + '\n', encoding='utf-8')


def table_cell(value) -> str:
    return str(value).replace('|', '/')


def values_table(case) -> list[str]:
    """Tabella Markdown di tutti i valori di riferimento del caso."""
    lines = ['| Valore di riferimento | Risultato |', '| --- | --- |']
    for label, value in case.valori().items():
        lines.append(f"| {label} | {table_cell(value)} |")
    return lines


def tre_numeri_table(case) -> list[str]:
    """Tabella Markdown domanda/risposta dei tre numeri da ricavare a mano."""
    values = case.valori()
    lines = ['| Domanda | Risposta |', '| --- | --- |']
    for question, key in TRE_NUMERI[case.SLUG]:
        lines.append(f"| {question} | {table_cell(values[key])} |")
    return lines


def reference_section(case) -> str:
    oggi = date.fromisoformat(case.OGGI)
    lines = [f'## {case.TITOLO} (gruppo {case.GRUPPO})', '',
             f'Data nei testi: {oggi.day} {MONTHS[oggi.month - 1]} {oggi.year}. '
             f'Eventi: {len(case.EVENTI)}.', '',
             '| Lavoro | Accesso | Dipende da |', '| --- | --- | --- |']
    for lavoro in case.LAVORI:
        lines.append(f"| {lavoro['nome']} | {lavoro['accesso']} | {lavoro.get('dipende_da') or '—'} |")
    lines += ['', f'- Solo amministratore: {case.RISERVATO}',
              f'- Azione che l\'agente non compie da solo: {case.AZIONE_NON_PERMESSA}',
              f'- Informazione assente dai testi: {case.INFORMAZIONE_ASSENTE}', '',
              *values_table(case),
              '', '**I tre numeri da ricavare a mano**', '', *tre_numeri_table(case)]
    return '\n'.join(lines) + '\n'


def build_cases() -> dict:
    """Controlla e scrive i cinque casi e i valori di riferimento; restituisce i moduli dei casi per slug."""
    cases, sections, failed = {}, [], False
    for slug in ORDER:
        case = load(slug)
        errors = check_case(case)
        if errors:
            failed = True
            print(f'{slug}: ERRORI', file=sys.stderr)
            for error in errors:
                print(f'  - {error}', file=sys.stderr)
            continue
        write_students(case)
        cases[slug] = case
        sections.append(reference_section(case))
        print(f'{slug}: ok ({len(case.EVENTI)} eventi, registro {len(registro_testo(case))} caratteri)')
    if failed:
        raise SystemExit(1)
    REFERENCE.parent.mkdir(parents=True, exist_ok=True)
    header = ('# Valori di riferimento dei cinque casi · lezione 7\n\n'
              'Documento riservato al docente. Calcolati dagli eventi in `docente/casi/` da '
              '`genera_materiali.py`: non trascrivere a mano.\n\n')
    REFERENCE.write_text(header + '\n'.join(sections), encoding='utf-8')
    print(f'Scritto {REFERENCE.relative_to(LESSON)}')
    return cases


def guide_replacements(cases: dict) -> dict[str, str]:
    """Segnaposto della guida docente: {{TRE_NUMERI_<caso>}} e {{VALORI_<caso>}} per ogni caso."""
    result = {}
    for slug, case in cases.items():
        result[f'{{{{TRE_NUMERI_{slug}}}}}'] = '\n\n' + '\n'.join(tre_numeri_table(case)) + '\n\n'
        result[f'{{{{VALORI_{slug}}}}}'] = '\n\n' + '\n'.join(values_table(case)) + '\n\n'
    return result


def office_program() -> str:
    for name in ('soffice', 'libreoffice'):
        if found := shutil.which(name):
            return found
    for folder in (os.environ.get('ProgramFiles', ''), os.environ.get('ProgramFiles(x86)', '')):
        candidate = Path(folder) / 'LibreOffice/program/soffice.exe'
        if folder and candidate.is_file():
            return str(candidate)
    raise SystemExit('Programma necessario non disponibile: LibreOffice')


def command(args: list[str], timeout: int = 180) -> str:
    result = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    if result.returncode:
        raise RuntimeError(f"Comando non riuscito: {args[0]}\n{result.stdout}\n{result.stderr}")
    return result.stdout


def remove_slides(prs, keep: set[int] | None = None) -> None:
    for item in list(prs.slides._sldIdLst):
        if keep is None or item.id not in keep:
            prs.part.drop_rel(item.rId)
            prs.slides._sldIdLst.remove(item)


def parse_slides(text: str) -> list[dict]:
    starts = list(re.finditer(r'^# Slide\s+\d+\s+[—–-]\s+(.+)\n', text, re.M))
    slides = []
    for i, match in enumerate(starts):
        body = text[match.end():starts[i + 1].start() if i + 1 < len(starts) else len(text)]
        layout_match = re.search(r'<!--\s*layout:\s*(\w+)\s*-->', body)
        if not layout_match or layout_match.group(1) not in LAYOUTS:
            raise ValueError(f"Layout mancante o non valido: {match.group(1)}")
        section_match = re.search(r'<!--\s*section:\s*(\d+)\s*-->', body)
        body = re.sub(r'<!--\s*layout:\s*\w+\s*-->', '', body)
        body = re.sub(r'<!--\s*section:\s*\d+\s*-->', '', body)
        body = re.sub(r'^---\s*$', '', body, flags=re.M).strip()
        slides.append({'title': match.group(1), 'layout': layout_match.group(1), 'body': body,
                       'section': int(section_match.group(1)) if section_match else None})
    if not slides:
        raise ValueError('Nessuna slide nel sorgente Markdown.')
    return slides


def cell_runs(cell) -> list[tuple[str, bool]]:
    """Testo di una cella come pezzi (testo, grassetto): il grassetto del Markdown arriva nel Word."""
    runs = [(cell.text or '', False)]
    for child in cell:
        runs.append((child.text_content(), child.tag in ('strong', 'b')))
        runs.append((child.tail or '', False))
    runs = [(text.replace('\n', ' '), bold) for text, bold in runs if text]
    if runs:
        runs[0] = (runs[0][0].lstrip(), runs[0][1])
        runs[-1] = (runs[-1][0].rstrip(), runs[-1][1])
    return runs


def blocks(text: str) -> list[dict]:
    rendered = markdown.markdown(text, extensions=['tables', 'sane_lists'])
    root = lxml_html.fragment_fromstring(rendered, create_parent='div')
    result = []
    for element in root:
        if not isinstance(element.tag, str):
            if 'pagebreak' in (element.text or ''):
                result.append({'kind': 'pagebreak'})
            continue
        tag = element.tag.lower()
        if tag == 'p' and element.xpath('.//img'):
            image = element.xpath('.//img')[0]
            result.append({'kind': 'image', 'src': image.get('src'), 'alt': image.get('alt') or ''})
        elif tag == 'p' and len(element) == 1 and element[0].tag == 'code' and not (element.text or '').strip() and not (element[0].tail or '').strip():
            result.append({'kind': 'code', 'text': element[0].text_content().strip()})
        elif tag == 'table':
            trs = element.xpath('.//tr')
            rows = [[cell.text_content().strip() for cell in row] for row in trs]
            runs = [[cell_runs(cell) for cell in row] for row in trs]
            result.append({'kind': 'table', 'rows': rows, 'runs': runs})
        elif tag in ('ul', 'ol'):
            for index, item in enumerate(element):
                prefix = f'{index + 1}. ' if tag == 'ol' else '• '
                result.append({'kind': 'list', 'text': prefix + item.text_content().strip()})
        else:
            value = element.text_content().strip()
            if value:
                url = tag == 'p' and re.fullmatch(r'https://\S+', value) is not None
                result.append({'kind': 'url' if url else tag, 'text': value})
    return result


def font_file(bold: bool = False) -> str:
    """Arial (Windows) oppure un sostituto con le stesse misure (Liberation Sans, Arimo) su Linux e macOS."""
    if bold not in FONT_FILES:
        windows = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / ('arialbd.ttf' if bold else 'arial.ttf')
        value = str(windows) if windows.is_file() else ''
        if not value and shutil.which('fc-match'):
            for family in ('Arial', 'Liberation Sans', 'Arimo'):
                found = command(['fc-match', '-f', '%{family}|%{file}', f'{family}:style=Bold' if bold else family]).strip()
                name, _, path = found.partition('|')
                if re.search(r'arial|liberation sans|arimo', name, re.I) and Path(path).is_file():
                    value = path
                    break
        if not value:
            wanted = ('LiberationSans-Bold.ttf', 'Arimo-Bold.ttf') if bold else ('LiberationSans-Regular.ttf', 'Arimo-Regular.ttf')
            for folder in ('/usr/share/fonts', '/usr/local/share/fonts', str(Path.home() / '.fonts'), '/Library/Fonts', '/System/Library/Fonts/Supplemental'):
                value = next((str(path) for name in wanted for path in Path(folder).rglob(name)), '')
                if value:
                    break
        if not value:
            raise RuntimeError('Carattere Arial o sostituto con le stesse misure (Liberation Sans) non disponibile.')
        FONT_FILES[bold] = value
    return FONT_FILES[bold]


@lru_cache(maxsize=12)
def measuring_font(size: int, bold: bool = False):
    return ImageFont.truetype(font_file(bold), size)


def lines_needed(text: str, width_pt: float, size_pt: float, bold: bool = False) -> int:
    font = measuring_font(round(size_pt * 96 / 72), bold)
    width = width_pt * 96 / 72
    count = 0
    for paragraph in text.split('\n'):
        current = ''
        for word in paragraph.split():
            candidate = f'{current} {word}'.strip()
            if current and font.getlength(candidate) > width:
                count += 1
                current = word
            else:
                current = candidate
        count += 1
    return count


def template_styles(prs) -> dict:
    styles = {}
    for slide in prs.slides:
        for shape in slide.placeholders:
            if not shape.has_text_frame:
                continue
            paragraph = shape.text_frame.paragraphs[0]
            styles[(slide.slide_layout.name, shape.placeholder_format.idx)] = (
                copy.deepcopy(paragraph._p.pPr),
                copy.deepcopy(paragraph.runs[0]._r.rPr) if paragraph.runs else None,
            )
    return styles


def set_placeholder(slide, idx: int, text: str, styles: dict, fallback: int = 23) -> None:
    shape = next((shape for shape in slide.placeholders if shape.placeholder_format.idx == idx), None)
    if shape is None:
        raise ValueError(f'Placeholder {idx} assente nel layout {slide.slide_layout.name}.')
    ppr, rpr = styles.get((slide.slide_layout.name, idx), (None, None))
    shape.text_frame.clear()
    shape.text_frame.word_wrap = True
    for index, value in enumerate(text.split('\n')):
        paragraph = shape.text_frame.paragraphs[0] if index == 0 else shape.text_frame.add_paragraph()
        if ppr is not None:
            paragraph._p.insert(0, copy.deepcopy(ppr))
        run = paragraph.add_run()
        if rpr is not None:
            run._r.insert(0, copy.deepcopy(rpr))
        run.font.name = FONT
        if run.font.size is None:
            run.font.size = Pt(fallback)
        run.text = value


def add_paragraph_box(slide, text: str, top: float, size: float = 23, bold: bool = False, color: str = INK) -> float:
    line_count = lines_needed(text, 11.8 * 72, size, bold)
    height = (line_count * size * 1.2 * 1.15 + 2) / 72  # l'interlinea 1,2 si applica all'altezza naturale di Arial (circa 1,15 volte il corpo)
    if top + height > 7.55:
        raise ValueError(f'Testo troppo lungo nella slide {len(slide.shapes)}: {text[:70]}')
    shape = slide.shapes.add_textbox(Inches(0.75), Inches(top), Inches(11.8), Inches(height))
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.line_spacing = 1.2
    p.space_before = p.space_after = Pt(0)
    run = p.add_run()
    run.text = text
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)
    return top + height + BODY_GAP


def add_slide_table(slide, rows: list[list[str]], top: float) -> float:
    count = max(len(row) for row in rows)
    proportions = [0.38, 0.62] if count == 2 else [1 / count] * count
    heights = []
    for row_index, row in enumerate(rows):
        n = max(lines_needed(cell, 11.8 * 72 * proportions[j] - 12, 18, row_index == 0) for j, cell in enumerate(row))
        heights.append(max(0.48, (n * 22 + 14) / 72))
    if top + sum(heights) > 7.55:
        raise ValueError('Tabella troppo alta per la slide ufficiale.')
    table = slide.shapes.add_table(len(rows), count, Inches(0.75), Inches(top), Inches(11.8), Inches(sum(heights))).table
    table.first_row = True
    for j, part in enumerate(proportions):
        table.columns[j].width = Inches(11.8 * part)
    for i, row in enumerate(rows):
        table.rows[i].height = Inches(heights[i])
        for j, value in enumerate(row):
            cell = table.cell(i, j)
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.06)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor.from_string(BLUE if i == 0 else PALE)
            cell.text = value
            for p in cell.text_frame.paragraphs:
                for run in p.runs:
                    run.font.name = FONT
                    run.font.size = Pt(18)
                    run.font.bold = i == 0
                    run.font.color.rgb = RGBColor.from_string('FFFFFF' if i == 0 else INK)
    return top + sum(heights) + 0.18


def add_slide_image(slide, source: str, alt: str, top: float) -> float:
    """Immagine centrata sotto il testo, ridotta per stare nello spazio rimasto (larghezza massima 11,8 pollici)."""
    path = TEACHER_BACKUP / source
    if not path.is_file():
        raise FileNotFoundError(f'Immagine della slide non trovata: {path}')
    with Image.open(path) as image:
        ratio = image.width / image.height
    top += 0.1  # margine di sicurezza: il testo sopra può andare a capo in modo diverso da quello stimato
    available = 7.55 - top
    if available < 1.2:
        raise ValueError(f'Spazio insufficiente per l\'immagine {source}: restano {available:.2f} pollici')
    height = min(available, 11.8 / ratio)
    width = height * ratio
    left = (13.333 - width) / 2
    picture = slide.shapes.add_picture(str(path), Inches(left), Inches(top), Inches(width), Inches(height))
    picture._element.nvPicPr.cNvPr.set('descr', alt)
    return top + height + BODY_GAP


def load_model():
    """Modello ufficiale; la fascia in basso delle pagine di contenuto deve riportare il programma della lezione."""
    prs = Presentation(MODEL)
    for layout in prs.slide_layouts:
        for shape in layout.shapes:
            if shape.has_text_frame and not shape.is_placeholder:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.text = run.text.replace(*PROGRAM)
    band = [shape.text_frame.text for layout in prs.slide_layouts for shape in layout.shapes if shape.has_text_frame and not shape.is_placeholder]
    if not any(PROGRAM[1] in text for text in band):
        raise SystemExit(f'La fascia in basso del modello non riporta «{PROGRAM[1]}»: controllare il testo nel modello.')
    return prs


def section_numbers(slides: list[dict]) -> list[int | None]:
    """Numero mostrato nelle slide di sezione: in ordine da 01, oppure quello indicato con <!-- section: N -->."""
    numbers, current = [], 0
    for data in slides:
        if data['layout'] == 'SEZIONE':
            current = data['section'] or current + 1
            numbers.append(current)
        else:
            numbers.append(None)
    return numbers


def build_pptx(slides: list[dict]) -> Path:
    prs = load_model()
    styles = template_styles(prs)
    layouts = {layout.name: layout for layout in prs.slide_layouts}
    remove_slides(prs)
    numbers = section_numbers(slides)
    for index, data in enumerate(slides, 1):
        slide = prs.slides.add_slide(layouts[data['layout']])
        paragraphs = [block['text'] for block in blocks(data['body']) if 'text' in block]
        if data['layout'] == 'COPERTINA':
            if len(paragraphs) < 2:
                raise ValueError(f'La copertina ha bisogno di due righe sotto il titolo (sottotitolo e corso): {data["title"]}')
            set_placeholder(slide, 104, data['title'], styles, 39)
            set_placeholder(slide, 105, paragraphs[0], styles, 19)
            set_placeholder(slide, 106, paragraphs[1], styles, 18)
        elif data['layout'] == 'SEZIONE':
            set_placeholder(slide, 102, f'{numbers[index - 1]:02}', styles, 80)
            set_placeholder(slide, 103, data['title'], styles, 39)
            set_placeholder(slide, 105, '\n'.join(paragraphs), styles, 23)
        elif data['layout'] == 'CHIUSURA':
            set_placeholder(slide, 102, data['title'], styles, 39)
            set_placeholder(slide, 104, '\n'.join(paragraphs), styles, 23)
        else:
            set_placeholder(slide, 102, data['title'], styles, 28)
            top = 1.95
            for block in blocks(data['body']):
                if block['kind'] == 'table':
                    top = add_slide_table(slide, block['rows'], top)
                elif block['kind'] == 'image':
                    top = add_slide_image(slide, block['src'], block['alt'], top)
                elif 'text' in block:
                    url = block['kind'] == 'url'
                    size = 28 if url else 44 if block['kind'] == 'h2' else 36 if block['kind'] == 'blockquote' else BODY_SIZE
                    top = add_paragraph_box(slide, block['text'], top, size, url or block['kind'].startswith('h'), BLUE if url else INK)
        number = next((shape for shape in slide.placeholders if shape.placeholder_format.idx == 4294967295), None)
        if number is not None:
            number.text = str(index)
            for p in number.text_frame.paragraphs:
                for run in p.runs:
                    run.font.name = FONT
                    run.font.size = Pt(11)
                    run.font.color.rgb = RGBColor.from_string(MUTED)
    prs.core_properties.title = TITLE
    prs.core_properties.subject = SUBJECT
    prs.core_properties.keywords = ''
    prs.core_properties.comments = ''
    output = DECK_DIR / f'{DECK_NAME}.pptx'
    prs.save(output)
    return output


def pdfs(inputs: list[Path], output: Path, work: Path) -> list[Path]:
    output.mkdir(parents=True, exist_ok=True)
    profile = work / 'libreoffice-profile'
    log = command([office_program(), '-env:UserInstallation=' + profile.as_uri(), '--headless', '--convert-to', 'pdf', '--outdir', str(output), *map(str, inputs)], timeout=600)
    print(log.strip())
    paths = [output / (path.stem + '.pdf') for path in inputs]
    for path in paths:
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(f'Esportazione PDF mancante: {path}')
    return paths


def background_images(work: Path) -> dict[str, str]:
    prs = load_model()
    order = [slide.slide_layout.name for slide in prs.slides]
    for slide in prs.slides:
        for shape in list(slide.shapes):
            shape._element.getparent().remove(shape._element)
    blank = work / 'fondali_ufficiali.pptx'
    prs.save(blank)
    pdf = pymupdf.open(pdfs([blank], work / 'fondali', work)[0])
    images = {}
    for page, name in zip(pdf, order):
        pixmap = page.get_pixmap(matrix=pymupdf.Matrix(1280 / page.rect.width, 800 / page.rect.height))
        images[name] = base64.b64encode(pixmap.tobytes('png')).decode('ascii')
    return images


def build_html(slides: list[dict], backgrounds: dict[str, str]) -> None:
    pages = []
    numbers = section_numbers(slides)
    for index, data in enumerate(slides, 1):
        layout = data['layout']
        content = markdown.markdown(data['body'], extensions=['tables', 'sane_lists'])
        content = re.sub(r'<p>(https://\S+)</p>', r'<p class="url">\1</p>', content)
        content = re.sub(r'src="([^"]+\.png)"', lambda m: 'src="data:image/png;base64,' + base64.b64encode((TEACHER_BACKUP / m.group(1)).read_bytes()).decode('ascii') + '"', content)
        title = html.escape(data['title'])
        if layout == 'COPERTINA':
            paragraphs = [block['text'] for block in blocks(data['body']) if 'text' in block]
            inner = f'<h1>{title}</h1><p class="subtitle">{html.escape(paragraphs[0])}</p><p class="course">{html.escape(paragraphs[1])}</p>'
        elif layout == 'SEZIONE':
            inner = f'<div class="section-number">{numbers[index - 1]:02}</div><h1>{title}</h1><div class="section-body">{content}</div><span class="slide-number">{index}</span>'
        elif layout == 'CHIUSURA':
            inner = f'<h1>{title}</h1><div class="closing-body">{content}</div>'
        else:
            inner = f'<h1>{title}</h1><div class="body">{content}</div><span class="slide-number">{index}</span>'
        pages.append(f'<section class="slide {layout.lower()}" aria-label="Slide {index}: {title}" style="background-image:url(data:image/png;base64,{backgrounds[layout]})">{inner}</section>')
    css = '''
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;font-family:Arial,sans-serif}body{background:#eaf0f6;color:#17344d;overflow:hidden}.deck{position:absolute;left:50%;top:12px;width:1280px;height:800px;transform-origin:top center}.slide{display:none;position:absolute;inset:0;width:1280px;height:800px;background-size:1280px 800px;overflow:hidden}.slide.active{display:block}.slide h1{position:absolute;margin:0;font-weight:700;line-height:1.12}.contenuto h1{left:62.4px;top:59.52px;width:1012.8px;height:100.8px;color:#1064a0;font-size:37.333px}.body{position:absolute;left:72px;top:187.2px;width:1132.8px;height:537.6px;font-size:30.667px;line-height:1.2}.body p{margin:0 0 12px}.body ul,.body ol{margin:0 0 12px;padding-left:29px}.body li{margin:0 0 12px}.body table{width:100%;border-collapse:collapse;margin:0 0 17px;font-size:24px;line-height:1.22}.body th,.body td{border:1px solid #4b6275;padding:8px;text-align:left;vertical-align:top}.body th{background:#1064a0;color:white}.body td{background:#eaf0f6}.slide-number{position:absolute;left:1118.4px;top:763.2px;width:98.9px;height:21.1px;text-align:right;font-size:14.667px;color:#4b6275}.copertina h1{left:62.4px;top:192px;width:1152px;height:139.2px;color:#1064a0;font-size:52px}.copertina .subtitle{position:absolute;left:62.4px;top:345.6px;width:1152px;margin:0;font-size:25.333px;line-height:1.2}.copertina .course{position:absolute;left:62.4px;top:408px;width:1142.4px;margin:0;font-size:24px}.sezione .section-number{position:absolute;left:62.4px;top:129.6px;width:384px;height:144px;color:#f5820b;font-size:106.667px;font-weight:700;line-height:1}.sezione h1{left:62.4px;top:283.2px;width:672px;height:139.2px;color:white;font-size:52px}.section-body{position:absolute;left:62.4px;top:456px;width:662.4px;height:153.6px;color:white;font-size:30.667px;line-height:1.2}.section-body p{margin:0}.chiusura h1{left:62.4px;top:211.2px;width:681.6px;height:153.6px;color:white;font-size:52px}.closing-body{position:absolute;left:62.4px;top:403.2px;width:662.4px;height:211.2px;color:white;font-size:30.667px;line-height:1.2}.closing-body p{margin:0 0 12px}.controls{position:fixed;bottom:10px;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:14px;font-size:15px;white-space:nowrap}button{font:inherit;padding:8px 14px;border:1px solid #1064a0;background:white;color:#1064a0;border-radius:3px;min-height:40px}button:disabled{opacity:.45}@media print{@page{size:1280px 800px;margin:0}html,body{height:auto;overflow:visible}.deck{position:static;transform:none!important;width:1280px;height:auto}.slide{display:block!important;position:relative;break-after:page;print-color-adjust:exact;-webkit-print-color-adjust:exact}.slide:last-child{break-after:auto}.controls{display:none}}
''' + f'''.body{{font-size:{BODY_SIZE * 4 / 3:.3f}px}}
.body p,.body ul,.body ol,.body li{{margin-bottom:{BODY_GAP * 96:.0f}px}}
.body h2{{font-size:58.667px;line-height:1.2;margin:0 0 {BODY_GAP * 96:.0f}px}}
.body blockquote{{font-size:48px;line-height:1.2;margin:0 0 {BODY_GAP * 96:.0f}px;padding:0}}
.body img{{display:block;margin:6px auto;max-width:100%;max-height:430px;object-fit:contain}}
.body blockquote p{{margin:0}}
.body p.url{{font-size:37.333px;font-weight:700;color:#1064a0;overflow-wrap:anywhere}}
'''
    js = '''
const slides=[...document.querySelectorAll('.slide')];let current=0;const previous=document.getElementById('previous'),next=document.getElementById('next'),position=document.getElementById('position');function show(index){current=Math.max(0,Math.min(slides.length-1,index));slides.forEach((slide,i)=>{slide.classList.toggle('active',i===current);slide.setAttribute('aria-hidden',i===current?'false':'true')});previous.disabled=current===0;next.disabled=current===slides.length-1;position.textContent=`${current+1} / ${slides.length}`}function fit(){const scale=Math.max(.1,Math.min((innerWidth-24)/1280,(innerHeight-72)/800));document.querySelector('.deck').style.transform=`translateX(-50%) scale(${scale})`}previous.addEventListener('click',()=>show(current-1));next.addEventListener('click',()=>show(current+1));document.addEventListener('keydown',event=>{if(event.target.closest('button,input,textarea,select,a'))return;if(['ArrowRight','PageDown',' '].includes(event.key)){event.preventDefault();show(current+1)}if(['ArrowLeft','PageUp'].includes(event.key)){event.preventDefault();show(current-1)}if(event.key==='Home')show(0);if(event.key==='End')show(slides.length-1)});addEventListener('resize',fit);show(0);fit();
'''
    output = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(TITLE) + '</title><style>' + css + '</style></head><body><main class="deck">' + ''.join(pages) + '</main><nav class="controls" aria-label="Navigazione slide"><button id="previous">Indietro</button><span id="position" aria-live="polite"></span><button id="next">Avanti</button></nav><script>' + js + '</script></body></html>'
    (TEACHER_BACKUP / f'{DECK_NAME}.html').write_text(output, encoding='utf-8')


def document_style(doc, title: str, footer_text: str = FOOTER) -> None:
    section = doc.sections[0]
    section.page_width, section.page_height = DocInches(8.2677), DocInches(11.6929)
    section.top_margin = section.bottom_margin = DocInches(0.62)
    section.left_margin = section.right_margin = DocInches(0.66)
    normal = doc.styles['Normal']
    normal.font.name, normal.font.size = FONT, DocPt(10.5)
    normal.paragraph_format.space_after = DocPt(5)
    normal.paragraph_format.line_spacing = 1.08
    footer_style = doc.styles['Footer']
    footer_style.font.name, footer_style.font.size = FONT, DocPt(8)
    for name, size in [('Title', 22), ('Heading 1', 21), ('Heading 2', 14), ('Heading 3', 12)]:
        style = doc.styles[name]
        style.font.name, style.font.size = FONT, DocPt(size)
        fonts = style.element.rPr.rFonts
        for attribute in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):  # il carattere del tema avrebbe la precedenza su Arial
            fonts.attrib.pop(qn(attribute), None)
        style.font.color.rgb = DocColor.from_string(BLUE)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.space_before = DocPt(8)
        style.paragraph_format.space_after = DocPt(5)
    doc.core_properties.title = title
    doc.core_properties.author = 'ITS MAKER Bologna'
    footer = section.footer.paragraphs[0]
    footer.text = footer_text
    for run in footer.runs:
        run.font.name, run.font.size = FONT, DocPt(8)
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    number = OxmlElement('w:r')
    properties = OxmlElement('w:rPr')
    fonts = OxmlElement('w:rFonts')
    fonts.set(qn('w:ascii'), FONT)
    fonts.set(qn('w:hAnsi'), FONT)
    size = OxmlElement('w:sz')
    size.set(qn('w:val'), '16')
    properties.extend([fonts, size])
    text = OxmlElement('w:t')
    text.text = '1'
    number.extend([properties, text])
    field.append(number)
    footer._p.append(field)


def word_table(doc, rows: list[list[str]], runs: list[list[list[tuple[str, bool]]]] | None = None) -> None:
    count = max(len(row) for row in rows)
    table = doc.add_table(rows=1, cols=count)
    table.style = 'Table Grid'
    table.autofit = False
    width = doc.sections[-1].page_width - doc.sections[-1].left_margin - doc.sections[-1].right_margin
    if count == 2:
        proportions = [0.40, 0.60]
    elif count >= 3:
        weights = [max(1.0, max(len(row[j]) if j < len(row) else 0 for row in rows)) ** 0.5 for j in range(count)]
        shares = [max(0.12, weight / sum(weights)) for weight in weights]
        proportions = [share / sum(shares) for share in shares]
    else:
        proportions = [1.0]
    for j, part in enumerate(proportions):
        table.columns[j].width = int(width * part)
    for i, values in enumerate(rows):
        row = table.rows[0] if i == 0 else table.add_row()
        row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
        row.height = DocInches(0.27 if i == 0 else 0.34)
        props = row._tr.get_or_add_trPr()
        props.append(OxmlElement('w:cantSplit'))
        if i == 0:
            props.append(OxmlElement('w:tblHeader'))
        for j, value in enumerate(values):
            cell = row.cells[j]
            cell.width = int(width * proportions[j])
            if i == 0:
                shade = OxmlElement('w:shd')
                shade.set(qn('w:val'), 'clear')
                shade.set(qn('w:fill'), PALE)
                cell._tc.get_or_add_tcPr().append(shade)  # shd prima di vAlign (ordine dello schema)
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if runs is not None and i > 0:
                paragraph = cell.paragraphs[0]
                for text, bold in runs[i][j]:
                    paragraph.add_run(text).bold = bold
            else:
                cell.text = value
            for p in cell.paragraphs:
                p.paragraph_format.space_after = p.paragraph_format.space_before = DocPt(2)
                for run in p.runs:
                    run.font.name, run.font.size = FONT, DocPt(9.5)
                    if runs is None or i == 0:
                        run.bold = i == 0


def markdown_doc(source: Path, target: Path, title: str | None = None, footer_text: str | None = None, replacements: dict[str, str] | None = None) -> None:
    doc = Document()
    document_style(doc, title or source.stem.replace('_', ' '), *([footer_text] if footer_text else []))
    pending_break = False
    previous_table = False
    text = source.read_text(encoding='utf-8')
    for placeholder, value in (replacements or {}).items():
        if placeholder in text:
            text = text.replace(placeholder, value)
        else:
            print(f'Avviso: {placeholder} non compare in {source.name}; i valori calcolati non sono stati inseriti.')
    if '{{' in text:
        raise SystemExit(f'{source.name}: segnaposto non sostituito ({text[text.index("{{"):][:40]!r}).')
    for block in blocks(text):
        kind = block['kind']
        if kind == 'pagebreak':
            pending_break = True
            continue
        if kind == 'table':
            if not previous_table and not pending_break and doc.paragraphs:
                doc.paragraphs[-1].paragraph_format.keep_with_next = True  # la frase che introduce la tabella non resta sola a fine pagina
            if previous_table and not pending_break:
                spacer = doc.add_paragraph()
                spacer.paragraph_format.space_before = spacer.paragraph_format.space_after = DocPt(1)
                spacer.paragraph_format.line_spacing = DocPt(2)
            word_table(doc, block['rows'], block.get('runs'))
            if pending_break:
                doc.tables[-1].rows[0].cells[0].paragraphs[0].paragraph_format.page_break_before = True
        elif kind == 'code':
            paragraph = doc.add_paragraph()
            border = OxmlElement('w:pBdr')
            for side in ('top', 'left', 'bottom', 'right'):
                edge = OxmlElement(f'w:{side}')
                edge.set(qn('w:val'), 'single')
                edge.set(qn('w:sz'), '4')
                edge.set(qn('w:space'), '4')
                edge.set(qn('w:color'), '999999')
                border.append(edge)
            shade = OxmlElement('w:shd')
            shade.set(qn('w:val'), 'clear')
            shade.set(qn('w:fill'), PALE)
            paragraph._p.get_or_add_pPr().extend([border, shade])  # pBdr prima di shd, prima di spaziatura e rientro (ordine dello schema)
            paragraph.paragraph_format.left_indent = DocInches(0.2)
            paragraph.paragraph_format.space_before = paragraph.paragraph_format.space_after = DocPt(6)
            run = paragraph.add_run(block['text'])
            run.font.name, run.font.size = 'Consolas', DocPt(10.5)
            run._element.rPr.rFonts.set(qn('w:eastAsia'), 'Consolas')
            paragraph.paragraph_format.keep_with_next = True
            if pending_break:
                paragraph.paragraph_format.page_break_before = True
        else:
            if re.fullmatch(r'h[1-6]', kind):
                paragraph = doc.add_heading(block['text'], min(int(kind[1]), 3))
            else:
                paragraph = doc.add_paragraph(block['text'])
            if pending_break:
                paragraph.paragraph_format.page_break_before = True
        pending_break = False
        previous_table = kind == 'table'
    doc.save(target)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.parse_args()
    cases = build_cases()
    office_program()
    font_file()
    if not MODEL.is_file():
        raise SystemExit(f'Manca il modello PowerPoint ufficiale: {MODEL.name} (accanto a genera_materiali.py).')
    # (sorgente Markdown, Word, titolo, cartella del PDF, segnaposto da sostituire)
    documents = [
        (STUDENTS_BACKUP / 'ATTIVITA_LEZIONE7.md', STUDENTS / 'ATTIVITA_LEZIONE7.docx', 'Lezione 7 — attività', STUDENTS_BACKUP, {}),
        (STUDENTS_BACKUP / 'FOGLIO_DEL_GRUPPO.md', STUDENTS / 'FOGLIO_DEL_GRUPPO.docx', 'Lezione 7 — foglio del gruppo', STUDENTS_BACKUP, {}),
        (STUDENTS_BACKUP / 'FOGLIO_DEL_COLLAUDO.md', STUDENTS / 'FOGLIO_DEL_COLLAUDO.docx', 'Lezione 7 — foglio del collaudo', STUDENTS_BACKUP, {}),
        (TEACHER_BACKUP / 'TEST_LEZIONE7.md', STUDENTS / 'da_pubblicare_alla_fine' / 'TEST_LEZIONE7.docx', 'Lezione 7 — test individuale', TEACHER_BACKUP, {}),
        (TEACHER_BACKUP / 'GUIDA_DOCENTE.md', HERE / 'GUIDA_DOCENTE.docx', 'Lezione 7 — guida docente', TEACHER_BACKUP, guide_replacements(cases)),
    ]
    for old in (STUDENTS / 'TEST_LEZIONE7.docx', STUDENTS_BACKUP / 'TEST_LEZIONE7.md', STUDENTS_BACKUP / 'TEST_LEZIONE7.pdf'):
        old.unlink(missing_ok=True)  # posizioni precedenti del test individuale
    outputs: dict[Path, Path] = {}  # file da esportare in PDF -> cartella del PDF
    created, skipped = [], []
    slides = None
    if SLIDES_SOURCE.is_file():
        slides = parse_slides(SLIDES_SOURCE.read_text(encoding='utf-8'))
        TEACHER_BACKUP.mkdir(parents=True, exist_ok=True)
        pptx = build_pptx(slides)
        outputs[pptx] = TEACHER_BACKUP
        created.append(f'{len(slides)} slide')
    else:
        skipped.append(SLIDES_SOURCE)
    for source, target, title, pdf_folder, replacements in documents:
        if not source.is_file():
            skipped.append(source)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        markdown_doc(source, target, title, FOOTER, replacements)
        outputs[target] = pdf_folder
        created.append(target.name)
    for folder in {*outputs.values()}:
        folder.mkdir(parents=True, exist_ok=True)
    if outputs:
        with tempfile.TemporaryDirectory(prefix='its-maker-lezione7-') as folder:
            work = Path(folder)
            if slides:
                build_html(slides, background_images(work))
            converted = pdfs(list(outputs), work / 'pdf', work)
            for (source, pdf_folder), pdf in zip(outputs.items(), converted):
                shutil.copyfile(pdf, pdf_folder / f'{source.stem}.pdf')
    print(f'Creati in {LESSON}: {", ".join(created) or "nessun documento"} (con i PDF' + (' e l\'HTML delle slide)' if slides else ')'))
    for source in skipped:
        print(f'Sorgente mancante, saltato: {source.relative_to(LESSON)}')


if __name__ == '__main__':
    main()
