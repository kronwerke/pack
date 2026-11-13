# 012 farms/lava_seeds
#area 90 21 109 46
fill 90 64 21 109 91 46 minecraft:air
fill 90 60 21 109 62 46 minecraft:stone
fill 90 63 21 109 63 46 minecraft:light_gray_concrete
fill 94 64 27 109 79 27 minecraft:light_gray_concrete
fill 94 64 27 94 79 40 minecraft:light_gray_concrete
setblock 95 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "012"}','{"text": "farms"}','{"text": "lava_seeds"}','{"text": ""}']}}
setblock 96 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fire seed"}','{"text": "field, the lava"}','{"text": "bucket recipe,"}','{"text": "item drain into"}']}}
setblock 97 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fluid tanks"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 104 64 27 104 79 40 minecraft:light_gray_concrete
fill 97 63 31 101 63 33 minecraft:farmland[moisture=7]
setblock 99 63 32 minecraft:water
setblock 97 64 31 mysticalagriculture:fire_crop[age=7]
setblock 97 64 32 mysticalagriculture:fire_crop[age=7]
setblock 97 64 33 mysticalagriculture:fire_crop[age=7]
setblock 98 64 31 mysticalagriculture:fire_crop[age=7]
setblock 98 64 32 mysticalagriculture:fire_crop[age=7]
setblock 98 64 33 mysticalagriculture:fire_crop[age=7]
setblock 99 64 31 mysticalagriculture:fire_crop[age=7]
setblock 99 64 33 mysticalagriculture:fire_crop[age=7]
setblock 100 64 31 mysticalagriculture:fire_crop[age=7]
setblock 100 64 32 mysticalagriculture:fire_crop[age=7]
setblock 100 64 33 mysticalagriculture:fire_crop[age=7]
setblock 101 64 31 mysticalagriculture:fire_crop[age=7]
setblock 101 64 32 mysticalagriculture:fire_crop[age=7]
setblock 101 64 33 mysticalagriculture:fire_crop[age=7]
setblock 102 64 32 create:fluid_tank[bottom=true,shape=window,top=true]
setblock 102 65 32 create:item_drain
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
