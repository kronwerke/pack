#!/usr/bin/env python3
# unbundle6.py <tag> <outdir> <since_ms> <size> <name> [<name> ...]: joins the fetched bundle pieces (saved
# api_request answers newer than since_ms) and cuts them into PNGs by walking the PNG chunks. The names are
# the ones of the server's index.json, in its order; size is the index's "size". It refuses to write
# anything when the number of pictures or the size does not match.
import json, sys, base64, os, glob, struct
tag, out, since, size = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
names = sys.argv[5:]
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
assert sorted(pieces) == list(range(len(pieces))), 'a piece is missing: %s' % sorted(pieces)
assert len(blob) == size, 'size %d, index says %d' % (len(blob), size)
cuts = []; pos = 0
while pos < len(blob):
    assert blob[pos:pos + 8] == b'\x89PNG\r\n\x1a\n', 'no PNG at %d' % pos
    p = pos + 8
    while True:
        ln, kind = struct.unpack('>I4s', blob[p:p + 8]); p += 12 + ln
        if kind == b'IEND': break
    cuts.append((pos, p)); pos = p
assert len(cuts) == len(names), '%d pictures, %d names' % (len(cuts), len(names))
os.makedirs(out, exist_ok=True)
for (a, b), n in zip(cuts, names):
    assert n.startswith(tag), n
    open(os.path.join(out, n[len(tag):] + '.png'), 'wb').write(blob[a:b])
print('pieces', len(pieces), 'bytes', len(blob), 'pictures', len(cuts))
