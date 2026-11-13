# 133 hexerei/crow
#area 354 184 373 209
fill 354 64 184 373 91 209 minecraft:air
fill 354 60 184 373 62 209 minecraft:stone
fill 354 63 184 373 63 209 minecraft:light_gray_concrete
fill 358 64 190 373 79 190 minecraft:light_gray_concrete
fill 358 64 190 358 79 203 minecraft:light_gray_concrete
setblock 359 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133"}','{"text": "hexerei"}','{"text": "crow"}','{"text": ""}']}}
setblock 360 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "crow on the"}','{"text": "shoulder, crow"}','{"text": "flute menu"}','{"text": ""}']}}
fill 368 64 190 368 79 203 minecraft:light_gray_concrete
setblock 363 64 195 minecraft:smooth_stone_slab
summon item_display 363.5 65.4 195.5 {item:{id:"hexerei:crow_flute",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
