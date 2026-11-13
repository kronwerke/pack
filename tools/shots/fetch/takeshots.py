#!/usr/bin/env python3
# takeshots.py <dir of unbundled pictures> [-x name ...]: copies the pictures into the pack's quest book
# (kubejs/assets/kronwerke/textures/quests/shots/<chapter>_<quest>.png), all but the names after -x and
# the quests that show another quest's picture (tools/shots/same.json)
import sys, os, json
from PIL import Image
src = sys.argv[1]
skip = set(sys.argv[3:]) if len(sys.argv) > 2 and sys.argv[2] == '-x' else set()
skip |= {k.replace('/', '_') for k in json.load(open('/home/claude/kw/pack/tools/shots/same.json'))}
dst = '/home/claude/kw/pack/kubejs/assets/kronwerke/textures/quests/shots'
os.makedirs(dst, exist_ok=True)
n = 0
for f in sorted(os.listdir(src)):
    if not f.endswith('.png') or f[:-4] in skip: continue
    # the same picture, packed harder: about a quarter smaller, nothing lost
    Image.open(os.path.join(src, f)).save(os.path.join(dst, f), 'PNG', optimize=True); n += 1
print(n, 'pictures in', dst, 'skipped', sorted(skip))
