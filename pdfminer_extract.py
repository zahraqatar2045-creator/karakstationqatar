from pathlib import Path
from pdfminer.high_level import extract_text
p = Path('assets/img/menu/karak menu.pdf')
print('exists', p.exists())
text = extract_text(p)
print('len', len(text))
print(text[:2000])
