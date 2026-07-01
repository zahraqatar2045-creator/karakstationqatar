from pathlib import Path
from pypdf import PdfReader
p = Path('assets/img/menu/karak menu.pdf')
reader = PdfReader(p)
print('pages', len(reader.pages))
for i,page in enumerate(reader.pages, start=1):
    print('PAGE', i)
    print('Resources keys', list(page.get('/Resources', {}).keys()))
    contents = page.get('/Contents')
    print('Contents type', type(contents), contents)
    if hasattr(contents, 'get_object'):
        obj = contents.get_object()
        print('Contents object type', type(obj), repr(obj)[:200])
    try:
        boxes = {k: page.mediabox for k in ['mediabox']}
        print('MediaBox', page.mediabox)
    except Exception as e:
        print('MediaBox err', e)
    try:
        for n in ['/Font','/XObject','/ProcSet','/ColorSpace']:
            if page.get('/Resources') and page['/Resources'].get(n):
                print(n, type(page['/Resources'][n]), list(page['/Resources'][n].keys()))
    except Exception as e:
        print('Resources err', e)
    print()
