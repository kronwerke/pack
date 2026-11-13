# 149 industrial/frame_simple
#area 245 242 266 267
fill 245 64 242 266 91 267 minecraft:air
fill 245 60 242 266 62 267 minecraft:stone
fill 245 63 242 266 63 267 minecraft:light_gray_concrete
fill 249 64 248 266 79 248 minecraft:light_gray_concrete
fill 249 64 248 249 79 261 minecraft:light_gray_concrete
setblock 250 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149"}','{"text": "industrial"}','{"text": "frame_simple"}','{"text": ""}']}}
setblock 251 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the three frame"}','{"text": "recipes"}','{"text": ""}','{"text": ""}']}}
fill 261 64 248 261 79 261 minecraft:light_gray_concrete
setblock 252 64 253 industrialforegoing:machine_frame_pity
setblock 254 64 253 industrialforegoing:machine_frame_simple
setblock 256 64 253 industrialforegoing:machine_frame_advanced
setblock 258 64 253 industrialforegoing:machine_frame_supreme
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
