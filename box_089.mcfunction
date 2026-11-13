# 089 botania/pure_daisy
#area -4 147 15 172
fill -4 64 147 15 91 172 minecraft:air
fill -4 60 147 15 62 172 minecraft:stone
fill -4 63 147 15 63 172 minecraft:light_gray_concrete
fill 0 64 153 15 79 153 minecraft:light_gray_concrete
fill 0 64 153 0 79 166 minecraft:light_gray_concrete
setblock 1 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
fill 10 64 153 10 79 166 minecraft:light_gray_concrete
setblock 5 63 158 minecraft:grass_block
setblock 5 64 158 botania:pure_daisy
setblock 4 64 157 minecraft:stone
setblock 5 64 157 botania:livingrock
setblock 6 64 157 minecraft:stone
setblock 4 64 158 minecraft:oak_log[axis=y]
setblock 6 64 158 botania:livingwood_log[axis=y]
setblock 4 64 159 botania:livingrock
setblock 5 64 159 minecraft:stone
setblock 6 64 159 botania:livingrock
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
