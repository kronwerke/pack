# 162 silent_gear/stone_anvil, crude_mixer, repair_kit, alloy_forge
#area -4 401 45 426
fill -4 64 401 40 91 426 minecraft:air
fill 41 64 401 45 91 426 minecraft:air
fill -4 60 401 45 62 426 minecraft:stone
fill -4 63 401 45 63 426 minecraft:light_gray_concrete
fill 0 64 407 45 79 407 minecraft:light_gray_concrete
fill 0 64 407 0 79 420 minecraft:light_gray_concrete
setblock 1 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.1"}','{"text": "silent_gear"}','{"text": "stone_anvil"}','{"text": ""}']}}
setblock 2 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Steinamboss auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 407 10 79 420 minecraft:light_gray_concrete
setblock 4 64 412 silentgear:stone_anvil
setblock 6 64 412 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 412.5 {item:{id:"silentgear:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 11 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.2"}','{"text": "silent_gear"}','{"text": "crude_mixer"}','{"text": ""}']}}
setblock 12 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Crude"}','{"text": "Mixer"}','{"text": ""}','{"text": ""}']}}
fill 20 64 407 20 79 420 minecraft:light_gray_concrete
setblock 15 64 412 silentgear:crude_mixer[facing=south,lit=true]
setblock 21 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.3"}','{"text": "silent_gear"}','{"text": "repair_kit"}','{"text": ""}']}}
setblock 22 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Füll ein"}','{"text": "Reparaturkit"}','{"text": ""}','{"text": ""}']}}
fill 30 64 407 30 79 420 minecraft:light_gray_concrete
setblock 25 64 412 minecraft:smooth_stone_slab
summon item_display 25.5 65.4 412.5 {item:{id:"silentgear:crude_repair_kit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 31 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.4"}','{"text": "silent_gear"}','{"text": "alloy_forge"}','{"text": ""}']}}
setblock 32 64 419 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmiede"}','{"text": ""}','{"text": ""}']}}
fill 40 64 407 40 79 420 minecraft:light_gray_concrete
setblock 34 64 412 silentgear:alloy_forge[facing=south,lit=true]
setblock 36 64 412 silentgear:starlight_charger
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
