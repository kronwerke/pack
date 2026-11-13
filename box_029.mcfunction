# 029 mekanism_ores/shards
#area 58 65 78 90
fill 58 64 65 78 91 90 minecraft:air
fill 58 60 65 78 62 90 minecraft:stone
fill 58 63 65 78 63 90 minecraft:light_gray_concrete
fill 62 64 71 78 79 71 minecraft:light_gray_concrete
fill 62 64 71 62 79 84 minecraft:light_gray_concrete
setblock 63 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "mekanism_ores"}','{"text": "shards"}','{"text": ""}']}}
setblock 64 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 4x line"}','{"text": "with injection"}','{"text": "chamber, two"}','{"text": "separators and"}']}}
setblock 65 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chemical"}','{"text": "infuser"}','{"text": ""}','{"text": ""}']}}
fill 73 64 71 73 79 84 minecraft:light_gray_concrete
setblock 64 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 65 64 77 mekanism:chemical_injection_chamber[facing=south]
setblock 66 64 77 mekanism:purification_chamber[facing=south]
setblock 67 64 77 mekanism:crusher[facing=south]
setblock 68 64 77 mekanism:enrichment_chamber[facing=south]
setblock 69 64 77 mekanism:energized_smelter[facing=south]
setblock 70 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 64 64 76 mekanism:electrolytic_separator[facing=south]
setblock 65 64 76 mekanism:chemical_infuser[facing=south]
setblock 66 64 76 mekanism:electrolytic_separator[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
