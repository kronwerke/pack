# 132 hexerei/willow_broom
#area 339 184 358 209
fill 339 64 184 358 91 209 minecraft:air
fill 339 60 184 358 62 209 minecraft:stone
fill 339 63 184 358 63 209 minecraft:light_gray_concrete
fill 343 64 190 358 79 190 minecraft:light_gray_concrete
fill 343 64 190 343 79 203 minecraft:light_gray_concrete
setblock 344 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132"}','{"text": "hexerei"}','{"text": "willow_broom"}','{"text": ""}']}}
setblock 345 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "flying on a"}','{"text": "broom, plus the"}','{"text": "broom menu"}','{"text": ""}']}}
fill 353 64 190 353 79 203 minecraft:light_gray_concrete
setblock 348 64 195 minecraft:smooth_stone_slab
summon item_display 348.5 65.4 195.5 {item:{id:"hexerei:willow_broom",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
