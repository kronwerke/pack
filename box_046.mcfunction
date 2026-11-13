# 046 mekanism/ore_line
#area 41 95 63 120
fill 41 64 95 63 91 120 minecraft:air
fill 41 60 95 63 62 120 minecraft:stone
fill 41 63 95 63 63 120 minecraft:light_gray_concrete
fill 45 64 101 63 79 101 minecraft:light_gray_concrete
fill 45 64 101 45 79 114 minecraft:light_gray_concrete
setblock 46 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "046"}','{"text": "mekanism"}','{"text": "ore_line"}','{"text": ""}']}}
setblock 47 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the steel line"}','{"text": "from enrichment"}','{"text": "chamber to the"}','{"text": "obelisk chest"}']}}
fill 58 64 101 58 79 114 minecraft:light_gray_concrete
setblock 47 64 106 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 106 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 51 64 106 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 53 64 106 mekanism:basic_smelting_factory[facing=south,active=false]
setblock 55 64 106 minecraft:chest[facing=south]{Items:[]}
setblock 48 64 106 mekanism:basic_logistical_transporter
setblock 50 64 106 mekanism:basic_logistical_transporter
setblock 52 64 106 mekanism:basic_logistical_transporter
setblock 54 64 106 mekanism:basic_logistical_transporter
fill 49 64 105 54 64 105 mekanism:basic_universal_cable
setblock 55 64 105 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
