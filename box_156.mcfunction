# 156 list_dimensions/d_mining, r_plates, r_enderio
#area -4 361 34 386
fill -4 64 361 34 91 386 minecraft:air
fill -4 60 361 34 62 386 minecraft:stone
fill -4 63 361 34 63 386 minecraft:light_gray_concrete
fill 0 64 367 34 79 367 minecraft:light_gray_concrete
fill 0 64 367 0 79 380 minecraft:light_gray_concrete
setblock 1 64 379 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 2 64 379 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 9 64 367 9 79 380 minecraft:light_gray_concrete
setblock 3 65 372 kronwerke:grubenrahmen
setblock 3 66 372 kronwerke:grubenrahmen
setblock 3 67 372 kronwerke:grubenrahmen
setblock 4 64 372 kronwerke:grubenrahmen
setblock 4 68 372 kronwerke:grubenrahmen
setblock 5 64 372 kronwerke:grubenrahmen
setblock 5 68 372 kronwerke:grubenrahmen
setblock 6 65 372 kronwerke:grubenrahmen
setblock 6 66 372 kronwerke:grubenrahmen
setblock 6 67 372 kronwerke:grubenrahmen
kw testworld use 4 64 372 up ars_nouveau:source_gem
setblock 10 64 379 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 11 64 379 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 19 64 367 19 79 380 minecraft:light_gray_concrete
setblock 12 64 372 waystones:warp_plate[status=idle]
setblock 16 64 372 waystones:warp_plate[status=idle]
setblock 20 64 379 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 21 64 379 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 29 64 367 29 79 380 minecraft:light_gray_concrete
setblock 22 64 373 enderio:travel_anchor
fill 26 64 371 26 66 371 minecraft:stone_bricks
setblock 26 67 371 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
