# 054 gaia/arena
#area 169 105 194 136
fill 169 64 105 194 91 136 minecraft:air
fill 169 60 105 194 62 136 minecraft:stone
fill 169 63 105 194 63 136 minecraft:light_gray_concrete
fill 173 64 111 194 79 111 minecraft:light_gray_concrete
fill 173 64 111 173 79 130 minecraft:light_gray_concrete
setblock 174 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 175 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 189 64 111 189 79 130 minecraft:light_gray_concrete
fill 180 63 118 182 63 120 minecraft:iron_block
setblock 181 64 119 minecraft:beacon
setblock 177 64 115 minecraft:quartz_block
setblock 177 65 115 botania:gaia_pylon
setblock 177 64 123 minecraft:quartz_block
setblock 177 65 123 botania:gaia_pylon
setblock 185 64 115 minecraft:quartz_block
setblock 185 65 115 botania:gaia_pylon
setblock 185 64 123 minecraft:quartz_block
setblock 185 65 123 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
