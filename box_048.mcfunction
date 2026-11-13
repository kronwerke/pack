# 048 mekanism_ores/shards
#area 91 95 111 120
fill 91 64 95 111 91 120 minecraft:air
fill 91 60 95 111 62 120 minecraft:stone
fill 91 63 95 111 63 120 minecraft:light_gray_concrete
fill 95 64 101 111 79 101 minecraft:light_gray_concrete
fill 95 64 101 95 79 114 minecraft:light_gray_concrete
setblock 96 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "mekanism_ores"}','{"text": "shards"}','{"text": ""}']}}
setblock 97 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 4x line"}','{"text": "with injection"}','{"text": "chamber, two"}','{"text": "separators and"}']}}
setblock 98 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chemical"}','{"text": "infuser"}','{"text": ""}','{"text": ""}']}}
fill 106 64 101 106 79 114 minecraft:light_gray_concrete
setblock 97 64 107 minecraft:chest[facing=south]{Items:[]}
setblock 98 64 107 mekanism:chemical_injection_chamber[facing=south]
setblock 99 64 107 mekanism:purification_chamber[facing=south]
setblock 100 64 107 mekanism:crusher[facing=south]
setblock 101 64 107 mekanism:enrichment_chamber[facing=south]
setblock 102 64 107 mekanism:energized_smelter[facing=south]
setblock 103 64 107 minecraft:chest[facing=south]{Items:[]}
setblock 97 64 106 mekanism:electrolytic_separator[facing=south]
setblock 98 64 106 mekanism:chemical_infuser[facing=south]
setblock 99 64 106 mekanism:electrolytic_separator[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
