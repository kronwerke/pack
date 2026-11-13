# 103 gaia/arena
#area 214 147 239 178
fill 214 64 147 239 91 178 minecraft:air
fill 214 60 147 239 62 178 minecraft:stone
fill 214 63 147 239 63 178 minecraft:light_gray_concrete
fill 218 64 153 239 79 153 minecraft:light_gray_concrete
fill 218 64 153 218 79 172 minecraft:light_gray_concrete
setblock 219 64 171 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 220 64 171 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 234 64 153 234 79 172 minecraft:light_gray_concrete
fill 225 63 160 227 63 162 minecraft:iron_block
setblock 226 64 161 minecraft:beacon
setblock 222 64 157 minecraft:quartz_block
setblock 222 65 157 botania:gaia_pylon
setblock 222 64 165 minecraft:quartz_block
setblock 222 65 165 botania:gaia_pylon
setblock 230 64 157 minecraft:quartz_block
setblock 230 65 157 botania:gaia_pylon
setblock 230 64 165 minecraft:quartz_block
setblock 230 65 165 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
