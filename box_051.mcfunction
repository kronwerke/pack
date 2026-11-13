# 051 mekanism_ores/shards
#area 91 97 111 122
fill 91 64 97 111 91 122 minecraft:air
fill 91 60 97 111 62 122 minecraft:stone
fill 91 63 97 111 63 122 minecraft:light_gray_concrete
fill 95 64 103 111 79 103 minecraft:light_gray_concrete
fill 95 64 103 95 79 116 minecraft:light_gray_concrete
setblock 96 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "051"}','{"text": "mekanism_ores"}','{"text": "shards"}','{"text": ""}']}}
setblock 97 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the 4x line"}','{"text": "with injection"}','{"text": "chamber, two"}','{"text": "separators and"}']}}
setblock 98 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chemical"}','{"text": "infuser"}','{"text": ""}','{"text": ""}']}}
fill 106 64 103 106 79 116 minecraft:light_gray_concrete
setblock 97 64 109 minecraft:chest[facing=south]{Items:[]}
setblock 98 64 109 mekanism:chemical_injection_chamber[facing=south]
setblock 99 64 109 mekanism:purification_chamber[facing=south]
setblock 100 64 109 mekanism:crusher[facing=south]
setblock 101 64 109 mekanism:enrichment_chamber[facing=south]
setblock 102 64 109 mekanism:energized_smelter[facing=south]
setblock 103 64 109 minecraft:chest[facing=south]{Items:[]}
setblock 97 64 108 mekanism:electrolytic_separator[facing=south]
setblock 98 64 108 mekanism:chemical_infuser[facing=south]
setblock 99 64 108 mekanism:electrolytic_separator[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
