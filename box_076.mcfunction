# 076 botania/pure_daisy
#area -4 139 15 164
fill -4 64 139 15 91 164 minecraft:air
fill -4 60 139 15 62 164 minecraft:stone
fill -4 63 139 15 63 164 minecraft:light_gray_concrete
fill 0 64 145 15 79 145 minecraft:light_gray_concrete
fill 0 64 145 0 79 158 minecraft:light_gray_concrete
setblock 1 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
fill 10 64 145 10 79 158 minecraft:light_gray_concrete
setblock 5 63 150 minecraft:grass_block
setblock 5 64 150 botania:pure_daisy
setblock 4 64 149 minecraft:stone
setblock 5 64 149 botania:livingrock
setblock 6 64 149 minecraft:stone
setblock 4 64 150 minecraft:oak_log[axis=y]
setblock 6 64 150 botania:livingwood_log[axis=y]
setblock 4 64 151 botania:livingrock
setblock 5 64 151 minecraft:stone
setblock 6 64 151 botania:livingrock
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
