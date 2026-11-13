# 020 create/cobble_gen
#area 123 42 142 67
fill 123 64 42 142 91 67 minecraft:air
fill 123 60 42 142 62 67 minecraft:stone
fill 123 63 42 142 63 67 minecraft:light_gray_concrete
fill 127 64 48 142 79 48 minecraft:light_gray_concrete
fill 127 64 48 127 79 61 minecraft:light_gray_concrete
setblock 128 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 129 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
fill 137 64 48 137 79 61 minecraft:light_gray_concrete
setblock 129 64 52 minecraft:stone_bricks
setblock 129 64 54 minecraft:glass
setblock 130 64 52 minecraft:stone_bricks
setblock 130 64 54 minecraft:glass
setblock 131 64 52 minecraft:stone_bricks
setblock 131 64 54 minecraft:glass
setblock 132 64 52 minecraft:stone_bricks
setblock 132 64 54 minecraft:glass
setblock 133 64 52 minecraft:stone_bricks
setblock 133 64 54 minecraft:glass
setblock 134 64 52 minecraft:stone_bricks
setblock 134 64 54 minecraft:glass
setblock 135 64 52 minecraft:stone_bricks
setblock 135 64 54 minecraft:glass
setblock 129 64 53 minecraft:stone_bricks
setblock 135 64 53 minecraft:stone_bricks
setblock 130 64 53 minecraft:water
setblock 132 63 53 minecraft:air
setblock 133 64 53 minecraft:cobblestone
setblock 134 64 53 minecraft:lava
setblock 133 64 52 create:mechanical_drill[facing=south]
fill 132 64 51 134 65 51 create:andesite_casing
setblock 133 64 51 create:andesite_encased_shaft[axis=z]
setblock 133 64 50 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
