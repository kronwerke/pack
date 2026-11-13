# 151 exploration/e_compass
#area 25 336 44 361
fill 25 64 336 44 91 361 minecraft:air
fill 25 60 336 44 62 361 minecraft:stone
fill 25 63 336 44 63 361 minecraft:light_gray_concrete
fill 29 64 342 44 79 342 minecraft:light_gray_concrete
fill 29 64 342 29 79 355 minecraft:light_gray_concrete
setblock 30 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151"}','{"text": "exploration"}','{"text": "e_compass"}','{"text": ""}']}}
setblock 31 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Kompass"}','{"text": "der Natur"}','{"text": ""}','{"text": ""}']}}
fill 39 64 342 39 79 355 minecraft:light_gray_concrete
setblock 34 64 347 minecraft:smooth_stone_slab
summon item_display 34.5 65.4 347.5 {item:{id:"naturescompass:naturescompass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
