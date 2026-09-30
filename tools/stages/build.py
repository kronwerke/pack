#!/usr/bin/env python3
"""Writes the Chapters stage files from spec.py and the item registry in items.txt.

    python3 tools/stages/build.py            write kubejs/data/kronwerke/chapters/stages/stage2..5.json
    python3 tools/stages/build.py --check    fail when the files are not what the spec gives
    python3 tools/stages/build.py --show ID  print which rule decides an item

items.txt is the item registry of the test server (kubejs/exported/kw_items.json from the
dump script). Refresh it after adding or removing mods, then run this again.
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "kubejs", "data", "kronwerke", "chapters", "stages")
sys.path.insert(0, HERE)
import spec  # noqa: E402


def load_items():
    with open(os.path.join(HERE, "items.txt")) as f:
        return [l.strip() for l in f if l.strip()]


def matcher(entry):
    if entry.startswith("@"):
        ns = entry[1:] + ":"
        return lambda i: i.startswith(ns)
    if entry.startswith("re:"):
        rx = re.compile(entry[3:])
        return lambda i: rx.search(i) is not None
    return lambda i: i == entry


def assign(items):
    stage, why = {}, {}
    unused = []
    index = set(items)
    for n, entries in spec.RULES:
        for e in entries:
            m = matcher(e)
            if not e.startswith(("@", "re:")):
                hits = [e] if e in index else []
            else:
                hits = [i for i in items if m(i)]
            if not hits:
                unused.append(e)
            for i in hits:
                stage[i] = n
                why[i] = e
    return stage, why, unused


def render(stage):
    files = {}
    for n in range(2, 6):
        ids = sorted(i for i, s in stage.items() if s == n)
        d = {}
        if spec.DIMENSIONS.get(n):
            d["dimensions"] = spec.DIMENSIONS[n]
        d["items"] = ids
        text = "{\n"
        if "dimensions" in d:
            text += '  "dimensions": ' + json.dumps(d["dimensions"]) + ",\n"
        text += '  "items": [\n' + ",\n".join("    " + json.dumps(i) for i in ids) + "\n  ]\n}\n"
        files["stage%d.json" % n] = text
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--show", nargs="*")
    a = ap.parse_args()
    items = load_items()
    stage, why, unused = assign(items)
    if a.show:
        for i in a.show:
            print(i, "stage", stage.get(i, 1), "by", why.get(i, "(no rule)"))
        return
    for e in unused:
        print("warning: rule matches nothing:", e)
    files = render(stage)
    bad = False
    for name, text in files.items():
        p = os.path.join(OUT, name)
        old = open(p).read() if os.path.exists(p) else None
        if a.check:
            if old != text:
                print("out of date:", p)
                bad = True
        elif old != text:
            with open(p, "w") as f:
                f.write(text)
    counts = {n: sum(1 for s in stage.values() if s == n) for n in range(2, 6)}
    print("items per stage:", ", ".join("%d: %d" % kv for kv in counts.items()), "of", len(items))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
