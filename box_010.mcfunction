# 010 farms/lava_seeds
#area 75 21 94 46
fill 75 64 21 94 91 46 minecraft:air
fill 75 60 21 94 62 46 minecraft:stone
fill 75 63 21 94 63 46 minecraft:light_gray_concrete
fill 79 64 27 94 79 27 minecraft:light_gray_concrete
fill 79 64 27 79 79 40 minecraft:light_gray_concrete
setblock 80 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "farms"}','{"text": "lava_seeds"}','{"text": ""}']}}
setblock 81 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fire seed"}','{"text": "field, the lava"}','{"text": "bucket recipe,"}','{"text": "item drain into"}']}}
setblock 82 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fluid tanks"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 89 64 27 89 79 40 minecraft:light_gray_concrete
fill 82 63 31 86 63 33 minecraft:farmland[moisture=7]
setblock 84 63 32 minecraft:water
setblock 82 64 31 mysticalagriculture:fire_crop[age=7]
setblock 82 64 32 mysticalagriculture:fire_crop[age=7]
setblock 82 64 33 mysticalagriculture:fire_crop[age=7]
setblock 83 64 31 mysticalagriculture:fire_crop[age=7]
setblock 83 64 32 mysticalagriculture:fire_crop[age=7]
setblock 83 64 33 mysticalagriculture:fire_crop[age=7]
setblock 84 64 31 mysticalagriculture:fire_crop[age=7]
setblock 84 64 33 mysticalagriculture:fire_crop[age=7]
setblock 85 64 31 mysticalagriculture:fire_crop[age=7]
setblock 85 64 32 mysticalagriculture:fire_crop[age=7]
setblock 85 64 33 mysticalagriculture:fire_crop[age=7]
setblock 86 64 31 mysticalagriculture:fire_crop[age=7]
setblock 86 64 32 mysticalagriculture:fire_crop[age=7]
setblock 86 64 33 mysticalagriculture:fire_crop[age=7]
setblock 87 64 32 create:fluid_tank[bottom=true,shape=window,top=true]
setblock 87 65 32 create:item_drain
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
