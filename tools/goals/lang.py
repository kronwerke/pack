"""The community goals in the lang files.

Core shows a goal's title, description and pillar names through the keys
kronwerke.goal.<goal>.title, .description and .pillar.<pillar>, with goals.json as fallback.
Minecraft loads en_us under every language, so the German file must carry every key too, or
German players would read the English text. This writes the German entries from goals.json
and checks that the English file has one for each.

Usage: lang.py            write the German entries
       lang.py --check    fail when the German file is behind goals.json or English is missing a key
"""
import json
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, "..", "..")
goals = json.load(open(os.path.join(root, "config", "kronwerke", "goals.json"), encoding="utf-8"))
lang = os.path.join(root, "kubejs", "assets", "kronwerke", "lang")

want = {}
for g in goals:
    want[f"kronwerke.goal.{g['id']}.title"] = g.get("title") or g["id"]
    if g.get("description"):
        want[f"kronwerke.goal.{g['id']}.description"] = g["description"]
    for p in g.get("pillars", []):
        want[f"kronwerke.goal.{g['id']}.pillar.{p['id']}"] = p.get("title") or p["id"]


def load(name):
    with open(os.path.join(lang, name + ".json"), encoding="utf-8") as f:
        return json.load(f)


def save(name, data):
    with open(os.path.join(lang, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


de, en = load("de_de"), load("en_us")
stale = sorted(k for k, v in want.items() if de.get(k) != v)
goal_key = re.compile(r"kronwerke\.goal\.[^.]+\.(title|description|pillar\.[^.]+)$")
gone = sorted(k for k in de if goal_key.match(k) and k not in want)
no_en = sorted(k for k in want if k not in en)

if "--check" in sys.argv:
    bad = False
    if stale or gone:
        print("de_de.json is behind goals.json, run tools/goals/lang.py:", *(stale + gone), sep="\n  ")
        bad = True
    if no_en:
        print("en_us.json has no English for:", *no_en, sep="\n  ")
        bad = True
    sys.exit(1 if bad else 0)

for k in gone:
    del de[k]
de.update(want)
save("de_de", de)
print(f"{len(want)} goal keys written to de_de.json; {len(no_en)} without English")
