# 048 mekanism/ore_line
#area 41 97 63 122
fill 41 64 97 63 91 122 minecraft:air
fill 41 60 97 63 62 122 minecraft:stone
fill 41 63 97 63 63 122 minecraft:light_gray_concrete
fill 45 64 103 63 79 103 minecraft:light_gray_concrete
fill 45 64 103 45 79 116 minecraft:light_gray_concrete
setblock 46 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "mekanism"}','{"text": "ore_line"}','{"text": ""}']}}
setblock 47 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the steel line"}','{"text": "from enrichment"}','{"text": "chamber to the"}','{"text": "obelisk chest"}']}}
fill 58 64 103 58 79 116 minecraft:light_gray_concrete
setblock 47 64 108 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 108 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 51 64 108 mekanism:basic_infusing_factory[facing=south,active=false]
setblock 53 64 108 mekanism:basic_smelting_factory[facing=south,active=false]
setblock 55 64 108 minecraft:chest[facing=south]{Items:[]}
setblock 48 64 108 mekanism:basic_logistical_transporter
setblock 50 64 108 mekanism:basic_logistical_transporter
setblock 52 64 108 mekanism:basic_logistical_transporter
setblock 54 64 108 mekanism:basic_logistical_transporter
fill 49 64 107 54 64 107 mekanism:basic_universal_cable
setblock 55 64 107 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
