# 082 ae2/network, controller, autocraft, cpu
#area -4 231 47 256
fill -4 64 231 40 91 256 minecraft:air
fill 41 64 231 47 91 256 minecraft:air
fill -4 60 231 47 62 256 minecraft:stone
fill -4 63 231 47 63 256 minecraft:light_gray_concrete
fill 0 64 237 47 79 237 minecraft:light_gray_concrete
fill 0 64 237 0 79 250 minecraft:light_gray_concrete
setblock 1 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.1"}','{"text": "ae2"}','{"text": "network"}','{"text": ""}']}}
setblock 2 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ dein"}','{"text": "erstes Netz an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 237 11 79 250 minecraft:light_gray_concrete
setblock 3 63 242 ae2:creative_energy_cell
setblock 3 64 242 ae2:energy_acceptor
kw testworld use 3 64 242 east ae2:fluix_glass_cable
kw testworld use 4 64 242 east ae2:fluix_glass_cable
kw testworld use 5 64 242 east ae2:fluix_glass_cable
execute unless block 6 64 242 minecraft:air
setblock 7 64 242 ae2:drive[facing=south,spin=0]
kw testworld use 5 64 242 south ae2:terminal
setblock 12 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.2"}','{"text": "ae2"}','{"text": "controller"}','{"text": ""}']}}
setblock 13 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "ME-Controller"}','{"text": ""}','{"text": ""}']}}
fill 22 64 237 22 79 250 minecraft:light_gray_concrete
setblock 15 63 242 ae2:creative_energy_cell
fill 15 64 242 15 66 242 ae2:controller
kw testworld use 15 64 242 east ae2:fluix_smart_cable
kw testworld use 16 64 242 east ae2:fluix_smart_cable
kw testworld use 17 64 242 east ae2:fluix_smart_cable
kw testworld use 18 64 242 east ae2:fluix_smart_cable
execute unless block 18 64 242 minecraft:air
setblock 19 64 242 ae2:drive[facing=south,spin=0]
setblock 18 65 242 ae2:drive[facing=south,spin=0]
kw testworld use 16 64 242 south ae2:terminal
setblock 23 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.3"}','{"text": "ae2"}','{"text": "autocraft"}','{"text": ""}']}}
setblock 24 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Molekularassembler"}','{"text": "daneben"}','{"text": ""}']}}
fill 32 64 237 32 79 250 minecraft:light_gray_concrete
setblock 27 63 242 ae2:creative_energy_cell
setblock 27 64 242 ae2:pattern_provider[push_direction=all]
setblock 26 64 242 ae2:molecular_assembler
setblock 28 64 242 ae2:molecular_assembler
setblock 27 65 242 ae2:molecular_assembler
setblock 33 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082.4"}','{"text": "ae2"}','{"text": "cpu"}','{"text": ""}']}}
setblock 34 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Fertigungs-CPU"}','{"text": ""}','{"text": ""}']}}
fill 42 64 237 42 79 250 minecraft:light_gray_concrete
setblock 36 63 243 ae2:creative_energy_cell
fill 36 64 242 37 65 242 ae2:crafting_unit[formed=false]
fill 36 64 243 37 64 243 ae2:1k_crafting_storage[formed=false]
setblock 36 65 243 ae2:crafting_monitor[facing=south,formed=false]
setblock 37 65 243 ae2:crafting_accelerator[formed=false]
