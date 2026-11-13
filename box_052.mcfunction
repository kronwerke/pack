# 052 mekanism_ores/quintupling
#area 107 97 129 122
fill 107 64 97 129 91 122 minecraft:air
fill 107 60 97 129 62 122 minecraft:stone
fill 107 63 97 129 63 122 minecraft:light_gray_concrete
fill 111 64 103 129 79 103 minecraft:light_gray_concrete
fill 111 64 103 111 79 116 minecraft:light_gray_concrete
setblock 112 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "mekanism_ores"}','{"text": "quintupling"}','{"text": ""}']}}
setblock 113 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the full eight"}','{"text": "machine ladder"}','{"text": "with gas tubes"}','{"text": ""}']}}
fill 124 64 103 124 79 116 minecraft:light_gray_concrete
setblock 113 64 109 minecraft:chest[facing=south]{Items:[]}
setblock 114 64 109 mekanism:chemical_dissolution_chamber[facing=south]
setblock 115 64 109 mekanism:chemical_washer[facing=south]
setblock 116 64 109 mekanism:chemical_crystallizer[facing=south]
setblock 117 64 109 mekanism:chemical_injection_chamber[facing=south]
setblock 118 64 109 mekanism:purification_chamber[facing=south]
setblock 119 64 109 mekanism:crusher[facing=south]
setblock 120 64 109 mekanism:enrichment_chamber[facing=south]
setblock 121 64 109 mekanism:energized_smelter[facing=south]
setblock 122 64 109 minecraft:chest[facing=south]{Items:[]}
fill 114 65 109 116 65 109 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
