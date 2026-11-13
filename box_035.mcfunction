# 035 mekanism/ore_line
#area 41 65 63 90
fill 41 64 65 63 91 90 minecraft:air
fill 41 60 65 63 62 90 minecraft:stone
fill 41 63 65 63 63 90 minecraft:light_gray_concrete
fill 45 64 71 63 79 71 minecraft:light_gray_concrete
fill 45 64 71 45 79 84 minecraft:light_gray_concrete
setblock 46 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "mekanism"}','{"text": "ore_line"}','{"text": ""}']}}
setblock 47 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the steel line"}','{"text": "from enrichment"}','{"text": "chamber to the"}','{"text": "obelisk chest"}']}}
fill 58 64 71 58 79 84 minecraft:light_gray_concrete
setblock 47 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 76 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 51 64 76 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 53 64 76 mekanism:basic_smelting_factory[facing=south,active=false]
setblock 55 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 48 64 76 mekanism:basic_logistical_transporter
setblock 50 64 76 mekanism:basic_logistical_transporter
setblock 52 64 76 mekanism:basic_logistical_transporter
setblock 54 64 76 mekanism:basic_logistical_transporter
fill 49 64 75 54 64 75 mekanism:basic_universal_cable
setblock 55 64 75 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
