# 023 create_brass/crafter
#area 170 42 189 67
fill 170 64 42 189 91 67 minecraft:air
fill 170 60 42 189 62 67 minecraft:stone
fill 170 63 42 189 63 67 minecraft:light_gray_concrete
fill 174 64 48 189 79 48 minecraft:light_gray_concrete
fill 174 64 48 174 79 61 minecraft:light_gray_concrete
setblock 175 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 176 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 184 64 48 184 79 61 minecraft:light_gray_concrete
setblock 178 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 178 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 178 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 179 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 179 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 179 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 180 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 180 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 180 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 181 64 53 create:depot
setblock 177 64 53 create:cogwheel[axis=z]
fill 176 64 52 178 65 52 create:andesite_casing
setblock 177 64 52 create:andesite_encased_shaft[axis=z]
setblock 177 64 51 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
