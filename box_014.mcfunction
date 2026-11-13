# 014 farms/mana_endoflame
#area 122 21 143 46
fill 122 64 21 143 91 46 minecraft:air
fill 122 60 21 143 62 46 minecraft:stone
fill 122 63 21 143 63 46 minecraft:light_gray_concrete
fill 126 64 27 143 79 27 minecraft:light_gray_concrete
fill 126 64 27 126 79 40 minecraft:light_gray_concrete
setblock 127 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "farms"}','{"text": "mana_endoflame"}','{"text": ""}']}}
setblock 128 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Endoflame ring,"}','{"text": "spreader, open"}','{"text": "crate with"}','{"text": "hopper and"}']}}
setblock 129 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chest, pressure"}','{"text": "plate"}','{"text": ""}','{"text": ""}']}}
fill 138 64 27 138 79 40 minecraft:light_gray_concrete
fill 130 63 30 134 63 34 minecraft:grass_block
setblock 136 64 32 botania:mana_pool{mana:300000}
setblock 133 64 32 botania:mana_spreader{rotationX:180f,rotationY:0f,mana:1000}
setblock 131 64 31 botania:endoflame
setblock 132 64 31 botania:endoflame
setblock 133 64 31 botania:endoflame
setblock 131 64 33 botania:endoflame
setblock 132 64 33 botania:endoflame
setblock 133 64 33 botania:endoflame
setblock 132 64 32 botania:endoflame
setblock 130 64 32 minecraft:oak_pressure_plate
setblock 130 66 32 botania:open_crate
setblock 130 67 32 minecraft:hopper[facing=down]
setblock 130 68 32 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:64}]}
setblock 130 64 31 minecraft:redstone_wire
setblock 130 64 30 minecraft:stone_bricks
setblock 130 65 30 minecraft:redstone_wire
setblock 131 65 30 minecraft:stone_bricks
setblock 131 66 30 minecraft:redstone_wire
setblock 131 66 31 minecraft:stone_bricks
setblock 131 67 31 minecraft:redstone_wire
setblock 131 67 32 minecraft:stone_bricks
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
