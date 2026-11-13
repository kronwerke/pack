# 149 nether/welcome, ig_kill, nm_kill, debris
#area -4 336 50 367
fill -4 64 336 27 95 367 minecraft:air
fill 28 64 336 50 95 367 minecraft:air
fill -4 60 336 50 62 367 minecraft:stone
fill -4 63 336 50 63 367 minecraft:light_gray_concrete
fill 0 64 342 50 83 342 minecraft:light_gray_concrete
fill 0 64 342 0 83 361 minecraft:light_gray_concrete
setblock 1 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.1"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 342 9 83 361 minecraft:light_gray_concrete
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
setblock 10 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.2"}','{"text": "nether"}','{"text": "ig_kill"}','{"text": ""}']}}
setblock 11 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege Ignis"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 342 21 83 361 minecraft:light_gray_concrete
summon cataclysm:ignis 15.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 22 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.3"}','{"text": "nether"}','{"text": "nm_kill"}','{"text": ""}']}}
setblock 23 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Netherite"}','{"text": "Monstrosity"}','{"text": ""}']}}
fill 35 64 342 35 83 361 minecraft:light_gray_concrete
summon cataclysm:netherite_monstrosity 28.5 64 347.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 36 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149.4"}','{"text": "nether"}','{"text": "debris"}','{"text": ""}']}}
setblock 37 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Grab Antiken"}','{"text": "Schrott"}','{"text": ""}','{"text": ""}']}}
fill 45 64 342 45 83 361 minecraft:light_gray_concrete
fill 39 64 346 41 65 347 minecraft:netherrack
setblock 40 64 347 minecraft:ancient_debris
setblock 41 65 347 minecraft:ancient_debris
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
