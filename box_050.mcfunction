# 050 nether/welcome
#area -4 198 14 223
fill -4 64 198 14 91 223 minecraft:air
fill -4 60 198 14 62 223 minecraft:stone
fill -4 63 198 14 63 223 minecraft:light_gray_concrete
fill 0 64 204 14 79 204 minecraft:light_gray_concrete
fill 0 64 204 0 79 217 minecraft:light_gray_concrete
setblock 1 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 204 9 79 217 minecraft:light_gray_concrete
setblock 3 65 209 minecraft:obsidian
setblock 3 66 209 minecraft:obsidian
setblock 3 67 209 minecraft:obsidian
setblock 4 64 209 minecraft:obsidian
setblock 4 68 209 minecraft:obsidian
setblock 5 64 209 minecraft:obsidian
setblock 5 68 209 minecraft:obsidian
setblock 6 65 209 minecraft:obsidian
setblock 6 66 209 minecraft:obsidian
setblock 6 67 209 minecraft:obsidian
fill 4 65 209 5 67 209 minecraft:nether_portal[axis=x]
execute if block 4 66 209 minecraft:nether_portal
