# 150 the_end/arrival
#area 10 336 29 361
fill 10 64 336 29 91 361 minecraft:air
fill 10 60 336 29 62 361 minecraft:stone
fill 10 63 336 29 63 361 minecraft:light_gray_concrete
fill 14 64 342 29 79 342 minecraft:light_gray_concrete
fill 14 64 342 14 79 355 minecraft:light_gray_concrete
setblock 15 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 16 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 24 64 342 24 79 355 minecraft:light_gray_concrete
setblock 18 64 345 minecraft:end_portal_frame[eye=true,facing=south]
setblock 18 64 349 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 346 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 346 minecraft:end_portal_frame[eye=true,facing=west]
setblock 19 64 345 minecraft:end_portal_frame[eye=true,facing=south]
setblock 19 64 349 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 347 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 347 minecraft:end_portal_frame[eye=true,facing=west]
setblock 20 64 345 minecraft:end_portal_frame[eye=true,facing=south]
setblock 20 64 349 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 348 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 348 minecraft:end_portal_frame[eye=true,facing=west]
fill 18 64 346 20 64 348 minecraft:end_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
