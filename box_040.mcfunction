# 040 create_trains/cargo
#area 24 68 43 95
fill 24 64 68 43 91 95 minecraft:air
fill 24 60 68 43 62 95 minecraft:stone
fill 24 63 68 43 63 95 minecraft:light_gray_concrete
fill 28 64 74 43 79 74 minecraft:light_gray_concrete
fill 28 64 74 28 79 89 minecraft:light_gray_concrete
setblock 29 64 88 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040"}','{"text": "create_trains"}','{"text": "cargo"}','{"text": ""}']}}
setblock 30 64 88 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a portable"}','{"text": "storage"}','{"text": "interface pair"}','{"text": "at a platform"}']}}
fill 38 64 74 38 79 89 minecraft:light_gray_concrete
fill 33 64 76 33 64 84 create:track[shape=zo,turn=false,waterlogged=false]
setblock 33 65 78 create:small_bogey[axis=z,waterlogged=false]
setblock 33 65 82 create:small_bogey[axis=z,waterlogged=false]
fill 33 66 78 33 66 82 create:railway_casing
setblock 33 67 79 minecraft:barrel[facing=up]
setblock 33 67 80 create:portable_storage_interface[facing=east]
setblock 33 67 81 minecraft:barrel[facing=up]
fill 36 64 80 36 66 80 minecraft:stone_bricks
setblock 36 67 80 minecraft:barrel[facing=up]
setblock 35 67 80 create:portable_storage_interface[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
