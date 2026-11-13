# 027 create_brass/crafter
#area 216 42 235 67
fill 216 64 42 235 91 67 minecraft:air
fill 216 60 42 235 62 67 minecraft:stone
fill 216 63 42 235 63 67 minecraft:light_gray_concrete
fill 220 64 48 235 79 48 minecraft:light_gray_concrete
fill 220 64 48 220 79 61 minecraft:light_gray_concrete
setblock 221 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 222 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 230 64 48 230 79 61 minecraft:light_gray_concrete
setblock 224 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 224 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 224 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 225 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 225 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 225 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 226 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 226 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 226 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 227 64 53 create:depot
setblock 223 64 53 create:cogwheel[axis=z]
fill 222 64 52 224 65 52 create:andesite_casing
setblock 223 64 52 create:andesite_encased_shaft[axis=z]
setblock 223 64 51 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
