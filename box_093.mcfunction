# 093 gaia/arena
#area 214 145 239 176
fill 214 64 145 239 91 176 minecraft:air
fill 214 60 145 239 62 176 minecraft:stone
fill 214 63 145 239 63 176 minecraft:light_gray_concrete
fill 218 64 151 239 79 151 minecraft:light_gray_concrete
fill 218 64 151 218 79 170 minecraft:light_gray_concrete
setblock 219 64 169 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 220 64 169 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 234 64 151 234 79 170 minecraft:light_gray_concrete
fill 225 63 158 227 63 160 minecraft:iron_block
setblock 226 64 159 minecraft:beacon
setblock 222 64 155 minecraft:quartz_block
setblock 222 65 155 botania:gaia_pylon
setblock 222 64 163 minecraft:quartz_block
setblock 222 65 163 botania:gaia_pylon
setblock 230 64 155 minecraft:quartz_block
setblock 230 65 155 botania:gaia_pylon
setblock 230 64 163 minecraft:quartz_block
setblock 230 65 163 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
