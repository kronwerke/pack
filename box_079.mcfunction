# 079 botania/pure_daisy
#area -4 143 15 168
fill -4 64 143 15 91 168 minecraft:air
fill -4 60 143 15 62 168 minecraft:stone
fill -4 63 143 15 63 168 minecraft:light_gray_concrete
fill 0 64 149 15 79 149 minecraft:light_gray_concrete
fill 0 64 149 0 79 162 minecraft:light_gray_concrete
setblock 1 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
fill 10 64 149 10 79 162 minecraft:light_gray_concrete
setblock 5 63 154 minecraft:grass_block
setblock 5 64 154 botania:pure_daisy
setblock 4 64 153 minecraft:stone
setblock 5 64 153 botania:livingrock
setblock 6 64 153 minecraft:stone
setblock 4 64 154 minecraft:oak_log[axis=y]
setblock 6 64 154 botania:livingwood_log[axis=y]
setblock 4 64 155 botania:livingrock
setblock 5 64 155 minecraft:stone
setblock 6 64 155 botania:livingrock
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
