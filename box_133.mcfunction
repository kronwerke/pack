# 133 nether/welcome
#area -4 298 14 323
fill -4 64 298 14 91 323 minecraft:air
fill -4 60 298 14 62 323 minecraft:stone
fill -4 63 298 14 63 323 minecraft:light_gray_concrete
fill 0 64 304 14 79 304 minecraft:light_gray_concrete
fill 0 64 304 0 79 317 minecraft:light_gray_concrete
setblock 1 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 304 9 79 317 minecraft:light_gray_concrete
setblock 3 65 309 minecraft:obsidian
setblock 3 66 309 minecraft:obsidian
setblock 3 67 309 minecraft:obsidian
setblock 4 64 309 minecraft:obsidian
setblock 4 68 309 minecraft:obsidian
setblock 5 64 309 minecraft:obsidian
setblock 5 68 309 minecraft:obsidian
setblock 6 65 309 minecraft:obsidian
setblock 6 66 309 minecraft:obsidian
setblock 6 67 309 minecraft:obsidian
fill 4 65 309 5 67 309 minecraft:nether_portal[axis=x]
execute if block 4 66 309 minecraft:nether_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
