# 033 mekanism/configurator
#area -4 65 15 90
fill -4 64 65 15 91 90 minecraft:air
fill -4 60 65 15 62 90 minecraft:stone
fill -4 63 65 15 63 90 minecraft:light_gray_concrete
fill 0 64 71 15 79 71 minecraft:light_gray_concrete
fill 0 64 71 0 79 84 minecraft:light_gray_concrete
setblock 1 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "mekanism"}','{"text": "configurator"}','{"text": ""}']}}
setblock 2 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "side"}','{"text": "configuration"}','{"text": "tab with auto"}','{"text": "eject"}']}}
fill 10 64 71 10 79 84 minecraft:light_gray_concrete
setblock 4 64 76 mekanism:metallurgic_infuser[facing=south]
setblock 6 64 76 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 76.5 {item:{id:"mekanism:configurator",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
