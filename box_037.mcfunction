# 037 mekanism_ores/line2
#area 59 65 79 90
fill 59 64 65 79 91 90 minecraft:air
fill 59 60 65 79 62 90 minecraft:stone
fill 59 63 65 79 63 90 minecraft:light_gray_concrete
fill 63 64 71 79 79 71 minecraft:light_gray_concrete
fill 63 64 71 63 79 84 minecraft:light_gray_concrete
setblock 64 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 65 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 66 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 74 64 71 74 79 84 minecraft:light_gray_concrete
setblock 65 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 67 64 76 mekanism:enrichment_chamber[facing=south,active=false]
setblock 69 64 76 mekanism:energized_smelter[facing=south,active=false]
setblock 71 64 76 minecraft:chest[facing=south]{Items:[]}
setblock 66 64 76 mekanism:basic_logistical_transporter
setblock 68 64 76 mekanism:basic_logistical_transporter
setblock 70 64 76 mekanism:basic_logistical_transporter
fill 67 64 75 70 64 75 mekanism:basic_universal_cable
setblock 71 64 75 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
