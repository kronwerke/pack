# Keys

Kronwerke sets no keys of its own. Every mod keeps its default key, as in other large packs (ATM10 ships no key file, Craftoria changes five keys). Decided by Samuel on 15.11.2026: players who come from other packs find their keys where they know them, and whoever wants another layout sets it in the controls.

What that means:

- **Keys that are bound twice** show red in the controls. With about 200 mods there are many: V is the voice chat menu, the first origin skill and the cast key of Iron's Spells; G is the accessory slots, the second origin skill and the jetpack. Players rebind what they use.
- **The quest book prints the reader's own key.** A quest text names a key as `{key:key.voice_chat}`; `tools/quests/ftbq.py` (`keyed`) turns such a line into a JSON text component with the game's `keybind` part, which shows what the client has bound, with its modifier. Never write a key's letter into a quest text. The names are the ones of the controls (`options.txt`, `key_<name>`); a dump of all of them comes from Kronwerke Core with `-Dkronwerke.dumpKeys=<file>`.
- **KeyBind Bundles** (in the pack) puts several actions on one key as a radial menu, and **KeybindsPurger** adds buttons to the controls that unbind a category or every modded key.
- **Earlier layouts.** Until Pack 0.24.45 the pack moved 68 keys onto modifier combinations and unbound 22, so that nothing clashed (`config/defaultoptions/keybindings.txt`, `tools/keys/layout.py`; both are in the history). Instances from that time still carry those keys. Core's `assets/kronwerke/keys.tsv` (version 2, written by `tools/keys/defaults.py`) moves every key that still sits where the pack had put it back to the mod's default, once; a key the player chose stays.
