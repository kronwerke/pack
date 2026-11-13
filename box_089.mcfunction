# 089 gaia/arena
#area 199 139 224 170
fill 199 64 139 224 91 170 minecraft:air
fill 199 60 139 224 62 170 minecraft:stone
fill 199 63 139 224 63 170 minecraft:light_gray_concrete
fill 203 64 145 224 79 145 minecraft:light_gray_concrete
fill 203 64 145 203 79 164 minecraft:light_gray_concrete
setblock 204 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 205 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 219 64 145 219 79 164 minecraft:light_gray_concrete
fill 210 63 152 212 63 154 minecraft:iron_block
setblock 211 64 153 minecraft:beacon
setblock 207 64 149 minecraft:quartz_block
setblock 207 65 149 botania:gaia_pylon
setblock 207 64 157 minecraft:quartz_block
setblock 207 65 157 botania:gaia_pylon
setblock 215 64 149 minecraft:quartz_block
setblock 215 65 149 botania:gaia_pylon
setblock 215 64 157 minecraft:quartz_block
setblock 215 65 157 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
