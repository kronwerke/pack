# 104 the_end/arrival
#area 10 296 29 321
fill 10 64 296 29 91 321 minecraft:air
fill 10 60 296 29 62 321 minecraft:stone
fill 10 63 296 29 63 321 minecraft:light_gray_concrete
fill 14 64 302 29 79 302 minecraft:light_gray_concrete
fill 14 64 302 14 79 315 minecraft:light_gray_concrete
setblock 15 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 16 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 24 64 302 24 79 315 minecraft:light_gray_concrete
setblock 18 64 305 minecraft:end_portal_frame[eye=true,facing=south]
setblock 18 64 309 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 306 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 306 minecraft:end_portal_frame[eye=true,facing=west]
setblock 19 64 305 minecraft:end_portal_frame[eye=true,facing=south]
setblock 19 64 309 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 307 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 307 minecraft:end_portal_frame[eye=true,facing=west]
setblock 20 64 305 minecraft:end_portal_frame[eye=true,facing=south]
setblock 20 64 309 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 308 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 308 minecraft:end_portal_frame[eye=true,facing=west]
fill 18 64 306 20 64 308 minecraft:end_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
