# 012 create/cobble_gen
#area 106 21 125 46
fill 106 64 21 125 91 46 minecraft:air
fill 106 60 21 125 62 46 minecraft:stone
fill 106 63 21 125 63 46 minecraft:light_gray_concrete
fill 110 64 27 125 79 27 minecraft:light_gray_concrete
fill 110 64 27 110 79 40 minecraft:light_gray_concrete
setblock 111 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "create"}','{"text": "cobble_gen"}','{"text": ""}']}}
setblock 112 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "drill in front"}','{"text": "of a cobble"}','{"text": "generator"}','{"text": ""}']}}
fill 120 64 27 120 79 40 minecraft:light_gray_concrete
setblock 112 64 31 minecraft:stone_bricks
setblock 112 64 33 minecraft:glass
setblock 113 64 31 minecraft:stone_bricks
setblock 113 64 33 minecraft:glass
setblock 114 64 31 minecraft:stone_bricks
setblock 114 64 33 minecraft:glass
setblock 115 64 31 minecraft:stone_bricks
setblock 115 64 33 minecraft:glass
setblock 116 64 31 minecraft:stone_bricks
setblock 116 64 33 minecraft:glass
setblock 117 64 31 minecraft:stone_bricks
setblock 117 64 33 minecraft:glass
setblock 118 64 31 minecraft:stone_bricks
setblock 118 64 33 minecraft:glass
setblock 112 64 32 minecraft:stone_bricks
setblock 118 64 32 minecraft:stone_bricks
setblock 113 64 32 minecraft:water
setblock 115 63 32 minecraft:air
setblock 116 64 32 minecraft:cobblestone
setblock 117 64 32 minecraft:lava
setblock 116 64 31 create:mechanical_drill[facing=south]
fill 115 64 30 117 65 30 create:andesite_casing
setblock 116 64 30 create:andesite_encased_shaft[axis=z]
setblock 116 64 29 create:creative_motor[facing=south]{ScrollValue:32}
