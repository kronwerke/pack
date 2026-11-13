# 082 gaia/arena
#area 199 109 224 140
fill 199 64 109 224 91 140 minecraft:air
fill 199 60 109 224 62 140 minecraft:stone
fill 199 63 109 224 63 140 minecraft:light_gray_concrete
fill 203 64 115 224 79 115 minecraft:light_gray_concrete
fill 203 64 115 203 79 134 minecraft:light_gray_concrete
setblock 204 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 205 64 133 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": ""}']}}
fill 219 64 115 219 79 134 minecraft:light_gray_concrete
fill 210 63 122 212 63 124 minecraft:iron_block
setblock 211 64 123 minecraft:beacon
setblock 207 64 119 minecraft:quartz_block
setblock 207 65 119 botania:gaia_pylon
setblock 207 64 127 minecraft:quartz_block
setblock 207 65 127 botania:gaia_pylon
setblock 215 64 119 minecraft:quartz_block
setblock 215 65 119 botania:gaia_pylon
setblock 215 64 127 minecraft:quartz_block
setblock 215 65 127 botania:gaia_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
