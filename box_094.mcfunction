# 094 the_end/arrival
#area 10 277 29 302
fill 10 64 277 29 91 302 minecraft:air
fill 10 60 277 29 62 302 minecraft:stone
fill 10 63 277 29 63 302 minecraft:light_gray_concrete
fill 14 64 283 29 79 283 minecraft:light_gray_concrete
fill 14 64 283 14 79 296 minecraft:light_gray_concrete
setblock 15 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 16 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 24 64 283 24 79 296 minecraft:light_gray_concrete
setblock 18 64 286 minecraft:end_portal_frame[eye=true,facing=south]
setblock 18 64 290 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 287 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 287 minecraft:end_portal_frame[eye=true,facing=west]
setblock 19 64 286 minecraft:end_portal_frame[eye=true,facing=south]
setblock 19 64 290 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 288 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 288 minecraft:end_portal_frame[eye=true,facing=west]
setblock 20 64 286 minecraft:end_portal_frame[eye=true,facing=south]
setblock 20 64 290 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 289 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 289 minecraft:end_portal_frame[eye=true,facing=west]
fill 18 64 287 20 64 289 minecraft:end_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
