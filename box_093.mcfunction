# 093 nether/welcome
#area -4 277 14 302
fill -4 64 277 14 91 302 minecraft:air
fill -4 60 277 14 62 302 minecraft:stone
fill -4 63 277 14 63 302 minecraft:light_gray_concrete
fill 0 64 283 14 79 283 minecraft:light_gray_concrete
fill 0 64 283 0 79 296 minecraft:light_gray_concrete
setblock 1 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 283 9 79 296 minecraft:light_gray_concrete
setblock 3 65 288 minecraft:obsidian
setblock 3 66 288 minecraft:obsidian
setblock 3 67 288 minecraft:obsidian
setblock 4 64 288 minecraft:obsidian
setblock 4 68 288 minecraft:obsidian
setblock 5 64 288 minecraft:obsidian
setblock 5 68 288 minecraft:obsidian
setblock 6 65 288 minecraft:obsidian
setblock 6 66 288 minecraft:obsidian
setblock 6 67 288 minecraft:obsidian
fill 4 65 288 5 67 288 minecraft:nether_portal[axis=x]
execute if block 4 66 288 minecraft:nether_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
