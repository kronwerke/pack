# 023 create/cobble_gen
#area 154 42 173 67
fill 154 64 42 173 91 67 minecraft:air
fill 154 60 42 173 62 67 minecraft:stone
fill 154 63 42 173 63 67 minecraft:light_gray_concrete
fill 158 64 48 173 79 48 minecraft:light_gray_concrete
fill 158 64 48 158 79 61 minecraft:light_gray_concrete
setblock 159 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 160 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
fill 168 64 48 168 79 61 minecraft:light_gray_concrete
setblock 160 64 52 minecraft:stone_bricks
setblock 160 64 54 minecraft:glass
setblock 161 64 52 minecraft:stone_bricks
setblock 161 64 54 minecraft:glass
setblock 162 64 52 minecraft:stone_bricks
setblock 162 64 54 minecraft:glass
setblock 163 64 52 minecraft:stone_bricks
setblock 163 64 54 minecraft:glass
setblock 164 64 52 minecraft:stone_bricks
setblock 164 64 54 minecraft:glass
setblock 165 64 52 minecraft:stone_bricks
setblock 165 64 54 minecraft:glass
setblock 166 64 52 minecraft:stone_bricks
setblock 166 64 54 minecraft:glass
setblock 160 64 53 minecraft:stone_bricks
setblock 166 64 53 minecraft:stone_bricks
setblock 161 64 53 minecraft:water
setblock 163 63 53 minecraft:air
setblock 164 64 53 minecraft:cobblestone
setblock 165 64 53 minecraft:lava
setblock 164 64 52 create:mechanical_drill[facing=south]
fill 163 64 51 165 65 51 create:andesite_casing
setblock 164 64 51 create:andesite_encased_shaft[axis=z]
setblock 164 64 50 create:creative_motor[facing=south]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
