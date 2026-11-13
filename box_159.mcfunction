# 159 silent_gear/stone_anvil, crude_mixer, alloy_forge
#area -4 370 35 395
fill -4 64 370 35 91 395 minecraft:air
fill -4 60 370 35 62 395 minecraft:stone
fill -4 63 370 35 63 395 minecraft:light_gray_concrete
fill 0 64 376 35 79 376 minecraft:light_gray_concrete
fill 0 64 376 0 79 389 minecraft:light_gray_concrete
setblock 1 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.1"}','{"text": "silent_gear"}','{"text": "stone_anvil"}','{"text": ""}']}}
setblock 2 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Steinamboss auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 376 10 79 389 minecraft:light_gray_concrete
setblock 4 64 381 silentgear:stone_anvil
setblock 6 64 381 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 381.5 {item:{id:"silentgear:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 11 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.2"}','{"text": "silent_gear"}','{"text": "crude_mixer"}','{"text": ""}']}}
setblock 12 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Crude"}','{"text": "Mixer"}','{"text": ""}','{"text": ""}']}}
fill 20 64 376 20 79 389 minecraft:light_gray_concrete
setblock 15 64 381 silentgear:crude_mixer[facing=south,lit=true]
setblock 21 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159.3"}','{"text": "silent_gear"}','{"text": "alloy_forge"}','{"text": ""}']}}
setblock 22 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmiede"}','{"text": ""}','{"text": ""}']}}
fill 30 64 376 30 79 389 minecraft:light_gray_concrete
setblock 24 64 381 silentgear:alloy_forge[facing=south,lit=true]
setblock 26 64 381 silentgear:starlight_charger
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
