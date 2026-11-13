# 128 industrial/frame_simple
#area 21 246 42 271
fill 21 64 246 42 91 271 minecraft:air
fill 21 60 246 42 62 271 minecraft:stone
fill 21 63 246 42 63 271 minecraft:light_gray_concrete
fill 25 64 252 42 79 252 minecraft:light_gray_concrete
fill 25 64 252 25 79 265 minecraft:light_gray_concrete
setblock 26 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128"}','{"text": "industrial"}','{"text": "frame_simple"}','{"text": ""}']}}
setblock 27 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the three frame"}','{"text": "recipes"}','{"text": ""}','{"text": ""}']}}
fill 37 64 252 37 79 265 minecraft:light_gray_concrete
setblock 28 64 257 industrialforegoing:machine_frame_pity
setblock 30 64 257 industrialforegoing:machine_frame_simple
setblock 32 64 257 industrialforegoing:machine_frame_advanced
setblock 34 64 257 industrialforegoing:machine_frame_supreme
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
