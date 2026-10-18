"""Rigenera HTML e PDF dai Markdown; richiede Markdown, Playwright e Chrome/Edge."""

import argparse
import html
import os
import re
import shutil
import tempfile
from pathlib import Path

import markdown
from playwright.sync_api import Error as BrowserError, sync_playwright


ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "materiali_aula" / "SLIDE_DOCENTE_ITS_MAKER.md"
DOCUMENTS = (
    ROOT / "PROPOSTA_DIDATTICA_ITS_MAKER.md",
    ROOT / "materiali_aula" / "DISPENSA_OPERATIVA_STUDENTI.md",
)
DOC_CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { color: #172033; font: 11pt/1.45 'Segoe UI', Arial, sans-serif; }
h1 { font-size: 22pt; } h2 { font-size: 16pt; border-bottom: 1px solid #aab8cb; padding-bottom: .25em; }
h3 { font-size: 13pt; } h1, h2, h3, h4 { break-after: avoid; }
p, li { orphans: 3; widows: 3; } a { color: #144b87; overflow-wrap: anywhere; }
table { width: 100%; border-collapse: collapse; font-size: 9pt; margin: 1em 0; }
th, td { border: 1px solid #aab8cb; padding: .4em; text-align: left; vertical-align: top; overflow-wrap: anywhere; }
th { overflow-wrap: normal; word-break: normal; }
thead { display: table-header-group; } tr { break-inside: avoid; }
pre { padding: .8em; background: #f0f3f8; border: 1px solid #c5cedd; white-space: pre-wrap; overflow-wrap: anywhere; font: 9pt/1.4 Consolas, monospace; break-inside: avoid; }
code { font-family: Consolas, monospace; font-size: .92em; }
blockquote { border-left: 3px solid #805b00; margin-left: 0; padding-left: 1em; }
@media screen { body { max-width: 70rem; margin: 2rem auto; padding: 0 1rem; } }
"""
SLIDE_CSS = """
* { box-sizing: border-box; }
html, body { margin: 0; width: 100%; height: 100%; }
body { color: #f8fafc; background: #0f172a; font-family: 'Segoe UI', Arial, sans-serif; overflow: hidden; }
.deck { position: absolute; left: 50%; top: 12px; width: 1600px; height: 900px; transform-origin: top center; }
.slide { display: none; position: absolute; width: 1600px; height: 900px; padding: 40px 64px 64px; overflow-y: auto; background: #0f172a; }
.slide.active { display: block; }
.slide-header { font-size: 18px; color: #aebdd1; border-bottom: 1px solid #41516b; padding-bottom: 12px; margin-bottom: 24px; }
h1 { font-size: 48px; line-height: 1.16; margin: 0 0 24px; color: #7dd3fc; }
h2 { font-size: 40px; line-height: 1.2; margin: 0 0 24px; color: #7dd3fc; }
h3 { font-size: 30px; margin: 16px 0; }
p, li { font-size: 28px; line-height: 1.4; margin: 10px 0; }
li { padding-left: 4px; } strong { color: #fde68a; }
a { color: #93c5fd; overflow-wrap: anywhere; }
pre { padding: 18px; background: #1e293b; white-space: pre-wrap; overflow-wrap: anywhere; border-left: 4px solid #7dd3fc; font: 23px/1.35 Consolas, monospace; }
code { font-family: Consolas, monospace; font-size: .88em; }
blockquote { border-left: 4px solid #facc15; background: #1e293b; margin: 20px 0 0; padding: 12px 20px; }
blockquote p { color: #fde68a; font-size: 22px; line-height: 1.35; margin: 0; }
table { width: 100%; border-collapse: collapse; font-size: 23px; } th, td { border: 1px solid #64748b; padding: 10px; text-align: left; }
.controls { position: fixed; right: 16px; bottom: 10px; display: flex; align-items: center; gap: 12px; }
button { padding: 10px 16px; min-height: 44px; font: 16px 'Segoe UI', sans-serif; background: #1d4ed8; color: white; border: 1px solid #93c5fd; border-radius: 4px; cursor: pointer; }
button:disabled { opacity: .5; cursor: default; }
#position { font-size: 16px; }
@media print {
 @page { size: 1600px 900px; margin: 0; }
 html, body { height: auto; overflow: visible; background: white; color: #172033; }
 .deck { position: static; transform: none !important; width: 1600px; height: auto; }
 .slide { display: block !important; position: relative; height: 900px; break-after: page; overflow: visible; background: white; color: #172033; }
 .slide:last-child { break-after: auto; }
 h1, h2, strong { color: #144b87; } a { color: #144b87; }
 pre, blockquote { background: #f0f3f8; } blockquote p { color: #614900; }
 .slide-header { color: #46546b; } .controls { display: none; }
}
"""
SLIDE_JS = """
const slides = [...document.querySelectorAll('.slide')];
let current = 0;
const previous = document.getElementById('previous');
const next = document.getElementById('next');
function showSlide(index) {
 current = Math.max(0, Math.min(slides.length - 1, index));
 slides.forEach((slide, i) => slide.classList.toggle('active', i === current));
 previous.disabled = current === 0;
 next.disabled = current === slides.length - 1;
 document.getElementById('position').textContent = `${current + 1} / ${slides.length}`;
}
function fitDeck() {
 const scale = Math.min((innerWidth - 24) / 1600, (innerHeight - 68) / 900);
 document.querySelector('.deck').style.transform = `translateX(-50%) scale(${Math.max(.1, scale)})`;
}
previous.addEventListener('click', () => showSlide(current - 1));
next.addEventListener('click', () => showSlide(current + 1));
document.addEventListener('keydown', event => {
 if (event.target.closest('button, input, textarea, select, a')) return;
 if (['ArrowRight', 'PageDown', ' '].includes(event.key)) { event.preventDefault(); showSlide(current + 1); }
 if (['ArrowLeft', 'PageUp'].includes(event.key)) { event.preventDefault(); showSlide(current - 1); }
 if (event.key === 'Home') showSlide(0);
 if (event.key === 'End') showSlide(slides.length - 1);
});
addEventListener('resize', fitDeck);
showSlide(0); fitDeck();
"""


def convert(text):
    return markdown.markdown(text, extensions=["tables", "pymdownx.superfences", "sane_lists"])


def document_html(source):
    content = convert(source.read_text(encoding="utf-8"))
    return (
        '<!doctype html><html lang="it"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<base href="{html.escape(source.parent.as_uri())}/">'
        f'<title>{html.escape(source.stem)}</title><style>{DOC_CSS}</style>'
        f'</head><body>{content}</body></html>\n'
    )


def slides_html():
    chunks = [part.strip() for part in re.split(r"(?m)^\s*---\s*$", SLIDES.read_text(encoding="utf-8")) if part.strip()]
    if not chunks:
        raise ValueError("Il sorgente delle slide è vuoto.")
    sections = []
    for index, chunk in enumerate(chunks, start=1):
        sections.append(
            f'<section class="slide" data-index="{index}">'
            f'<div class="slide-header">ITS MAKER · AI, LLM e RAG · {index}/{len(chunks)}</div>'
            f'<div class="slide-content">{convert(chunk)}</div></section>'
        )
    return (
        '<!doctype html><html lang="it"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>ITS MAKER — AI, LLM e RAG</title><style>{SLIDE_CSS}</style></head><body>'
        f'<div class="deck">{"".join(sections)}</div>'
        '<nav class="controls" aria-label="Navigazione slide">'
        '<button id="previous" type="button">← Precedente</button>'
        '<span id="position" aria-live="polite"></span>'
        '<button id="next" type="button">Successiva →</button></nav>'
        f'<script>{SLIDE_JS}</script></body></html>\n'
    )


def find_browser(explicit):
    if explicit:
        if not explicit.is_file():
            raise ValueError(f"Browser inesistente: {explicit}")
        return str(explicit.resolve())
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome", "msedge"):
        result = shutil.which(name)
        if result:
            return result
    candidates = [Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")]
    for variable in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"):
        if os.environ.get(variable):
            base = Path(os.environ[variable])
            candidates.extend((base / "Google/Chrome/Application/chrome.exe", base / "Microsoft/Edge/Application/msedge.exe"))
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    raise ValueError("Chrome/Chromium/Edge non trovato: specificare --browser PATH o usare --html-only.")


def print_pdf(browser, source, target, build_dir):
    with tempfile.TemporaryDirectory(prefix="its-print-", dir=build_dir) as temp:
        output = Path(temp) / "documento.pdf"
        page = browser.new_page(viewport={"width": 1600, "height": 900})
        try:
            page.goto(source.resolve().as_uri(), wait_until="load")
            page.pdf(
                path=str(output), prefer_css_page_size=True,
                print_background=True, display_header_footer=False,
            )
        finally:
            page.close()
        with output.open("rb") as stream:
            if stream.read(5) != b"%PDF-":
                raise ValueError(f"Output non PDF: {source.name}")
        shutil.copyfile(output, target)
    print(f"PDF: {target.relative_to(ROOT)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html-only", action="store_true", help="Genera HTML senza avviare il browser")
    parser.add_argument("--browser", type=Path, help="Eseguibile Chrome, Chromium o Edge")
    parser.add_argument("--output-dir", type=Path, default=ROOT / ".build-materiali")
    args = parser.parse_args()
    try:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        pairs = []
        for source in DOCUMENTS:
            target = args.output_dir / source.with_suffix(".html").name
            target.write_text(document_html(source), encoding="utf-8")
            pairs.append((target, source.with_suffix(".pdf")))
        slide_target = SLIDES.with_suffix(".html")
        slide_target.write_text(slides_html(), encoding="utf-8")
        pairs.append((slide_target, SLIDES.with_suffix(".pdf")))
        print(f"HTML slide: {slide_target.relative_to(ROOT)}")
        print(f"HTML di stampa: {args.output_dir.resolve()}")
        if not args.html_only:
            executable = find_browser(args.browser)
            with sync_playwright() as playwright:
                browser = playwright.chromium.launch(executable_path=executable, headless=True)
                try:
                    for source, target in pairs:
                        print_pdf(browser, source, target, args.output_dir)
                finally:
                    browser.close()
    except (OSError, ValueError, BrowserError) as exc:
        parser.exit(1, f"Generazione interrotta: {exc}\n")


if __name__ == "__main__":
    main()
