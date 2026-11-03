"""Rigenera la lezione 3 con il modello PowerPoint ufficiale.

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
from PIL import ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

import dati_p03

HERE = Path(__file__).resolve().parent
LESSON = HERE.parent
STUDENTS = LESSON / 'studenti'
STUDENTS_BACKUP = STUDENTS / 'backup'
TEACHER_BACKUP = HERE / 'backup'
SOURCES = TEACHER_BACKUP / 'fonti'
PUBLIC_SOURCES = TEACHER_BACKUP / 'fonti_online'
NOTEBOOK_DOCS = STUDENTS / 'Documenti_P03_Blocco_appunti'
WORKBOOK = STUDENTS / 'Diari_P03_gennaio_giugno_2026.xlsx'
DECK_NAME = 'Lezione3_Blocco_appunti_e_agente_Python_P03_ITS_MAKER'
MODEL = HERE / 'MODELLO_ITS_MAKER.pptx'
TITLE = 'Lezione 3 — Dai diari della P03 a numeri controllati'
REPARTO_DOCS = (
    (SOURCES / '02_GUIDA_ALLARMI_P03.md', 'Guida_allarmi_P03_IO-P03-07.docx', 'Guida agli allarmi della pressa P03', 'Reparto presse · IO-P03-07 Rev. 3 · pag. '),
    (SOURCES / '03_REGOLE_INDICATORI_P03.md', 'Regole_indicatori_P03_PR-IND-03.docx', 'Regole di calcolo degli indicatori della P03', 'Ufficio produzione · PR-IND-03 Rev. 2 · pag. '),
    (SOURCES / '04_REGISTRO_P03_13-15_OTTOBRE_2026.txt', 'Registro_P03_13-15_ottobre_2026.docx', 'Registro della pressa P03 · 13–15 ottobre 2026', 'Registro della pressa P03 · pag. '),
)
LAYOUTS = ('COPERTINA', 'CONTENUTO', 'SEZIONE', 'CHIUSURA')
PROGRAM = ('UNSLOTH STUDIO', 'MICROSOFT COPILOT')
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
        if tag == 'table':
            rows = [[cell.text_content().strip() for cell in row] for row in element.xpath('.//tr')]
            result.append({'kind': 'table', 'rows': rows})
        elif tag in ('ul', 'ol'):
            for index, item in enumerate(element):
                prefix = f'{index + 1}. ' if tag == 'ol' else '• '
                result.append({'kind': 'list', 'text': prefix + item.text_content().strip()})
        else:
            value = element.text_content().strip()
            if value:
                result.append({'kind': tag, 'text': value})
    return result


def font_file(bold: bool = False) -> str:
    if bold not in FONT_FILES:
        windows = Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts' / ('arialbd.ttf' if bold else 'arial.ttf')
        if windows.is_file():
            value = str(windows)
        elif shutil.which('fc-match'):
            value = command(['fc-match', '-f', '%{file}', 'Arial:style=Bold' if bold else 'Arial']).strip()
        else:
            value = ''
        if not value:
            raise RuntimeError('Carattere Arial o sostituto metrico non disponibile.')
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


def add_paragraph_box(slide, text: str, top: float, size: float = 23, bold: bool = False) -> float:
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
    run.font.color.rgb = RGBColor.from_string(INK)
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


def load_model():
    """Modello ufficiale con il programma della lezione nella fascia in basso."""
    prs = Presentation(MODEL)
    for layout in prs.slide_layouts:
        for shape in layout.shapes:
            if shape.has_text_frame and not shape.is_placeholder:
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.text = run.text.replace(*PROGRAM)
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
                elif 'text' in block:
                    top = add_paragraph_box(slide, block['text'], top, BODY_SIZE, block['kind'].startswith('h'))
        number = next((shape for shape in slide.placeholders if shape.placeholder_format.idx == 4294967295), None)
        if number is not None:
            number.text = str(index)
            for p in number.text_frame.paragraphs:
                for run in p.runs:
                    run.font.name = FONT
                    run.font.size = Pt(11)
                    run.font.color.rgb = RGBColor.from_string(MUTED)
    prs.core_properties.title = TITLE
    prs.core_properties.subject = 'Microsoft Copilot: Blocco appunti, scheda di passaggio e agente con Python'
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
''' + f'.body{{font-size:{BODY_SIZE * 4 / 3:.3f}px}}.body p,.body ul,.body ol,.body li{{margin-bottom:{BODY_GAP * 96:.0f}px}}'
    js = '''
const slides=[...document.querySelectorAll('.slide')];let current=0;const previous=document.getElementById('previous'),next=document.getElementById('next'),position=document.getElementById('position');function show(index){current=Math.max(0,Math.min(slides.length-1,index));slides.forEach((slide,i)=>{slide.classList.toggle('active',i===current);slide.setAttribute('aria-hidden',i===current?'false':'true')});previous.disabled=current===0;next.disabled=current===slides.length-1;position.textContent=`${current+1} / ${slides.length}`}function fit(){const scale=Math.max(.1,Math.min((innerWidth-24)/1280,(innerHeight-72)/800));document.querySelector('.deck').style.transform=`translateX(-50%) scale(${scale})`}previous.addEventListener('click',()=>show(current-1));next.addEventListener('click',()=>show(current+1));document.addEventListener('keydown',event=>{if(event.target.closest('button,input,textarea,select,a'))return;if(['ArrowRight','PageDown',' '].includes(event.key)){event.preventDefault();show(current+1)}if(['ArrowLeft','PageUp'].includes(event.key)){event.preventDefault();show(current-1)}if(event.key==='Home')show(0);if(event.key==='End')show(slides.length-1)});addEventListener('resize',fit);show(0);fit();
'''
    output = '<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + html.escape(TITLE) + '</title><style>' + css + '</style></head><body><main class="deck">' + ''.join(pages) + '</main><nav class="controls" aria-label="Navigazione slide"><button id="previous">Indietro</button><span id="position" aria-live="polite"></span><button id="next">Avanti</button></nav><script>' + js + '</script></body></html>'
    (TEACHER_BACKUP / f'{DECK_NAME}.html').write_text(output, encoding='utf-8')


def document_style(doc, title: str, footer_text: str = 'ITS MAKER Bologna · Lezione 3 · ') -> None:
    section = doc.sections[0]
    section.page_width, section.page_height = DocInches(8.2677), DocInches(11.6929)
    section.top_margin = section.bottom_margin = DocInches(0.62)
    section.left_margin = section.right_margin = DocInches(0.66)
    normal = doc.styles['Normal']
    normal.font.name, normal.font.size = FONT, DocPt(10.5)
    normal.paragraph_format.space_after = DocPt(5)
    normal.paragraph_format.line_spacing = 1.08
    for name, size in [('Title', 22), ('Heading 1', 21), ('Heading 2', 14), ('Heading 3', 12)]:
        style = doc.styles[name]
        style.font.name, style.font.size = FONT, DocPt(size)
        style.font.color.rgb = DocColor.from_string(BLUE)
        style.paragraph_format.keep_with_next = True
        style.paragraph_format.space_before = DocPt(8)
        style.paragraph_format.space_after = DocPt(5)
    doc.core_properties.title = title
    doc.core_properties.author = 'ITS MAKER Bologna'
    footer = section.footer.paragraphs[0]
    footer.text = footer_text
    field = OxmlElement('w:fldSimple')
    field.set(qn('w:instr'), 'PAGE')
    footer._p.append(field)
    for run in footer.runs:
        run.font.name, run.font.size = FONT, DocPt(8)


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


def markdown_doc(source: Path, target: Path, title: str | None = None, footer_text: str | None = None) -> None:
    doc = Document()
    document_style(doc, title or source.stem.replace('_', ' '), *([footer_text] if footer_text else []))
    pending_break = False
    previous_table = False
    for block in blocks(source.read_text(encoding='utf-8')):
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


def add_source_text(doc, text: str) -> None:
    pieces = re.split(r'\n\s*\n', text.strip())
    for i, piece in enumerate(pieces):
        lines = piece.splitlines()
        if i == 0:
            p = doc.add_paragraph()
            p.paragraph_format.keep_with_next = True
            run = p.add_run(piece)
            run.bold = True
            run.font.name, run.font.size = FONT, DocPt(20)
            run.font.color.rgb = DocColor.from_string(BLUE)
        elif len(lines) >= 2 and all('|' in line for line in lines):
            word_table(doc, [[cell.strip() for cell in line.split('|')] for line in lines])
        elif len(lines) >= 3 and all('|' in line for line in lines[1:]):
            p = doc.add_paragraph(lines[0])
            p.paragraph_format.keep_with_next = True
            word_table(doc, [[cell.strip() for cell in line.split('|')] for line in lines[1:]])
        else:
            p = doc.add_paragraph(piece)
            for run in p.runs:
                run.font.name, run.font.size = FONT, DocPt(10.5)
    

def text_doc(source: Path, target: Path, title: str, footer_text: str) -> None:
    doc = Document()
    document_style(doc, title, footer_text)
    add_source_text(doc, source.read_text(encoding='utf-8'))
    doc.save(target)


def notebook_documents() -> list[Path]:
    """Cartella da caricare nel Blocco appunti: diari P03, documenti di reparto e fonti pubbliche."""
    for old in NOTEBOOK_DOCS.glob('*') if NOTEBOOK_DOCS.is_dir() else ():
        old.unlink()
    files = dati_p03.convert_diaries(NOTEBOOK_DOCS)
    for source, name, title, footer_text in REPARTO_DOCS:
        target = NOTEBOOK_DOCS / name
        if source.suffix == '.md':
            markdown_doc(source, target, title, footer_text)
        else:
            text_doc(source, target, title, footer_text)
        files.append(target)
    public = sorted(path for path in PUBLIC_SOURCES.glob('E[0-9][0-9]_*') if path.is_file())
    if not public:
        raise RuntimeError(f'Nessuna fonte pubblica in {PUBLIC_SOURCES}')
    for path in public:
        files.append(Path(shutil.copy2(path, NOTEBOOK_DOCS / path.name)))
    return files


def workbook() -> Path:
    months = dati_p03.read_months(NOTEBOOK_DOCS)
    problems = [problem for month in months for problem in dati_p03.check_summary(month, dati_p03.indicators(month))]
    if problems:
        raise RuntimeError('Riepiloghi dei diari non coerenti: ' + '; '.join(problems))
    return dati_p03.write_workbook(months, WORKBOOK)


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
    slides = parse_slides((TEACHER_BACKUP / 'SLIDE_LEZIONE3.md').read_text(encoding='utf-8'))
    STUDENTS_BACKUP.mkdir(parents=True, exist_ok=True)
    documents = notebook_documents()
    workbook()
    pptx = build_pptx(slides)
    worksheet = STUDENTS / 'ATTIVITA_LEZIONE3.docx'
    guide = HERE / 'GUIDA_DOCENTE.docx'
    markdown_doc(STUDENTS_BACKUP / 'ATTIVITA_LEZIONE3.md', worksheet, 'Lezione 3 — scheda di lavoro')
    markdown_doc(TEACHER_BACKUP / 'GUIDA_DOCENTE.md', guide, 'Lezione 3 — guida docente')
    with tempfile.TemporaryDirectory(prefix='its-maker-lezione3-') as folder:
        work = Path(folder)
        build_html(slides, background_images(work))
        outputs = {pptx: TEACHER_BACKUP, worksheet: STUDENTS_BACKUP, guide: TEACHER_BACKUP}
        converted = pdfs(list(outputs), work / 'pdf', work)
        for (source, folder_pdf), pdf in zip(outputs.items(), converted):
            shutil.copyfile(pdf, folder_pdf / f'{source.stem}.pdf')
    print(f'Creati {len(slides)} slide, {len(documents)} documenti per il Blocco appunti e il file Excel dei diari in {LESSON}')


if __name__ == '__main__':
    main()
