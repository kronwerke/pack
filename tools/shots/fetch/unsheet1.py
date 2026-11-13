#!/usr/bin/env python3
# unsheet1.py <outdir> <since_ms>: the fetched pieces of a /kw cam sheet as plain JPEG files, without names
import json, sys, base64, os, glob, io
from PIL import Image
out = sys.argv[1]; since = float(sys.argv[2])
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
blob = b''.join(pieces[i] for i in sorted(pieces))
pos = 0; k = 0
while pos + 4 <= len(blob):
    ln = int.from_bytes(blob[pos:pos + 4], 'big')
    if ln == 0 or pos + 4 + ln > len(blob): break
    Image.open(io.BytesIO(blob[pos + 4:pos + 4 + ln])).convert('RGB').save(os.path.join(out, 'sheet_%02d.jpg' % k), quality=92); pos += 4 + ln; k += 1
print('pieces', len(pieces), 'sheets', k)
