# 047 mekanism_ores/line2
#area 59 95 79 120
fill 59 64 95 79 91 120 minecraft:air
fill 59 60 95 79 62 120 minecraft:stone
fill 59 63 95 79 63 120 minecraft:light_gray_concrete
fill 63 64 101 79 79 101 minecraft:light_gray_concrete
fill 63 64 101 63 79 114 minecraft:light_gray_concrete
setblock 64 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 65 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 66 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 74 64 101 74 79 114 minecraft:light_gray_concrete
setblock 65 64 106 minecraft:chest[facing=south]{Items:[]}
setblock 67 64 106 mekanism:enrichment_chamber[facing=south,active=false]
setblock 69 64 106 mekanism:energized_smelter[facing=south,active=false]
setblock 71 64 106 minecraft:chest[facing=south]{Items:[]}
setblock 66 64 106 mekanism:basic_logistical_transporter
setblock 68 64 106 mekanism:basic_logistical_transporter
setblock 70 64 106 mekanism:basic_logistical_transporter
fill 67 64 105 70 64 105 mekanism:basic_universal_cable
setblock 71 64 105 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
