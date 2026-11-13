# 134 industrial/frame_simple
#area 245 240 266 265
fill 245 64 240 266 91 265 minecraft:air
fill 245 60 240 266 62 265 minecraft:stone
fill 245 63 240 266 63 265 minecraft:light_gray_concrete
fill 249 64 246 266 79 246 minecraft:light_gray_concrete
fill 249 64 246 249 79 259 minecraft:light_gray_concrete
setblock 250 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134"}','{"text": "industrial"}','{"text": "frame_simple"}','{"text": ""}']}}
setblock 251 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the three frame"}','{"text": "recipes"}','{"text": ""}','{"text": ""}']}}
fill 261 64 246 261 79 259 minecraft:light_gray_concrete
setblock 252 64 251 industrialforegoing:machine_frame_pity
setblock 254 64 251 industrialforegoing:machine_frame_simple
setblock 256 64 251 industrialforegoing:machine_frame_advanced
setblock 258 64 251 industrialforegoing:machine_frame_supreme
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
