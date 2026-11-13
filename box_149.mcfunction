# 149 nether/welcome
#area -4 336 14 361
fill -4 64 336 14 91 361 minecraft:air
fill -4 60 336 14 62 361 minecraft:stone
fill -4 63 336 14 63 361 minecraft:light_gray_concrete
fill 0 64 342 14 79 342 minecraft:light_gray_concrete
fill 0 64 342 0 79 355 minecraft:light_gray_concrete
setblock 1 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 342 9 79 355 minecraft:light_gray_concrete
setblock 3 65 347 minecraft:obsidian
setblock 3 66 347 minecraft:obsidian
setblock 3 67 347 minecraft:obsidian
setblock 4 64 347 minecraft:obsidian
setblock 4 68 347 minecraft:obsidian
setblock 5 64 347 minecraft:obsidian
setblock 5 68 347 minecraft:obsidian
setblock 6 65 347 minecraft:obsidian
setblock 6 66 347 minecraft:obsidian
setblock 6 67 347 minecraft:obsidian
fill 4 65 347 5 67 347 minecraft:nether_portal[axis=x]
execute if block 4 66 347 minecraft:nether_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
