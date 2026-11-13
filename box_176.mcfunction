# 176 list_dimensions/d_mining, r_plates, r_enderio
#area -4 367 34 392
fill -4 64 367 34 91 392 minecraft:air
fill -4 60 367 34 62 392 minecraft:stone
fill -4 63 367 34 63 392 minecraft:light_gray_concrete
fill 0 64 373 34 79 373 minecraft:light_gray_concrete
fill 0 64 373 0 79 386 minecraft:light_gray_concrete
setblock 1 64 385 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "176.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 2 64 385 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 9 64 373 9 79 386 minecraft:light_gray_concrete
setblock 3 65 378 kronwerke:grubenrahmen
setblock 3 66 378 kronwerke:grubenrahmen
setblock 3 67 378 kronwerke:grubenrahmen
setblock 4 64 378 kronwerke:grubenrahmen
setblock 4 68 378 kronwerke:grubenrahmen
setblock 5 64 378 kronwerke:grubenrahmen
setblock 5 68 378 kronwerke:grubenrahmen
setblock 6 65 378 kronwerke:grubenrahmen
setblock 6 66 378 kronwerke:grubenrahmen
setblock 6 67 378 kronwerke:grubenrahmen
kw testworld use 4 64 378 up ars_nouveau:source_gem
setblock 10 64 385 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "176.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 11 64 385 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 19 64 373 19 79 386 minecraft:light_gray_concrete
setblock 12 64 378 waystones:warp_plate[status=idle]
setblock 16 64 378 waystones:warp_plate[status=idle]
setblock 20 64 385 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "176.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 21 64 385 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 29 64 373 29 79 386 minecraft:light_gray_concrete
setblock 22 64 379 enderio:travel_anchor
fill 26 64 377 26 66 377 minecraft:stone_bricks
setblock 26 67 377 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
