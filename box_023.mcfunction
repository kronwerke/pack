# 023 mekanism_ores/shards
#area 43 63 63 88
fill 43 64 63 63 91 88 minecraft:air
fill 43 60 63 63 62 88 minecraft:stone
fill 43 63 63 63 63 88 minecraft:light_gray_concrete
fill 47 64 69 63 79 69 minecraft:light_gray_concrete
fill 47 64 69 47 79 82 minecraft:light_gray_concrete
setblock 48 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "mekanism_ores"}','{"text": "shards"}','{"text": ""}']}}
setblock 49 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 4x line"}','{"text": "with injection"}','{"text": "chamber, two"}','{"text": "separators and"}']}}
setblock 50 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chemical"}','{"text": "infuser"}','{"text": ""}','{"text": ""}']}}
fill 58 64 69 58 79 82 minecraft:light_gray_concrete
setblock 49 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 50 64 75 mekanism:chemical_injection_chamber[facing=south]
setblock 51 64 75 mekanism:purification_chamber[facing=south]
setblock 52 64 75 mekanism:crusher[facing=south]
setblock 53 64 75 mekanism:enrichment_chamber[facing=south]
setblock 54 64 75 mekanism:energized_smelter[facing=south]
setblock 55 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 74 mekanism:electrolytic_separator[facing=south]
setblock 50 64 74 mekanism:chemical_infuser[facing=south]
setblock 51 64 74 mekanism:electrolytic_separator[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
