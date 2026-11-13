# 044 mekanism/ethene
#area 26 95 45 120
fill 26 64 95 45 91 120 minecraft:air
fill 26 60 95 45 62 120 minecraft:stone
fill 26 63 95 45 63 120 minecraft:light_gray_concrete
fill 30 64 101 45 79 101 minecraft:light_gray_concrete
fill 30 64 101 30 79 114 minecraft:light_gray_concrete
setblock 31 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "mekanism"}','{"text": "ethene"}','{"text": ""}']}}
setblock 32 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressurized"}','{"text": "reaction"}','{"text": "chamber making"}','{"text": "ethene"}']}}
fill 40 64 101 40 79 114 minecraft:light_gray_concrete
setblock 35 64 106 mekanism:pressurized_reaction_chamber[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
