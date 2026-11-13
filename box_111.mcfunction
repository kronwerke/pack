# 111 industrial/frame_simple
#area 21 214 42 239
fill 21 64 214 42 91 239 minecraft:air
fill 21 60 214 42 62 239 minecraft:stone
fill 21 63 214 42 63 239 minecraft:light_gray_concrete
fill 25 64 220 42 79 220 minecraft:light_gray_concrete
fill 25 64 220 25 79 233 minecraft:light_gray_concrete
setblock 26 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111"}','{"text": "industrial"}','{"text": "frame_simple"}','{"text": ""}']}}
setblock 27 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the three frame"}','{"text": "recipes"}','{"text": ""}','{"text": ""}']}}
fill 37 64 220 37 79 233 minecraft:light_gray_concrete
setblock 28 64 225 industrialforegoing:machine_frame_pity
setblock 30 64 225 industrialforegoing:machine_frame_simple
setblock 32 64 225 industrialforegoing:machine_frame_advanced
setblock 34 64 225 industrialforegoing:machine_frame_supreme
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
