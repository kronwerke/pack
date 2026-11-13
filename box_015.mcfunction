# 015 create/cobble_gen
#area 106 40 125 65
fill 106 64 40 125 91 65 minecraft:air
fill 106 60 40 125 62 65 minecraft:stone
fill 106 63 40 125 63 65 minecraft:light_gray_concrete
fill 110 64 46 125 79 46 minecraft:light_gray_concrete
fill 110 64 46 110 79 59 minecraft:light_gray_concrete
setblock 111 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "015"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 112 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
fill 120 64 46 120 79 59 minecraft:light_gray_concrete
setblock 112 64 50 minecraft:stone_bricks
setblock 112 64 52 minecraft:glass
setblock 113 64 50 minecraft:stone_bricks
setblock 113 64 52 minecraft:glass
setblock 114 64 50 minecraft:stone_bricks
setblock 114 64 52 minecraft:glass
setblock 115 64 50 minecraft:stone_bricks
setblock 115 64 52 minecraft:glass
setblock 116 64 50 minecraft:stone_bricks
setblock 116 64 52 minecraft:glass
setblock 117 64 50 minecraft:stone_bricks
setblock 117 64 52 minecraft:glass
setblock 118 64 50 minecraft:stone_bricks
setblock 118 64 52 minecraft:glass
setblock 112 64 51 minecraft:stone_bricks
setblock 118 64 51 minecraft:stone_bricks
setblock 113 64 51 minecraft:water
setblock 115 63 51 minecraft:air
setblock 116 64 51 minecraft:cobblestone
setblock 117 64 51 minecraft:lava
setblock 116 64 50 create:mechanical_drill[facing=south]
fill 115 64 49 117 65 49 create:andesite_casing
setblock 116 64 49 create:andesite_encased_shaft[axis=z]
setblock 116 64 48 create:creative_motor[facing=south]{ScrollValue:32}
