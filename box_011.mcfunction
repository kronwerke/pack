# 011 farms/mobs_dark
#area 75 21 94 50
fill 75 64 21 94 105 50 minecraft:air
fill 75 60 21 94 62 50 minecraft:stone
fill 75 63 21 94 63 50 minecraft:light_gray_concrete
fill 79 64 27 94 93 27 minecraft:light_gray_concrete
fill 79 64 27 79 93 44 minecraft:light_gray_concrete
setblock 80 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "011"}','{"text": "farms"}','{"text": "mobs_dark"}','{"text": ""}']}}
setblock 81 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cutaway of the"}','{"text": "dark room with"}','{"text": "trapdoor edges"}','{"text": "and the 22"}']}}
setblock 82 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "block shaft"}','{"text": "with hoppers"}','{"text": ""}','{"text": ""}']}}
fill 89 64 27 89 93 44 minecraft:light_gray_concrete
fill 82 87 30 86 87 34 minecraft:cobblestone
fill 82 88 30 86 90 30 minecraft:cobblestone
fill 82 88 31 82 90 34 minecraft:cobblestone
fill 86 88 31 86 90 34 minecraft:cobblestone
fill 82 91 30 86 91 34 minecraft:cobblestone
fill 84 87 32 84 87 32 minecraft:air
setblock 83 87 32 minecraft:oak_trapdoor[facing=east,half=top,open=true]
setblock 85 87 32 minecraft:oak_trapdoor[facing=west,half=top,open=true]
setblock 84 87 31 minecraft:oak_trapdoor[facing=south,half=top,open=true]
setblock 84 87 33 minecraft:oak_trapdoor[facing=north,half=top,open=true]
fill 83 65 31 85 86 33 minecraft:glass
fill 84 65 32 84 86 32 minecraft:air
fill 84 65 33 84 86 33 minecraft:air
setblock 84 64 32 minecraft:hopper[facing=south]
setblock 84 64 33 minecraft:chest[facing=south,type=single,waterlogged=false]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
