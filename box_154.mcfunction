# 154 list_dimensions/d_mining, r_plates, r_enderio
#area 97 336 135 361
fill 97 64 336 135 91 361 minecraft:air
fill 97 60 336 135 62 361 minecraft:stone
fill 97 63 336 135 63 361 minecraft:light_gray_concrete
fill 101 64 342 135 79 342 minecraft:light_gray_concrete
fill 101 64 342 101 79 355 minecraft:light_gray_concrete
setblock 102 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 103 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 110 64 342 110 79 355 minecraft:light_gray_concrete
setblock 104 65 347 kronwerke:grubenrahmen
setblock 104 66 347 kronwerke:grubenrahmen
setblock 104 67 347 kronwerke:grubenrahmen
setblock 105 64 347 kronwerke:grubenrahmen
setblock 105 68 347 kronwerke:grubenrahmen
setblock 106 64 347 kronwerke:grubenrahmen
setblock 106 68 347 kronwerke:grubenrahmen
setblock 107 65 347 kronwerke:grubenrahmen
setblock 107 66 347 kronwerke:grubenrahmen
setblock 107 67 347 kronwerke:grubenrahmen
kw testworld use 105 64 347 up ars_nouveau:source_gem
setblock 111 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 112 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 120 64 342 120 79 355 minecraft:light_gray_concrete
setblock 113 64 347 waystones:warp_plate[status=idle]
setblock 117 64 347 waystones:warp_plate[status=idle]
setblock 121 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 122 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 130 64 342 130 79 355 minecraft:light_gray_concrete
setblock 123 64 348 enderio:travel_anchor
fill 127 64 346 127 66 346 minecraft:stone_bricks
setblock 127 67 346 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
