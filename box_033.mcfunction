# 033 mekanism_ores/line2
#area 44 65 64 90
fill 44 64 65 64 91 90 minecraft:air
fill 44 60 65 64 62 90 minecraft:stone
fill 44 63 65 64 63 90 minecraft:light_gray_concrete
fill 48 64 71 64 79 71 minecraft:light_gray_concrete
fill 48 64 71 48 79 84 minecraft:light_gray_concrete
setblock 49 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 50 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 51 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 59 64 71 59 79 84 minecraft:light_gray_concrete
setblock 50 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 52 64 76 mekanism:enrichment_chamber[facing=south,active=false]
setblock 54 64 76 mekanism:energized_smelter[facing=south,active=false]
setblock 56 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 51 64 76 mekanism:basic_logistical_transporter
setblock 53 64 76 mekanism:basic_logistical_transporter
setblock 55 64 76 mekanism:basic_logistical_transporter
fill 52 64 75 55 64 75 mekanism:basic_universal_cable
setblock 56 64 75 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
