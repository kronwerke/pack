# 145 nether/welcome
#area -4 330 14 355
fill -4 64 330 14 91 355 minecraft:air
fill -4 60 330 14 62 355 minecraft:stone
fill -4 63 330 14 63 355 minecraft:light_gray_concrete
fill 0 64 336 14 79 336 minecraft:light_gray_concrete
fill 0 64 336 0 79 349 minecraft:light_gray_concrete
setblock 1 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 336 9 79 349 minecraft:light_gray_concrete
setblock 3 65 341 minecraft:obsidian
setblock 3 66 341 minecraft:obsidian
setblock 3 67 341 minecraft:obsidian
setblock 4 64 341 minecraft:obsidian
setblock 4 68 341 minecraft:obsidian
setblock 5 64 341 minecraft:obsidian
setblock 5 68 341 minecraft:obsidian
setblock 6 65 341 minecraft:obsidian
setblock 6 66 341 minecraft:obsidian
setblock 6 67 341 minecraft:obsidian
fill 4 65 341 5 67 341 minecraft:nether_portal[axis=x]
execute if block 4 66 341 minecraft:nether_portal
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
