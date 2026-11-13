# 025 create/cobble_gen
#area 139 44 158 69
fill 139 64 44 158 91 69 minecraft:air
fill 139 60 44 158 62 69 minecraft:stone
fill 139 63 44 158 63 69 minecraft:light_gray_concrete
fill 143 64 50 158 79 50 minecraft:light_gray_concrete
fill 143 64 50 143 79 63 minecraft:light_gray_concrete
setblock 144 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 145 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
fill 153 64 50 153 79 63 minecraft:light_gray_concrete
setblock 145 64 54 minecraft:stone_bricks
setblock 145 64 56 minecraft:glass
setblock 146 64 54 minecraft:stone_bricks
setblock 146 64 56 minecraft:glass
setblock 147 64 54 minecraft:stone_bricks
setblock 147 64 56 minecraft:glass
setblock 148 64 54 minecraft:stone_bricks
setblock 148 64 56 minecraft:glass
setblock 149 64 54 minecraft:stone_bricks
setblock 149 64 56 minecraft:glass
setblock 150 64 54 minecraft:stone_bricks
setblock 150 64 56 minecraft:glass
setblock 151 64 54 minecraft:stone_bricks
setblock 151 64 56 minecraft:glass
setblock 145 64 55 minecraft:stone_bricks
setblock 151 64 55 minecraft:stone_bricks
setblock 146 64 55 minecraft:water
setblock 148 63 55 minecraft:air
setblock 149 64 55 minecraft:cobblestone
setblock 150 64 55 minecraft:lava
setblock 149 64 54 create:mechanical_drill[facing=south]
fill 148 64 53 150 65 53 create:andesite_casing
setblock 149 64 53 create:andesite_encased_shaft[axis=z]
setblock 149 64 52 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
