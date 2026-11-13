# 152 aether/portal, altar, ride, gloves, slider, queen
#area 40 336 114 363
fill 40 64 336 80 91 363 minecraft:air
fill 81 64 336 114 91 363 minecraft:air
fill 40 60 336 114 62 363 minecraft:stone
fill 40 63 336 114 63 363 minecraft:light_gray_concrete
fill 44 64 342 114 79 342 minecraft:light_gray_concrete
fill 44 64 342 44 79 357 minecraft:light_gray_concrete
setblock 45 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 46 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 53 64 342 53 79 357 minecraft:light_gray_concrete
setblock 47 65 347 minecraft:glowstone
setblock 47 66 347 minecraft:glowstone
setblock 47 67 347 minecraft:glowstone
setblock 48 64 347 minecraft:glowstone
setblock 48 68 347 minecraft:glowstone
setblock 49 64 347 minecraft:glowstone
setblock 49 68 347 minecraft:glowstone
setblock 50 65 347 minecraft:glowstone
setblock 50 66 347 minecraft:glowstone
setblock 50 67 347 minecraft:glowstone
fill 48 65 347 49 67 347 aether:aether_portal[axis=x]
execute if block 48 66 347 aether:aether_portal
setblock 54 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 55 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 63 64 342 63 79 357 minecraft:light_gray_concrete
fill 56 63 346 60 63 348 aether:holystone
setblock 56 64 347 aether:altar
setblock 58 64 347 aether:freezer
setblock 60 64 347 aether:incubator
setblock 64 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.3"}','{"text": "aether"}','{"text": "ride"}','{"text": ""}']}}
setblock 65 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reite ein Moa"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 75 64 342 75 79 357 minecraft:light_gray_concrete
summon aether:moa 69.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 76 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.4"}','{"text": "aether"}','{"text": "gloves"}','{"text": ""}']}}
setblock 77 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Trag Handschuhe"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 85 64 342 85 79 357 minecraft:light_gray_concrete
setblock 80 64 347 minecraft:smooth_stone_slab
summon item_display 80.5 65.4 347.5 {item:{id:"aether:zanite_gloves",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 86 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.5"}','{"text": "aether"}','{"text": "slider"}','{"text": ""}']}}
setblock 87 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege den"}','{"text": "Slider"}','{"text": ""}','{"text": ""}']}}
fill 97 64 342 97 79 357 minecraft:light_gray_concrete
summon aether:slider 91.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
setblock 98 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.6"}','{"text": "aether"}','{"text": "queen"}','{"text": ""}']}}
setblock 99 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Besiege die"}','{"text": "Valkyrie Queen"}','{"text": ""}','{"text": ""}']}}
fill 109 64 342 109 79 357 minecraft:light_gray_concrete
summon aether:valkyrie_queen 103.5 64 348.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
