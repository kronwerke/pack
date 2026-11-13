# 162 silent_gear/stone_anvil, crude_mixer, repair_kit, alloy_forge
#area -4 378 45 403
fill -4 64 378 40 91 403 minecraft:air
fill 41 64 378 45 91 403 minecraft:air
fill -4 60 378 45 62 403 minecraft:stone
fill -4 63 378 45 63 403 minecraft:light_gray_concrete
fill 0 64 384 45 79 384 minecraft:light_gray_concrete
fill 0 64 384 0 79 397 minecraft:light_gray_concrete
setblock 1 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.1"}','{"text": "silent_gear"}','{"text": "stone_anvil"}','{"text": ""}']}}
setblock 2 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Steinamboss auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 384 10 79 397 minecraft:light_gray_concrete
setblock 4 64 389 silentgear:stone_anvil
setblock 6 64 389 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 389.5 {item:{id:"silentgear:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 11 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.2"}','{"text": "silent_gear"}','{"text": "crude_mixer"}','{"text": ""}']}}
setblock 12 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Crude"}','{"text": "Mixer"}','{"text": ""}','{"text": ""}']}}
fill 20 64 384 20 79 397 minecraft:light_gray_concrete
setblock 15 64 389 silentgear:crude_mixer[facing=south,lit=true]
setblock 21 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.3"}','{"text": "silent_gear"}','{"text": "repair_kit"}','{"text": ""}']}}
setblock 22 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Füll ein"}','{"text": "Reparaturkit"}','{"text": ""}','{"text": ""}']}}
fill 30 64 384 30 79 397 minecraft:light_gray_concrete
setblock 25 64 389 minecraft:smooth_stone_slab
summon item_display 25.5 65.4 389.5 {item:{id:"silentgear:crude_repair_kit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 31 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "162.4"}','{"text": "silent_gear"}','{"text": "alloy_forge"}','{"text": ""}']}}
setblock 32 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmiede"}','{"text": ""}','{"text": ""}']}}
fill 40 64 384 40 79 397 minecraft:light_gray_concrete
setblock 34 64 389 silentgear:alloy_forge[facing=south,lit=true]
setblock 36 64 389 silentgear:starlight_charger
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
