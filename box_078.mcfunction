# 078 gaia/arena
#area 199 107 224 138
fill 199 64 107 224 91 138 minecraft:air
fill 199 60 107 224 62 138 minecraft:stone
fill 199 63 107 224 63 138 minecraft:light_gray_concrete
fill 203 64 113 224 79 113 minecraft:light_gray_concrete
fill 203 64 113 203 79 132 minecraft:light_gray_concrete
setblock 204 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 205 64 131 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 219 64 113 219 79 132 minecraft:light_gray_concrete
fill 210 63 120 212 63 122 minecraft:iron_block
setblock 211 64 121 minecraft:beacon
setblock 207 64 117 minecraft:quartz_block
setblock 207 65 117 botania:gaia_pylon
setblock 207 64 125 minecraft:quartz_block
setblock 207 65 125 botania:gaia_pylon
setblock 215 64 117 minecraft:quartz_block
setblock 215 65 117 botania:gaia_pylon
setblock 215 64 125 minecraft:quartz_block
setblock 215 65 125 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
