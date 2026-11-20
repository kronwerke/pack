#!/usr/bin/env python3
"""Exports the quest book for the website (kronwerke.com/questbuch).

Usage: web.py OUT_DIR MODS_DIR [MINECRAFT_JAR] [CORE_JAR]

Writes, from the same chapters build.py turns into FTB Quests files:
  OUT_DIR/book.json             groups and chapters in book order, titles in German and English
  OUT_DIR/chapters/<name>.json  one chapter: quests with their place after layout.py, texts in both
                                languages, tasks, rewards, dependencies (by quest name), canvas pictures
  OUT_DIR/items.json            every item the book names: German and English name, mod, stage
  OUT_DIR/tex/<ns>/<path>.png   every picture the book shows: camera shots, banners, item textures
  OUT_DIR/help/<chapter>.json   the hand written help of tools/quests/help, if there is any

Texts keep the book's own markup: & colour codes, {image:ns:path width:w height:h align:a} and
{key:name}; the website renders them. Item names come from the mod jars' lang files, so the
website says what the game says.
"""
import glob
import importlib
import io
import json
import os
import re
import shutil
import sys
import zipfile

here = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(here))
sys.path.insert(0, here)
import ftbq  # noqa: E402
import layout  # noqa: E402

STAGES = os.path.join(ROOT, "kubejs", "data", "kronwerke", "chapters", "stages")
ASSETS = os.path.join(ROOT, "kubejs", "assets")
IMAGE = re.compile(r"\{image:([a-z0-9_.-]+:[a-z0-9_./-]+)")


def load_chapters():
    for f in sorted(os.listdir(os.path.join(here, "chapters"))):
        if f.endswith(".py") and not f.startswith("_"):
            importlib.import_module("chapters." + f[:-3])
    # banners are made by the build; their kind decides how layout.py places a heading
    return ftbq._chapters


def stage_of():
    """item id -> first stage that lists it (or its namespace as @ns); 1 when none does."""
    items, spaces = {}, {}
    for f in sorted(glob.glob(os.path.join(STAGES, "stage*.json"))):
        n = int(re.search(r"stage(\d+)", f).group(1))
        with open(f) as fh:
            d = json.load(fh)
        for i in d.get("items", []):
            if i.startswith("@"):
                spaces.setdefault(i[1:], n)
            else:
                items.setdefault(i, n)
    return lambda i: items.get(i) or spaces.get(i.split(":")[0]) or 1


class Jars:
    """Lang files and textures from the mod jars, the game jar and the Core jar."""

    def __init__(self, paths):
        self.zips = []
        for p in paths:
            try:
                self.zips.append(zipfile.ZipFile(p))
            except (zipfile.BadZipFile, OSError):
                pass
        self.lang = {"de_de": {}, "en_us": {}}
        for z in self.zips:
            for n in z.namelist():
                m = re.match(r"assets/[^/]+/lang/(de_de|en_us)\.json$", n)
                if m:
                    try:
                        self.lang[m.group(1)].update(json.loads(z.read(n).decode("utf-8", "replace")))
                    except ValueError:
                        pass
        # the pack's own lang files win, like in the game (KubeJS loads after the mods)
        for f in glob.glob(os.path.join(ASSETS, "*", "lang", "*.json")):
            loc = os.path.basename(f)[:-5]
            if loc in self.lang:
                with open(f, encoding="utf-8") as fh:
                    try:
                        self.lang[loc].update(json.load(fh))
                    except ValueError:
                        pass
        self.index = {}
        for z in self.zips:
            for n in z.namelist():
                if n.startswith("assets/") and n.endswith(".png"):
                    self.index.setdefault(n, z)

    def name(self, iid, loc):
        ns, path = iid.split(":", 1)
        for key in (f"item.{ns}.{path}", f"block.{ns}.{path}", f"entity.{ns}.{path}", f"fluid.{ns}.{path}"):
            t = self.lang[loc].get(key)
            if t:
                return t
        if loc == "de_de":
            return self.name(iid, "en_us")
        return path.replace("_", " ").title()

    def texture(self, tex):
        """bytes of ns:textures/....png, from the pack's assets first, then the jars."""
        ns, path = tex.split(":", 1)
        local = os.path.join(ASSETS, ns, path)
        if os.path.exists(local):
            with open(local, "rb") as f:
                return f.read()
        z = self.index.get(f"assets/{ns}/{path}")
        return z.read(f"assets/{ns}/{path}") if z else None


def collect_items(value, out):
    """every item id in a task, reward or icon."""
    if isinstance(value, dict):
        if "id" in value and isinstance(value["id"], str) and ":" in value["id"] and "count" in value:
            out.add(value["id"])
        for k, v in value.items():
            if k in ("item", "icon") and isinstance(v, str) and ":" in v:
                out.add(v)
            collect_items(v, out)
    elif isinstance(value, list):
        for v in value:
            collect_items(v, out)


def main():
    out, mods = sys.argv[1], sys.argv[2]
    extra = sys.argv[3:]
    chapters = load_chapters()
    de_en = ftbq._translations("en_us")
    tr = lambda v: ftbq.translate(v, de_en)
    stage = stage_of()

    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(os.path.join(out, "chapters"))

    groups = [{"name": g, "title": {"de": t, "en": tr(t)}} for g, t in ftbq._groups]
    banner_kind = lambda tex: ftbq._banners.get(tex, ("", "section", ""))[1]
    items, textures = set(), set()
    book = []
    for i, ch in enumerate(chapters):
        layout.layout(ch, banner_kind)
        quests = []
        for q in ch["quests"]:
            desc = list(q["description"])
            shot = ftbq._shot(ch["name"], q["name"])
            if shot:
                desc = [shot] + desc
            for line in desc:
                textures.update(IMAGE.findall(line))
            tasks = []
            for t in q["tasks"]:
                t = dict(t)
                if "title" in t:
                    t["title"] = {"de": t["title"], "en": tr(t["title"])}
                tasks.append(t)
            rewards = []
            for r in q["rewards"]:
                r = dict(r)
                if r.get("type") == "loot":
                    tbl = ftbq._tables.get(r["table"], {})
                    r["title"] = {"de": tbl.get("title", r["table"]), "en": tr(tbl.get("title", r["table"]))}
                    r["icon"] = tbl.get("icon")
                rewards.append(r)
            d = {"name": q["name"], "id": ftbq.qid("quest", ch["name"], q["name"]), "x": q["x"], "y": q["y"],
                 "title": {"de": q["title"], "en": tr(q["title"])},
                 "subtitle": {"de": q["subtitle"], "en": tr(q["subtitle"])} if q["subtitle"] else None,
                 "description": {"de": desc, "en": tr(desc)},
                 "tasks": tasks, "rewards": rewards, "deps": q["deps"], "icon": q["icon"],
                 "size": q["size"], "shape": q["shape"], "optional": q["optional"], "hide": q["hide"]}
            collect_items([tasks, rewards, q["icon"]], items)
            quests.append({k: v for k, v in d.items() if not (v is None or v is False or v == [] or v == "")})
        images = []
        for im in ch["images"]:
            textures.add(im["image"])
            images.append({"image": im["image"], "x": im["x"], "y": im["y"], "w": im["width"], "h": im["height"],
                           "rot": im["rotation"], "order": im["order"], "kind": banner_kind(im["image"])
                           if im["image"] in ftbq._banners else "picture"})
        items.add(ch["icon"])
        c = {"name": ch["name"], "title": {"de": ch["title"], "en": tr(ch["title"])},
             "subtitle": {"de": ch["subtitle"], "en": tr(ch["subtitle"])} if ch["subtitle"] else None,
             "icon": ch["icon"], "group": ch["group"], "stage": ch["stage"], "shape": ch["shape"],
             "hideLines": ch["hide_dependency_lines"], "quests": quests, "images": images}
        with open(os.path.join(out, "chapters", ch["name"] + ".json"), "w", encoding="utf-8") as f:
            json.dump({k: v for k, v in c.items() if v is not None}, f, ensure_ascii=False, separators=(",", ":"))
        book.append({"name": ch["name"], "title": c["title"], "icon": ch["icon"], "group": ch["group"],
                     "stage": ch["stage"], "order": ch["order"] if ch["order"] is not None else i,
                     "quests": len(quests)})
    book.sort(key=lambda c: c["order"])
    with open(os.path.join(out, "book.json"), "w", encoding="utf-8") as f:
        json.dump({"groups": groups, "chapters": book}, f, ensure_ascii=False, separators=(",", ":"))

    # the banners are drawn by the build; draw them here too so nothing depends on a build before
    import banners
    tmp = os.path.join(out, ".banners")
    for tex, (text, kind, colour) in ftbq._banners.items():
        ns, path = tex.split(":", 1)
        banners.write(os.path.join(tmp, ns, path), text, kind, colour)

    # items the help names with [[ns:item]] need a name and an icon too
    for f in glob.glob(os.path.join(here, "help", "*.json")):
        try:
            with open(f, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            continue
        items.update(re.findall(r"\[\[([a-z0-9_.-]+:[a-z0-9_./-]+)\]\]", text))

    jars = Jars(sorted(glob.glob(os.path.join(mods, "*.jar"))) + extra)
    names = {}
    for iid in sorted(items):
        if not isinstance(iid, str) or ":" not in iid:
            continue
        names[iid] = {"de": jars.name(iid, "de_de"), "en": jars.name(iid, "en_us"), "stage": stage(iid)}
    with open(os.path.join(out, "items.json"), "w", encoding="utf-8") as f:
        json.dump(names, f, ensure_ascii=False, separators=(",", ":"))

    # names of what is not an item: mobs of kill tasks, dimensions, keys named in texts
    other = {}
    for ch in chapters:
        for q in ch["quests"]:
            for t in q["tasks"]:
                if t.get("type") == "kill":
                    other[t["entity"]] = "entity"
                elif t.get("type") == "dimension":
                    other[t["dimension"]] = "dimension"
            for line in q["description"]:
                for k in re.findall(r"\{key:([A-Za-z0-9_.$-]+)\}", line):
                    other[k] = "key"
    words = {}
    for k, kind in sorted(other.items()):
        if kind == "key":
            de, en = jars.lang["de_de"].get(k), jars.lang["en_us"].get(k)
        else:
            ns, path = k.split(":", 1)
            lk = f"entity.{ns}.{path}" if kind == "entity" else f"dimension.{ns}.{path}"
            en = jars.lang["en_us"].get(lk)
            de = jars.lang["de_de"].get(lk)
        human = k.split(":")[-1].split(".")[-1].replace("_", " ").title()
        words[k] = {"de": de or en or human, "en": en or human}
    with open(os.path.join(out, "words.json"), "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, separators=(",", ":"))

    missing = []
    for tex in sorted(textures):
        ns, path = tex.split(":", 1)
        data = None
        drawn = os.path.join(tmp, ns, path)
        if os.path.exists(drawn):
            with open(drawn, "rb") as f:
                data = f.read()
        else:
            data = jars.texture(tex)
        if data is None:
            missing.append(tex)
            continue
        # webp next to the png's name: camera shots lossy (a third of the size), the rest lossless
        dst = os.path.join(out, "tex", ns, path.replace("textures/", "", 1))[:-4] + ".webp"
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        from PIL import Image
        im = Image.open(io.BytesIO(data))
        im = im.convert("RGBA")
        if "/shots/" in path:
            im.convert("RGB").save(dst, quality=82, method=6)
        else:
            im.save(dst, lossless=True, method=6)
    shutil.rmtree(tmp, ignore_errors=True)

    # help files that do not load (one being written right now) are left out, not copied broken
    help_dir = os.path.join(here, "help")
    helped = 0
    if os.path.isdir(help_dir):
        os.makedirs(os.path.join(out, "help"))
        for f in sorted(os.listdir(help_dir)):
            if not f.endswith(".json"):
                continue
            try:
                with open(os.path.join(help_dir, f), encoding="utf-8") as fh:
                    h = json.load(fh)
            except ValueError:
                print("help: skipped", f, "(not valid JSON)")
                continue
            h = {k: {"de": v.get("de", []), "en": v.get("en", [])} for k, v in h.items() if isinstance(v, dict)}
            helped += len(h)
            with open(os.path.join(out, "help", f), "w", encoding="utf-8") as fh:
                json.dump(h, fh, ensure_ascii=False, separators=(",", ":"))
    print(f"help for {helped} quests")

    n = sum(c["quests"] for c in book)
    print(f"{len(book)} chapters, {n} quests, {len(names)} items, {len(textures) - len(missing)} pictures"
          + (f", missing: {', '.join(missing[:10])}" if missing else ""))


if __name__ == "__main__":
    main()
