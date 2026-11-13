# 024 create_brass/crafter
#area 185 42 204 67
fill 185 64 42 204 91 67 minecraft:air
fill 185 60 42 204 62 67 minecraft:stone
fill 185 63 42 204 63 67 minecraft:light_gray_concrete
fill 189 64 48 204 79 48 minecraft:light_gray_concrete
fill 189 64 48 189 79 61 minecraft:light_gray_concrete
setblock 190 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "create_brass"}','{"text": "crafter"}','{"text": ""}']}}
setblock 191 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a 3x3"}','{"text": "mechanical"}','{"text": "crafter grid"}','{"text": "with its arrows"}']}}
fill 199 64 48 199 79 61 minecraft:light_gray_concrete
setblock 193 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 193 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 193 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 194 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 194 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 194 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 195 64 53 create:mechanical_crafter[facing=south,pointing=right]
setblock 195 65 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 195 66 53 create:mechanical_crafter[facing=south,pointing=down]
setblock 196 64 53 create:depot
setblock 192 64 53 create:cogwheel[axis=z]
fill 191 64 52 193 65 52 create:andesite_casing
setblock 192 64 52 create:andesite_encased_shaft[axis=z]
setblock 192 64 51 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
