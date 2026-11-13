# 064 botania/pure_daisy
#area -4 107 15 132
fill -4 64 107 15 91 132 minecraft:air
fill -4 60 107 15 62 132 minecraft:stone
fill -4 63 107 15 63 132 minecraft:light_gray_concrete
fill 0 64 113 15 79 113 minecraft:light_gray_concrete
fill 0 64 113 0 79 126 minecraft:light_gray_concrete
setblock 1 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "botania"}','{"text": "pure_daisy"}','{"text": ""}']}}
setblock 2 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the daisy with"}','{"text": "8 stone or"}','{"text": "logs, half"}','{"text": "converted"}']}}
fill 10 64 113 10 79 126 minecraft:light_gray_concrete
setblock 5 63 118 minecraft:grass_block
setblock 5 64 118 botania:pure_daisy
setblock 4 64 117 minecraft:stone
setblock 5 64 117 botania:livingrock
setblock 6 64 117 minecraft:stone
setblock 4 64 118 minecraft:oak_log[axis=y]
setblock 6 64 118 botania:livingwood_log[axis=y]
setblock 4 64 119 botania:livingrock
setblock 5 64 119 minecraft:stone
setblock 6 64 119 botania:livingrock
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
