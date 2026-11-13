# 015 farms/s2_xp
#area 139 21 156 44
fill 139 64 21 156 91 44 minecraft:air
fill 139 60 21 156 62 44 minecraft:stone
fill 139 63 21 156 63 44 minecraft:light_gray_concrete
fill 143 64 27 156 79 27 minecraft:light_gray_concrete
fill 143 64 27 143 79 38 minecraft:light_gray_concrete
setblock 144 64 37 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "015"}','{"text": "farms"}','{"text": "s2_xp"}','{"text": ""}']}}
setblock 145 64 37 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "grindstone"}','{"text": "drain stack"}','{"text": "with experience"}','{"text": "hatch on a tank"}']}}
fill 151 64 27 151 79 38 minecraft:light_gray_concrete
kw testworld place shots:create/grindstone/basic 145 63 29 none
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
