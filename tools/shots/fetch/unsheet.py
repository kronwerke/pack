#!/usr/bin/env python3
# unsheet.py <shots-world sha> <tag> <prefix> <outdir> [since_ms]: joins the fetched pieces of /kw cam sheet <prefix>
# (saved api_request answers newer than since_ms), writes the sheets as JPEG with the shots' names lettered in
import json, sys, base64, os, glob, subprocess, io
from PIL import Image, ImageDraw
sha, tag, prefix, out = sys.argv[1:5]
since = float(sys.argv[5]) if len(sys.argv) > 5 else 0
shots = json.loads(subprocess.check_output(['git', '-C', '/home/claude/kw/shots-world', 'show', sha + ':shots.json']))['shots']
names = sorted(s['name'] + '.png' for s in shots if s['name'].startswith(prefix))
os.makedirs(out, exist_ok=True)
T = '/root/.claude/projects/-home-claude/5104831e-b480-51ad-a455-43f4ce763a04/tool-results'
pieces = {}
for f in sorted(glob.glob(T + '/mcp-Elchi_Ops-api_request-*.txt'), key=os.path.getmtime):
    if os.path.getmtime(f) * 1000 < since: continue
    try:
        d = json.load(open(f)); data = d['json']['data']
    except Exception:
        continue
    if isinstance(data, dict) and str(data.get('path', '')).startswith('kronwerke/shots/bundle/') and data['path'].endswith('.bin'):
        pieces[int(data['path'][-7:-4])] = base64.b64decode(data['data'])
n = 0
while n in pieces: n += 1
blob = b''.join(pieces[i] for i in range(n))
pos = 0; k = 0; made = []
while pos + 4 <= len(blob):
    ln = int.from_bytes(blob[pos:pos + 4], 'big')
    if ln == 0 or pos + 4 + ln > len(blob): break
    im = Image.open(io.BytesIO(blob[pos + 4:pos + 4 + ln])).convert('RGB'); pos += 4 + ln
    w, h = im.width // 2, 270
    dr = ImageDraw.Draw(im)
    for j in range(8):
        i = k * 8 + j
        if i >= len(names): break
        x, y = (j % 2) * w, (j // 2) * h
        label = names[i][len(tag):-4]
        dr.rectangle((x, y + h - 13, x + 7 * len(label) + 6, y + h), fill=(0, 0, 0)); dr.text((x + 3, y + h - 12), label, fill=(255, 255, 255))
    p = os.path.join(out, 'sheet_%02d.jpg' % k); im.save(p, quality=90); made.append(p); k += 1
print('pieces', n, 'bytes', len(blob), 'sheets', k, 'pictures', len(names))
for p in made: print(p)
