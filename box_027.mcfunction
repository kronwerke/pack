# 027 mekanism_ores/quintupling
#area 74 63 96 88
fill 74 64 63 96 91 88 minecraft:air
fill 74 60 63 96 62 88 minecraft:stone
fill 74 63 63 96 63 88 minecraft:light_gray_concrete
fill 78 64 69 96 79 69 minecraft:light_gray_concrete
fill 78 64 69 78 79 82 minecraft:light_gray_concrete
setblock 79 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "mekanism_ores"}','{"text": "quintupling"}','{"text": ""}']}}
setblock 80 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the full eight"}','{"text": "machine ladder"}','{"text": "with gas tubes"}','{"text": ""}']}}
fill 91 64 69 91 79 82 minecraft:light_gray_concrete
setblock 80 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 81 64 75 mekanism:chemical_dissolution_chamber[facing=south]
setblock 82 64 75 mekanism:chemical_washer[facing=south]
setblock 83 64 75 mekanism:chemical_crystallizer[facing=south]
setblock 84 64 75 mekanism:chemical_injection_chamber[facing=south]
setblock 85 64 75 mekanism:purification_chamber[facing=south]
setblock 86 64 75 mekanism:crusher[facing=south]
setblock 87 64 75 mekanism:enrichment_chamber[facing=south]
setblock 88 64 75 mekanism:energized_smelter[facing=south]
setblock 89 64 75 minecraft:chest[facing=south]{Items:[]}
fill 81 65 75 83 65 75 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
