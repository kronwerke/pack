# 027 mekanism_ores/line2
#area 26 65 46 90
fill 26 64 65 46 91 90 minecraft:air
fill 26 60 65 46 62 90 minecraft:stone
fill 26 63 65 46 63 90 minecraft:light_gray_concrete
fill 30 64 71 46 79 71 minecraft:light_gray_concrete
fill 30 64 71 30 79 84 minecraft:light_gray_concrete
setblock 31 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 32 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 33 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 41 64 71 41 79 84 minecraft:light_gray_concrete
setblock 32 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 34 64 76 mekanism:enrichment_chamber[facing=south,active=false]
setblock 36 64 76 mekanism:energized_smelter[facing=south,active=false]
setblock 38 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 33 64 76 mekanism:basic_logistical_transporter
setblock 35 64 76 mekanism:basic_logistical_transporter
setblock 37 64 76 mekanism:basic_logistical_transporter
fill 34 64 75 37 64 75 mekanism:basic_universal_cable
setblock 38 64 75 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
