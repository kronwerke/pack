# 156 list_dimensions/d_mining, r_plates, r_enderio
#area 341 336 379 361
fill 341 64 336 379 91 361 minecraft:air
fill 341 60 336 379 62 361 minecraft:stone
fill 341 63 336 379 63 361 minecraft:light_gray_concrete
fill 345 64 342 379 79 342 minecraft:light_gray_concrete
fill 345 64 342 345 79 355 minecraft:light_gray_concrete
setblock 346 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 347 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 354 64 342 354 79 355 minecraft:light_gray_concrete
setblock 348 65 347 kronwerke:grubenrahmen
setblock 348 66 347 kronwerke:grubenrahmen
setblock 348 67 347 kronwerke:grubenrahmen
setblock 349 64 347 kronwerke:grubenrahmen
setblock 349 68 347 kronwerke:grubenrahmen
setblock 350 64 347 kronwerke:grubenrahmen
setblock 350 68 347 kronwerke:grubenrahmen
setblock 351 65 347 kronwerke:grubenrahmen
setblock 351 66 347 kronwerke:grubenrahmen
setblock 351 67 347 kronwerke:grubenrahmen
kw testworld use 349 64 347 up ars_nouveau:source_gem
setblock 355 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 356 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 364 64 342 364 79 355 minecraft:light_gray_concrete
setblock 357 64 347 waystones:warp_plate[status=idle]
setblock 361 64 347 waystones:warp_plate[status=idle]
setblock 365 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 366 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 374 64 342 374 79 355 minecraft:light_gray_concrete
setblock 367 64 348 enderio:travel_anchor
fill 371 64 346 371 66 346 minecraft:stone_bricks
setblock 371 67 346 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
