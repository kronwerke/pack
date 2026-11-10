# Keys

About 200 mods register 460 keys, and many of their defaults collide: V was the voice chat menu, the first origin skill, the Ars Nouveau spell wheel, the Iron's Spells cast key and three Cataclysm armour abilities at once. Kronwerke ships `config/defaultoptions/keybindings.txt` with every key, written by `tools/keys/layout.py`, which refuses to write while two keys that can act at the same time share a key. Default Options applies it on an instance's first start; for instances started before, Kronwerke Core (0.25.0 on) moves every key that still sits on its mod default to the pack's, once per layout version. A key a player chose is left alone.

## The keys that matter

| Topic | Key | What it does |
|---|---|---|
| Origins | Z, X, C | Skill 1, 2, 3 of the origin |
| Origins | Alt+R | Skill 4 |
| Origins | H | Class skill (Händler, Arkanist and so on) |
| Origins | O | Overview of origin and class |
| Origins | K | Night vision toggle (Tiefgräber) |
| Ars Nouveau | V | Spell selection wheel |
| Ars Nouveau | Ctrl+C | Open the spell book |
| Ars Nouveau | Ctrl+Z, Ctrl+X | Previous and next spell |
| Iron's Spells | R (hold) | Spell wheel |
| Iron's Spells | Ctrl+V | Cast the active spell |
| Map | M | FTB Chunks map and claims |
| JEI | R, U | Recipes and uses (in menus) |
| Ultimine | ` (left of 1) | Vein mining while held |
| Backpack | B | Open the backpack |
| Curios | G | Accessory slots |
| Death | U | Death history (outside menus) |
| Voice chat | Alt+V | Voice chat menu |
| Voice chat | Shift+G | Groups |
| Ponder | W (held) | Create ponder scenes |
| Zoom | Mouse 4 (held) | Zume zoom, scroll for more or less |
| Accessories | I | Accessory slots of Accessories and the Aether |
| Mekanism | N | Tool mode |
| Mekanism | Alt+1 to Alt+4, Alt+0 | MekaSuit head, chest, legs, feet mode; HUD |
| JourneyMap | J | Full map |

## What Kronwerke moved, and why

| Mapping | Default | Kronwerke | Why |
|---|---|---|---|
| Origins skill 1, 2, 3 | V, G, N | Z, X, C | The most used ability keys go next to WASD, away from voice chat |
| Origins skill 4 | B | Alt+R | B is the backpack |
| Vanilla save and load hotbar | C, X | unbound | Makes room for the origin skills; almost nobody uses them |
| Ars Nouveau previous and next spell | Z, X | Ctrl+Z, Ctrl+X | Origins |
| Ars Nouveau open spell book | C | Ctrl+C | Origins |
| Iron's Spells cast | V | Ctrl+V | V stays the Ars wheel |
| Voice chat menu | V | Alt+V | Opened rarely |
| Voice chat groups | G | Shift+G | G is Curios |
| Voice chat mute, disable, hide icons | M, N, H | unbound | Pressed by accident in fights; all three are in the voice chat menu |
| Cataclysm armour abilities | V, V, Y, C | Shift+V, Ctrl+B, Ctrl+Y, Alt+Y | Boss gear, used rarely |
| Inventory Tweak sort | B | Middle mouse | Backpack; one click in any inventory (Samuel, 2026-10-09) |
| Ping Wheel ping | Mouse 5 | Middle mouse | Same button as sorting, in the world instead of a screen (Samuel, 2026-10-09) |
| Vanilla pick block | Middle mouse | Mouse 5 | Makes room for the ping |
| Occultism satchel, ender bag, storage remote | B, V, N | Alt+G, Alt+E, Alt+S | Freed letters |
| Simple Magnets toggle | H | Alt+M | Class skill |
| Ender IO magnet, travel staff | M, G | Shift+M, Ctrl+G | Map and Curios |
| Draconic tool config, place item | C, P | Alt+C, Alt+P | Origins and vanilla social screen |
| Hexerei glasses zoom, broom start | Z, G | Ctrl+H, Alt+J | Origins and Curios |
| Hexerei book recipe and uses | R, U | Ctrl+R, Alt+U | Iron's Spells wheel and death history |
| Hostile Neural Networks deep learner | U | Alt+D | Death history |
| PneumaticCraft armour keys | C, H, U, Y, Ctrl+X | Ctrl+L, Ctrl+P, Ctrl+U, unbound, Ctrl+J | Stage 4 armour, rare |
| Deeper and Darker transmit, boost | V, B | Alt+T, Alt+N | Freed letters |
| Aether invisibility | V | Shift+I | Freed letter |
| Botania corporea request | C | Ctrl+N | Origins |
| Oritech augments | G | Alt+A | Curios |
| Mahou Tsukai circle, displacement, gun | M, H, arrows | Ctrl+M, Shift+H, Alt+arrows | Map, class skill, Ultimine shape |
| Iris reload, toggle, pack menu | R, K, O | F6, Alt+K, Alt+O | Shader keys pressed by accident |
| KubeJS Kubedex, Toast Control clear | K, J | unbound | Developer and cosmetic keys |
| Zume zoom (added in 0.12.2) | Z | Mouse 4 | Z is the first origin skill |
| Zume zoom in, out | =, - | unbound | Scroll while zoomed |
| MekaSuit modes, HUD | V, G, J, B, H | Alt+1 to Alt+4, Alt+0 | Ars wheel, Curios, map, backpack, class skill |
| Mekanism module tweaker | \\ | Alt+\\ | RFTools and JourneyMap |
| JourneyMap waypoint, minimap keys | B, N, G, [, \\, Ctrl+J | Shift+B, rest unbound | All of it is in the map; FTB Chunks has the claims |
| FTB Chunks minimap zoom | =, - | unbound | JourneyMap's minimap zooms with them |
| Accessories screen | H | I | Class skill; the Aether's own I key opened the same screen and is unbound |
| Iron Jetpacks on, hover | G, H | Shift+J, Shift+K | Curios, class skill |
| Building Gadgets settings, anchor, range, undo | G, H, R, U | Alt+B, Ctrl+A, Shift+R, Shift+U | Only while a gadget is in hand, but the plain keys acted too |
| Just Dire Things tool toggle | V | Shift+T | Ars wheel |
| Immersive Engineering magnet | S | Ctrl+S | Walking backwards |
| Supplementaries quiver | V | Alt+Q | Ars wheel |
| Ars Elemental pouch | J | Shift+P | Map |
| EvilCraft fart, exalted crafting, RFTools unmount | P, C, \\ | unbound | Social screen, origin skill, accidental |

Keys that still share a letter on purpose: Space, Shift and Ctrl for the Hexerei broom and the PneumaticCraft jet boots (they only act while flying), and the middle mouse button: in the world it pings, in inventories it sorts, and Sophisticated Storage, Immersive Engineering and ExtendedAE also use it in some of their screens.

## Changing it

Edit `LAYOUT` in `tools/keys/layout.py` and run it with a key dump (a client with Kronwerke Core started with `-Dkronwerke.dumpKeys=<file>` writes one and quits) and Core's `src/main/resources/assets/kronwerke/keys.tsv` as the second argument; it writes `config/defaultoptions/keybindings.txt` and Core's list. Raise `VERSION` in the script, so Core applies the change once more to keys still on a mod default.
