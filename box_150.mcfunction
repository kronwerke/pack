# 150 the_end/arrival
#area 10 334 29 359
fill 10 64 334 29 91 359 minecraft:air
fill 10 60 334 29 62 359 minecraft:stone
fill 10 63 334 29 63 359 minecraft:light_gray_concrete
fill 14 64 340 29 79 340 minecraft:light_gray_concrete
fill 14 64 340 14 79 353 minecraft:light_gray_concrete
setblock 15 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 16 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 24 64 340 24 79 353 minecraft:light_gray_concrete
setblock 18 64 343 minecraft:end_portal_frame[eye=true,facing=south]
setblock 18 64 347 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 344 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 344 minecraft:end_portal_frame[eye=true,facing=west]
setblock 19 64 343 minecraft:end_portal_frame[eye=true,facing=south]
setblock 19 64 347 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 345 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 345 minecraft:end_portal_frame[eye=true,facing=west]
setblock 20 64 343 minecraft:end_portal_frame[eye=true,facing=south]
setblock 20 64 347 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 346 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 346 minecraft:end_portal_frame[eye=true,facing=west]
fill 18 64 344 20 64 346 minecraft:end_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
