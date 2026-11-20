#!/usr/bin/env python3
"""Look things up while writing the web help for quests (tools/quests/help).

Everything comes from the real pack: the recipe dump of the full server
(srv/kronwerke-dump/recipes.json, written by Core's dump command), the lang files of the mod
jars, the stage files and the exported book (web.py).

  helpq.py quest CHAPTER [NAME]   the quest(s) as the book has them: German text, tasks, rewards, deps
  helpq.py item ID                German/English name, stage, every recipe that makes it
  helpq.py uses ID [N]            recipes that use the item (first N, default 15)
  helpq.py find WORDS             items whose German or English name or id contains all words
  helpq.py recipe RECIPE_ID       one recipe in full (raw json)
  helpq.py lang KEYPART           lang lines (de and en) whose key contains KEYPART, first 30

Environment: KW_SRV (default /home/claude/kw/srv), KW_BOOK (exported book, default
/home/claude/kw/qbook), KW_CACHE (default /home/claude/kw/qhelp-cache).
"""
import glob
import json
import os
import re
import sys
import zipfile

SRV = os.environ.get("KW_SRV", "/home/claude/kw/srv")
BOOK = os.environ.get("KW_BOOK", "/home/claude/kw/qbook")
CACHE = os.environ.get("KW_CACHE", "/home/claude/kw/qhelp-cache")
GAME_JAR = os.environ.get("KW_GAME_JAR", "/home/claude/kw/mcclient/versions/1.21.1/1.21.1.jar")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STAGES = os.path.join(ROOT, "kubejs", "data", "kronwerke", "chapters", "stages")


def build_cache():
    os.makedirs(CACHE, exist_ok=True)
    lang = {"de_de": {}, "en_us": {}}
    jars = sorted(glob.glob(os.path.join(SRV, "mods", "*.jar"))) + [GAME_JAR]
    for p in jars:
        try:
            z = zipfile.ZipFile(p)
        except (OSError, zipfile.BadZipFile):
            continue
        for n in z.namelist():
            m = re.match(r"assets/[^/]+/lang/(de_de|en_us)\.json$", n)
            if m:
                try:
                    lang[m.group(1)].update(json.loads(z.read(n).decode("utf-8", "replace")))
                except ValueError:
                    pass
    for f in glob.glob(os.path.join(ROOT, "kubejs", "assets", "*", "lang", "*.json")):
        loc = os.path.basename(f)[:-5]
        if loc in lang:
            try:
                lang[loc].update(json.load(open(f, encoding="utf-8")))
            except ValueError:
                pass
    with open(os.path.join(CACHE, "lang.json"), "w") as f:
        json.dump(lang, f, ensure_ascii=False)
    recipes = json.load(open(os.path.join(SRV, "kronwerke-dump", "recipes.json")))["recipes"]
    by_result, uses = {}, {}
    for r in recipes:
        res = r.get("result")
        if res:
            by_result.setdefault(res, []).append(r["id"])
        for i in set(ingredients(r["json"])):
            uses.setdefault(i, []).append(r["id"])
    with open(os.path.join(CACHE, "index.json"), "w") as f:
        json.dump({"by_result": by_result, "uses": uses}, f)
    with open(os.path.join(CACHE, "recipes.json"), "w") as f:
        json.dump({r["id"]: r["json"] for r in recipes}, f)


def ingredients(j, out=None, top=True):
    """item ids and #tags anywhere in a recipe, except its result."""
    if out is None:
        out = []
    if isinstance(j, dict):
        for k, v in j.items():
            if top and k in ("result", "results", "output", "outputs", "result_item"):
                continue
            if k in ("item", "id") and isinstance(v, str) and ":" in v:
                out.append(v)
            elif k == "tag" and isinstance(v, str):
                out.append("#" + v)
            else:
                ingredients(v, out, False)
    elif isinstance(j, list):
        for v in j:
            ingredients(v, out, False)
    return out


def load():
    if not os.path.exists(os.path.join(CACHE, "index.json")):
        build_cache()
    lang = json.load(open(os.path.join(CACHE, "lang.json")))
    index = json.load(open(os.path.join(CACHE, "index.json")))
    return lang, index


def name(lang, iid, loc):
    if iid.startswith("#"):
        return iid
    ns, path = iid.split(":", 1) if ":" in iid else ("minecraft", iid)
    for k in (f"item.{ns}.{path}", f"block.{ns}.{path}", f"fluid_type.{ns}.{path}", f"fluid.{ns}.{path}",
              f"chemical.{ns}.{path}", f"entity.{ns}.{path}"):
        if k in lang[loc]:
            return lang[loc][k]
    return None


def stage(iid):
    found = None
    for f in sorted(glob.glob(os.path.join(STAGES, "stage*.json"))):
        n = int(re.search(r"stage(\d+)", f).group(1))
        d = json.load(open(f))
        its = d.get("items", [])
        if iid in its or "@" + iid.split(":")[0] in its:
            return n
    return found or 1


def show_recipe(lang, rid, j):
    t = j.get("type", "?")
    ins = ingredients(j)
    counts = {}
    for i in ins:
        counts[i] = counts.get(i, 0) + 1
    parts = []
    for i, c in counts.items():
        n = name(lang, i, "de_de") or name(lang, i, "en_us") or ""
        parts.append(f"{c}x {i}" + (f" ({n})" if n else ""))
    res = json.dumps({k: j[k] for k in j if k in ("result", "results", "output", "outputs")}, ensure_ascii=False)
    extra = {k: j[k] for k in j if k in ("pattern", "processingTime", "processing_time", "heat_requirement", "heatRequirement",
                                           "energy", "mana", "source", "time", "cookingtime", "chemicalInput", "infusionInput",
                                           "fluid", "fluidInput", "pressure", "temperature", "mainInput", "itemInput")}
    print(f"  [{t}] {rid}\n    in: {', '.join(parts)[:600]}\n    out: {res[:300]}")
    if extra:
        print(f"    more: {json.dumps(extra, ensure_ascii=False)[:400]}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "rebuild":
        build_cache()
        print("cache rebuilt")
        return
    if cmd == "quest":
        ch = json.load(open(os.path.join(BOOK, "chapters", args[0] + ".json")))
        qs = [q for q in ch["quests"] if len(args) < 2 or q["name"] == args[1]]
        for q in qs:
            print(f"== {ch['name']}/{q['name']}  (chapter stage {ch['stage']})")
            print("title:", q["title"]["de"])
            if q.get("subtitle"):
                print("subtitle:", q["subtitle"]["de"])
            for line in q["description"]["de"]:
                print("  |", line)
            print("tasks:", json.dumps(q.get("tasks", []), ensure_ascii=False))
            print("rewards:", json.dumps(q.get("rewards", []), ensure_ascii=False)[:300])
            print("deps:", q.get("deps", []))
        return
    lang, index = load()
    recipes = None
    if cmd in ("item", "uses", "recipe"):
        recipes = json.load(open(os.path.join(CACHE, "recipes.json")))
    if cmd == "item":
        iid = args[0]
        print(f"{iid}: de={name(lang, iid, 'de_de')!r} en={name(lang, iid, 'en_us')!r} stage={stage(iid)}")
        rs = index["by_result"].get(iid, [])
        print(f"{len(rs)} recipe(s) make it:")
        for rid in rs[:12]:
            show_recipe(lang, rid, recipes[rid])
        print(f"used in {len(index['uses'].get(iid, []))} recipe(s)")
    elif cmd == "uses":
        iid = args[0]
        n = int(args[1]) if len(args) > 1 else 15
        rs = index["uses"].get(iid, [])
        print(f"{len(rs)} recipe(s) use {iid}:")
        for rid in rs[:n]:
            show_recipe(lang, rid, recipes[rid])
    elif cmd == "recipe":
        print(json.dumps(recipes.get(args[0]), ensure_ascii=False, indent=1)[:4000])
    elif cmd == "find":
        words = [w.lower() for w in args]
        hits = []
        for loc in ("de_de", "en_us"):
            for k, v in lang[loc].items():
                m = re.match(r"(item|block)\.([a-z0-9_]+)\.([a-z0-9_/]+)$", k)
                if not m:
                    continue
                hay = (k + " " + v).lower()
                if all(w in hay for w in words):
                    hits.append((f"{m.group(2)}:{m.group(3)}", v))
        seen = set()
        for iid, v in hits:
            if iid in seen:
                continue
            seen.add(iid)
            print(f"{iid}  de={name(lang, iid, 'de_de')!r} en={name(lang, iid, 'en_us')!r}")
            if len(seen) >= 40:
                break
    elif cmd == "lang":
        n = 0
        for k in sorted(lang["en_us"]):
            if args[0] in k:
                print(f"{k}\n  de: {lang['de_de'].get(k)!r}\n  en: {lang['en_us'][k]!r}")
                n += 1
                if n >= 30:
                    break
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
