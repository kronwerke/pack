# 146 the_end/arrival
#area 10 330 29 355
fill 10 64 330 29 91 355 minecraft:air
fill 10 60 330 29 62 355 minecraft:stone
fill 10 63 330 29 63 355 minecraft:light_gray_concrete
fill 14 64 336 29 79 336 minecraft:light_gray_concrete
fill 14 64 336 14 79 349 minecraft:light_gray_concrete
setblock 15 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 16 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 24 64 336 24 79 349 minecraft:light_gray_concrete
setblock 18 64 339 minecraft:end_portal_frame[eye=true,facing=south]
setblock 18 64 343 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 340 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 340 minecraft:end_portal_frame[eye=true,facing=west]
setblock 19 64 339 minecraft:end_portal_frame[eye=true,facing=south]
setblock 19 64 343 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 341 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 341 minecraft:end_portal_frame[eye=true,facing=west]
setblock 20 64 339 minecraft:end_portal_frame[eye=true,facing=south]
setblock 20 64 343 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 342 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 342 minecraft:end_portal_frame[eye=true,facing=west]
fill 18 64 340 20 64 342 minecraft:end_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
