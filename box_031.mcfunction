# 031 create_trains/cargo
#area 281 42 302 67
fill 281 64 42 302 91 67 minecraft:air
fill 281 60 42 302 62 67 minecraft:stone
fill 281 63 42 302 63 67 minecraft:light_gray_concrete
fill 285 64 48 302 79 48 minecraft:light_gray_concrete
fill 285 64 48 285 79 61 minecraft:light_gray_concrete
setblock 286 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "create_trains"}','{"text": "cargo"}','{"text": ""}']}}
setblock 287 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a portable"}','{"text": "storage"}','{"text": "interface pair"}','{"text": "at a platform"}']}}
fill 297 64 48 297 79 61 minecraft:light_gray_concrete
fill 287 64 53 295 64 53 create:track[shape=xo,turn=false,waterlogged=false]
setblock 289 65 53 create:small_bogey[axis=x,waterlogged=false]
setblock 293 65 53 create:small_bogey[axis=x,waterlogged=false]
fill 289 66 53 293 66 53 create:railway_casing
setblock 290 67 53 minecraft:barrel[facing=up]
setblock 291 67 53 create:portable_storage_interface[facing=south]
setblock 292 67 53 minecraft:barrel[facing=up]
fill 291 64 56 291 66 56 minecraft:stone_bricks
setblock 291 67 56 minecraft:barrel[facing=up]
setblock 291 67 55 create:portable_storage_interface[facing=north]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
