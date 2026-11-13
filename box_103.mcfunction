# 103 nether/welcome
#area -4 296 14 321
fill -4 64 296 14 91 321 minecraft:air
fill -4 60 296 14 62 321 minecraft:stone
fill -4 63 296 14 63 321 minecraft:light_gray_concrete
fill 0 64 302 14 79 302 minecraft:light_gray_concrete
fill 0 64 302 0 79 315 minecraft:light_gray_concrete
setblock 1 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 302 9 79 315 minecraft:light_gray_concrete
setblock 3 65 307 minecraft:obsidian
setblock 3 66 307 minecraft:obsidian
setblock 3 67 307 minecraft:obsidian
setblock 4 64 307 minecraft:obsidian
setblock 4 68 307 minecraft:obsidian
setblock 5 64 307 minecraft:obsidian
setblock 5 68 307 minecraft:obsidian
setblock 6 65 307 minecraft:obsidian
setblock 6 66 307 minecraft:obsidian
setblock 6 67 307 minecraft:obsidian
fill 4 65 307 5 67 307 minecraft:nether_portal[axis=x]
execute if block 4 66 307 minecraft:nether_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
