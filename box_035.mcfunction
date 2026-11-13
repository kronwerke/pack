# 035 mekanism/ethene
#area 26 65 45 90
fill 26 64 65 45 91 90 minecraft:air
fill 26 60 65 45 62 90 minecraft:stone
fill 26 63 65 45 63 90 minecraft:light_gray_concrete
fill 30 64 71 45 79 71 minecraft:light_gray_concrete
fill 30 64 71 30 79 84 minecraft:light_gray_concrete
setblock 31 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "mekanism"}','{"text": "ethene"}','{"text": ""}']}}
setblock 32 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressurized"}','{"text": "reaction"}','{"text": "chamber making"}','{"text": "ethene"}']}}
fill 40 64 71 40 79 84 minecraft:light_gray_concrete
setblock 35 64 76 mekanism:pressurized_reaction_chamber[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
