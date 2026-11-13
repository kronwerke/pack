# 150 list_dimensions/d_mining, r_plates, r_enderio
#area 97 330 135 355
fill 97 64 330 135 91 355 minecraft:air
fill 97 60 330 135 62 355 minecraft:stone
fill 97 63 330 135 63 355 minecraft:light_gray_concrete
fill 101 64 336 135 79 336 minecraft:light_gray_concrete
fill 101 64 336 101 79 349 minecraft:light_gray_concrete
setblock 102 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 103 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 110 64 336 110 79 349 minecraft:light_gray_concrete
setblock 104 65 341 kronwerke:grubenrahmen
setblock 104 66 341 kronwerke:grubenrahmen
setblock 104 67 341 kronwerke:grubenrahmen
setblock 105 64 341 kronwerke:grubenrahmen
setblock 105 68 341 kronwerke:grubenrahmen
setblock 106 64 341 kronwerke:grubenrahmen
setblock 106 68 341 kronwerke:grubenrahmen
setblock 107 65 341 kronwerke:grubenrahmen
setblock 107 66 341 kronwerke:grubenrahmen
setblock 107 67 341 kronwerke:grubenrahmen
kw testworld use 105 64 341 up ars_nouveau:source_gem
setblock 111 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 112 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 120 64 336 120 79 349 minecraft:light_gray_concrete
setblock 113 64 341 waystones:warp_plate[status=idle]
setblock 117 64 341 waystones:warp_plate[status=idle]
setblock 121 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 122 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 130 64 336 130 79 349 minecraft:light_gray_concrete
setblock 123 64 342 enderio:travel_anchor
fill 127 64 340 127 66 340 minecraft:stone_bricks
setblock 127 67 340 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
