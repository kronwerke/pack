# 140 list_dimensions/d_mining, r_plates, r_enderio
#area 97 300 135 325
fill 97 64 300 135 91 325 minecraft:air
fill 97 60 300 135 62 325 minecraft:stone
fill 97 63 300 135 63 325 minecraft:light_gray_concrete
fill 101 64 306 135 79 306 minecraft:light_gray_concrete
fill 101 64 306 101 79 319 minecraft:light_gray_concrete
setblock 102 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 103 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 110 64 306 110 79 319 minecraft:light_gray_concrete
setblock 104 65 311 kronwerke:grubenrahmen
setblock 104 66 311 kronwerke:grubenrahmen
setblock 104 67 311 kronwerke:grubenrahmen
setblock 105 64 311 kronwerke:grubenrahmen
setblock 105 68 311 kronwerke:grubenrahmen
setblock 106 64 311 kronwerke:grubenrahmen
setblock 106 68 311 kronwerke:grubenrahmen
setblock 107 65 311 kronwerke:grubenrahmen
setblock 107 66 311 kronwerke:grubenrahmen
setblock 107 67 311 kronwerke:grubenrahmen
kw testworld use 105 64 311 up ars_nouveau:source_gem
setblock 111 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 112 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 120 64 306 120 79 319 minecraft:light_gray_concrete
setblock 113 64 311 waystones:warp_plate[status=idle]
setblock 117 64 311 waystones:warp_plate[status=idle]
setblock 121 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 122 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 130 64 306 130 79 319 minecraft:light_gray_concrete
setblock 123 64 312 enderio:travel_anchor
fill 127 64 310 127 66 310 minecraft:stone_bricks
setblock 127 67 310 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
