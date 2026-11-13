# 108 list_dimensions/d_mining, r_plates, r_enderio
#area 97 296 135 321
fill 97 64 296 135 91 321 minecraft:air
fill 97 60 296 135 62 321 minecraft:stone
fill 97 63 296 135 63 321 minecraft:light_gray_concrete
fill 101 64 302 135 79 302 minecraft:light_gray_concrete
fill 101 64 302 101 79 315 minecraft:light_gray_concrete
setblock 102 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 103 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 110 64 302 110 79 315 minecraft:light_gray_concrete
setblock 104 65 307 kronwerke:grubenrahmen
setblock 104 66 307 kronwerke:grubenrahmen
setblock 104 67 307 kronwerke:grubenrahmen
setblock 105 64 307 kronwerke:grubenrahmen
setblock 105 68 307 kronwerke:grubenrahmen
setblock 106 64 307 kronwerke:grubenrahmen
setblock 106 68 307 kronwerke:grubenrahmen
setblock 107 65 307 kronwerke:grubenrahmen
setblock 107 66 307 kronwerke:grubenrahmen
setblock 107 67 307 kronwerke:grubenrahmen
kw testworld use 105 64 307 up ars_nouveau:source_gem
setblock 111 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 112 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 120 64 302 120 79 315 minecraft:light_gray_concrete
setblock 113 64 307 waystones:warp_plate[status=idle]
setblock 117 64 307 waystones:warp_plate[status=idle]
setblock 121 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 122 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 130 64 302 130 79 315 minecraft:light_gray_concrete
setblock 123 64 308 enderio:travel_anchor
fill 127 64 306 127 66 306 minecraft:stone_bricks
setblock 127 67 306 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
