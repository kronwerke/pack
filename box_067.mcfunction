# 067 botania/pure_daisy
#area -4 109 15 134
fill -4 64 109 15 91 134 minecraft:air
fill -4 60 109 15 62 134 minecraft:stone
fill -4 63 109 15 63 134 minecraft:light_gray_concrete
fill 0 64 115 15 79 115 minecraft:light_gray_concrete
fill 0 64 115 0 79 128 minecraft:light_gray_concrete
setblock 1 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
fill 10 64 115 10 79 128 minecraft:light_gray_concrete
setblock 5 63 120 minecraft:grass_block
setblock 5 64 120 botania:pure_daisy
setblock 4 64 119 minecraft:stone
setblock 5 64 119 botania:livingrock
setblock 6 64 119 minecraft:stone
setblock 4 64 120 minecraft:oak_log[axis=y]
setblock 6 64 120 botania:livingwood_log[axis=y]
setblock 4 64 121 botania:livingrock
setblock 5 64 121 minecraft:stone
setblock 6 64 121 botania:livingrock
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
