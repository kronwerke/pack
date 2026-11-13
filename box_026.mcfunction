# 026 mekanism_ores/shards
#area 58 63 78 88
fill 58 64 63 78 91 88 minecraft:air
fill 58 60 63 78 62 88 minecraft:stone
fill 58 63 63 78 63 88 minecraft:light_gray_concrete
fill 62 64 69 78 79 69 minecraft:light_gray_concrete
fill 62 64 69 62 79 82 minecraft:light_gray_concrete
setblock 63 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "mekanism_ores"}','{"text": "shards"}','{"text": ""}']}}
setblock 64 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 4x line"}','{"text": "with injection"}','{"text": "chamber, two"}','{"text": "separators and"}']}}
setblock 65 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chemical"}','{"text": "infuser"}','{"text": ""}','{"text": ""}']}}
fill 73 64 69 73 79 82 minecraft:light_gray_concrete
setblock 64 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 65 64 75 mekanism:chemical_injection_chamber[facing=south]
setblock 66 64 75 mekanism:purification_chamber[facing=south]
setblock 67 64 75 mekanism:crusher[facing=south]
setblock 68 64 75 mekanism:enrichment_chamber[facing=south]
setblock 69 64 75 mekanism:energized_smelter[facing=south]
setblock 70 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 64 64 74 mekanism:electrolytic_separator[facing=south]
setblock 65 64 74 mekanism:chemical_infuser[facing=south]
setblock 66 64 74 mekanism:electrolytic_separator[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
