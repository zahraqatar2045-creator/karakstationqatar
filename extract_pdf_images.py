from pathlib import Path
from pypdf import PdfReader
p = Path('assets/img/menu/karak menu.pdf')
reader = PdfReader(p)
out_dir = Path('pdf_page_images')
out_dir.mkdir(exist_ok=True)
for i,page in enumerate(reader.pages, start=1):
    resources = page.get('/Resources')
    if not resources:
        print(i, 'no resources')
        continue
    xobject = resources.get('/XObject')
    if not xobject:
        print(i, 'no XObject')
        continue
    for name, obj in xobject.items():
        try:
            img = obj.get_object()
        except Exception as e:
            print(i, name, 'get_object fail', e)
            continue
        t = img.get('/Subtype')
        if t != '/Image':
            print(i, name, 'not image', t)
            continue
        filters = img.get('/Filter')
        if isinstance(filters, list):
            filters = [str(f) for f in filters]
        elif filters is not None:
            filters = [str(filters)]
        else:
            filters = []
        data = img.get_data()
        ext = 'bin'
        if '/DCTDecode' in filters or '/DCT' in filters:
            ext = 'jpg'
        elif '/JPXDecode' in filters:
            ext = 'jp2'
        elif '/FlateDecode' in filters or '/Flate' in filters:
            ext = 'png'
        elif '/LZWDecode' in filters:
            ext = 'img'
        fname = out_dir / f'page{i}_{name[1:]}.{ext}'
        with open(fname, 'wb') as f:
            f.write(data)
        print(i, name, 'filters', filters, 'saved', fname)
