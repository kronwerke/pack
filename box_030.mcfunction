# 030 mekanism_ores/quintupling
#area 74 65 96 90
fill 74 64 65 96 91 90 minecraft:air
fill 74 60 65 96 62 90 minecraft:stone
fill 74 63 65 96 63 90 minecraft:light_gray_concrete
fill 78 64 71 96 79 71 minecraft:light_gray_concrete
fill 78 64 71 78 79 84 minecraft:light_gray_concrete
setblock 79 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "mekanism_ores"}','{"text": "quintupling"}','{"text": ""}']}}
setblock 80 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the full eight"}','{"text": "machine ladder"}','{"text": "with gas tubes"}','{"text": ""}']}}
fill 91 64 71 91 79 84 minecraft:light_gray_concrete
setblock 80 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 81 64 77 mekanism:chemical_dissolution_chamber[facing=south]
setblock 82 64 77 mekanism:chemical_washer[facing=south]
setblock 83 64 77 mekanism:chemical_crystallizer[facing=south]
setblock 84 64 77 mekanism:chemical_injection_chamber[facing=south]
setblock 85 64 77 mekanism:purification_chamber[facing=south]
setblock 86 64 77 mekanism:crusher[facing=south]
setblock 87 64 77 mekanism:enrichment_chamber[facing=south]
setblock 88 64 77 mekanism:energized_smelter[facing=south]
setblock 89 64 77 minecraft:chest[facing=south]{Items:[]}
fill 81 65 77 83 65 77 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
