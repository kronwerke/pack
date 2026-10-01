# Keys

About 200 mods register keys, and many of their defaults collide: V was the voice chat menu, the first origin skill, the Ars Nouveau spell wheel, the Iron's Spells cast key and three Cataclysm armour abilities at once. Kronwerke ships `config/defaultoptions/keybindings.txt`, which Default Options applies on first start. A key a player already changed is left alone.

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
| Inventory Tweak sort | B | Alt+B | Backpack |
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

Keys that still share a letter on purpose: Space, Shift and Ctrl for the Hexerei broom and the PneumaticCraft jet boots (they only act while flying), and the middle mouse button, which Sophisticated Storage, Immersive Engineering and ExtendedAE use in different screens.

## Changing it

Edit `config/defaultoptions/keybindings.txt`. One line per mapping: `key_<mapping>:key.keyboard.<key>:<NONE|CONTROL|SHIFT|ALT>`. Default Options only sets a key that is still on its mod default, so players who already changed a key keep their own.
