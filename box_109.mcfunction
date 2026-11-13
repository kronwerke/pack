# 109 alfheim/elementium_line
#area 332 147 351 172
fill 332 64 147 351 91 172 minecraft:air
fill 332 60 147 351 62 172 minecraft:stone
fill 332 63 147 351 63 172 minecraft:light_gray_concrete
fill 336 64 153 351 79 153 minecraft:light_gray_concrete
fill 336 64 153 336 79 166 minecraft:light_gray_concrete
setblock 337 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "109"}','{"text": "alfheim"}','{"text": "elementium_line"}','{"text": ""}']}}
setblock 338 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an automated"}','{"text": "manasteel block"}','{"text": "line into the"}','{"text": "portal"}']}}
fill 346 64 153 346 79 166 minecraft:light_gray_concrete
setblock 341 64 158 minecraft:smooth_stone_slab
summon item_display 341.5 65.4 158.5 {item:{id:"botania:elementium_ingot",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
