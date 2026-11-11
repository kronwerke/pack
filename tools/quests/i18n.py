#!/usr/bin/env python3
"""The English quest book: which German lines still need a translation, and taking new ones in.

  i18n.py status                 how much is translated, per chapter
  i18n.py todo <chapter> [n]     the next n (default 150) untranslated lines of a chapter as JSON
                                 ({"German": ""}), in quest order; "next" picks the first chapter
                                 in book order that still has some
  i18n.py merge <file.json>      takes {"German": "English"} into i18n/en_us.json, after checking
                                 that colour codes, images and placeholders are kept
  i18n.py check                  the whole table against the rules merge uses

Translations are kept by the German text (see ftbq._translations): a changed quest needs only
its changed lines again.
"""
import collections
import importlib
import json
import os
import re
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import ftbq  # noqa: E402

TABLE = os.path.join(here, "i18n", "en_us.json")
CODES = re.compile(r"&[0-9a-fk-or]|\{[^}]*\}|%[sd]|\\n")


def load():
    with open(TABLE, encoding="utf-8") as f:
        return json.load(f)


def save(table):
    with open(TABLE, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(table.items())), f, ensure_ascii=False, indent=0)
        f.write("\n")


def lines_by_chapter():
    """chapter name -> German lines in book order (each once)."""
    for f in sorted(os.listdir(os.path.join(here, "chapters"))):
        if f.endswith(".py") and not f.startswith("_"):
            importlib.import_module("chapters." + f[:-3])
    out = collections.OrderedDict()
    seen = set()
    common = [t for _, t in ftbq._groups] + [ftbq.FILE_TITLE] + [t["title"] for t in ftbq._tables.values()]
    out["_book"] = [s for s in common if not (s in seen or seen.add(s))]
    chapters = sorted(ftbq._chapters, key=lambda c: (c["order"] is None, c["order"] or 0))
    for ch in chapters:
        lang = {}
        ftbq._build_chapter(ch, 0, lang)
        lines = []
        for v in lang.values():
            for s in (v if isinstance(v, list) else [v]):
                if isinstance(s, str) and s.strip() and s not in seen:
                    seen.add(s)
                    lines.append(s)
        out[ch["name"]] = lines
    return out


def problems(de, en):
    if not isinstance(en, str) or not en.strip():
        return "empty"
    if sorted(CODES.findall(de)) != sorted(CODES.findall(en)):
        return "codes differ: %s vs %s" % (sorted(CODES.findall(de)), sorted(CODES.findall(en)))
    if de.count("&") != en.count("&"):
        return "a different number of &"
    return None


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    table = load()
    if cmd == "status":
        total = done = 0
        for name, lines in lines_by_chapter().items():
            n = sum(1 for s in lines if s in table)
            total += len(lines)
            done += n
            if n < len(lines):
                print(f"{name:28} {n:5}/{len(lines):5}  {sum(len(s) for s in lines if s not in table):7} chars left")
        print(f"total {done}/{total} lines")
    elif cmd == "todo":
        want = sys.argv[2]
        n = int(sys.argv[3]) if len(sys.argv) > 3 else 150
        chapters = lines_by_chapter()
        if want == "next":
            want = next((c for c, ls in chapters.items() if any(s not in table for s in ls)), None)
            if want is None:
                print("{}")
                return
        todo = [s for s in chapters[want] if s not in table][:n]
        print(json.dumps({"chapter": want, "lines": {s: "" for s in todo}}, ensure_ascii=False, indent=1))
    elif cmd == "merge":
        with open(sys.argv[2], encoding="utf-8") as f:
            new = json.load(f)
        if "lines" in new:
            new = new["lines"]
        bad = 0
        for de, en in new.items():
            why = problems(de, en)
            if why:
                bad += 1
                print(f"skipped ({why}): {de[:80]}")
                continue
            table[de] = en
        save(table)
        print(f"merged {len(new) - bad}, skipped {bad}, table has {len(table)}")
    elif cmd == "check":
        bad = [(de, problems(de, en)) for de, en in table.items() if problems(de, en)]
        for de, why in bad:
            print(f"{why}: {de[:80]}")
        print(f"{len(table)} lines, {len(bad)} with problems")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
