# 143 silent_gear/stone_anvil, crude_mixer, alloy_forge
#area -4 338 35 363
fill -4 64 338 35 91 363 minecraft:air
fill -4 60 338 35 62 363 minecraft:stone
fill -4 63 338 35 63 363 minecraft:light_gray_concrete
fill 0 64 344 35 79 344 minecraft:light_gray_concrete
fill 0 64 344 0 79 357 minecraft:light_gray_concrete
setblock 1 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.1"}','{"text": "silent_gear"}','{"text": "stone_anvil"}','{"text": ""}']}}
setblock 2 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Steinamboss auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 344 10 79 357 minecraft:light_gray_concrete
setblock 4 64 349 silentgear:stone_anvil
setblock 6 64 349 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 349.5 {item:{id:"silentgear:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 11 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.2"}','{"text": "silent_gear"}','{"text": "crude_mixer"}','{"text": ""}']}}
setblock 12 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Crude"}','{"text": "Mixer"}','{"text": ""}','{"text": ""}']}}
fill 20 64 344 20 79 357 minecraft:light_gray_concrete
setblock 15 64 349 silentgear:crude_mixer[facing=south,lit=true]
setblock 21 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143.3"}','{"text": "silent_gear"}','{"text": "alloy_forge"}','{"text": ""}']}}
setblock 22 64 356 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmiede"}','{"text": ""}','{"text": ""}']}}
fill 30 64 344 30 79 357 minecraft:light_gray_concrete
setblock 24 64 349 silentgear:alloy_forge[facing=south,lit=true]
setblock 26 64 349 silentgear:starlight_charger
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
