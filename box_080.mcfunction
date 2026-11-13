# 080 botania/endo_auto
#area 11 145 30 170
fill 11 64 145 30 91 170 minecraft:air
fill 11 60 145 30 62 170 minecraft:stone
fill 11 63 145 30 63 170 minecraft:light_gray_concrete
fill 15 64 151 30 79 151 minecraft:light_gray_concrete
fill 15 64 151 15 79 164 minecraft:light_gray_concrete
setblock 16 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "botania"}','{"text": "endo_auto"}','{"text": ""}']}}
setblock 17 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, hopper"}','{"text": "and open crate"}','{"text": "over four"}','{"text": "Endoflames,"}']}}
setblock 18 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressure plate"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 151 25 79 164 minecraft:light_gray_concrete
fill 19 63 156 21 63 157 minecraft:grass_block
setblock 20 63 156 minecraft:light_gray_concrete
setblock 19 64 156 botania:endoflame
setblock 21 64 156 botania:endoflame
setblock 19 64 157 botania:endoflame
setblock 20 64 157 botania:endoflame
setblock 21 64 157 botania:endoflame
setblock 20 64 156 minecraft:oak_pressure_plate
setblock 20 66 156 botania:open_crate
setblock 20 67 156 minecraft:hopper[facing=down]
setblock 20 68 156 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 20 64 155 minecraft:redstone_wire
setblock 20 64 154 minecraft:stone_bricks
setblock 20 65 154 minecraft:redstone_wire
setblock 21 65 154 minecraft:stone_bricks
setblock 21 66 154 minecraft:redstone_wire
setblock 21 66 155 minecraft:stone_bricks
setblock 21 67 155 minecraft:redstone_wire
setblock 21 67 156 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
