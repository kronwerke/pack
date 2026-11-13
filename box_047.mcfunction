# 047 mekanism_ores/quintupling
#area 107 95 129 120
fill 107 64 95 129 91 120 minecraft:air
fill 107 60 95 129 62 120 minecraft:stone
fill 107 63 95 129 63 120 minecraft:light_gray_concrete
fill 111 64 101 129 79 101 minecraft:light_gray_concrete
fill 111 64 101 111 79 114 minecraft:light_gray_concrete
setblock 112 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047"}','{"text": "mekanism_ores"}','{"text": "quintupling"}','{"text": ""}']}}
setblock 113 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the full eight"}','{"text": "machine ladder"}','{"text": "with gas tubes"}','{"text": ""}']}}
fill 124 64 101 124 79 114 minecraft:light_gray_concrete
setblock 113 64 107 minecraft:chest[facing=south]{Items:[]}
setblock 114 64 107 mekanism:chemical_dissolution_chamber[facing=south]
setblock 115 64 107 mekanism:chemical_washer[facing=south]
setblock 116 64 107 mekanism:chemical_crystallizer[facing=south]
setblock 117 64 107 mekanism:chemical_injection_chamber[facing=south]
setblock 118 64 107 mekanism:purification_chamber[facing=south]
setblock 119 64 107 mekanism:crusher[facing=south]
setblock 120 64 107 mekanism:enrichment_chamber[facing=south]
setblock 121 64 107 mekanism:energized_smelter[facing=south]
setblock 122 64 107 minecraft:chest[facing=south]{Items:[]}
fill 114 65 107 116 65 107 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
