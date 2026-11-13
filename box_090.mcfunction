# 090 botania/endo_auto
#area 11 147 30 172
fill 11 64 147 30 91 172 minecraft:air
fill 11 60 147 30 62 172 minecraft:stone
fill 11 63 147 30 63 172 minecraft:light_gray_concrete
fill 15 64 153 30 79 153 minecraft:light_gray_concrete
fill 15 64 153 15 79 166 minecraft:light_gray_concrete
setblock 16 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090"}','{"text": "botania"}','{"text": "endo_auto"}','{"text": ""}']}}
setblock 17 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, hopper"}','{"text": "and open crate"}','{"text": "over four"}','{"text": "Endoflames,"}']}}
setblock 18 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressure plate"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 153 25 79 166 minecraft:light_gray_concrete
fill 19 63 158 21 63 159 minecraft:grass_block
setblock 20 63 158 minecraft:light_gray_concrete
setblock 19 64 158 botania:endoflame
setblock 21 64 158 botania:endoflame
setblock 19 64 159 botania:endoflame
setblock 20 64 159 botania:endoflame
setblock 21 64 159 botania:endoflame
setblock 20 64 158 minecraft:oak_pressure_plate
setblock 20 66 158 botania:open_crate
setblock 20 67 158 minecraft:hopper[facing=down]
setblock 20 68 158 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 20 64 157 minecraft:redstone_wire
setblock 20 64 156 minecraft:stone_bricks
setblock 20 65 156 minecraft:redstone_wire
setblock 21 65 156 minecraft:stone_bricks
setblock 21 66 156 minecraft:redstone_wire
setblock 21 66 157 minecraft:stone_bricks
setblock 21 67 157 minecraft:redstone_wire
setblock 21 67 158 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
