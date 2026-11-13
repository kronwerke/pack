# 080 botania/endo_auto
#area 11 143 30 168
fill 11 64 143 30 91 168 minecraft:air
fill 11 60 143 30 62 168 minecraft:stone
fill 11 63 143 30 63 168 minecraft:light_gray_concrete
fill 15 64 149 30 79 149 minecraft:light_gray_concrete
fill 15 64 149 15 79 162 minecraft:light_gray_concrete
setblock 16 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "botania"}','{"text": "endo_auto"}','{"text": ""}']}}
setblock 17 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, hopper"}','{"text": "and open crate"}','{"text": "over four"}','{"text": "Endoflames,"}']}}
setblock 18 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "pressure plate"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 25 64 149 25 79 162 minecraft:light_gray_concrete
fill 19 63 154 21 63 155 minecraft:grass_block
setblock 20 63 154 minecraft:light_gray_concrete
setblock 19 64 154 botania:endoflame
setblock 21 64 154 botania:endoflame
setblock 19 64 155 botania:endoflame
setblock 20 64 155 botania:endoflame
setblock 21 64 155 botania:endoflame
setblock 20 64 154 minecraft:oak_pressure_plate
setblock 20 66 154 botania:open_crate
setblock 20 67 154 minecraft:hopper[facing=down]
setblock 20 68 154 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 20 64 153 minecraft:redstone_wire
setblock 20 64 152 minecraft:stone_bricks
setblock 20 65 152 minecraft:redstone_wire
setblock 21 65 152 minecraft:stone_bricks
setblock 21 66 152 minecraft:redstone_wire
setblock 21 66 153 minecraft:stone_bricks
setblock 21 67 153 minecraft:redstone_wire
setblock 21 67 154 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
