# 005 farms/cobble_drill
#area -4 21 15 46
fill -4 64 21 15 91 46 minecraft:air
fill -4 60 21 15 62 46 minecraft:stone
fill -4 63 21 15 63 46 minecraft:light_gray_concrete
fill 0 64 27 15 79 27 minecraft:light_gray_concrete
fill 0 64 27 0 79 40 minecraft:light_gray_concrete
setblock 1 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "005"}','{"text": "farms"}','{"text": "cobble_drill"}','{"text": ""}']}}
setblock 2 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water and lava"}','{"text": "cobble"}','{"text": "generator with"}','{"text": "a drill and an"}']}}
setblock 3 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "andesite"}','{"text": "funnel, belt"}','{"text": "leading away"}','{"text": ""}']}}
fill 10 64 27 10 79 40 minecraft:light_gray_concrete
setblock 2 64 31 minecraft:stone_bricks
setblock 2 65 31 minecraft:stone_bricks
setblock 2 65 33 minecraft:glass
setblock 2 64 33 minecraft:stone_bricks
setblock 2 64 32 minecraft:stone_bricks
setblock 3 64 31 minecraft:stone_bricks
setblock 3 65 31 minecraft:stone_bricks
setblock 3 65 33 minecraft:glass
setblock 3 64 33 minecraft:stone_bricks
setblock 3 64 32 minecraft:stone_bricks
setblock 4 64 31 minecraft:stone_bricks
setblock 4 65 31 minecraft:stone_bricks
setblock 4 65 33 minecraft:glass
setblock 4 64 33 minecraft:stone_bricks
setblock 4 64 32 minecraft:stone_bricks
setblock 5 64 31 minecraft:stone_bricks
setblock 5 65 31 minecraft:stone_bricks
setblock 5 65 33 minecraft:glass
setblock 5 64 33 minecraft:stone_bricks
setblock 5 64 32 minecraft:stone_bricks
setblock 6 64 31 minecraft:stone_bricks
setblock 6 65 31 minecraft:stone_bricks
setblock 6 65 33 minecraft:glass
setblock 7 64 31 minecraft:stone_bricks
setblock 7 65 31 minecraft:stone_bricks
setblock 7 65 33 minecraft:glass
setblock 7 64 33 minecraft:stone_bricks
setblock 7 64 32 minecraft:stone_bricks
setblock 8 64 31 minecraft:stone_bricks
setblock 8 65 31 minecraft:stone_bricks
setblock 8 65 33 minecraft:glass
setblock 8 64 33 minecraft:stone_bricks
setblock 8 64 32 minecraft:stone_bricks
setblock 2 65 32 minecraft:stone_bricks
setblock 8 65 32 minecraft:stone_bricks
setblock 5 64 32 minecraft:air
setblock 5 63 32 minecraft:air
setblock 6 64 32 create:shaft[axis=x]
setblock 6 64 35 create:shaft[axis=x]
kw testworld use 6 64 32 up create:belt_connector
kw testworld use 6 64 35 up create:belt_connector
execute unless block 6 64 33 minecraft:air
setblock 7 64 35 create:creative_motor[facing=west]{ScrollValue:16}
setblock 8 64 35 create:andesite_casing
setblock 7 64 36 create:andesite_casing
setblock 7 64 34 create:andesite_casing
setblock 7 65 35 create:andesite_casing
setblock 3 65 32 minecraft:water
setblock 6 65 32 minecraft:cobblestone
setblock 7 65 32 minecraft:lava
setblock 6 65 31 create:mechanical_drill[facing=south,waterlogged=false]
fill 5 64 30 7 66 30 create:andesite_casing
setblock 6 65 30 create:andesite_encased_shaft[axis=z]
setblock 6 65 29 create:creative_motor[facing=south]{ScrollValue:32}
