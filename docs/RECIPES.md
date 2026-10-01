# Recipes

How Kronwerke changes recipes, and why. The stages decide when a mod opens; the recipes decide how the mods lean on each other once they are open. Stage assignments live in `tools/stages/spec.py`, the recipe changes in `kubejs/server_scripts/kronwerke/`.

## Principles

1. **Not an expert pack.** About a hundred changed recipes in a pack of 34 000. Every change has a reason a player can see in the quest book. No recipe needs more than two mods it does not belong to.
2. **Slow first, fast later.** The first route to a key material is manual and a little painful. A second route opens a stage later and is built for automation: more output per input, but it needs machines. Nobody should hand craft a stage 4 goal.
3. **Tech and magic lean on each other.** Every stage has at least one key tech item that needs magic and one key magic item that needs tech.
4. **One way to a milestone.** When an item is a milestone (brass, charged certus, the precision mechanism), alternative routes from other mods are removed. Compat recipes that would skip a milestone go.
5. **Goal items cannot be made before their stage.** Chapters only stops players from holding locked items, not machines from making them. So the last step of every goal item is either a crafting recipe (Chapters blocks crafting a locked item) or needs a machine or input that is itself locked until that stage. The one exception is on purpose: steel opens in stage 2 and is the bulk item of stage 3, where it has to run by the thousand.

## The ladder

| Stage | Tech milestone | Magic milestone | Storage |
| --- | --- | --- | --- |
| 1 Steinwerk | Andesite alloy, water wheels | Source gems, infused iron | Drawers, copper and iron chests |
| 2 Messingwerk | Brass, precision mechanism, electron tube | Manasteel, mana pearl, terrasteel | Compacting drawers, gold chests |
| 3 Stahlwerk | Steel at scale, advanced circuits, charged certus | Elementium, afrit essence | AE2 up to 16k, Refined Storage up to 16k |
| 4 Sternwerk | Elite circuits, draconium | Gaia spirit, mystic staff | AE2 64k and 256k, MEGA up to 4M, Advanced AE patterns |
| 5 Chaoswerk | Awakened draconium, antimatter | Gaia ingot | MEGA 16M to 256M, bulk cells, the quantum computer |

## Changes by family

The id of each new recipe is `kronwerke:<family>/<name>`. "Remove all" means every recipe that outputs the item, whatever mod adds it (Oritech, Create Crafts & Additions, Advanced AE and Productive Metalworks all add shortcuts).

### Create

| Item | Change | Why |
| --- | --- | --- |
| Brass ingot | Remove all. Heated mixing: 2 copper, 1 zinc, 1 blaze powder gives 1 brass. Superheated mixing: 2 copper, 1 zinc gives 2 brass. Crafting from nuggets and blocks stays. | Brass is the stage 2 milestone. The first ingots cost blaze powder; a blaze cake line doubles the output. |
| Precision mechanism | Remove all. Sequenced assembly on a brass sheet, 5 loops: deploy cogwheel, deploy electron tube, deploy iron nugget, press. 60 percent precision mechanism, the rest brass nuggets and cogwheels as scrap. | Speed controllers, arms and schematicannons should feel earned. |
| Mechanical crafter | Needs a precision mechanism. | Autocrafting with Create needs the milestone. |
| Andesite alloy | Crafting stays 1 per craft. Mixing gives 2. | Stage 1 goal item: hand crafting is slow, a mixer line doubles it. |

### Applied Energistics 2

| Item | Change | Why |
| --- | --- | --- |
| Charged certus quartz | Remove all (charger, Crafts & Additions, Oritech laser, Advanced AE reaction chamber). Ars Nouveau imbuement: certus crystal, 2 000 source, pedestals with redstone and glowstone dust, gives 1. Powah energizing orb: certus crystal and redstone, 20 000 FE, gives 2. | The stage 3 storage entry needs a mage first, a power plant later. |
| Fluix smart cable (and the coloured ones) | 4 covered cable, 2 redstone, 2 glowstone, 1 electron tube gives 4. | Smart cables are a comfort, not a given. |
| ME drive | 2 advanced control circuits in place of 2 of its fluix. | Storage needs Mekanism's circuits. |
| ME controller | Needs a spirit attuned gem from Occultism. | Networks need a ritual. |
| Molecular assembler | 2 precision mechanisms in place of the annihilation and formation cores. | Autocrafting needs Create. |
| Pattern provider | Needs a precision mechanism. | Same. |
| 64k and 256k cell components | Need a Nature's Aura sky ingot (64k) and a draconium ingot (256k). | The big cells are stage 4. |
| MEGA 1M and 4M components | Need a draconium ingot. | Stage 4. |
| MEGA 16M and larger, bulk cell component | Need an awakened draconium nugget. | Stage 5, the millions. |

### Mekanism, Immersive Engineering and other tech

| Item | Change | Why |
| --- | --- | --- |
| Basic control circuit | Remove all. Metallurgic infusing: electron tube and 20 redstone. | Mekanism's first circuit needs Create's rose quartz and brass tier. |
| Advanced control circuit | Remove all. Crafting: basic circuit, 2 infused alloy, 1 AE2 printed silicon. | Stage 3 goal item: only craftable once AE2's inscriber is open. |
| Elite control circuit | Remove all. Crafting: 2 advanced circuits, 2 reinforced alloy, 1 draconium dust. | Stage 4 goal item: needs the End. |
| Ultimate control circuit | Remove all but Mekanism's own crafting. | Stays as it is, stage 4. |
| Steel casing | Andesite alloy in place of glass. | Andesite alloy for Mekanism. |
| Crusher | Crushing wheel from Create in place of the lava bucket. | Mekanism grinds with Create's wheels. |
| Metallurgic infuser | Manasteel (already in `tech_and_magic.js`). | |
| Light engineering block | Brass sheet in place of one copper ingot. | IE's machines need brass. |
| Heavy engineering block | A precision mechanism in place of one steel component. | IE's big machines need Create. |
| Powah energizing orb | A Botania mana diamond on top. | The power mod needs mana to start. |
| Ender IO soul binder | Malum soul stained steel. | The soul side of Ender IO is Malum. |
| Draconic energy core stabilizer | A Gaia spirit. | The dragon's power needs Gaia. |
| Mekanism laser focus matrix | Ars Nouveau source gem block. | Fusion needs magic to start. |
| Awakened draconium (fusion) | Gaia spirit ingots in the injectors. | The finale needs both. |
| Oritech foundry netherite | Removed. | One gold and one scrap made an ingot, a quarter of the vanilla price. |
| Mekanism More Machine replicators | The item replicator copies stones, ores, logs, planks and only iron, copper and gold ingots; the chemical replicator copies nothing (`kubejs/data/mekmm/data_maps/`). | It copied every ingot, including Gaia spirit and awakened draconium ingots of the stage 5 goal, and multiplied fissile fuel and antimatter. |
| PneumaticCraft flux compressor and pneumatic dynamo | A Mekanism basic control circuit instead of the printed circuit board. | The FE side of PneumaticCraft starts with the one circuit route of the pack. |
| PneumaticCraft drone | A precision mechanism under the circuit board. | A flying machine, like the AE2 assembler. |
| Flux Networks core | A source gem instead of the eye of ender. | Wireless power is where magic meets tech. |
| Flux Networks controller | An advanced control circuit in the middle. | The controller is the stage 3 unlock of the mod. |
| Hostile Neural Networks simulation chamber | A source gem block instead of obsidian in the middle. | Simulations run on source. |
| Hostile Neural Networks loot fabricator | An engineering processor instead of the comparator. | The fabricator is a stage 4 machine. |
| Mahou Tsukai Mystic Staff | Summoning costs 2 000 mana instead of 100 (`config/mahoutsukai-server.toml`). | The stage 4 goal asks for 30 staffs, each meant as a real investment of one mage. |

### Magic

| Item | Change | Why |
| --- | --- | --- |
| Manasteel ingot | Remove the pool recipe from iron and Mystical Agriculture's essence recipe. New first route: Nature's Aura ritual of the forest around an oak sapling with 4 infused iron, 2 livingwood twigs, 1 mana diamond and 1 gold leaf, gives 4 manasteel. Mass route: mana pool infusion of infused iron, 3 000 mana. | The first manasteel comes from a ritual, later from a pool fed by an altar. |
| Manasteel block | Pool route removed, crafting from ingots stays. | |
| Mana pearl | Mana pool infusion now needs a brass casing under the pool as catalyst. | Stage 2 goal item: the brass tier gates it, and tech meets magic. |
| Spirit attuned gem | Unlocked in stage 2. Spirit fire from lapis stays; the Ars Ocultas apparatus shortcut goes. | Occultism's stage 2 rituals need it. |
| Runic altar | A brass ingot in place of one livingrock. | Runes need an engineer. |
| Terrestrial agglomeration plate | Brass casings (already in `tech_and_magic.js`). | |
| Elven gateway core | Moves to stage 3 with the whole Alfheim trade. | Elementium is the stage 3 goal. |

### Milestones

One crafted item per pillar in stages 1 to 3, registered in `kubejs/startup_scripts/milestones.js`, recipes in `kubejs/server_scripts/kronwerke/milestones.js`, textures built by `tools/items/compose.py` from CC0 art (credits in `tools/items/sources/CREDITS.md`).

| Stage | Item | Recipe |
| --- | --- | --- |
| 1 | Steinwerk-Getriebe | Andesite casings, a large cogwheel, a mechanical press, a millstone, a water wheel, infused iron |
| 1 | Quellschlussstein | Source gem blocks, a source jar, mana diamonds, andesite alloy, gold leaf |
| 2 | Messingherz | Brass casings, a precision mechanism, electron tubes, a fire rune, a blaze burner |
| 2 | Runenkern | Water, air, fire and earth runes, mana pearls, brass plates, terrasteel |
| 3 | Stahlkern | Heavy engineering blocks, advanced control circuits, engineering processors, a steel casing, elementium |
| 3 | Elfenstern | Dragonstone, pixie dust, afrit essence, reinforced alloy |

### World generation

Draconium ore only generates in the End: the overworld and Nether ore features are switched off in `kubejs/data/draconicevolution/neoforge/biome_modifier/`. Otherwise stage 4's draconium could be mined and smelted on day one.

## Notes for writing recipes

- `event.remove({ output: ... })` misses Oritech's recipes, which list their outputs under `results`. Remove those by id.
- Scripts share one scope. Use `let` inside the event and names that do not clash across files.

## Checking

After a change, on the test server: `/reload`, then read `logs/kubejs/server.log` for errors from the file, then run the progression checker on the fresh dump:

```
python3 tools/check_progression.py /path/to/kubejs/exported/kw_recipes.json /path/to/mods kubejs/data/kronwerke/chapters/stages --goals config/kronwerke/goals.json --quests config/ftbquests/quests --report report.md
```

Every goal item must show up as reachable in its stage and nowhere in the leak list before it.
