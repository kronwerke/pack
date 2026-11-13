# 151 exploration/e_compass
#area 103 336 122 361
fill 103 64 336 122 91 361 minecraft:air
fill 103 60 336 122 62 361 minecraft:stone
fill 103 63 336 122 63 361 minecraft:light_gray_concrete
fill 107 64 342 122 79 342 minecraft:light_gray_concrete
fill 107 64 342 107 79 355 minecraft:light_gray_concrete
setblock 108 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151"}','{"text": "exploration"}','{"text": "e_compass"}','{"text": ""}']}}
setblock 109 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Kompass"}','{"text": "der Natur"}','{"text": ""}','{"text": ""}']}}
fill 117 64 342 117 79 355 minecraft:light_gray_concrete
setblock 112 64 347 minecraft:smooth_stone_slab
summon item_display 112.5 65.4 347.5 {item:{id:"naturescompass:naturescompass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
