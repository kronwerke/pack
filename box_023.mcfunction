# 023 create/cobble_gen
#area 139 42 158 67
fill 139 64 42 158 91 67 minecraft:air
fill 139 60 42 158 62 67 minecraft:stone
fill 139 63 42 158 63 67 minecraft:light_gray_concrete
fill 143 64 48 158 79 48 minecraft:light_gray_concrete
fill 143 64 48 143 79 61 minecraft:light_gray_concrete
setblock 144 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 145 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
fill 153 64 48 153 79 61 minecraft:light_gray_concrete
setblock 145 64 52 minecraft:stone_bricks
setblock 145 64 54 minecraft:glass
setblock 146 64 52 minecraft:stone_bricks
setblock 146 64 54 minecraft:glass
setblock 147 64 52 minecraft:stone_bricks
setblock 147 64 54 minecraft:glass
setblock 148 64 52 minecraft:stone_bricks
setblock 148 64 54 minecraft:glass
setblock 149 64 52 minecraft:stone_bricks
setblock 149 64 54 minecraft:glass
setblock 150 64 52 minecraft:stone_bricks
setblock 150 64 54 minecraft:glass
setblock 151 64 52 minecraft:stone_bricks
setblock 151 64 54 minecraft:glass
setblock 145 64 53 minecraft:stone_bricks
setblock 151 64 53 minecraft:stone_bricks
setblock 146 64 53 minecraft:water
setblock 148 63 53 minecraft:air
setblock 149 64 53 minecraft:cobblestone
setblock 150 64 53 minecraft:lava
setblock 149 64 52 create:mechanical_drill[facing=south]
fill 148 64 51 150 65 51 create:andesite_casing
setblock 149 64 51 create:andesite_encased_shaft[axis=z]
setblock 149 64 50 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
