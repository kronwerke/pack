# 175 eternal_starlight/orb, portal, starfire, golem, monstrosity
#area 340 342 411 369
fill 340 64 342 380 91 369 minecraft:air
fill 381 64 342 411 91 369 minecraft:air
fill 340 60 342 411 62 369 minecraft:stone
fill 340 63 342 411 63 369 minecraft:light_gray_concrete
fill 344 64 348 411 79 348 minecraft:light_gray_concrete
fill 344 64 348 344 79 363 minecraft:light_gray_concrete
setblock 345 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.1"}','{"text": "eternal_starlight"}','{"text": "orb"}','{"text": ""}']}}
setblock 346 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Gatekeeper"}','{"text": ""}','{"text": ""}']}}
fill 356 64 348 356 79 363 minecraft:light_gray_concrete
summon eternal_starlight:the_gatekeeper 350.5 64 354.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 357 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.2"}','{"text": "eternal_starlight"}','{"text": "portal"}','{"text": ""}']}}
setblock 358 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne das"}','{"text": "Portal"}','{"text": ""}','{"text": ""}']}}
fill 372 64 348 372 79 363 minecraft:light_gray_concrete
kw testworld place shots:eternalstarlight/portal_ruins/common 358 63 350 none
setblock 368 65 353 minecraft:air
kw testworld use 361 65 353 south eternal_starlight:orb_of_prophecy
execute if block 361 67 353 eternal_starlight:starlight_portal
setblock 373 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.3"}','{"text": "eternal_starlight"}','{"text": "starfire"}','{"text": ""}']}}
setblock 374 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol Starfire"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 382 64 348 382 79 363 minecraft:light_gray_concrete
setblock 377 64 353 minecraft:smooth_stone_slab
summon item_display 377.5 65.4 353.5 {item:{id:"eternal_starlight:starfire",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 383 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.4"}','{"text": "eternal_starlight"}','{"text": "golem"}','{"text": ""}']}}
setblock 384 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Starlight Golem"}','{"text": ""}','{"text": ""}']}}
fill 394 64 348 394 79 363 minecraft:light_gray_concrete
summon eternal_starlight:starlight_golem 388.5 64 354.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 395 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "175.5"}','{"text": "eternal_starlight"}','{"text": "monstrosity"}','{"text": ""}']}}
setblock 396 64 362 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Lunar"}','{"text": "Monstrosity"}','{"text": ""}']}}
fill 406 64 348 406 79 363 minecraft:light_gray_concrete
summon eternal_starlight:lunar_monstrosity 400.5 64 354.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
