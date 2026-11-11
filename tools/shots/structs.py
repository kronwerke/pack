#!/usr/bin/env python3
"""Structures the mods ship, for the screenshot world.

A scene should stand the way its mod builds it, so scenes take their layout from the mod's
own files wherever there is one: Create's Ponder scenes (assets/create/ponder), Immersive
Engineering's multiblocks (data/immersiveengineering/structure/multiblocks), Occultism's
pentacles (data/occultism/modonomicon/multiblocks) and the like.

  structs.py list <pattern>                 structure files in the mod jars matching a pattern
  structs.py show <jar part> <path in jar>  a structure layer by layer, with its legend
  structs.py vendor <jar part> <path> <name>  copies it to kubejs/data/kronwerke/structure/shots/<name>.nbt

The mod jars are looked up in $KW_MODS (folders separated by ':'), by default the local
client and server installs.
"""
import glob
import gzip
import io
import json
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
MODS = os.environ.get("KW_MODS", "/home/claude/kw/clientmods/mods:/home/claude/kw/srv/mods").split(":")
VENDOR = os.path.join(ROOT, "kubejs", "data", "kronwerke", "structure", "shots")


def jar(part):
    """The first jar whose file name contains part."""
    for d in MODS:
        for f in sorted(glob.glob(os.path.join(d, "*.jar"))):
            if part.lower() in os.path.basename(f).lower():
                return f
    raise FileNotFoundError(f"no jar matching {part} in {MODS}")


def raw(part, path):
    with zipfile.ZipFile(jar(part)) as z:
        return z.read(path)


def load(part, path):
    """-> (size, palette [state string], blocks [(x, y, z, palette index, has nbt)], entities)"""
    import nbtlib
    data = raw(part, path)
    try:
        data = gzip.decompress(data)
    except OSError:
        pass
    root = nbtlib.File.parse(io.BytesIO(data))
    return parse(root)


def load_file(path):
    import nbtlib
    return parse(nbtlib.load(path))


def state(entry):
    name = str(entry["Name"])
    props = entry.get("Properties")
    if props:
        name += "[" + ",".join(f"{k}={v}" for k, v in sorted(props.items())) + "]"
    return name


def parse(root):
    size = tuple(int(v) for v in root["size"])
    palette = [state(p) for p in root["palette"]]
    blocks = [(int(b["pos"][0]), int(b["pos"][1]), int(b["pos"][2]), int(b["state"]), "nbt" in b) for b in root["blocks"]]
    return size, palette, blocks, root.get("entities", [])


def show(size, palette, blocks, out=sys.stdout):
    """Layers from the bottom up, north at the top: x runs right, z runs down."""
    used = sorted({b[3] for b in blocks if not palette[b[3]].startswith("minecraft:air")})
    sym = {}
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*+=<>?"
    for i, p in enumerate(used):
        sym[p] = chars[i % len(chars)]
    at = {(x, y, z): p for x, y, z, p, _ in blocks}
    has_nbt = {(x, y, z) for x, y, z, _, n in blocks if n}
    print(f"size x={size[0]} y={size[1]} z={size[2]}", file=out)
    for y in range(size[1]):
        rows = []
        for z in range(size[2]):
            rows.append("".join(sym.get(at.get((x, y, z)), ".") for x in range(size[0])))
        if all(set(r) <= {"."} for r in rows):
            continue
        print(f"y={y}", file=out)
        for r in rows:
            print("  " + r, file=out)
    for p in used:
        n = sum(1 for b in blocks if b[3] == p)
        print(f"  {sym[p]} = {palette[p]}  x{n}", file=out)
    print(f"  ({len(has_nbt)} blocks with data)", file=out)


def vendor(part, path, name):
    os.makedirs(os.path.dirname(os.path.join(VENDOR, name + ".nbt")), exist_ok=True)
    with open(os.path.join(VENDOR, name + ".nbt"), "wb") as fh:
        fh.write(raw(part, path))
    return f"kronwerke:shots/{name}"


def modonomicon(part, path):
    """A Modonomicon dense multiblock -> (layers top down as the file has them, mapping)."""
    js = json.loads(raw(part, path))
    return js["pattern"], js["mapping"]


def main():
    cmd = sys.argv[1]
    if cmd == "list":
        pat = sys.argv[2].lower()
        seen = set()
        for d in MODS:
            for f in sorted(glob.glob(os.path.join(d, "*.jar"))):
                try:
                    names = zipfile.ZipFile(f).namelist()
                except zipfile.BadZipFile:
                    continue
                for n in names:
                    if pat in n.lower() and (n.endswith(".nbt") or "multiblock" in n) and (os.path.basename(f), n) not in seen:
                        seen.add((os.path.basename(f), n))
                        print(os.path.basename(f), n)
    elif cmd == "show":
        show(*load(sys.argv[2], sys.argv[3])[:3])
    elif cmd == "vendor":
        print(vendor(sys.argv[2], sys.argv[3], sys.argv[4]))


if __name__ == "__main__":
    main()
