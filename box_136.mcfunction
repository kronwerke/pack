# 136 the_end/arrival
#area 10 300 29 325
fill 10 64 300 29 91 325 minecraft:air
fill 10 60 300 29 62 325 minecraft:stone
fill 10 63 300 29 63 325 minecraft:light_gray_concrete
fill 14 64 306 29 79 306 minecraft:light_gray_concrete
fill 14 64 306 14 79 319 minecraft:light_gray_concrete
setblock 15 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 16 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 24 64 306 24 79 319 minecraft:light_gray_concrete
setblock 18 64 309 minecraft:end_portal_frame[eye=true,facing=south]
setblock 18 64 313 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 310 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 310 minecraft:end_portal_frame[eye=true,facing=west]
setblock 19 64 309 minecraft:end_portal_frame[eye=true,facing=south]
setblock 19 64 313 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 311 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 311 minecraft:end_portal_frame[eye=true,facing=west]
setblock 20 64 309 minecraft:end_portal_frame[eye=true,facing=south]
setblock 20 64 313 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 312 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 312 minecraft:end_portal_frame[eye=true,facing=west]
fill 18 64 310 20 64 312 minecraft:end_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
