# 098 list_dimensions/d_mining, r_plates, r_enderio
#area 97 277 135 302
fill 97 64 277 135 91 302 minecraft:air
fill 97 60 277 135 62 302 minecraft:stone
fill 97 63 277 135 63 302 minecraft:light_gray_concrete
fill 101 64 283 135 79 283 minecraft:light_gray_concrete
fill 101 64 283 101 79 296 minecraft:light_gray_concrete
setblock 102 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 103 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 110 64 283 110 79 296 minecraft:light_gray_concrete
setblock 104 65 288 kronwerke:grubenrahmen
setblock 104 66 288 kronwerke:grubenrahmen
setblock 104 67 288 kronwerke:grubenrahmen
setblock 105 64 288 kronwerke:grubenrahmen
setblock 105 68 288 kronwerke:grubenrahmen
setblock 106 64 288 kronwerke:grubenrahmen
setblock 106 68 288 kronwerke:grubenrahmen
setblock 107 65 288 kronwerke:grubenrahmen
setblock 107 66 288 kronwerke:grubenrahmen
setblock 107 67 288 kronwerke:grubenrahmen
kw testworld use 105 64 288 up ars_nouveau:source_gem
setblock 111 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 112 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 120 64 283 120 79 296 minecraft:light_gray_concrete
setblock 113 64 288 waystones:warp_plate[status=idle]
setblock 117 64 288 waystones:warp_plate[status=idle]
setblock 121 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 122 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 130 64 283 130 79 296 minecraft:light_gray_concrete
setblock 123 64 289 enderio:travel_anchor
fill 127 64 287 127 66 287 minecraft:stone_bricks
setblock 127 67 287 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
