# 088 nether/welcome
#area -4 269 14 294
fill -4 64 269 14 91 294 minecraft:air
fill -4 60 269 14 62 294 minecraft:stone
fill -4 63 269 14 63 294 minecraft:light_gray_concrete
fill 0 64 275 14 79 275 minecraft:light_gray_concrete
fill 0 64 275 0 79 288 minecraft:light_gray_concrete
setblock 1 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 275 9 79 288 minecraft:light_gray_concrete
setblock 3 65 280 minecraft:obsidian
setblock 3 66 280 minecraft:obsidian
setblock 3 67 280 minecraft:obsidian
setblock 4 64 280 minecraft:obsidian
setblock 4 68 280 minecraft:obsidian
setblock 5 64 280 minecraft:obsidian
setblock 5 68 280 minecraft:obsidian
setblock 6 65 280 minecraft:obsidian
setblock 6 66 280 minecraft:obsidian
setblock 6 67 280 minecraft:obsidian
fill 4 65 280 5 67 280 minecraft:nether_portal[axis=x]
execute if block 4 66 280 minecraft:nether_portal
