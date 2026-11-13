# 027 create_brass/crafter
#area 201 42 220 67
fill 201 64 42 220 91 67 minecraft:air
fill 201 60 42 220 62 67 minecraft:stone
fill 201 63 42 220 63 67 minecraft:light_gray_concrete
fill 205 64 48 220 79 48 minecraft:light_gray_concrete
fill 205 64 48 205 79 61 minecraft:light_gray_concrete
setblock 206 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 207 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 215 64 48 215 79 61 minecraft:light_gray_concrete
setblock 209 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 209 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 209 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 210 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 210 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 210 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 211 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 211 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 211 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 212 64 53 create:depot
setblock 208 64 53 create:cogwheel[axis=z]
fill 207 64 52 209 65 52 create:andesite_casing
setblock 208 64 52 create:andesite_encased_shaft[axis=z]
setblock 208 64 51 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
