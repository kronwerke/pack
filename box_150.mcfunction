# 150 the_end/arrival, crystals, egg, elytra, cg_kill
#area 46 336 107 365
fill 46 64 336 79 95 365 minecraft:air
fill 80 64 336 107 95 365 minecraft:air
fill 46 60 336 107 62 365 minecraft:stone
fill 46 63 336 107 63 365 minecraft:light_gray_concrete
fill 50 64 342 107 83 342 minecraft:light_gray_concrete
fill 50 64 342 50 83 359 minecraft:light_gray_concrete
setblock 51 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.1"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 52 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 60 64 342 60 83 359 minecraft:light_gray_concrete
setblock 54 64 345 minecraft:end_portal_frame[eye=true,facing=south]
setblock 54 64 349 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 346 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 346 minecraft:end_portal_frame[eye=true,facing=west]
setblock 55 64 345 minecraft:end_portal_frame[eye=true,facing=south]
setblock 55 64 349 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 347 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 347 minecraft:end_portal_frame[eye=true,facing=west]
setblock 56 64 345 minecraft:end_portal_frame[eye=true,facing=south]
setblock 56 64 349 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 348 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 348 minecraft:end_portal_frame[eye=true,facing=west]
fill 54 64 346 56 64 348 minecraft:end_portal
setblock 61 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.2"}','{"text": "the_end"}','{"text": "crystals"}','{"text": ""}']}}
setblock 62 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zerstör die"}','{"text": "Endkristalle"}','{"text": ""}','{"text": ""}']}}
fill 70 64 342 70 83 359 minecraft:light_gray_concrete
fill 64 64 345 66 69 347 minecraft:obsidian
setblock 65 70 346 minecraft:bedrock
summon minecraft:end_crystal 65.5 71 346.5 {Tags:["kw_shot"],ShowBottom:0b}
setblock 71 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.3"}','{"text": "the_end"}','{"text": "egg"}','{"text": ""}']}}
setblock 72 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol das"}','{"text": "Drachenei"}','{"text": ""}','{"text": ""}']}}
fill 80 64 342 80 83 359 minecraft:light_gray_concrete
fill 74 64 346 76 64 348 minecraft:bedrock
fill 75 65 347 75 67 347 minecraft:bedrock
setblock 75 68 347 minecraft:dragon_egg
setblock 81 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.4"}','{"text": "the_end"}','{"text": "elytra"}','{"text": ""}']}}
setblock 82 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol dir Elytren"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 90 64 342 90 83 359 minecraft:light_gray_concrete
summon armor_stand 85.5 64 347.5 {ArmorItems:[{},{},{id:"minecraft:elytra",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 91 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.5"}','{"text": "the_end"}','{"text": "cg_kill"}','{"text": ""}']}}
setblock 92 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Ender Guardian"}','{"text": ""}','{"text": ""}']}}
fill 102 64 342 102 83 359 minecraft:light_gray_concrete
summon cataclysm:ender_guardian 96.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
