"""Rigenera la lezione 4 con il modello PowerPoint ufficiale.

Prima esecuzione:
    python genera_materiali.py --template /percorso/Lezione1_AI_processi_ITS_MAKER.pptx
Rigenerazioni successive:
    python genera_materiali.py

Richiede i pacchetti di requirements_materiali.txt e LibreOffice. Non occorre
installare nulla sulle postazioni studente. Il modello ripulito conserva quattro
pagine ufficiali prive di vecchi contenuti e note; HTML e PowerPoint usano gli
stessi fondali e testi modificabili.
"""
from __future__ import annotations

import argparse
import base64
import copy
import html
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime
from functools import lru_cache
from pathlib import Path

import markdown
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_ROW_HEIGHT_RULE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches as DocInches
from docx.shared import Pt as DocPt
from docx.shared import RGBColor as DocColor
import pymupdf
from lxml import html as lxml_html
from PIL import Image, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
LESSON = HERE.parent
STUDENTS = LESSON / 'studenti'
STUDENTS_BACKUP = STUDENTS / 'backup'
TEACHER_BACKUP = HERE / 'backup'
SOURCES = TEACHER_BACKUP / 'fonti'
REGISTER_SOURCE = SOURCES / '04_REGISTRO_RUOTA_LIBERA_7-8_NOVEMBRE_2026.txt'
REGISTER_COPY = STUDENTS / 'Registro_Ruota_Libera_7-8_novembre_2026.txt'
TEXT_DOCUMENTS = {  # documenti del caso: sorgente Markdown, copia di testo semplice da incollare in Copilot
    SOURCES / '02_GUIDA_GUASTI_RUOTA_LIBERA.md': STUDENTS / 'Guida_guasti_Ruota_Libera.txt',
    SOURCES / '03_REGOLE_NOLEGGIO_RUOTA_LIBERA.md': STUDENTS / 'Regole_noleggio_Ruota_Libera.txt',
}
DECK_NAME = 'Lezione4_Reti_neurali_e_agenti_con_orchestrazione_ITS_MAKER'
MODEL = HERE / 'MODELLO_ITS_MAKER.pptx'
TITLE = 'Lezione 4 — Un agente, più lavori'
LAYOUTS = ('COPERTINA', 'CONTENUTO', 'SEZIONE', 'CHIUSURA')
PROGRAM = ('UNSLOTH STUDIO', 'MICROSOFT COPILOT')  # il modello riporta ancora il programma della lezione 1: si sostituisce al caricamento
BLUE, INK, MUTED, PALE = '1064A0', '17344D', '4B6275', 'EAF0F6'
FONT = 'Arial'
BODY_SIZE, BODY_GAP = 26, 0.16  # punti e pollici: testo delle slide di contenuto e spazio fra i paragrafi
FONT_FILES: dict[bool, str] = {}


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


def empty_text(shape) -> None:
    tf = shape.text_frame
    paragraph = tf.paragraphs[0]
    ppr = copy.deepcopy(paragraph._p.pPr)
    rpr = copy.deepcopy(paragraph.runs[0]._r.rPr) if paragraph.runs else None
    tf.clear()
    paragraph = tf.paragraphs[0]
    if ppr is not None:
        if paragraph._p.pPr is not None:
            paragraph._p.remove(paragraph._p.pPr)
        paragraph._p.insert(0, ppr)
    run = paragraph.add_run()
    if rpr is not None:
        run._r.insert(0, rpr)
    run.text = ''


def prepare_model(source: Path) -> None:
    prs = Presentation(source)
    chosen = {}
    for slide in prs.slides:
        if slide.slide_layout.name in LAYOUTS:
            chosen.setdefault(slide.slide_layout.name, slide.slide_id)
    if set(chosen) != set(LAYOUTS):
        raise ValueError('Il modello non contiene tutti e quattro i tipi di pagina ufficiali.')
    if abs(prs.slide_width / prs.slide_height - 1.6) > 0.001:
        raise ValueError('Il modello ufficiale deve essere 16:10.')
    remove_slides(prs, set(chosen.values()))
    for slide in prs.slides:
        for shape in list(slide.shapes):
            if shape.is_placeholder and shape.has_text_frame:
                empty_text(shape)
            else:
                shape._element.getparent().remove(shape._element)
        for rel in list(slide.part.rels.values()):
            if 'notesSlide' in rel.reltype or 'comments' in rel.reltype:
                slide.part.drop_rel(rel.rId)
    prs.core_properties.title = 'Modello ufficiale ITS MAKER — quattro tipi di pagina'
    prs.core_properties.subject = 'Modello grafico ripulito, senza contenuti di lezioni precedenti'
    prs.core_properties.keywords = ''
    prs.core_properties.comments = ''
    prs.save(MODEL)


def parse_slides(text: str) -> list[dict[str, str]]:
    starts = list(re.finditer(r'^# Slide\s+\d+\s+[—–-]\s+(.+)\n', text, re.M))
    slides = []
    for i, match in enumerate(starts):
        body = text[match.end():starts[i + 1].start() if i + 1 < len(starts) else len(text)]
        layout_match = re.search(r'<!--\s*layout:\s*(\w+)\s*-->', body)
        if not layout_match or layout_match.group(1) not in LAYOUTS:
            raise ValueError(f"Layout mancante o non valido: {match.group(1)}")
        body = re.sub(r'<!--\s*layout:\s*\w+\s*-->', '', body)
        body = re.sub(r'^---\s*$', '', body, flags=re.M).strip()
        slides.append({'title': match.group(1), 'layout': layout_match.group(1), 'body': body})
    if not slides:
        raise ValueError('Nessuna slide nel sorgente Markdown.')
    return slides


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
        elif tag == 'table':
            rows = [[cell.text_content().strip() for cell in row] for row in element.xpath('.//tr')]
            result.append({'kind': 'table', 'rows': rows})
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
    height = (line_count * size * 1.2 + 2) / 72
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


def build_pptx(slides: list[dict]) -> Path:
    prs = load_model()
    styles = template_styles(prs)
    layouts = {layout.name: layout for layout in prs.slide_layouts}
    remove_slides(prs)
    section_number = 0
    for index, data in enumerate(slides, 1):
        slide = prs.slides.add_slide(layouts[data['layout']])
        paragraphs = [block['text'] for block in blocks(data['body']) if 'text' in block]
        if data['layout'] == 'COPERTINA':
            set_placeholder(slide, 104, data['title'], styles, 39)
            set_placeholder(slide, 105, paragraphs[0], styles, 19)
            set_placeholder(slide, 106, paragraphs[1], styles, 18)
        elif data['layout'] == 'SEZIONE':
            section_number += 1
            set_placeholder(slide, 102, f'{section_number:02}', styles, 80)
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
    prs.core_properties.subject = 'Reti neurali nel browser e agente con più competenze in Microsoft Copilot'
    prs.core_properties.comments = ''
    output = LESSON / f'{DECK_NAME}.pptx'
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
    section = 0
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
            section += 1
            inner = f'<div class="section-number">{section:02}</div><h1>{title}</h1><div class="section-body">{content}</div><span class="slide-number">{index}</span>'
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


def document_style(doc, title: str, footer_text: str = 'ITS MAKER Bologna · Lezione 4 · ') -> None:
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


def word_table(doc, rows: list[list[str]]) -> None:
    count = max(len(row) for row in rows)
    table = doc.add_table(rows=1, cols=count)
    table.style = 'Table Grid'
    table.autofit = False
    width = doc.sections[-1].page_width - doc.sections[-1].left_margin - doc.sections[-1].right_margin
    proportions = [0.40, 0.60] if count == 2 else [1 / count] * count
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
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            cell.text = value
            for p in cell.paragraphs:
                p.paragraph_format.space_after = p.paragraph_format.space_before = DocPt(2)
                for run in p.runs:
                    run.font.name, run.font.size = FONT, DocPt(9.5)
                    run.bold = i == 0
            if i == 0:
                shade = OxmlElement('w:shd')
                shade.set(qn('w:fill'), PALE)
                cell._tc.get_or_add_tcPr().append(shade)


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
            if previous_table and not pending_break:
                spacer = doc.add_paragraph()
                spacer.paragraph_format.space_before = spacer.paragraph_format.space_after = DocPt(1)
                spacer.paragraph_format.line_spacing = DocPt(2)
            word_table(doc, block['rows'])
            if pending_break:
                doc.tables[-1].rows[0].cells[0].paragraphs[0].paragraph_format.page_break_before = True
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


NOTE_HEADER = re.compile(r'^(\d{2})/(\d{2})/(\d{4}) · (\d{2}):(\d{2})[ \t]*$', re.M)
NUMBER = r'\d{1,3}(?:\.\d{3})+|\d+'


def register_fail(message: str) -> None:
    raise SystemExit(f'Registro Ruota Libera ({REGISTER_SOURCE.name}): {message}')


def euro(value: float) -> str:
    return f'{value:.2f}'.replace('.', ',') + ' euro'


def register_values(text: str) -> dict:
    """Ricava dal registro i valori di riferimento della guida. Si ferma se un dato non si trova o non torna."""
    headers = list(NOTE_HEADER.finditer(text))
    if not headers:
        register_fail('nessuna nota con intestazione «GG/MM/AAAA · HH:MM».')
    notes = []
    for header, following in zip(headers, headers[1:] + [None]):
        day, month, year, hour, minute = map(int, header.groups())
        body = text[header.end():following.start() if following else len(text)].strip().split('\n\n')[0]
        notes.append({'when': datetime(year, month, day, hour, minute), 'label': f'{day:02}/{month:02}/{year} · {hour:02}:{minute:02}', 'text': ' '.join(body.split())})
    if re.search(r'euro|€|tariffa|scontrino|a ore|per la giornata', text, re.I):
        register_fail('il registro non deve riportare importi, tariffe o il tipo di noleggio.')
    if re.search(r'dopo\s+\d+\s+minuti', text, re.I):
        register_fail('il registro non deve riportare durate già calcolate («dopo N minuti»).')

    def find(pattern: str, what: str, count: int = 1):
        found = [note for note in notes if re.search(pattern, note['text'], re.I)]
        if len(found) != count:
            register_fail(f'attese {count} note per «{what}», trovate {len(found)}.')
        return found[0] if count == 1 else found

    def minutes_between(start: dict, end: dict) -> int:
        return round((end['when'] - start['when']).total_seconds() / 60)

    outages = {}
    for bike, ending in (('12', r'rimette la bici in fila'), ('5', r'torna in fila con le altre')):
        start = find(rf'\bbici {bike}\b.*\btolta dal noleggio', f'bici {bike} tolta dal noleggio')
        end = find(rf'\bbici {bike}\b.*{ending}', f'bici {bike} di nuovo disponibile')
        outages[bike] = {'start': start, 'end': end, 'minutes': minutes_between(start, end)}
    report = find(r'cliente della bici 12 torna al banco', 'segnalazione della bici 12')
    swap = find(r'Rientra la bici 7\b.*al posto di quella guasta', 'cambio della bici 12')
    test = find(r'prova la bici 12 nel cortile', 'prova del meccanico')
    if not (report['when'] < outages['12']['start']['when'] < swap['when'] < test['when'] < outages['12']['end']['when']):
        register_fail('gli orari della bici 12 (segnalazione, fuori servizio, cambio, prova, disponibile) non sono in ordine.')
    no_bike = minutes_between(report, swap)
    for note in find(r'ritirano le biciclette', 'ritiri', 2):
        bikes = re.findall(r'\d+', re.search(r'ritirano le biciclette ([\d, e]+?)\.', note['text']).group(1))
        left = re.search(r'restano (\d+) biciclette', note['text'])
        if not left or int(left.group(1)) != 20 - len(bikes):
            register_fail(f'{note["label"]}: le biciclette rimaste non tornano con {len(bikes)} ritiri su 20.')
    codes = {}
    for code in ('PF-44', 'CA-26'):
        holders = [note for note in notes if code in note['text']]
        if not holders:
            register_fail(f'il codice {code} non compare nel registro.')
        codes[code] = (len(holders), sum(note['text'].count(code) for note in notes))
    adjust = find(r'rimette a posto in dieci minuti.*senza togliere la bici dal noleggio', 'aggiustamento al banco della bici 9')
    cause = find(r'trova le pastiglie del freno posteriore consumate', 'causa del guasto della bici 12')
    return {'notes': len(notes), 'words': len(text.split()), 'outages': outages, 'report': report, 'swap': swap, 'test': test, 'no_bike': no_bike,
            'refund_hour': no_bike * 5 / 60, 'refund_day': no_bike * 3 / 60, 'codes': codes, 'adjust': adjust, 'cause': cause,
            'minutes': outages['12']['minutes'], 'stop': outages['12']['start'], 'restart': outages['12']['end']}


def register_tables(values: dict) -> str:
    """Tabelle Markdown dei valori di riferimento, da inserire al posto di {{VALORI_REGISTRO}}."""
    o12, o5 = values['outages']['12'], values['outages']['5']
    pf, ca = values['codes']['PF-44'], values['codes']['CA-26']
    rows = [
        '| Dato | Valore |', '| --- | --- |',
        f'| Note nel registro | {values["notes"]} |',
        f'| Parole del registro | {values["words"]} (testo intero, parole separate da spazi) |',
        f'| Segnalazione della bici 12 | {values["report"]["label"]}: i freni non tengono |',
        f'| Bici 12 tolta dal noleggio | {o12["start"]["label"]} |',
        f'| Cambio: il cliente riceve la bici 7 | {values["swap"]["label"]} |',
        f'| Prova del meccanico, bici 12 | {values["test"]["label"]}: i freni tengono, ma la bici resta nel retro |',
        f'| Bici 12 di nuovo disponibile | {o12["end"]["label"]}: il banco la rimette in fila |',
        f'| Minuti fuori servizio, bici 12 | {o12["minutes"]}, calcolati dagli orari del registro |',
        f'| Minuti senza bici del cliente | {values["no_bike"]}, dalla segnalazione al cambio |',
        f'| Rimborso proposto, se il noleggio era a ore | {euro(values["refund_hour"])} ({values["no_bike"]} ÷ 60 × 5) |',
        f'| Rimborso proposto, se il noleggio era per la giornata | {euro(values["refund_day"])} ({values["no_bike"]} ÷ 60 × 3) |',
        f'| Bici 5: tolta dal noleggio e di nuovo disponibile | {o5["start"]["label"]} → {o5["end"]["label"]}, {o5["minutes"]} minuti |',
        f'| Causa del guasto della bici 12 | pastiglie del freno posteriore consumate, constatate il {values["cause"]["label"]} |',
        f'| Codice pastiglie PF-44 | in {pf[0]} note ({pf[1]} volte) |',
        f'| Codice camera d\'aria CA-26 | in {ca[0]} note ({ca[1]} volte) |',
        f'| Aggiustamento al banco, non fuori servizio | bici 9, {values["adjust"]["label"]}: catena rimessa a posto in dieci minuti |',
    ]
    return '\n'.join(rows)


def turn_notes(text: str) -> str:
    """Tabella Markdown delle note del registro che nominano il turno, più i cambi turno per giorno e le divisioni accettabili delle note."""
    headers = list(NOTE_HEADER.finditer(text))
    rows = ['| Data e ora | Frase della nota che nomina il turno |', '| --- | --- |']
    days: dict[str, dict[str, list[str]]] = {}
    for header, following in zip(headers, headers[1:] + [None]):
        day, month, year, hour, minute = map(int, header.groups())
        body = ' '.join(text[header.end():following.start() if following else len(text)].strip().split('\n\n')[0].split())
        key, clock = f'{day:02}/{month:02}', f'{hour:02}:{minute:02}'
        entry = days.setdefault(key, {'first': [], 'changes': []})
        entry['first'].append(clock)
        sentences = [s for s in re.split(r'(?<=[.!?])\s+', body) if re.search(r'\bturno\b', s, re.I)]
        if sentences:
            rows.append(f'| {day:02}/{month:02}/{year} · {clock} | {" ".join(sentences)} |')
        if re.search(r'cambio del turno', body, re.I):
            entry['changes'].append(clock)
    if len(rows) == 2:
        register_fail('nessuna nota nomina il turno.')
    changes = '; '.join(f'{key}: {" e ".join(entry["changes"]) if entry["changes"] else "nessuno"}' for key, entry in days.items())
    divisions = [f'{key}, note dalle {start} alle {end}' for key, entry in days.items() for start, end in zip(entry['first'][:1] + entry['changes'][:-1], entry['changes'])]
    return '\n'.join(rows) + f'\n\nCambi turno indicati con «cambio del turno», per giorno: {changes}. Divisioni delle note in turni che l\'agente può proporre, tutte accettabili: {"; ".join(divisions)}.'


def alarm_table(text: str) -> str:
    """Per ogni guasto della guida: quali delle tre parti del lavoro «Spiegare un guasto» sono scritte, e quali altre parti ha."""
    parts = ('Che cosa significa', 'Primo controllo del banco', 'Chi interviene')
    sections = re.split(r'^### ', text, flags=re.M)[1:]
    if not sections:
        raise SystemExit('Guida ai guasti: nessun guasto trovato (titoli «### Nome del guasto»).')
    rows = ['| Guasto | ' + ' | '.join(parts) + ' | Altre parti |', '| --- | ' + ' | '.join('---' for _ in parts) + ' | --- |']
    for section in sections:
        title, _, body = section.partition('\n')
        labels = re.findall(r'^\*\*(.+?)\.\*\*', body, re.M)
        others = [label for label in labels if label not in parts]
        rows.append(f'| {title.strip()} | ' + ' | '.join('scritto' if part in labels else 'non indicato' for part in parts) + f' | {", ".join(others) if others else "nessuna"} |')
    return '\n'.join(rows)


def plain_text(source: str) -> str:
    """Markdown dei documenti del caso in testo semplice: niente simboli di titolo o di grassetto, tabelle come righe «voce: descrizione»."""
    lines = []
    table_header = True
    for line in source.splitlines():
        if line.startswith('|'):
            cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
            if all(re.fullmatch(r':?-{3,}:?', cell) for cell in cells):
                table_header = False
                continue
            if table_header:
                continue
            lines.append(': '.join(cells))
            continue
        table_header = True
        lines.append(re.sub(r'^#+\s*', '', line).replace('**', ''))
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip() + '\n'


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template', type=Path, help='Modello PowerPoint ufficiale originale, richiesto soltanto alla prima esecuzione.')
    args = parser.parse_args()
    office_program()
    font_file()
    if args.template:
        prepare_model(args.template.resolve())
    elif not MODEL.is_file():
        raise SystemExit('Fornire il modello originale con --template alla prima esecuzione.')
    values = register_values(REGISTER_SOURCE.read_text(encoding='utf-8'))
    slide_source = (TEACHER_BACKUP / 'SLIDE_LEZIONE4.md').read_text(encoding='utf-8')
    for key, value in {
        '{{MINUTI_FUORI_SERVIZIO}}': str(values['minutes']),
        '{{ORA_FUORI_SERVIZIO}}': values['stop']['when'].strftime('%H:%M'),
        '{{ORA_DISPONIBILE}}': values['restart']['when'].strftime('%H:%M'),
        '{{ORA_SEGNALAZIONE}}': values['report']['when'].strftime('%H:%M'),
        '{{ORA_CAMBIO}}': values['swap']['when'].strftime('%H:%M'),
        '{{MINUTI_SENZA_BICI}}': str(values['no_bike']),
    }.items():
        slide_source = slide_source.replace(key, value)
    slides = parse_slides(slide_source)
    STUDENTS_BACKUP.mkdir(parents=True, exist_ok=True)
    pptx = build_pptx(slides)
    worksheet = STUDENTS / 'ATTIVITA_LEZIONE4.docx'
    guide = HERE / 'GUIDA_DOCENTE.docx'
    markdown_doc(STUDENTS_BACKUP / 'ATTIVITA_LEZIONE4.md', worksheet, 'Lezione 4 — attività')
    replacements = {
        '{{VALORI_REGISTRO}}': register_tables(values),
        '{{NOTE_TURNO}}': turn_notes(REGISTER_SOURCE.read_text(encoding='utf-8')),
        '{{VALORI_GUIDA}}': alarm_table((SOURCES / '02_GUIDA_GUASTI_RUOTA_LIBERA.md').read_text(encoding='utf-8')),
    }
    markdown_doc(TEACHER_BACKUP / 'GUIDA_DOCENTE.md', guide, 'Lezione 4 — guida docente', replacements=replacements)
    shutil.copyfile(REGISTER_SOURCE, REGISTER_COPY)  # testo da incollare in Copilot, copia byte per byte (UTF-8)
    for source, target in TEXT_DOCUMENTS.items():
        target.write_text(plain_text(source.read_text(encoding='utf-8')), encoding='utf-8')
    with tempfile.TemporaryDirectory(prefix='its-maker-lezione4-') as folder:
        work = Path(folder)
        build_html(slides, background_images(work))
        outputs = {pptx: TEACHER_BACKUP, worksheet: STUDENTS_BACKUP, guide: TEACHER_BACKUP}
        converted = pdfs(list(outputs), work / 'pdf', work)
        for (source, folder_pdf), pdf in zip(outputs.items(), converted):
            shutil.copyfile(pdf, folder_pdf / f'{source.stem}.pdf')
    print(f'Creati {len(slides)} slide, due documenti Word, il registro e due documenti di testo da incollare in {LESSON}')


if __name__ == '__main__':
    main()
