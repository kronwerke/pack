#!/usr/bin/env python3
"""A catalog of what the mods really have, read from their jars: blocks with their state
properties, items, entity types and structure templates. build.py --check holds every scene
against it, so a wrong id or a block state that does not exist shows up before the server
sees it.

Usage: catalog.py <mods folder> <minecraft client jar> [out.json]
       (out defaults to $KW_CATALOG or /tmp/claude-0/cat/catalog.json)
"""
import json
import os
import re
import sys
import zipfile


def states(js):
    """blockstates json -> {property: sorted values}"""
    props = {}

    def add(k, v):
        for one in str(v).split("|"):
            props.setdefault(k, set()).add(one)

    for key in js.get("variants", {}):
        for kv in key.split(","):
            if "=" in kv:
                k, v = kv.split("=", 1)
                add(k, v)

    def when(w):
        if not isinstance(w, dict):
            return
        for k, v in w.items():
            if k in ("OR", "AND"):
                for sub in v:
                    when(sub)
            else:
                add(k, v)

    for part in js.get("multipart", []):
        when(part.get("when"))
    return {k: sorted(v) for k, v in props.items()}


def scan(jar, cat):
    try:
        z = zipfile.ZipFile(jar)
    except zipfile.BadZipFile:
        return
    for name in z.namelist():
        m = re.match(r"assets/([a-z0-9_.-]+)/blockstates/(.+)\.json$", name)
        if m:
            try:
                cat["blocks"][f"{m[1]}:{m[2]}"] = states(json.loads(z.read(name)))
            except (ValueError, KeyError):
                cat["blocks"].setdefault(f"{m[1]}:{m[2]}", {})
            continue
        m = re.match(r"assets/([a-z0-9_.-]+)/models/item/(.+)\.json$", name)
        if m:
            cat["items"].add(f"{m[1]}:{m[2]}")
            continue
        m = re.match(r"data/([a-z0-9_.-]+)/structure/(.+)\.nbt$", name)
        if m:
            cat["structures"].add(f"{m[1]}:{m[2]}")
            continue
        m = re.match(r"assets/([a-z0-9_.-]+)/lang/en_us\.json$", name)
        if m:
            try:
                lang = json.loads(z.read(name))
            except ValueError:
                continue
            for k in lang:
                e = re.match(r"entity\.([a-z0-9_.-]+)\.([a-z0-9_/]+)$", k)
                if e:
                    cat["entities"].add(f"{e[1]}:{e[2]}")
                i = re.match(r"item\.([a-z0-9_.-]+)\.([a-z0-9_/]+)$", k)
                if i:
                    cat["items"].add(f"{i[1]}:{i[2]}")
    # jars inside jars (jarjar)
    for name in z.namelist():
        if name.startswith("META-INF/jarjar/") and name.endswith(".jar"):
            import io
            try:
                scan(io.BytesIO(z.read(name)), cat)
            except Exception:
                pass


def main():
    mods, client = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else os.environ.get("KW_CATALOG", "/tmp/claude-0/cat/catalog.json")
    cat = {"blocks": {}, "items": set(), "entities": set(), "structures": set()}
    scan(client, cat)
    for f in sorted(os.listdir(mods)):
        if f.endswith(".jar"):
            scan(os.path.join(mods, f), cat)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump({"blocks": cat["blocks"], "items": sorted(cat["items"]), "entities": sorted(cat["entities"]),
                   "structures": sorted(cat["structures"])}, fh)
    print(f"{len(cat['blocks'])} blocks, {len(cat['items'])} items, {len(cat['entities'])} entities, "
          f"{len(cat['structures'])} structures -> {out}")


if __name__ == "__main__":
    main()
