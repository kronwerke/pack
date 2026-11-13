# 170 the_end/arrival, crystals, egg, elytra, cg_kill
#area 46 342 107 371
fill 46 64 342 79 95 371 minecraft:air
fill 80 64 342 107 95 371 minecraft:air
fill 46 60 342 107 62 371 minecraft:stone
fill 46 63 342 107 63 371 minecraft:light_gray_concrete
fill 50 64 348 107 83 348 minecraft:light_gray_concrete
fill 50 64 348 50 83 365 minecraft:light_gray_concrete
setblock 51 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "170.1"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 52 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 60 64 348 60 83 365 minecraft:light_gray_concrete
setblock 54 64 351 minecraft:end_portal_frame[eye=true,facing=south]
setblock 54 64 355 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 352 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 352 minecraft:end_portal_frame[eye=true,facing=west]
setblock 55 64 351 minecraft:end_portal_frame[eye=true,facing=south]
setblock 55 64 355 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 353 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 353 minecraft:end_portal_frame[eye=true,facing=west]
setblock 56 64 351 minecraft:end_portal_frame[eye=true,facing=south]
setblock 56 64 355 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 354 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 354 minecraft:end_portal_frame[eye=true,facing=west]
fill 54 64 352 56 64 354 minecraft:end_portal
setblock 61 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "170.2"}','{"text": "the_end"}','{"text": "crystals"}','{"text": ""}']}}
setblock 62 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zerstör die"}','{"text": "Endkristalle"}','{"text": ""}','{"text": ""}']}}
fill 70 64 348 70 83 365 minecraft:light_gray_concrete
fill 64 64 351 66 69 353 minecraft:obsidian
setblock 65 70 352 minecraft:bedrock
summon minecraft:end_crystal 65.5 71 352.5 {Tags:["kw_shot"],ShowBottom:0b}
setblock 71 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "170.3"}','{"text": "the_end"}','{"text": "egg"}','{"text": ""}']}}
setblock 72 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol das"}','{"text": "Drachenei"}','{"text": ""}','{"text": ""}']}}
fill 80 64 348 80 83 365 minecraft:light_gray_concrete
fill 74 64 352 76 64 354 minecraft:bedrock
fill 75 65 353 75 67 353 minecraft:bedrock
setblock 75 68 353 minecraft:dragon_egg
setblock 81 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "170.4"}','{"text": "the_end"}','{"text": "elytra"}','{"text": ""}']}}
setblock 82 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol dir Elytren"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 90 64 348 90 83 365 minecraft:light_gray_concrete
summon armor_stand 85.5 64 353.5 {ArmorItems:[{},{},{id:"minecraft:elytra",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 91 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "170.5"}','{"text": "the_end"}','{"text": "cg_kill"}','{"text": ""}']}}
setblock 92 64 364 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Ender Guardian"}','{"text": ""}','{"text": ""}']}}
fill 102 64 348 102 83 365 minecraft:light_gray_concrete
summon cataclysm:ender_guardian 96.5 64 354.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
