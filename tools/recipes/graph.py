"""The recipe graph of the pack, from a dump of the running server (/kwdump of the test mod).

Reads dump/items.json, dump/recipes.json and the Chapters stage files, and answers:
  which stage every item is in,
  which recipes make an item and from what,
  which mods a mod's items lean on, and which mods lean on it.

Usage:
  python3 tools/recipes/graph.py DUMP_DIR mods            one line per content mod: links in and out
  python3 tools/recipes/graph.py DUMP_DIR mod NAMESPACE   the mod's items: stage, how they are made, who uses them
  python3 tools/recipes/graph.py DUMP_DIR item ID         every recipe that makes the item, and every one that uses it
"""
import collections
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STAGES = os.path.join(ROOT, "kubejs", "data", "kronwerke", "chapters", "stages")

# Namespaces that are plumbing, not content: a recipe that needs them is not "another mod".
PLUMBING = {"minecraft", "c", "neoforge", "forge", "kubejs", "kronwerke", "chapters", "almostunified",
            "framedblocks", "copycats", "chipped", "rechiseled", "supplementaries", "amendments", "quark",
            "botanypots", "everycomp", "handcrafted", "moredelight", "farmersdelight"}

# Recipe types that only reshape or repaint what is there; they are not how a mod is made.
COSMETIC_TYPES = {"minecraft:stonecutting", "mekanism:painting", "mekanism:pigment_extracting", "framedblocks:frame",
                  "minecraft:smithing", "create:sandpaper_polishing", "botanypots:crop", "botanypots:soil",
                  "mekanism:sawing", "create:cutting", "minecraft:crafting_special_armordye", "chipped:alchemy_bench"}

OUT_KEYS = ("result", "results", "output", "outputs", "product", "products", "secondary", "byproduct")


def load(dump):
    items = json.load(open(os.path.join(dump, "items.json")))
    recipes = json.load(open(os.path.join(dump, "recipes.json")))
    stage = {}
    for n in (2, 3, 4, 5):
        p = os.path.join(STAGES, f"stage{n}.json")
        if os.path.exists(p):
            for it in json.load(open(p))["items"]:
                stage.setdefault(it, n)
    tags = collections.defaultdict(set)
    for it in items:
        for t in it["tags"]:
            tags[t].add(it["id"])
    return items, recipes, stage, tags


def refs(node, tags, out=False, acc=None):
    """Item ids in a recipe's json; outputs are the subtrees under OUT_KEYS."""
    if acc is None:
        acc = {"in": set(), "out": set()}
    side = "out" if out else "in"
    if isinstance(node, dict):
        for k in ("item", "id"):
            v = node.get(k)
            if isinstance(v, str) and ":" in v:
                acc[side].add(v)
        t = node.get("tag")
        if isinstance(t, str):
            acc[side].update("#" + t for _ in [0])
        for k, v in node.items():
            if k in ("item", "id", "tag", "type"):
                continue
            refs(v, tags, out or k in OUT_KEYS or k.startswith("result") or k.startswith("output"), acc)
    elif isinstance(node, list):
        for v in node:
            refs(v, tags, out, acc)
    elif isinstance(node, str) and out and ":" in node and not node.startswith("#"):
        acc["out"].add(node)
    return acc


def expand(ids, tags, known):
    """Items behind tags; a tag stays as one entry per mod it holds."""
    flat = set()
    for i in ids:
        if i.startswith("#"):
            members = tags.get(i[1:], set())
            flat.update(m for m in members)
        elif i in known:
            flat.add(i)
    return flat


def ns(i):
    return i.split(":", 1)[0]


def build(dump):
    items, recipes, stage, tags = load(dump)
    known = {it["id"] for it in items}
    makes = collections.defaultdict(list)   # item -> recipes making it
    uses = collections.defaultdict(list)    # item -> recipes using it
    for r in recipes:
        if "json" not in r:
            continue
        a = refs(r["json"], tags)
        outs = {o for o in a["out"] if o in known}
        ins_raw = a["in"] - a["out"]
        # a tag input counts for the mods in it only when it is not a common material tag
        ins = set()
        for i in ins_raw:
            if i.startswith("#"):
                members = tags.get(i[1:], set())
                mods = {ns(m) for m in members}
                ins.add(i if len(mods) > 1 else next(iter(members), i))
            elif i in known:
                ins.add(i)
        rec = {"id": r["id"], "type": r["type"], "in": sorted(ins), "out": sorted(outs)}
        for o in outs:
            makes[o].append(rec)
        for i in ins:
            uses[i].append(rec)
    return items, recipes, stage, tags, makes, uses


def mods_report(dump):
    items, recipes, stage, tags, makes, uses = build(dump)
    by_mod = collections.defaultdict(list)
    for it in items:
        by_mod[ns(it["id"])].append(it["id"])
    rows = []
    for mod, ids in by_mod.items():
        if mod in PLUMBING or len(ids) < 8:
            continue
        lean_on = collections.Counter()
        leaned_by = collections.Counter()
        crafted = 0
        for i in ids:
            rs = [r for r in makes.get(i, []) if r["type"] not in COSMETIC_TYPES]
            if rs:
                crafted += 1
            for r in rs:
                for x in r["in"]:
                    m = "tag" if x.startswith("#") else ns(x)
                    if m not in PLUMBING and m != mod and m != "tag":
                        lean_on[m] += 1
            for r in uses.get(i, []):
                if r["type"] in COSMETIC_TYPES:
                    continue
                for o in r["out"]:
                    m = ns(o)
                    if m not in PLUMBING and m != mod:
                        leaned_by[m] += 1
        st = collections.Counter(stage.get(i, 1) for i in ids)
        rows.append((mod, len(ids), crafted, dict(sorted(st.items())), lean_on, leaned_by))
    rows.sort(key=lambda r: (len(r[4]) + len(r[5]), r[0]))
    for mod, n, crafted, st, lo, lb in rows:
        print(f"{mod:28} items {n:5} made {crafted:5} stages {st}")
        print(f"    leans on  {len(lo):3}: {', '.join(f'{m} {c}' for m, c in lo.most_common(8))}")
        print(f"    leaned by {len(lb):3}: {', '.join(f'{m} {c}' for m, c in lb.most_common(8))}")


def mod_report(dump, mod):
    items, recipes, stage, tags, makes, uses = build(dump)
    names = {it["id"]: it["name"] for it in items}
    ids = sorted(it["id"] for it in items if ns(it["id"]) == mod)
    usage = collections.Counter()
    for i in ids:
        usage[i] = sum(1 for r in uses.get(i, []) if r["type"] not in COSMETIC_TYPES)
    for i in sorted(ids, key=lambda x: (-usage[x], x)):
        rs = [r for r in makes.get(i, []) if r["type"] not in COSMETIC_TYPES]
        other = sorted({x for r in rs for x in r["in"] if (x.startswith("#") or ns(x) not in PLUMBING) and (x.startswith("#") or ns(x) != mod)})
        print(f"{i:55} s{stage.get(i, 1)} used {usage[i]:4} made by {len(rs):2} [{', '.join(sorted({r['type'] for r in rs}))}] {names.get(i, '')}")
        if other:
            print("        from other mods: " + ", ".join(other[:12]))


def item_report(dump, item):
    items, recipes, stage, tags, makes, uses = build(dump)
    print(f"{item} stage {stage.get(item, 1)}")
    print("made by:")
    for r in makes.get(item, []):
        print(f"  {r['id']} [{r['type']}] <- {', '.join(r['in'])}")
    print("used in:")
    for r in uses.get(item, [])[:80]:
        print(f"  {r['id']} [{r['type']}] -> {', '.join(r['out'])}")




def keys_report(dump, mods, top=8):
    """The items each mod leans on most (its bottlenecks), with stage and how they are made now."""
    items, recipes, stage, tags, makes, uses = build(dump)
    names = {it["id"]: it["name"] for it in items}
    for mod in mods:
        ids = [it["id"] for it in items if ns(it["id"]) == mod]
        usage = collections.Counter()
        for i in ids:
            usage[i] = sum(1 for r in uses.get(i, []) if r["type"] not in COSMETIC_TYPES)
        print(f"== {mod} ({len(ids)} items)")
        for i, n in usage.most_common(top):
            if n == 0:
                break
            rs = [r for r in makes.get(i, []) if r["type"] not in COSMETIC_TYPES]
            how = "; ".join(f"{r['type'].split(':')[-1]}<{','.join(x.split(':')[-1] for x in r['in'][:6])}" for r in rs[:3]) or "not crafted"
            print(f"  {i} s{stage.get(i, 1)} used {n} [{names.get(i, '')}] {how}")


if __name__ == "__main__":
    d, what = sys.argv[1], sys.argv[2]
    if what == "mods":
        mods_report(d)
    elif what == "mod":
        mod_report(d, sys.argv[3])
    elif what == "item":
        item_report(d, sys.argv[3])
    elif what == "keys":
        keys_report(d, sys.argv[3].split(","))
