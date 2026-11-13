# 090 nether/welcome
#area -4 271 14 296
fill -4 64 271 14 91 296 minecraft:air
fill -4 60 271 14 62 296 minecraft:stone
fill -4 63 271 14 63 296 minecraft:light_gray_concrete
fill 0 64 277 14 79 277 minecraft:light_gray_concrete
fill 0 64 277 0 79 290 minecraft:light_gray_concrete
setblock 1 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 277 9 79 290 minecraft:light_gray_concrete
setblock 3 65 282 minecraft:obsidian
setblock 3 66 282 minecraft:obsidian
setblock 3 67 282 minecraft:obsidian
setblock 4 64 282 minecraft:obsidian
setblock 4 68 282 minecraft:obsidian
setblock 5 64 282 minecraft:obsidian
setblock 5 68 282 minecraft:obsidian
setblock 6 65 282 minecraft:obsidian
setblock 6 66 282 minecraft:obsidian
setblock 6 67 282 minecraft:obsidian
fill 4 65 282 5 67 282 minecraft:nether_portal[axis=x]
execute if block 4 66 282 minecraft:nether_portal
