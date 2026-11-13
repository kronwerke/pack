# 043 create_trains/cargo
#area 46 70 65 97
fill 46 64 70 65 91 97 minecraft:air
fill 46 60 70 65 62 97 minecraft:stone
fill 46 63 70 65 63 97 minecraft:light_gray_concrete
fill 50 64 76 65 79 76 minecraft:light_gray_concrete
fill 50 64 76 50 79 91 minecraft:light_gray_concrete
setblock 51 64 90 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "043"}','{"text": "create_trains"}','{"text": "cargo"}','{"text": ""}']}}
setblock 52 64 90 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a portable"}','{"text": "storage"}','{"text": "interface pair"}','{"text": "at a platform"}']}}
fill 60 64 76 60 79 91 minecraft:light_gray_concrete
fill 55 64 78 55 64 86 create:track[shape=zo,turn=false,waterlogged=false]
setblock 55 65 80 create:small_bogey[axis=z,waterlogged=false]
setblock 55 65 84 create:small_bogey[axis=z,waterlogged=false]
fill 55 66 80 55 66 84 create:railway_casing
setblock 55 67 81 minecraft:barrel[facing=up]
setblock 55 67 82 create:portable_storage_interface[facing=east]
setblock 55 67 83 minecraft:barrel[facing=up]
fill 58 64 82 58 66 82 minecraft:stone_bricks
setblock 58 67 82 minecraft:barrel[facing=up]
setblock 57 67 82 create:portable_storage_interface[facing=west]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
