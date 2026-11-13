# 093 gaia/arena
#area 214 143 239 174
fill 214 64 143 239 91 174 minecraft:air
fill 214 60 143 239 62 174 minecraft:stone
fill 214 63 143 239 63 174 minecraft:light_gray_concrete
fill 218 64 149 239 79 149 minecraft:light_gray_concrete
fill 218 64 149 218 79 168 minecraft:light_gray_concrete
setblock 219 64 167 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 220 64 167 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 234 64 149 234 79 168 minecraft:light_gray_concrete
fill 225 63 156 227 63 158 minecraft:iron_block
setblock 226 64 157 minecraft:beacon
setblock 222 64 153 minecraft:quartz_block
setblock 222 65 153 botania:gaia_pylon
setblock 222 64 161 minecraft:quartz_block
setblock 222 65 161 botania:gaia_pylon
setblock 230 64 153 minecraft:quartz_block
setblock 230 65 153 botania:gaia_pylon
setblock 230 64 161 minecraft:quartz_block
setblock 230 65 161 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
