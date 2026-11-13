# 038 mekanism_ores/shards
#area 91 65 111 90
fill 91 64 65 111 91 90 minecraft:air
fill 91 60 65 111 62 90 minecraft:stone
fill 91 63 65 111 63 90 minecraft:light_gray_concrete
fill 95 64 71 111 79 71 minecraft:light_gray_concrete
fill 95 64 71 95 79 84 minecraft:light_gray_concrete
setblock 96 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "mekanism_ores"}','{"text": "shards"}','{"text": ""}']}}
setblock 97 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 4x line"}','{"text": "with injection"}','{"text": "chamber, two"}','{"text": "separators and"}']}}
setblock 98 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chemical"}','{"text": "infuser"}','{"text": ""}','{"text": ""}']}}
fill 106 64 71 106 79 84 minecraft:light_gray_concrete
setblock 97 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 98 64 77 mekanism:chemical_injection_chamber[facing=south]
setblock 99 64 77 mekanism:purification_chamber[facing=south]
setblock 100 64 77 mekanism:crusher[facing=south]
setblock 101 64 77 mekanism:enrichment_chamber[facing=south]
setblock 102 64 77 mekanism:energized_smelter[facing=south]
setblock 103 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 97 64 76 mekanism:electrolytic_separator[facing=south]
setblock 98 64 76 mekanism:chemical_infuser[facing=south]
setblock 99 64 76 mekanism:electrolytic_separator[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
