# 130 hexerei/blood
#area 309 184 328 209
fill 309 64 184 328 91 209 minecraft:air
fill 309 60 184 328 62 209 minecraft:stone
fill 309 63 184 328 63 209 minecraft:light_gray_concrete
fill 313 64 190 328 79 190 minecraft:light_gray_concrete
fill 313 64 190 313 79 203 minecraft:light_gray_concrete
setblock 314 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130"}','{"text": "hexerei"}','{"text": "blood"}','{"text": ""}']}}
setblock 315 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cauldron menu"}','{"text": "with the blood"}','{"text": "sigil"}','{"text": ""}']}}
fill 323 64 190 323 79 203 minecraft:light_gray_concrete
setblock 317 64 195 minecraft:smooth_stone_slab
summon item_display 317.5 64.95 195.5 {item:{id:"hexerei:blood_sigil",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 319 64 195 minecraft:smooth_stone_slab
summon item_display 319.5 64.95 195.5 {item:{id:"hexerei:blood_bottle",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
