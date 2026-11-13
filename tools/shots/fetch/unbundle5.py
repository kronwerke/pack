#!/usr/bin/env python3
# unbundle5.py <tag> <outdir> <since_ms>: joins the fetched bundle pieces (saved api_request answers newer than
# since_ms) and cuts them by the bundle's own index, which must have been fetched after them with
#   GET servers/main/logs?path=logs/../kronwerke/shots/bundle/index.json&lines=5
# A small index comes back inline and is not saved: write its line into a file and pass that as fourth argument.
# Names come from the server, so a stray picture with the same prefix (an old test shot) cannot shift the rest.
import json, sys, base64, os, glob
tag, out, since = sys.argv[1], sys.argv[2], float(sys.argv[3])
os.makedirs(out, exist_ok=True)
T = '/root/.claude/projects/-home-claude/5104831e-b480-51ad-a455-43f4ce763a04/tool-results'
pieces = {}; index = None
for f in sorted(glob.glob(T + '/mcp-Elchi_Ops-api_request-*.txt'), key=os.path.getmtime):
    if os.path.getmtime(f) * 1000 < since: continue
    try:
        d = json.load(open(f)); data = d['json']['data']
    except Exception:
        continue
    if isinstance(data, dict) and str(data.get('path', '')).startswith('kronwerke/shots/bundle/') and data['path'].endswith('.bin'):
        pieces[int(data['path'][-7:-4])] = base64.b64decode(data['data'])
    elif isinstance(data, list) and data and str(data[0]).startswith('{"size"'):
        index = json.loads(data[0])
if len(sys.argv) > 4: index = json.loads(open(sys.argv[4]).read())
assert index, 'no index: fetch it, or pass a file with it as fourth argument'
blob = b''.join(pieces[i] for i in range(index['pieces']))
assert len(blob) == index['size'], (len(blob), index['size'])
n = 0
for e in index['files']:
    data = blob[e['offset']:e['offset'] + e['length']]
    assert data[:8] == b'\x89PNG\r\n\x1a\n', e['name']
    if not e['name'].startswith(tag): continue
    open(os.path.join(out, e['name'][len(tag):] + '.png'), 'wb').write(data); n += 1
print('pieces', index['pieces'], 'bytes', len(blob), 'pictures', n, 'of', len(index['files']))
