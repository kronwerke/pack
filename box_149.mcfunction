# 149 nether/welcome
#area -4 334 14 359
fill -4 64 334 14 91 359 minecraft:air
fill -4 60 334 14 62 359 minecraft:stone
fill -4 63 334 14 63 359 minecraft:light_gray_concrete
fill 0 64 340 14 79 340 minecraft:light_gray_concrete
fill 0 64 340 0 79 353 minecraft:light_gray_concrete
setblock 1 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 340 9 79 353 minecraft:light_gray_concrete
setblock 3 65 345 minecraft:obsidian
setblock 3 66 345 minecraft:obsidian
setblock 3 67 345 minecraft:obsidian
setblock 4 64 345 minecraft:obsidian
setblock 4 68 345 minecraft:obsidian
setblock 5 64 345 minecraft:obsidian
setblock 5 68 345 minecraft:obsidian
setblock 6 65 345 minecraft:obsidian
setblock 6 66 345 minecraft:obsidian
setblock 6 67 345 minecraft:obsidian
fill 4 65 345 5 67 345 minecraft:nether_portal[axis=x]
execute if block 4 66 345 minecraft:nether_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
