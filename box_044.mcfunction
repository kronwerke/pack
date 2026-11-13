# 044 botania/endo_auto
#area 11 105 30 130
fill 11 64 105 30 91 130 minecraft:air
fill 11 60 105 30 62 130 minecraft:stone
fill 11 63 105 30 63 130 minecraft:light_gray_concrete
fill 15 64 111 30 79 111 minecraft:light_gray_concrete
fill 15 64 111 15 79 124 minecraft:light_gray_concrete
setblock 16 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "botania"}','{"text": "endo_auto"}','{"text": ""}']}}
setblock 17 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, hopper"}','{"text": "and open crate"}','{"text": "over four"}','{"text": "Endoflames,"}']}}
setblock 18 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressure plate"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 111 25 79 124 minecraft:light_gray_concrete
fill 19 63 116 21 63 117 minecraft:grass_block
setblock 20 63 116 minecraft:light_gray_concrete
setblock 19 64 116 botania:endoflame
setblock 21 64 116 botania:endoflame
setblock 19 64 117 botania:endoflame
setblock 20 64 117 botania:endoflame
setblock 21 64 117 botania:endoflame
setblock 20 64 116 minecraft:oak_pressure_plate
setblock 20 66 116 botania:open_crate
setblock 20 67 116 minecraft:hopper[facing=down]
setblock 20 68 116 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 20 64 115 minecraft:redstone_wire
setblock 20 64 114 minecraft:stone_bricks
setblock 20 65 114 minecraft:redstone_wire
setblock 21 65 114 minecraft:stone_bricks
setblock 21 66 114 minecraft:redstone_wire
setblock 21 66 115 minecraft:stone_bricks
setblock 21 67 115 minecraft:redstone_wire
setblock 21 67 116 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
