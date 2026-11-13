# 024 mekanism_ores/line2
#area 26 63 46 88
fill 26 64 63 46 91 88 minecraft:air
fill 26 60 63 46 62 88 minecraft:stone
fill 26 63 63 46 63 88 minecraft:light_gray_concrete
fill 30 64 69 46 79 69 minecraft:light_gray_concrete
fill 30 64 69 30 79 82 minecraft:light_gray_concrete
setblock 31 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 32 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 33 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 41 64 69 41 79 82 minecraft:light_gray_concrete
setblock 32 64 74 minecraft:chest[facing=south]{Items:[]}
setblock 34 64 74 mekanism:enrichment_chamber[facing=south,active=false]
setblock 36 64 74 mekanism:energized_smelter[facing=south,active=false]
setblock 38 64 74 minecraft:chest[facing=south]{Items:[]}
setblock 33 64 74 mekanism:basic_logistical_transporter
setblock 35 64 74 mekanism:basic_logistical_transporter
setblock 37 64 74 mekanism:basic_logistical_transporter
fill 34 64 73 37 64 73 mekanism:basic_universal_cable
setblock 38 64 73 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
