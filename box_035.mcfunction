# 035 mekanism_ores/shards
#area 76 65 96 90
fill 76 64 65 96 91 90 minecraft:air
fill 76 60 65 96 62 90 minecraft:stone
fill 76 63 65 96 63 90 minecraft:light_gray_concrete
fill 80 64 71 96 79 71 minecraft:light_gray_concrete
fill 80 64 71 80 79 84 minecraft:light_gray_concrete
setblock 81 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "mekanism_ores"}','{"text": "shards"}','{"text": ""}']}}
setblock 82 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 4x line"}','{"text": "with injection"}','{"text": "chamber, two"}','{"text": "separators and"}']}}
setblock 83 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chemical"}','{"text": "infuser"}','{"text": ""}','{"text": ""}']}}
fill 91 64 71 91 79 84 minecraft:light_gray_concrete
setblock 82 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 83 64 77 mekanism:chemical_injection_chamber[facing=south]
setblock 84 64 77 mekanism:purification_chamber[facing=south]
setblock 85 64 77 mekanism:crusher[facing=south]
setblock 86 64 77 mekanism:enrichment_chamber[facing=south]
setblock 87 64 77 mekanism:energized_smelter[facing=south]
setblock 88 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 82 64 76 mekanism:electrolytic_separator[facing=south]
setblock 83 64 76 mekanism:chemical_infuser[facing=south]
setblock 84 64 76 mekanism:electrolytic_separator[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
