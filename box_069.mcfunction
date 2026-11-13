# 069 botania/endo_auto
#area 11 109 30 134
fill 11 64 109 30 91 134 minecraft:air
fill 11 60 109 30 62 134 minecraft:stone
fill 11 63 109 30 63 134 minecraft:light_gray_concrete
fill 15 64 115 30 79 115 minecraft:light_gray_concrete
fill 15 64 115 15 79 128 minecraft:light_gray_concrete
setblock 16 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "botania"}','{"text": "endo_auto"}','{"text": ""}']}}
setblock 17 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, hopper"}','{"text": "and open crate"}','{"text": "over four"}','{"text": "Endoflames,"}']}}
setblock 18 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressure plate"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 115 25 79 128 minecraft:light_gray_concrete
fill 19 63 120 21 63 121 minecraft:grass_block
setblock 20 63 120 minecraft:light_gray_concrete
setblock 19 64 120 botania:endoflame
setblock 21 64 120 botania:endoflame
setblock 19 64 121 botania:endoflame
setblock 20 64 121 botania:endoflame
setblock 21 64 121 botania:endoflame
setblock 20 64 120 minecraft:oak_pressure_plate
setblock 20 66 120 botania:open_crate
setblock 20 67 120 minecraft:hopper[facing=down]
setblock 20 68 120 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 20 64 119 minecraft:redstone_wire
setblock 20 64 118 minecraft:stone_bricks
setblock 20 65 118 minecraft:redstone_wire
setblock 21 65 118 minecraft:stone_bricks
setblock 21 66 118 minecraft:redstone_wire
setblock 21 66 119 minecraft:stone_bricks
setblock 21 67 119 minecraft:redstone_wire
setblock 21 67 120 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
