# 036 mekanism_ores/quintupling
#area 92 65 114 90
fill 92 64 65 114 91 90 minecraft:air
fill 92 60 65 114 62 90 minecraft:stone
fill 92 63 65 114 63 90 minecraft:light_gray_concrete
fill 96 64 71 114 79 71 minecraft:light_gray_concrete
fill 96 64 71 96 79 84 minecraft:light_gray_concrete
setblock 97 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "036"}','{"text": "mekanism_ores"}','{"text": "quintupling"}','{"text": ""}']}}
setblock 98 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the full eight"}','{"text": "machine ladder"}','{"text": "with gas tubes"}','{"text": ""}']}}
fill 109 64 71 109 79 84 minecraft:light_gray_concrete
setblock 98 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 99 64 77 mekanism:chemical_dissolution_chamber[facing=south]
setblock 100 64 77 mekanism:chemical_washer[facing=south]
setblock 101 64 77 mekanism:chemical_crystallizer[facing=south]
setblock 102 64 77 mekanism:chemical_injection_chamber[facing=south]
setblock 103 64 77 mekanism:purification_chamber[facing=south]
setblock 104 64 77 mekanism:crusher[facing=south]
setblock 105 64 77 mekanism:enrichment_chamber[facing=south]
setblock 106 64 77 mekanism:energized_smelter[facing=south]
setblock 107 64 77 minecraft:chest[facing=south]{Items:[]}
fill 99 65 77 101 65 77 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
