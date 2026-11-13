# 160 eternal_starlight/orb, portal, starfire, golem, monstrosity
#area 340 340 411 367
fill 340 64 340 380 91 367 minecraft:air
fill 381 64 340 411 91 367 minecraft:air
fill 340 60 340 411 62 367 minecraft:stone
fill 340 63 340 411 63 367 minecraft:light_gray_concrete
fill 344 64 346 411 79 346 minecraft:light_gray_concrete
fill 344 64 346 344 79 361 minecraft:light_gray_concrete
setblock 345 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.1"}','{"text": "eternal_starlight"}','{"text": "orb"}','{"text": ""}']}}
setblock 346 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Gatekeeper"}','{"text": ""}','{"text": ""}']}}
fill 356 64 346 356 79 361 minecraft:light_gray_concrete
summon eternal_starlight:the_gatekeeper 350.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 357 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.2"}','{"text": "eternal_starlight"}','{"text": "portal"}','{"text": ""}']}}
setblock 358 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne das"}','{"text": "Portal"}','{"text": ""}','{"text": ""}']}}
fill 372 64 346 372 79 361 minecraft:light_gray_concrete
kw testworld place shots:eternalstarlight/portal_ruins/common 358 63 348 none
setblock 368 65 351 minecraft:air
kw testworld use 361 65 351 south eternal_starlight:orb_of_prophecy
execute if block 361 67 351 eternal_starlight:starlight_portal
setblock 373 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.3"}','{"text": "eternal_starlight"}','{"text": "starfire"}','{"text": ""}']}}
setblock 374 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol Starfire"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 382 64 346 382 79 361 minecraft:light_gray_concrete
setblock 377 64 351 minecraft:smooth_stone_slab
summon item_display 377.5 65.4 351.5 {item:{id:"eternal_starlight:starfire",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 383 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.4"}','{"text": "eternal_starlight"}','{"text": "golem"}','{"text": ""}']}}
setblock 384 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Starlight Golem"}','{"text": ""}','{"text": ""}']}}
fill 394 64 346 394 79 361 minecraft:light_gray_concrete
summon eternal_starlight:starlight_golem 388.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 395 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.5"}','{"text": "eternal_starlight"}','{"text": "monstrosity"}','{"text": ""}']}}
setblock 396 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Lunar"}','{"text": "Monstrosity"}','{"text": ""}']}}
fill 406 64 346 406 79 361 minecraft:light_gray_concrete
summon eternal_starlight:lunar_monstrosity 400.5 64 352.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
