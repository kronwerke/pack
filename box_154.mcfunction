# 154 nether/welcome, ig_kill, nm_kill, debris
#area -4 340 50 371
fill -4 64 340 27 95 371 minecraft:air
fill 28 64 340 50 95 371 minecraft:air
fill -4 60 340 50 62 371 minecraft:stone
fill -4 63 340 50 63 371 minecraft:light_gray_concrete
fill 0 64 346 50 83 346 minecraft:light_gray_concrete
fill 0 64 346 0 83 365 minecraft:light_gray_concrete
setblock 1 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.1"}','{"text": "nether"}','{"text": "welcome"}','{"text": ""}']}}
setblock 2 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt den"}','{"text": "Nether"}','{"text": ""}','{"text": ""}']}}
fill 9 64 346 9 83 365 minecraft:light_gray_concrete
setblock 3 65 351 minecraft:obsidian
setblock 3 66 351 minecraft:obsidian
setblock 3 67 351 minecraft:obsidian
setblock 4 64 351 minecraft:obsidian
setblock 4 68 351 minecraft:obsidian
setblock 5 64 351 minecraft:obsidian
setblock 5 68 351 minecraft:obsidian
setblock 6 65 351 minecraft:obsidian
setblock 6 66 351 minecraft:obsidian
setblock 6 67 351 minecraft:obsidian
fill 4 65 351 5 67 351 minecraft:nether_portal[axis=x]
execute if block 4 66 351 minecraft:nether_portal
setblock 10 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.2"}','{"text": "nether"}','{"text": "ig_kill"}','{"text": ""}']}}
setblock 11 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege Ignis"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 21 64 346 21 83 365 minecraft:light_gray_concrete
summon cataclysm:ignis 15.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 22 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.3"}','{"text": "nether"}','{"text": "nm_kill"}','{"text": ""}']}}
setblock 23 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Netherite"}','{"text": "Monstrosity"}','{"text": ""}']}}
fill 35 64 346 35 83 365 minecraft:light_gray_concrete
summon cataclysm:netherite_monstrosity 28.5 64 351.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 36 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.4"}','{"text": "nether"}','{"text": "debris"}','{"text": ""}']}}
setblock 37 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Grab Antiken"}','{"text": "Schrott"}','{"text": ""}','{"text": ""}']}}
fill 45 64 346 45 83 365 minecraft:light_gray_concrete
fill 39 64 350 41 65 351 minecraft:netherrack
setblock 40 64 351 minecraft:ancient_debris
setblock 41 65 351 minecraft:ancient_debris
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
