# 060 botania/endo_auto
#area 11 107 30 132
fill 11 64 107 30 91 132 minecraft:air
fill 11 60 107 30 62 132 minecraft:stone
fill 11 63 107 30 63 132 minecraft:light_gray_concrete
fill 15 64 113 30 79 113 minecraft:light_gray_concrete
fill 15 64 113 15 79 126 minecraft:light_gray_concrete
setblock 16 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "060"}','{"text": "botania"}','{"text": "endo_auto"}','{"text": ""}']}}
setblock 17 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, hopper"}','{"text": "and open crate"}','{"text": "over four"}','{"text": "Endoflames,"}']}}
setblock 18 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressure plate"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 113 25 79 126 minecraft:light_gray_concrete
fill 19 63 118 21 63 119 minecraft:grass_block
setblock 20 63 118 minecraft:light_gray_concrete
setblock 19 64 118 botania:endoflame
setblock 21 64 118 botania:endoflame
setblock 19 64 119 botania:endoflame
setblock 20 64 119 botania:endoflame
setblock 21 64 119 botania:endoflame
setblock 20 64 118 minecraft:oak_pressure_plate
setblock 20 66 118 botania:open_crate
setblock 20 67 118 minecraft:hopper[facing=down]
setblock 20 68 118 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 20 64 117 minecraft:redstone_wire
setblock 20 64 116 minecraft:stone_bricks
setblock 20 65 116 minecraft:redstone_wire
setblock 21 65 116 minecraft:stone_bricks
setblock 21 66 116 minecraft:redstone_wire
setblock 21 66 117 minecraft:stone_bricks
setblock 21 67 117 minecraft:redstone_wire
setblock 21 67 118 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
