# 161 list_dimensions/d_mining, r_plates, r_enderio
#area -4 365 34 390
fill -4 64 365 34 91 390 minecraft:air
fill -4 60 365 34 62 390 minecraft:stone
fill -4 63 365 34 63 390 minecraft:light_gray_concrete
fill 0 64 371 34 79 371 minecraft:light_gray_concrete
fill 0 64 371 0 79 384 minecraft:light_gray_concrete
setblock 1 64 383 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 2 64 383 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 9 64 371 9 79 384 minecraft:light_gray_concrete
setblock 3 65 376 kronwerke:grubenrahmen
setblock 3 66 376 kronwerke:grubenrahmen
setblock 3 67 376 kronwerke:grubenrahmen
setblock 4 64 376 kronwerke:grubenrahmen
setblock 4 68 376 kronwerke:grubenrahmen
setblock 5 64 376 kronwerke:grubenrahmen
setblock 5 68 376 kronwerke:grubenrahmen
setblock 6 65 376 kronwerke:grubenrahmen
setblock 6 66 376 kronwerke:grubenrahmen
setblock 6 67 376 kronwerke:grubenrahmen
kw testworld use 4 64 376 up ars_nouveau:source_gem
setblock 10 64 383 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 11 64 383 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 19 64 371 19 79 384 minecraft:light_gray_concrete
setblock 12 64 376 waystones:warp_plate[status=idle]
setblock 16 64 376 waystones:warp_plate[status=idle]
setblock 20 64 383 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 21 64 383 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 29 64 371 29 79 384 minecraft:light_gray_concrete
setblock 22 64 377 enderio:travel_anchor
fill 26 64 375 26 66 375 minecraft:stone_bricks
setblock 26 67 375 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
