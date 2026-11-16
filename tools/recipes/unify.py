#!/usr/bin/env python3
"""Works out Almost Unified's settings: which mod's item stands for each material and form.

usage: unify.py <tags.txt> [--write]

tags.txt is Almost Unified's own dump of the tags it unifies with every item in them
(`logs/almostunified/debug/tags.txt` of a server started with `dump_tags` true in
`config/almostunified/debug.json`). Without --write the choices are only printed.

The rule: the item of the lowest stage wins, so that nothing a stage can make turns into a
locked item; between items of the same stage the order of ORDER decides. One mod per material
where that costs no stage (ingot, block, nugget and dust of lead are all Mekanism's). Ores are
left alone: every mod's ore block stays in the world and in the recipe viewer, loot
unification makes them all drop the same raw material.

--write writes `config/almostunified/unification/materials.json` and puts the chosen items in
place of the others in the quest chapters (`tools/quests/chapters`).
"""
import collections
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.normpath(os.path.join(HERE, '..', '..'))

# earlier wins among items of the same stage; a mod that is not listed is never chosen
ORDER = ["minecraft", "kubejs", "create", "mekanism", "immersiveengineering", "occultism", "silentgear",
         "createaddition", "enderio", "oritech", "powergrid", "createdeco", "eidolon_repraised", "mekmm", "malum",
         "eternal_starlight", "irons_spellbooks", "appflux", "extendedae", "ae2", "industrialforegoing",
         "justdirethings", "pneumaticcraft", "nuclearcraft"]
# in a material's tag but not that material: a tier of its own, a shard, or a thing with a use of its own
# (Power Grid's wires are strung between terminals, they are no crafting part)
IGNORE = ["oritech:biosteel_ingot", "silentgear:diamond_shard", "silentgear:emerald_shard", "create:sturdy_sheet",
          "powergrid:wire", "powergrid:golden_wire", "powergrid:iron_wire"]
# the whole material from one mod although another has a form a stage earlier (Silent Gear's bronze
# ingot is open in stage 1, but bronze needs tin, which is stage 2)
HOME = {"bronze": "mekanism"}
TAGS = ["c:dusts/{material}", "c:gears/{material}", "c:gems/{material}", "c:ingots/{material}",
        "c:nuggets/{material}", "c:plates/{material}", "c:raw_materials/{material}", "c:rods/{material}",
        "c:storage_blocks/raw_{material}", "c:storage_blocks/{material}", "c:wires/{material}"]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    write = '--write' in sys.argv
    tags = {}
    for line in open(args[0]):
        if '=>' in line:
            t, items = line.split('=>')
            tags[t.strip()] = [x.strip() for x in items.split(',') if x.strip()]
    stage = {}
    for n in (2, 3, 4, 5):
        d = json.load(open(os.path.join(PACK, 'kubejs/data/kronwerke/chapters/stages/stage%d.json' % n)))
        for it in d.get('items', []):
            if isinstance(it, str):
                stage[it] = n

    def mod(i):
        return i.split(':')[0]

    def rank(m):
        return ORDER.index(m) if m in ORDER else 999

    def best(items):
        return min(items, key=lambda i: (stage.get(i, 1), rank(mod(i))))

    mats = collections.defaultdict(dict)
    for t, items in tags.items():
        kind, mat = t.split(':')[1].split('/', 1)
        if kind == 'ores':
            continue
        items = [i for i in items if i not in IGNORE]
        mats[mat.replace('raw_', '') if kind == 'storage_blocks' else mat][t] = items
    home = {}
    for mat, ts in mats.items():
        for k in ('c:ingots/' + mat, 'c:gems/' + mat, 'c:dusts/' + mat):
            if ts.get(k):
                home[mat] = mod(best(ts[k]))
                break
    home.update(HOME)
    picks, over, mapping = {}, {}, {}
    for mat, ts in sorted(mats.items()):
        for t, items in sorted(ts.items()):
            if len(items) < 2:
                continue
            b = best(items)
            own = [i for i in items if mod(i) == home.get(mat)]
            if own and (stage.get(own[0], 1) <= stage.get(b, 1) or mat in HOME):
                b = own[0]
            picks[t] = b
            default = min(items, key=lambda i: rank(mod(i)))
            if rank(mod(default)) == 999:
                print('no mod of ORDER has an item in', t, items)
            if mod(b) != mod(default):
                over[t] = mod(b)
            for i in items:
                if i != b:
                    mapping[i] = b
        row = ['%s %s (stage %d)' % (t.split(':')[1].split('/')[0], picks[t], stage.get(picks[t], 1))
               for t in sorted(ts) if t in picks]
        if row:
            print('%-12s %s' % (mat, '; '.join(row)))
    print(len(picks), 'tags,', len(over), 'overrides,', len(mapping), 'items give way')
    if not write:
        return
    cfg = {"mod_priorities": ORDER, "priority_overrides": dict(sorted(over.items())),
           "stone_variants": ["stone", "andesite", "deepslate", "diorite", "granite", "netherrack", "end_stone"],
           "tags": TAGS, "ignored_tags": [], "ignored_items": IGNORE,
           "ignored_recipe_types": ["cucumber:shaped_tag"], "ignored_recipe_ids": [],
           "recipe_viewer_hiding": True, "loot_unification": True, "ignored_loot_tables": []}
    path = os.path.join(PACK, 'config/almostunified/unification/materials.json')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(cfg, f, indent=2)
        f.write('\n')
    changed = []
    for f in sorted(glob.glob(os.path.join(PACK, 'tools/quests/chapters/*.py'))):
        s = open(f).read()
        t = s
        for i, b in mapping.items():
            t = re.sub(r'(?<![a-z0-9_:/])' + re.escape(i) + r'(?![a-z0-9_/])', b, t)
        if t != s:
            open(f, 'w').write(t)
            changed.append(os.path.basename(f))
    print('written:', os.path.relpath(path, PACK), '; quest chapters changed:', ', '.join(changed) or 'none')


if __name__ == '__main__':
    main()
