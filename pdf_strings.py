from pathlib import Path
from pypdf import PdfReader
p = Path('assets/img/menu/karak menu.pdf')
reader = PdfReader(p)
print('num_objs', len(reader.trailer['/Root'].keys()) if '/Root' in reader.trailer else 'no-root')
# search across all indirect objects for strings
strings = set()
for i, obj in enumerate(reader.objects.values()):
    if isinstance(obj, bytes):
        try:
            text = obj.decode('utf-8', errors='ignore')
        except Exception:
            continue
        for line in text.splitlines():
            if len(line.strip()) >= 4 and any(c.isalpha() for c in line):
                strings.add(line.strip())
    elif isinstance(obj, str):
        if len(obj.strip()) >= 4:
            strings.add(obj.strip())
# print some candidates
for line in sorted(strings)[:200]:
    print(line)
