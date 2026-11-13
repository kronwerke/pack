# 160 silent_gear/stone_anvil, crude_mixer, repair_kit, alloy_forge
#area -4 374 45 399
fill -4 64 374 40 91 399 minecraft:air
fill 41 64 374 45 91 399 minecraft:air
fill -4 60 374 45 62 399 minecraft:stone
fill -4 63 374 45 63 399 minecraft:light_gray_concrete
fill 0 64 380 45 79 380 minecraft:light_gray_concrete
fill 0 64 380 0 79 393 minecraft:light_gray_concrete
setblock 1 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.1"}','{"text": "silent_gear"}','{"text": "stone_anvil"}','{"text": ""}']}}
setblock 2 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Steinamboss auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 380 10 79 393 minecraft:light_gray_concrete
setblock 4 64 385 silentgear:stone_anvil
setblock 6 64 385 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 385.5 {item:{id:"silentgear:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 11 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.2"}','{"text": "silent_gear"}','{"text": "crude_mixer"}','{"text": ""}']}}
setblock 12 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Crude"}','{"text": "Mixer"}','{"text": ""}','{"text": ""}']}}
fill 20 64 380 20 79 393 minecraft:light_gray_concrete
setblock 15 64 385 silentgear:crude_mixer[facing=south,lit=true]
setblock 21 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.3"}','{"text": "silent_gear"}','{"text": "repair_kit"}','{"text": ""}']}}
setblock 22 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Füll ein"}','{"text": "Reparaturkit"}','{"text": ""}','{"text": ""}']}}
fill 30 64 380 30 79 393 minecraft:light_gray_concrete
setblock 25 64 385 minecraft:smooth_stone_slab
summon item_display 25.5 64.95 385.5 {item:{id:"silentgear:crude_repair_kit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 31 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.4"}','{"text": "silent_gear"}','{"text": "alloy_forge"}','{"text": ""}']}}
setblock 32 64 392 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmiede"}','{"text": ""}','{"text": ""}']}}
fill 40 64 380 40 79 393 minecraft:light_gray_concrete
setblock 34 64 385 silentgear:alloy_forge[facing=south,lit=true]
setblock 36 64 385 silentgear:starlight_charger
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
