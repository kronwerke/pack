# 125 list_dimensions/d_mining, r_plates, r_enderio
#area 97 298 135 323
fill 97 64 298 135 91 323 minecraft:air
fill 97 60 298 135 62 323 minecraft:stone
fill 97 63 298 135 63 323 minecraft:light_gray_concrete
fill 101 64 304 135 79 304 minecraft:light_gray_concrete
fill 101 64 304 101 79 317 minecraft:light_gray_concrete
setblock 102 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 103 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 110 64 304 110 79 317 minecraft:light_gray_concrete
setblock 104 65 309 kronwerke:grubenrahmen
setblock 104 66 309 kronwerke:grubenrahmen
setblock 104 67 309 kronwerke:grubenrahmen
setblock 105 64 309 kronwerke:grubenrahmen
setblock 105 68 309 kronwerke:grubenrahmen
setblock 106 64 309 kronwerke:grubenrahmen
setblock 106 68 309 kronwerke:grubenrahmen
setblock 107 65 309 kronwerke:grubenrahmen
setblock 107 66 309 kronwerke:grubenrahmen
setblock 107 67 309 kronwerke:grubenrahmen
kw testworld use 105 64 309 up ars_nouveau:source_gem
setblock 111 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 112 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 120 64 304 120 79 317 minecraft:light_gray_concrete
setblock 113 64 309 waystones:warp_plate[status=idle]
setblock 117 64 309 waystones:warp_plate[status=idle]
setblock 121 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 122 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 130 64 304 130 79 317 minecraft:light_gray_concrete
setblock 123 64 310 enderio:travel_anchor
fill 127 64 308 127 66 308 minecraft:stone_bricks
setblock 127 67 308 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
