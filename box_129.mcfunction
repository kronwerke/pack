# 129 industrial/frame_simple
#area 21 252 42 277
fill 21 64 252 42 91 277 minecraft:air
fill 21 60 252 42 62 277 minecraft:stone
fill 21 63 252 42 63 277 minecraft:light_gray_concrete
fill 25 64 258 42 79 258 minecraft:light_gray_concrete
fill 25 64 258 25 79 271 minecraft:light_gray_concrete
setblock 26 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129"}','{"text": "industrial"}','{"text": "frame_simple"}','{"text": ""}']}}
setblock 27 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the three frame"}','{"text": "recipes"}','{"text": ""}','{"text": ""}']}}
fill 37 64 258 37 79 271 minecraft:light_gray_concrete
setblock 28 64 263 industrialforegoing:machine_frame_pity
setblock 30 64 263 industrialforegoing:machine_frame_simple
setblock 32 64 263 industrialforegoing:machine_frame_advanced
setblock 34 64 263 industrialforegoing:machine_frame_supreme
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
