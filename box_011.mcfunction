# 011 farms/mana_endoflame
#area 92 21 113 46
fill 92 64 21 113 91 46 minecraft:air
fill 92 60 21 113 62 46 minecraft:stone
fill 92 63 21 113 63 46 minecraft:light_gray_concrete
fill 96 64 27 113 79 27 minecraft:light_gray_concrete
fill 96 64 27 96 79 40 minecraft:light_gray_concrete
setblock 97 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "farms"}','{"text": "mana_endoflame"}','{"text": ""}']}}
setblock 98 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Endoflame ring,"}','{"text": "spreader, open"}','{"text": "crate with"}','{"text": "hopper and"}']}}
setblock 99 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, pressure"}','{"text": "plate"}','{"text": ""}','{"text": ""}']}}
fill 108 64 27 108 79 40 minecraft:light_gray_concrete
fill 100 63 30 104 63 34 minecraft:grass_block
setblock 106 64 32 botania:mana_pool{mana:300000}
setblock 103 64 32 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 101 64 31 botania:endoflame
setblock 102 64 31 botania:endoflame
setblock 103 64 31 botania:endoflame
setblock 101 64 33 botania:endoflame
setblock 102 64 33 botania:endoflame
setblock 103 64 33 botania:endoflame
setblock 102 64 32 botania:endoflame
setblock 100 64 32 minecraft:oak_pressure_plate
setblock 100 66 32 botania:open_crate
setblock 100 67 32 minecraft:hopper[facing=down]
setblock 100 68 32 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 100 64 31 minecraft:redstone_wire
setblock 100 64 30 minecraft:stone_bricks
setblock 100 65 30 minecraft:redstone_wire
setblock 101 65 30 minecraft:stone_bricks
setblock 101 66 30 minecraft:redstone_wire
setblock 101 66 31 minecraft:stone_bricks
setblock 101 67 31 minecraft:redstone_wire
setblock 101 67 32 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
