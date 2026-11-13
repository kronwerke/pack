# 047 mekanism/ethene
#area 26 97 45 122
fill 26 64 97 45 91 122 minecraft:air
fill 26 60 97 45 62 122 minecraft:stone
fill 26 63 97 45 63 122 minecraft:light_gray_concrete
fill 30 64 103 45 79 103 minecraft:light_gray_concrete
fill 30 64 103 30 79 116 minecraft:light_gray_concrete
setblock 31 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047"}','{"text": "mekanism"}','{"text": "ethene"}','{"text": ""}']}}
setblock 32 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressurized"}','{"text": "reaction"}','{"text": "chamber making"}','{"text": "ethene"}']}}
fill 40 64 103 40 79 116 minecraft:light_gray_concrete
setblock 35 64 108 mekanism:pressurized_reaction_chamber[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
