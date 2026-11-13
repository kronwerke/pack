# 079 nether/welcome
#area -4 250 14 275
fill -4 64 250 14 91 275 minecraft:air
fill -4 60 250 14 62 275 minecraft:stone
fill -4 63 250 14 63 275 minecraft:light_gray_concrete
fill 0 64 256 14 79 256 minecraft:light_gray_concrete
fill 0 64 256 0 79 269 minecraft:light_gray_concrete
setblock 1 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "079"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 256 9 79 269 minecraft:light_gray_concrete
setblock 3 65 261 minecraft:obsidian
setblock 3 66 261 minecraft:obsidian
setblock 3 67 261 minecraft:obsidian
setblock 4 64 261 minecraft:obsidian
setblock 4 68 261 minecraft:obsidian
setblock 5 64 261 minecraft:obsidian
setblock 5 68 261 minecraft:obsidian
setblock 6 65 261 minecraft:obsidian
setblock 6 66 261 minecraft:obsidian
setblock 6 67 261 minecraft:obsidian
fill 4 65 261 5 67 261 minecraft:nether_portal[axis=x]
execute if block 4 66 261 minecraft:nether_portal
