#!/usr/bin/env python3
"""Checks every id in the Chapters stage files against the mod jars.
Usage: check_stages.py <stages dir> <mods dir>"""
import glob, json, os, re, sys, zipfile

sdir, mods = sys.argv[1], sys.argv[2]
known, modids, dims = set(), set(), set()
for jar in os.listdir(mods):
    if not jar.endswith(".jar"):
        continue
    try:
        z = zipfile.ZipFile(os.path.join(mods, jar))
    except zipfile.BadZipFile:
        continue
    names = z.namelist()
    if "META-INF/neoforge.mods.toml" in names:
        for m in re.finditer(r'modId\s*=\s*"([a-z0-9_]+)"', z.read("META-INF/neoforge.mods.toml").decode(errors="replace")):
            modids.add(m.group(1))
    for n in names:
        m = re.match(r"data/([a-z0-9_.-]+)/dimension/([a-z0-9_/]+)\.json$", n)
        if m:
            dims.add(f"{m.group(1)}:{m.group(2)}")
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
dims |= {"minecraft:overworld", "minecraft:the_nether", "minecraft:the_end"}

bad = 0
for f in sorted(glob.glob(os.path.join(sdir, "*.json"))):
    d = json.load(open(f))
    for it in d.get("items", []):
        if it.startswith("@"):
            if it[1:] not in modids:
                print(f"{os.path.basename(f)}: unknown mod {it}"); bad += 1
        elif it.startswith("#") or it.startswith("minecraft:"):
            continue
        elif it not in known:
            print(f"{os.path.basename(f)}: unknown item {it}"); bad += 1
    for dm in d.get("dimensions", []):
        if not dm.startswith("#") and dm not in dims:
            print(f"{os.path.basename(f)}: unknown dimension {dm}"); bad += 1
print(f"{bad} problems")
sys.exit(1 if bad else 0)
