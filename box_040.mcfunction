# 040 mekanism_ores/quintupling
#area 107 65 129 90
fill 107 64 65 129 91 90 minecraft:air
fill 107 60 65 129 62 90 minecraft:stone
fill 107 63 65 129 63 90 minecraft:light_gray_concrete
fill 111 64 71 129 79 71 minecraft:light_gray_concrete
fill 111 64 71 111 79 84 minecraft:light_gray_concrete
setblock 112 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "mekanism_ores"}','{"text": "quintupling"}','{"text": ""}']}}
setblock 113 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the full eight"}','{"text": "machine ladder"}','{"text": "with gas tubes"}','{"text": ""}']}}
fill 124 64 71 124 79 84 minecraft:light_gray_concrete
setblock 113 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 114 64 77 mekanism:chemical_dissolution_chamber[facing=south]
setblock 115 64 77 mekanism:chemical_washer[facing=south]
setblock 116 64 77 mekanism:chemical_crystallizer[facing=south]
setblock 117 64 77 mekanism:chemical_injection_chamber[facing=south]
setblock 118 64 77 mekanism:purification_chamber[facing=south]
setblock 119 64 77 mekanism:crusher[facing=south]
setblock 120 64 77 mekanism:enrichment_chamber[facing=south]
setblock 121 64 77 mekanism:energized_smelter[facing=south]
setblock 122 64 77 minecraft:chest[facing=south]{Items:[]}
fill 114 65 77 116 65 77 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
