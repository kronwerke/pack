# 118 industrial/frame_simple
#area 21 216 42 241
fill 21 64 216 42 91 241 minecraft:air
fill 21 60 216 42 62 241 minecraft:stone
fill 21 63 216 42 63 241 minecraft:light_gray_concrete
fill 25 64 222 42 79 222 minecraft:light_gray_concrete
fill 25 64 222 25 79 235 minecraft:light_gray_concrete
setblock 26 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118"}','{"text": "industrial"}','{"text": "frame_simple"}','{"text": ""}']}}
setblock 27 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the three frame"}','{"text": "recipes"}','{"text": ""}','{"text": ""}']}}
fill 37 64 222 37 79 235 minecraft:light_gray_concrete
setblock 28 64 227 industrialforegoing:machine_frame_pity
setblock 30 64 227 industrialforegoing:machine_frame_simple
setblock 32 64 227 industrialforegoing:machine_frame_advanced
setblock 34 64 227 industrialforegoing:machine_frame_supreme
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
