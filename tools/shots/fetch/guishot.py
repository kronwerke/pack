#!/usr/bin/env python3
# guishot.py <chapter_quest> [x y [width]]: the newest fetched probe picture (960x540 JPEG) cut to the book's 480x270,
# its window in the middle (or with the cut's left top corner at x y), written into the pack as PNG.
# guishot.py <chapter_quest> half: the whole screen at half size instead (for a HUD or a map).
# Always writes /tmp/claude-0/gui/<chapter_quest>.png first to look at; add "take" as last word to copy it into the pack.
import json, sys, glob, os, base64, io
from PIL import Image
args = sys.argv[1:]; take = args and args[-1] == 'take'
if take: args = args[:-1]
name = args[0]
T = '/root/.claude/projects/-home-claude/5104831e-b480-51ad-a455-43f4ce763a04/tool-results'
out = '/tmp/claude-0/gui/' + name + '.png'
if not take:
    f = max(glob.glob(T + '/mcp-Elchi_Ops-api_request-*.txt'), key=os.path.getmtime)
    d = json.load(open(f))['json']['data']
    assert d['path'].endswith('.jpg'), d['path']
    im = Image.open(io.BytesIO(base64.b64decode(d['data']))).convert('RGB')
    assert im.size == (960, 540), im.size
    if len(args) > 1 and args[1] == 'half':
        im = im.resize((480, 270), Image.LANCZOS)
    else:
        x, y = (int(args[1]), int(args[2])) if len(args) > 2 else (240, 135)
        w = int(args[3]) if len(args) > 3 else 480          # a wider cut is scaled down to the book's size
        im = im.crop((x, y, x + w, y + w * 9 // 16))
        if w != 480: im = im.resize((480, 270), Image.LANCZOS)
    os.makedirs('/tmp/claude-0/gui', exist_ok=True)
    im.save(out, 'PNG', optimize=True)
    print(d['path'], '->', out)
else:
    dst = '/home/claude/kw/pack/kubejs/assets/kronwerke/textures/quests/shots/' + name + '.png'
    Image.open(out).save(dst, 'PNG', optimize=True)
    print('taken', dst, os.path.getsize(dst))
