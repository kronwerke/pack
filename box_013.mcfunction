# 013 farms/s2_xp
#area 124 21 141 44
fill 124 64 21 141 91 44 minecraft:air
fill 124 60 21 141 62 44 minecraft:stone
fill 124 63 21 141 63 44 minecraft:light_gray_concrete
fill 128 64 27 141 79 27 minecraft:light_gray_concrete
fill 128 64 27 128 79 38 minecraft:light_gray_concrete
setblock 129 64 37 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "013"}','{"text": "farms"}','{"text": "s2_xp"}','{"text": ""}']}}
setblock 130 64 37 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "grindstone"}','{"text": "drain stack"}','{"text": "with experience"}','{"text": "hatch on a tank"}']}}
fill 136 64 27 136 79 38 minecraft:light_gray_concrete
kw testworld place shots:create/grindstone/basic 130 63 29 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
