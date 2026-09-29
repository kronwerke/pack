#!/usr/bin/env python3
"""Checks every item id in the built quest files against the lang files inside the mod jars.
Usage: check_items.py <quests dir> <mods dir>"""
import json, os, re, sys, zipfile
qdir, mods = sys.argv[1], sys.argv[2]
ids = set()
for root, _, files in os.walk(qdir):
    for f in files:
        if f.endswith(".snbt"):
            ids |= set(re.findall(r'id: "([a-z0-9_.-]+:[a-z0-9_./-]+)"', open(os.path.join(root, f)).read()))
known = set()
for jar in os.listdir(mods):
    if not jar.endswith(".jar"): continue
    try:
        z = zipfile.ZipFile(os.path.join(mods, jar))
    except zipfile.BadZipFile:
        continue
    for n in z.namelist():
        m = re.match(r"assets/([a-z0-9_.-]+)/lang/en_us\.json$", n)
        if m:
            try:
                d = json.loads(z.read(n))
            except Exception:
                continue
            for k in d:
                mm = re.match(r"(item|block)\.([a-z0-9_.-]+)\.([a-z0-9_./-]+)$", k)
                if mm:
                    known.add(f"{mm.group(2)}:{mm.group(3)}")
# vanilla: accept anything under minecraft:
missing = sorted(i for i in ids if not i.startswith("minecraft:") and i not in known and not i.startswith("ftbquests:"))
print(f"{len(ids)} ids checked, {len(missing)} not found")
for m in missing: print("  ", m)
