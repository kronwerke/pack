# 115 nether/welcome
#area -4 300 14 325
fill -4 64 300 14 91 325 minecraft:air
fill -4 60 300 14 62 325 minecraft:stone
fill -4 63 300 14 63 325 minecraft:light_gray_concrete
fill 0 64 306 14 79 306 minecraft:light_gray_concrete
fill 0 64 306 0 79 319 minecraft:light_gray_concrete
setblock 1 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "115"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 306 9 79 319 minecraft:light_gray_concrete
setblock 3 65 311 minecraft:obsidian
setblock 3 66 311 minecraft:obsidian
setblock 3 67 311 minecraft:obsidian
setblock 4 64 311 minecraft:obsidian
setblock 4 68 311 minecraft:obsidian
setblock 5 64 311 minecraft:obsidian
setblock 5 68 311 minecraft:obsidian
setblock 6 65 311 minecraft:obsidian
setblock 6 66 311 minecraft:obsidian
setblock 6 67 311 minecraft:obsidian
fill 4 65 311 5 67 311 minecraft:nether_portal[axis=x]
execute if block 4 66 311 minecraft:nether_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
