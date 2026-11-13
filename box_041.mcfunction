# 041 create_trains/cargo
#area 46 68 65 95
fill 46 64 68 65 91 95 minecraft:air
fill 46 60 68 65 62 95 minecraft:stone
fill 46 63 68 65 63 95 minecraft:light_gray_concrete
fill 50 64 74 65 79 74 minecraft:light_gray_concrete
fill 50 64 74 50 79 89 minecraft:light_gray_concrete
setblock 51 64 88 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "create_trains"}','{"text": "cargo"}','{"text": ""}']}}
setblock 52 64 88 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a portable"}','{"text": "storage"}','{"text": "interface pair"}','{"text": "at a platform"}']}}
fill 60 64 74 60 79 89 minecraft:light_gray_concrete
fill 55 64 76 55 64 84 create:track[shape=zo,turn=false,waterlogged=false]
setblock 55 65 78 create:small_bogey[axis=z,waterlogged=false]
setblock 55 65 82 create:small_bogey[axis=z,waterlogged=false]
fill 55 66 78 55 66 82 create:railway_casing
setblock 55 67 79 minecraft:barrel[facing=up]
setblock 55 67 80 create:portable_storage_interface[facing=east]
setblock 55 67 81 minecraft:barrel[facing=up]
fill 58 64 80 58 66 80 minecraft:stone_bricks
setblock 58 67 80 minecraft:barrel[facing=up]
setblock 57 67 80 create:portable_storage_interface[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
