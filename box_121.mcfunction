# 121 the_end/arrival
#area 10 298 29 323
fill 10 64 298 29 91 323 minecraft:air
fill 10 60 298 29 62 323 minecraft:stone
fill 10 63 298 29 63 323 minecraft:light_gray_concrete
fill 14 64 304 29 79 304 minecraft:light_gray_concrete
fill 14 64 304 14 79 317 minecraft:light_gray_concrete
setblock 15 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 16 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 24 64 304 24 79 317 minecraft:light_gray_concrete
setblock 18 64 307 minecraft:end_portal_frame[eye=true,facing=south]
setblock 18 64 311 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 308 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 308 minecraft:end_portal_frame[eye=true,facing=west]
setblock 19 64 307 minecraft:end_portal_frame[eye=true,facing=south]
setblock 19 64 311 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 309 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 309 minecraft:end_portal_frame[eye=true,facing=west]
setblock 20 64 307 minecraft:end_portal_frame[eye=true,facing=south]
setblock 20 64 311 minecraft:end_portal_frame[eye=true,facing=north]
setblock 17 64 310 minecraft:end_portal_frame[eye=true,facing=east]
setblock 21 64 310 minecraft:end_portal_frame[eye=true,facing=west]
fill 18 64 308 20 64 310 minecraft:end_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
