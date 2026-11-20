# Help for the web quest book

The website (kronwerke.com/questbuch) shows every quest as the game does, plus a short help
text written for the web. One file per chapter: `<chapter>.json`, keyed by quest name.

```json
{
  "quest_name": {
    "de": ["Absatz eins.", "Absatz zwei."],
    "en": ["Paragraph one.", "Paragraph two."],
    "sources": ["create:item_application/andesite_casing_from_log", "config/kronwerke/goals.json"],
    "client": ["what could only be checked in the game client, if anything"]
  }
}
```

## What the help is for

The quest text in the game says what to do. The help says what the quest text does not:

- how exactly: the recipe (machine, ingredients, amounts), the steps in order, the multiblock shape;
- where the materials come from (which mob, ore, biome, structure, machine, earlier quest);
- the usual pitfalls (needs power, needs a stage, needs the right side, consumed or not);
- what it leads to (the next quests or chapters, by name).

Do not repeat the quest text. If the quest is trivial and there is nothing to add, write one
short useful sentence (a tip, where it leads), never filler.

Length: 2 to 5 sentences per language, about 40 to 90 words. One to three paragraphs.

## Everything must be true for this pack

Check every claim against the real data before writing it:

- `python3 tools/quests/helpq.py quest <chapter> [name]`: the quest as the book has it.
- `python3 tools/quests/helpq.py item <id>`: names, stage and every recipe that makes it,
  from the recipe dump of the running full server (KubeJS changes included).
- `python3 tools/quests/helpq.py uses <id>`, `find <words>`, `recipe <id>`, `lang <key part>`.
- Pack configs in `config/`, `defaultconfigs/`, `kubejs/`; Kronwerke rules in `docs/STAGES.md`,
  `docs/SERVER.md`, `config/kronwerke/goals.json`; stage lists in
  `kubejs/data/kronwerke/chapters/stages/`; the mod jars in `/home/claude/kw/srv/mods`
  (lang, data, assets) when a recipe or behaviour is not in the dump.

Put the recipe ids, files or jar paths you used in `sources`. If something can only be seen in
the game (how a GUI looks, a key, an animation, mob behaviour), either leave it out or write it
and list it in `client`, so it gets checked in the test client before it goes live. Never guess
numbers.

## Language and style

- German: du, short clear sentences, the game's German item names (`helpq.py item` shows them;
  if the quest text uses its own name for something, use the quest text's name). English: the
  official English item names, and `tools/quests/i18n/glossary.md` for Kronwerke's own words
  and chapter names. Stage names in English are Stone Works, Brass Works, Steel Works, Star
  Works, Chaos Works. The mining world is the Farmwelt / farm world.
- No dashes as punctuation (no "–", "—", no " - " between words), no emojis, no exclamation
  marks in a row, no "Tipp:" or "Hinweis:" labels, no Markdown headings.
- Markup the website understands:
  - `[[ns:item_id]]` shows the item with its icon and its name in the reader's language.
    Use it for the items that matter, not for every word.
  - `{{chapter/quest}}` links another quest (shows its title).
  - `**bold**` for the one thing not to miss.
- The recipe viewer in this pack is EMI (with JEI underneath); write "EMI".
