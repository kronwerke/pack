# 029 create_brass/crafter
#area 201 44 220 69
fill 201 64 44 220 91 69 minecraft:air
fill 201 60 44 220 62 69 minecraft:stone
fill 201 63 44 220 63 69 minecraft:light_gray_concrete
fill 205 64 50 220 79 50 minecraft:light_gray_concrete
fill 205 64 50 205 79 63 minecraft:light_gray_concrete
setblock 206 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 207 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 215 64 50 215 79 63 minecraft:light_gray_concrete
setblock 209 64 55 create:mechanical_crafter[facing=south,pointing=right]
setblock 209 65 55 create:mechanical_crafter[facing=south,pointing=down]
setblock 209 66 55 create:mechanical_crafter[facing=south,pointing=down]
setblock 210 64 55 create:mechanical_crafter[facing=south,pointing=right]
setblock 210 65 55 create:mechanical_crafter[facing=south,pointing=down]
setblock 210 66 55 create:mechanical_crafter[facing=south,pointing=down]
setblock 211 64 55 create:mechanical_crafter[facing=south,pointing=right]
setblock 211 65 55 create:mechanical_crafter[facing=south,pointing=down]
setblock 211 66 55 create:mechanical_crafter[facing=south,pointing=down]
setblock 212 64 55 create:depot
setblock 208 64 55 create:cogwheel[axis=z]
fill 207 64 54 209 65 54 create:andesite_casing
setblock 208 64 54 create:andesite_encased_shaft[axis=z]
setblock 208 64 53 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
