# 028 mekanism/ethene
#area 11 65 30 90
fill 11 64 65 30 91 90 minecraft:air
fill 11 60 65 30 62 90 minecraft:stone
fill 11 63 65 30 63 90 minecraft:light_gray_concrete
fill 15 64 71 30 79 71 minecraft:light_gray_concrete
fill 15 64 71 15 79 84 minecraft:light_gray_concrete
setblock 16 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "mekanism"}','{"text": "ethene"}','{"text": ""}']}}
setblock 17 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressurized"}','{"text": "reaction"}','{"text": "chamber making"}','{"text": "ethene"}']}}
fill 25 64 71 25 79 84 minecraft:light_gray_concrete
setblock 20 64 76 mekanism:pressurized_reaction_chamber[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
