# 034 mekanism/ore_line
#area 26 65 48 90
fill 26 64 65 48 91 90 minecraft:air
fill 26 60 65 48 62 90 minecraft:stone
fill 26 63 65 48 63 90 minecraft:light_gray_concrete
fill 30 64 71 48 79 71 minecraft:light_gray_concrete
fill 30 64 71 30 79 84 minecraft:light_gray_concrete
setblock 31 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "mekanism"}','{"text": "ore_line"}','{"text": ""}']}}
setblock 32 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the steel line"}','{"text": "from enrichment"}','{"text": "chamber to the"}','{"text": "obelisk chest"}']}}
fill 43 64 71 43 79 84 minecraft:light_gray_concrete
setblock 32 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 34 64 76 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 36 64 76 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 38 64 76 mekanism:basic_smelting_factory[facing=south,active=false]
setblock 40 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 33 64 76 mekanism:basic_logistical_transporter
setblock 35 64 76 mekanism:basic_logistical_transporter
setblock 37 64 76 mekanism:basic_logistical_transporter
setblock 39 64 76 mekanism:basic_logistical_transporter
fill 34 64 75 39 64 75 mekanism:basic_universal_cable
setblock 40 64 75 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
