# 155 the_end/arrival, crystals, egg, elytra, cg_kill
#area 46 340 107 369
fill 46 64 340 79 95 369 minecraft:air
fill 80 64 340 107 95 369 minecraft:air
fill 46 60 340 107 62 369 minecraft:stone
fill 46 63 340 107 63 369 minecraft:light_gray_concrete
fill 50 64 346 107 83 346 minecraft:light_gray_concrete
fill 50 64 346 50 83 363 minecraft:light_gray_concrete
setblock 51 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.1"}','{"text": "the_end"}','{"text": "arrival"}','{"text": ""}']}}
setblock 52 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betritt das End"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 60 64 346 60 83 363 minecraft:light_gray_concrete
setblock 54 64 349 minecraft:end_portal_frame[eye=true,facing=south]
setblock 54 64 353 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 350 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 350 minecraft:end_portal_frame[eye=true,facing=west]
setblock 55 64 349 minecraft:end_portal_frame[eye=true,facing=south]
setblock 55 64 353 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 351 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 351 minecraft:end_portal_frame[eye=true,facing=west]
setblock 56 64 349 minecraft:end_portal_frame[eye=true,facing=south]
setblock 56 64 353 minecraft:end_portal_frame[eye=true,facing=north]
setblock 53 64 352 minecraft:end_portal_frame[eye=true,facing=east]
setblock 57 64 352 minecraft:end_portal_frame[eye=true,facing=west]
fill 54 64 350 56 64 352 minecraft:end_portal
setblock 61 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.2"}','{"text": "the_end"}','{"text": "crystals"}','{"text": ""}']}}
setblock 62 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zerstör die"}','{"text": "Endkristalle"}','{"text": ""}','{"text": ""}']}}
fill 70 64 346 70 83 363 minecraft:light_gray_concrete
fill 64 64 349 66 69 351 minecraft:obsidian
setblock 65 70 350 minecraft:bedrock
summon minecraft:end_crystal 65.5 71 350.5 {Tags:["kw_shot"],ShowBottom:0b}
setblock 71 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.3"}','{"text": "the_end"}','{"text": "egg"}','{"text": ""}']}}
setblock 72 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol das"}','{"text": "Drachenei"}','{"text": ""}','{"text": ""}']}}
fill 80 64 346 80 83 363 minecraft:light_gray_concrete
fill 74 64 350 76 64 352 minecraft:bedrock
fill 75 65 351 75 67 351 minecraft:bedrock
setblock 75 68 351 minecraft:dragon_egg
setblock 81 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.4"}','{"text": "the_end"}','{"text": "elytra"}','{"text": ""}']}}
setblock 82 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol dir Elytren"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 90 64 346 90 83 363 minecraft:light_gray_concrete
summon armor_stand 85.5 64 351.5 {ArmorItems:[{},{},{id:"minecraft:elytra",count:1},{}],ShowArms:1b,NoBasePlate:1b,Tags:["kw_shot"],Rotation:[20f,0f]}
setblock 91 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.5"}','{"text": "the_end"}','{"text": "cg_kill"}','{"text": ""}']}}
setblock 92 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Ender Guardian"}','{"text": ""}','{"text": ""}']}}
fill 102 64 346 102 83 363 minecraft:light_gray_concrete
summon cataclysm:ender_guardian 96.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
