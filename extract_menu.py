from pathlib import Path
from pypdf import PdfReader
p = Path('assets/img/menu/karak menu.pdf')
print('EXISTS', p.exists())
reader = PdfReader(p)
print('PAGES', len(reader.pages))
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text() or ''
    print('--- PAGE', i, '---')
    print(text[:8000])
