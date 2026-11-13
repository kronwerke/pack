# 082 botania/manastar
#area 41 139 60 164
fill 41 64 139 60 91 164 minecraft:air
fill 41 60 139 60 62 164 minecraft:stone
fill 41 63 139 60 63 164 minecraft:light_gray_concrete
fill 45 64 145 60 79 145 minecraft:light_gray_concrete
fill 45 64 145 45 79 158 minecraft:light_gray_concrete
setblock 46 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "botania"}','{"text": "manastar"}','{"text": ""}']}}
setblock 47 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a blue Manastar"}','{"text": "next to a pool"}','{"text": ""}','{"text": ""}']}}
fill 55 64 145 55 79 158 minecraft:light_gray_concrete
fill 48 63 148 52 63 152 minecraft:grass_block
setblock 50 64 150 botania:mana_pool{mana:400000}
setblock 51 64 150 botania:manastar
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
