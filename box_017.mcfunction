# 017 mekanism_ores/line2
#area 11 44 31 69
fill 11 64 44 31 91 69 minecraft:air
fill 11 60 44 31 62 69 minecraft:stone
fill 11 63 44 31 63 69 minecraft:light_gray_concrete
fill 15 64 50 31 79 50 minecraft:light_gray_concrete
fill 15 64 50 15 79 63 minecraft:light_gray_concrete
setblock 16 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "017"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 17 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 18 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 26 64 50 26 79 63 minecraft:light_gray_concrete
setblock 17 64 55 minecraft:chest[facing=south]{Items:[]}
setblock 19 64 55 mekanism:enrichment_chamber[facing=south,active=false]
setblock 21 64 55 mekanism:energized_smelter[facing=south,active=false]
setblock 23 64 55 minecraft:chest[facing=south]{Items:[]}
setblock 18 64 55 mekanism:basic_logistical_transporter
setblock 20 64 55 mekanism:basic_logistical_transporter
setblock 22 64 55 mekanism:basic_logistical_transporter
fill 19 64 54 22 64 54 mekanism:basic_universal_cable
setblock 23 64 54 mekanism:basic_energy_cube[facing=south]
