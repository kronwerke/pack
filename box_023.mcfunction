# 023 mekanism/ethene
#area 11 63 30 88
fill 11 64 63 30 91 88 minecraft:air
fill 11 60 63 30 62 88 minecraft:stone
fill 11 63 63 30 63 88 minecraft:light_gray_concrete
fill 15 64 69 30 79 69 minecraft:light_gray_concrete
fill 15 64 69 15 79 82 minecraft:light_gray_concrete
setblock 16 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "mekanism"}','{"text": "ethene"}','{"text": ""}']}}
setblock 17 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressurized"}','{"text": "reaction"}','{"text": "chamber making"}','{"text": "ethene"}']}}
fill 25 64 69 25 79 82 minecraft:light_gray_concrete
setblock 20 64 74 mekanism:pressurized_reaction_chamber[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
