# 155 eternal_starlight/orb, starfire, golem, monstrosity
#area 202 336 257 363
fill 202 64 336 242 91 363 minecraft:air
fill 243 64 336 257 91 363 minecraft:air
fill 202 60 336 257 62 363 minecraft:stone
fill 202 63 336 257 63 363 minecraft:light_gray_concrete
fill 206 64 342 257 79 342 minecraft:light_gray_concrete
fill 206 64 342 206 79 357 minecraft:light_gray_concrete
setblock 207 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.1"}','{"text": "eternal_starlight"}','{"text": "orb"}','{"text": ""}']}}
setblock 208 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Gatekeeper"}','{"text": ""}','{"text": ""}']}}
fill 218 64 342 218 79 357 minecraft:light_gray_concrete
summon eternal_starlight:the_gatekeeper 212.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 219 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.2"}','{"text": "eternal_starlight"}','{"text": "starfire"}','{"text": ""}']}}
setblock 220 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Hol Starfire"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 228 64 342 228 79 357 minecraft:light_gray_concrete
setblock 223 64 347 minecraft:smooth_stone_slab
summon item_display 223.5 65.4 347.5 {item:{id:"eternal_starlight:starfire",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 229 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.3"}','{"text": "eternal_starlight"}','{"text": "golem"}','{"text": ""}']}}
setblock 230 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Starlight Golem"}','{"text": ""}','{"text": ""}']}}
fill 240 64 342 240 79 357 minecraft:light_gray_concrete
summon eternal_starlight:starlight_golem 234.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 241 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.4"}','{"text": "eternal_starlight"}','{"text": "monstrosity"}','{"text": ""}']}}
setblock 242 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Lunar"}','{"text": "Monstrosity"}','{"text": ""}']}}
fill 252 64 342 252 79 357 minecraft:light_gray_concrete
summon eternal_starlight:lunar_monstrosity 246.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
