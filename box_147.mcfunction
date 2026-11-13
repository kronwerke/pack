# 147 silent_gear/stone_anvil, crude_mixer, alloy_forge
#area -4 340 35 365
fill -4 64 340 35 91 365 minecraft:air
fill -4 60 340 35 62 365 minecraft:stone
fill -4 63 340 35 63 365 minecraft:light_gray_concrete
fill 0 64 346 35 79 346 minecraft:light_gray_concrete
fill 0 64 346 0 79 359 minecraft:light_gray_concrete
setblock 1 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.1"}','{"text": "silent_gear"}','{"text": "stone_anvil"}','{"text": ""}']}}
setblock 2 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Steinamboss auf"}','{"text": ""}','{"text": ""}']}}
fill 10 64 346 10 79 359 minecraft:light_gray_concrete
setblock 4 64 351 silentgear:stone_anvil
setblock 6 64 351 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 351.5 {item:{id:"silentgear:hammer",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 11 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.2"}','{"text": "silent_gear"}','{"text": "crude_mixer"}','{"text": ""}']}}
setblock 12 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Crude"}','{"text": "Mixer"}','{"text": ""}','{"text": ""}']}}
fill 20 64 346 20 79 359 minecraft:light_gray_concrete
setblock 15 64 351 silentgear:crude_mixer[facing=south,lit=true]
setblock 21 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.3"}','{"text": "silent_gear"}','{"text": "alloy_forge"}','{"text": ""}']}}
setblock 22 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Legierungsschmiede"}','{"text": ""}','{"text": ""}']}}
fill 30 64 346 30 79 359 minecraft:light_gray_concrete
setblock 24 64 351 silentgear:alloy_forge[facing=south,lit=true]
setblock 26 64 351 silentgear:starlight_charger
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
