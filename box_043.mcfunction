# 043 botania/pure_daisy
#area -4 105 15 130
fill -4 64 105 15 91 130 minecraft:air
fill -4 60 105 15 62 130 minecraft:stone
fill -4 63 105 15 63 130 minecraft:light_gray_concrete
fill 0 64 111 15 79 111 minecraft:light_gray_concrete
fill 0 64 111 0 79 124 minecraft:light_gray_concrete
setblock 1 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "043"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
fill 10 64 111 10 79 124 minecraft:light_gray_concrete
setblock 5 63 116 minecraft:grass_block
setblock 5 64 116 botania:pure_daisy
setblock 4 64 115 minecraft:stone
setblock 5 64 115 botania:livingrock
setblock 6 64 115 minecraft:stone
setblock 4 64 116 minecraft:oak_log[axis=y]
setblock 6 64 116 botania:livingwood_log[axis=y]
setblock 4 64 117 botania:livingrock
setblock 5 64 117 minecraft:stone
setblock 6 64 117 botania:livingrock
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
