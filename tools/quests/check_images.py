#!/usr/bin/env python3
"""Checks that every picture the quest book uses exists: on chapter canvases and inside
quest texts. A texture counts as present when a mod jar or kubejs/assets has it.
Vanilla textures are checked against the client jar when one is given.
Usage: check_images.py <quests dir> <mods dir> [kubejs assets dir] [minecraft client jar]"""
import os
import re
import sys
import zipfile

qdir, mods = sys.argv[1], sys.argv[2]
assets = sys.argv[3] if len(sys.argv) > 3 else "kubejs/assets"
client = sys.argv[4] if len(sys.argv) > 4 else None

used = set()
for root, _, files in os.walk(qdir):
    for f in files:
        if f.endswith(".snbt"):
            text = open(os.path.join(root, f)).read()
            used |= set(re.findall(r'image: "([a-z0-9_.-]+:[a-z0-9_./-]+\.png)"', text))
            used |= set(re.findall(r'\{image:([a-z0-9_.-]+:[a-z0-9_./-]+\.png)', text))

have = set()
jars = [os.path.join(mods, j) for j in os.listdir(mods) if j.endswith(".jar")]
if client:
    jars.append(client)
for jar in jars:
    try:
        z = zipfile.ZipFile(jar)
    except zipfile.BadZipFile:
        continue
    for n in z.namelist():
        m = re.match(r"assets/([a-z0-9_.-]+)/(textures/.+\.png)$", n)
        if m:
            have.add(f"{m.group(1)}:{m.group(2)}")
for root, _, files in os.walk(assets):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), assets).split(os.sep)
        if len(rel) > 2 and f.endswith(".png"):
            have.add(f"{rel[0]}:{'/'.join(rel[1:])}")

missing = sorted(u for u in used if u not in have and (client or not u.startswith("minecraft:")))
print(f"{len(used)} pictures checked, {len(missing)} missing")
for m in missing:
    print("  ", m)
sys.exit(1 if missing else 0)
