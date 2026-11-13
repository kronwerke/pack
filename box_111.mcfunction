# 111 alfheim/corporea_index
#area 362 147 381 172
fill 362 64 147 381 91 172 minecraft:air
fill 362 60 147 381 62 172 minecraft:stone
fill 362 63 147 381 63 172 minecraft:light_gray_concrete
fill 366 64 153 381 79 153 minecraft:light_gray_concrete
fill 366 64 153 366 79 166 minecraft:light_gray_concrete
setblock 367 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111"}','{"text": "alfheim"}','{"text": "corporea_index"}','{"text": ""}']}}
setblock 368 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the index with"}','{"text": "a chat request"}','{"text": ""}','{"text": ""}']}}
fill 376 64 153 376 79 166 minecraft:light_gray_concrete
setblock 371 64 158 minecraft:smooth_stone_slab
summon item_display 371.5 65.4 158.5 {item:{id:"botania:corporea_index",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
