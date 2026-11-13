# 049 mekanism_ores/line2
#area 59 97 79 122
fill 59 64 97 79 91 122 minecraft:air
fill 59 60 97 79 62 122 minecraft:stone
fill 59 63 97 79 63 122 minecraft:light_gray_concrete
fill 63 64 103 79 79 103 minecraft:light_gray_concrete
fill 63 64 103 63 79 116 minecraft:light_gray_concrete
setblock 64 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "049"}','{"text": "mekanism_ores"}','{"text": "line2"}','{"text": ""}']}}
setblock 65 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest,"}','{"text": "transporters,"}','{"text": "enrichment"}','{"text": "chamber,"}']}}
setblock 66 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "smelter, chest,"}','{"text": "cables"}','{"text": ""}','{"text": ""}']}}
fill 74 64 103 74 79 116 minecraft:light_gray_concrete
setblock 65 64 108 minecraft:chest[facing=south]{Items:[]}
setblock 67 64 108 mekanism:enrichment_chamber[facing=south,active=false]
setblock 69 64 108 mekanism:energized_smelter[facing=south,active=false]
setblock 71 64 108 minecraft:chest[facing=south]{Items:[]}
setblock 66 64 108 mekanism:basic_logistical_transporter
setblock 68 64 108 mekanism:basic_logistical_transporter
setblock 70 64 108 mekanism:basic_logistical_transporter
fill 67 64 107 70 64 107 mekanism:basic_universal_cable
setblock 71 64 107 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
