# 079 botania/pure_daisy
#area -4 145 15 170
fill -4 64 145 15 91 170 minecraft:air
fill -4 60 145 15 62 170 minecraft:stone
fill -4 63 145 15 63 170 minecraft:light_gray_concrete
fill 0 64 151 15 79 151 minecraft:light_gray_concrete
fill 0 64 151 0 79 164 minecraft:light_gray_concrete
setblock 1 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
fill 10 64 151 10 79 164 minecraft:light_gray_concrete
setblock 5 63 156 minecraft:grass_block
setblock 5 64 156 botania:pure_daisy
setblock 4 64 155 minecraft:stone
setblock 5 64 155 botania:livingrock
setblock 6 64 155 minecraft:stone
setblock 4 64 156 minecraft:oak_log[axis=y]
setblock 6 64 156 botania:livingwood_log[axis=y]
setblock 4 64 157 botania:livingrock
setblock 5 64 157 minecraft:stone
setblock 6 64 157 botania:livingrock
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
