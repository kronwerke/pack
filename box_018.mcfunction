# 018 create/cobble_gen
#area 106 42 125 67
fill 106 64 42 125 91 67 minecraft:air
fill 106 60 42 125 62 67 minecraft:stone
fill 106 63 42 125 63 67 minecraft:light_gray_concrete
fill 110 64 48 125 79 48 minecraft:light_gray_concrete
fill 110 64 48 110 79 61 minecraft:light_gray_concrete
setblock 111 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 112 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
fill 120 64 48 120 79 61 minecraft:light_gray_concrete
setblock 112 64 52 minecraft:stone_bricks
setblock 112 64 54 minecraft:glass
setblock 113 64 52 minecraft:stone_bricks
setblock 113 64 54 minecraft:glass
setblock 114 64 52 minecraft:stone_bricks
setblock 114 64 54 minecraft:glass
setblock 115 64 52 minecraft:stone_bricks
setblock 115 64 54 minecraft:glass
setblock 116 64 52 minecraft:stone_bricks
setblock 116 64 54 minecraft:glass
setblock 117 64 52 minecraft:stone_bricks
setblock 117 64 54 minecraft:glass
setblock 118 64 52 minecraft:stone_bricks
setblock 118 64 54 minecraft:glass
setblock 112 64 53 minecraft:stone_bricks
setblock 118 64 53 minecraft:stone_bricks
setblock 113 64 53 minecraft:water
setblock 115 63 53 minecraft:air
setblock 116 64 53 minecraft:cobblestone
setblock 117 64 53 minecraft:lava
setblock 116 64 52 create:mechanical_drill[facing=south]
fill 115 64 51 117 65 51 create:andesite_casing
setblock 116 64 51 create:andesite_encased_shaft[axis=z]
setblock 116 64 50 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
