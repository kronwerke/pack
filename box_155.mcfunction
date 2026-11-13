# 155 eternal_starlight/orb, starfire, golem, monstrosity
#area 290 336 345 363
fill 290 64 336 330 91 363 minecraft:air
fill 331 64 336 345 91 363 minecraft:air
fill 290 60 336 345 62 363 minecraft:stone
fill 290 63 336 345 63 363 minecraft:light_gray_concrete
fill 294 64 342 345 79 342 minecraft:light_gray_concrete
fill 294 64 342 294 79 357 minecraft:light_gray_concrete
setblock 295 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.1"}','{"text": "eternal_starlight"}','{"text": "orb"}','{"text": ""}']}}
setblock 296 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Gatekeeper"}','{"text": ""}','{"text": ""}']}}
fill 306 64 342 306 79 357 minecraft:light_gray_concrete
summon eternal_starlight:the_gatekeeper 300.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 307 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.2"}','{"text": "eternal_starlight"}','{"text": "starfire"}','{"text": ""}']}}
setblock 308 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol Starfire"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 316 64 342 316 79 357 minecraft:light_gray_concrete
setblock 311 64 347 minecraft:smooth_stone_slab
summon item_display 311.5 65.4 347.5 {item:{id:"eternal_starlight:starfire",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 317 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.3"}','{"text": "eternal_starlight"}','{"text": "golem"}','{"text": ""}']}}
setblock 318 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Starlight Golem"}','{"text": ""}','{"text": ""}']}}
fill 328 64 342 328 79 357 minecraft:light_gray_concrete
summon eternal_starlight:starlight_golem 322.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 329 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.4"}','{"text": "eternal_starlight"}','{"text": "monstrosity"}','{"text": ""}']}}
setblock 330 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Lunar"}','{"text": "Monstrosity"}','{"text": ""}']}}
fill 340 64 342 340 79 357 minecraft:light_gray_concrete
summon eternal_starlight:lunar_monstrosity 334.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
