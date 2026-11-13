# 020 mekanism_ores/line2
#area 11 63 31 88
fill 11 64 63 31 91 88 minecraft:air
fill 11 60 63 31 62 88 minecraft:stone
fill 11 63 63 31 63 88 minecraft:light_gray_concrete
fill 15 64 69 31 79 69 minecraft:light_gray_concrete
fill 15 64 69 15 79 82 minecraft:light_gray_concrete
setblock 16 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 17 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 18 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 26 64 69 26 79 82 minecraft:light_gray_concrete
setblock 17 64 74 minecraft:chest[facing=south]{Items:[]}
setblock 19 64 74 mekanism:enrichment_chamber[facing=south,active=false]
setblock 21 64 74 mekanism:energized_smelter[facing=south,active=false]
setblock 23 64 74 minecraft:chest[facing=south]{Items:[]}
setblock 18 64 74 mekanism:basic_logistical_transporter
setblock 20 64 74 mekanism:basic_logistical_transporter
setblock 22 64 74 mekanism:basic_logistical_transporter
fill 19 64 73 22 64 73 mekanism:basic_universal_cable
setblock 23 64 73 mekanism:basic_energy_cube[facing=south]
