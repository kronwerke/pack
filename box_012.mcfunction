# 012 farms/mana_endoflame
#area 107 21 128 46
fill 107 64 21 128 91 46 minecraft:air
fill 107 60 21 128 62 46 minecraft:stone
fill 107 63 21 128 63 46 minecraft:light_gray_concrete
fill 111 64 27 128 79 27 minecraft:light_gray_concrete
fill 111 64 27 111 79 40 minecraft:light_gray_concrete
setblock 112 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "farms"}','{"text": "mana_endoflame"}','{"text": ""}']}}
setblock 113 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Endoflame ring,"}','{"text": "spreader, open"}','{"text": "crate with"}','{"text": "hopper and"}']}}
setblock 114 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, pressure"}','{"text": "plate"}','{"text": ""}','{"text": ""}']}}
fill 123 64 27 123 79 40 minecraft:light_gray_concrete
fill 115 63 30 119 63 34 minecraft:grass_block
setblock 121 64 32 botania:mana_pool{mana:300000}
setblock 118 64 32 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 116 64 31 botania:endoflame
setblock 117 64 31 botania:endoflame
setblock 118 64 31 botania:endoflame
setblock 116 64 33 botania:endoflame
setblock 117 64 33 botania:endoflame
setblock 118 64 33 botania:endoflame
setblock 117 64 32 botania:endoflame
setblock 115 64 32 minecraft:oak_pressure_plate
setblock 115 66 32 botania:open_crate
setblock 115 67 32 minecraft:hopper[facing=down]
setblock 115 68 32 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 115 64 31 minecraft:redstone_wire
setblock 115 64 30 minecraft:stone_bricks
setblock 115 65 30 minecraft:redstone_wire
setblock 116 65 30 minecraft:stone_bricks
setblock 116 66 30 minecraft:redstone_wire
setblock 116 66 31 minecraft:stone_bricks
setblock 116 67 31 minecraft:redstone_wire
setblock 116 67 32 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
