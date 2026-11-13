# 010 farms/mana_endoflame
#area 77 21 98 46
fill 77 64 21 98 91 46 minecraft:air
fill 77 60 21 98 62 46 minecraft:stone
fill 77 63 21 98 63 46 minecraft:light_gray_concrete
fill 81 64 27 98 79 27 minecraft:light_gray_concrete
fill 81 64 27 81 79 40 minecraft:light_gray_concrete
setblock 82 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "farms"}','{"text": "mana_endoflame"}','{"text": ""}']}}
setblock 83 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Endoflame ring,"}','{"text": "spreader, open"}','{"text": "crate with"}','{"text": "hopper and"}']}}
setblock 84 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, pressure"}','{"text": "plate"}','{"text": ""}','{"text": ""}']}}
fill 93 64 27 93 79 40 minecraft:light_gray_concrete
fill 85 63 30 89 63 34 minecraft:grass_block
setblock 91 64 32 botania:mana_pool{mana:300000}
setblock 88 64 32 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 86 64 31 botania:endoflame
setblock 87 64 31 botania:endoflame
setblock 88 64 31 botania:endoflame
setblock 86 64 33 botania:endoflame
setblock 87 64 33 botania:endoflame
setblock 88 64 33 botania:endoflame
setblock 87 64 32 botania:endoflame
setblock 85 64 32 minecraft:oak_pressure_plate
setblock 85 66 32 botania:open_crate
setblock 85 67 32 minecraft:hopper[facing=down]
setblock 85 68 32 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 85 64 31 minecraft:redstone_wire
setblock 85 64 30 minecraft:stone_bricks
setblock 85 65 30 minecraft:redstone_wire
setblock 86 65 30 minecraft:stone_bricks
setblock 86 66 30 minecraft:redstone_wire
setblock 86 66 31 minecraft:stone_bricks
setblock 86 67 31 minecraft:redstone_wire
setblock 86 67 32 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
