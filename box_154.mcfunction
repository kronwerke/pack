# 154 list_dimensions/d_mining, r_plates, r_enderio
#area 97 334 135 359
fill 97 64 334 135 91 359 minecraft:air
fill 97 60 334 135 62 359 minecraft:stone
fill 97 63 334 135 63 359 minecraft:light_gray_concrete
fill 101 64 340 135 79 340 minecraft:light_gray_concrete
fill 101 64 340 101 79 353 minecraft:light_gray_concrete
setblock 102 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 103 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 110 64 340 110 79 353 minecraft:light_gray_concrete
setblock 104 65 345 kronwerke:grubenrahmen
setblock 104 66 345 kronwerke:grubenrahmen
setblock 104 67 345 kronwerke:grubenrahmen
setblock 105 64 345 kronwerke:grubenrahmen
setblock 105 68 345 kronwerke:grubenrahmen
setblock 106 64 345 kronwerke:grubenrahmen
setblock 106 68 345 kronwerke:grubenrahmen
setblock 107 65 345 kronwerke:grubenrahmen
setblock 107 66 345 kronwerke:grubenrahmen
setblock 107 67 345 kronwerke:grubenrahmen
kw testworld use 105 64 345 up ars_nouveau:source_gem
setblock 111 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 112 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 120 64 340 120 79 353 minecraft:light_gray_concrete
setblock 113 64 345 waystones:warp_plate[status=idle]
setblock 117 64 345 waystones:warp_plate[status=idle]
setblock 121 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 122 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 130 64 340 130 79 353 minecraft:light_gray_concrete
setblock 123 64 346 enderio:travel_anchor
fill 127 64 344 127 66 344 minecraft:stone_bricks
setblock 127 67 344 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
