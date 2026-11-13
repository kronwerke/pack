# 129 industrial/frame_simple
#area 21 250 42 275
fill 21 64 250 42 91 275 minecraft:air
fill 21 60 250 42 62 275 minecraft:stone
fill 21 63 250 42 63 275 minecraft:light_gray_concrete
fill 25 64 256 42 79 256 minecraft:light_gray_concrete
fill 25 64 256 25 79 269 minecraft:light_gray_concrete
setblock 26 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129"}','{"text": "industrial"}','{"text": "frame_simple"}','{"text": ""}']}}
setblock 27 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the three frame"}','{"text": "recipes"}','{"text": ""}','{"text": ""}']}}
fill 37 64 256 37 79 269 minecraft:light_gray_concrete
setblock 28 64 261 industrialforegoing:machine_frame_pity
setblock 30 64 261 industrialforegoing:machine_frame_simple
setblock 32 64 261 industrialforegoing:machine_frame_advanced
setblock 34 64 261 industrialforegoing:machine_frame_supreme
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
