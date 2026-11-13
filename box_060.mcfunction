# 060 gaia/arena
#area 199 105 224 136
fill 199 64 105 224 91 136 minecraft:air
fill 199 60 105 224 62 136 minecraft:stone
fill 199 63 105 224 63 136 minecraft:light_gray_concrete
fill 203 64 111 224 79 111 minecraft:light_gray_concrete
fill 203 64 111 203 79 130 minecraft:light_gray_concrete
setblock 204 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "060"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 205 64 129 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 219 64 111 219 79 130 minecraft:light_gray_concrete
fill 210 63 118 212 63 120 minecraft:iron_block
setblock 211 64 119 minecraft:beacon
setblock 207 64 115 minecraft:quartz_block
setblock 207 65 115 botania:gaia_pylon
setblock 207 64 123 minecraft:quartz_block
setblock 207 65 123 botania:gaia_pylon
setblock 215 64 115 minecraft:quartz_block
setblock 215 65 115 botania:gaia_pylon
setblock 215 64 123 minecraft:quartz_block
setblock 215 65 123 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
