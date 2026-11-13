# 043 mekanism/configurator
#area -4 95 15 120
fill -4 64 95 15 91 120 minecraft:air
fill -4 60 95 15 62 120 minecraft:stone
fill -4 63 95 15 63 120 minecraft:light_gray_concrete
fill 0 64 101 15 79 101 minecraft:light_gray_concrete
fill 0 64 101 0 79 114 minecraft:light_gray_concrete
setblock 1 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "043"}','{"text": "mekanism"}','{"text": "configurator"}','{"text": ""}']}}
setblock 2 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "side"}','{"text": "configuration"}','{"text": "tab with auto"}','{"text": "eject"}']}}
fill 10 64 101 10 79 114 minecraft:light_gray_concrete
setblock 4 64 106 mekanism:metallurgic_infuser[facing=south]
setblock 6 64 106 minecraft:smooth_stone_slab
summon item_display 6.5 64.95 106.5 {item:{id:"mekanism:configurator",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
