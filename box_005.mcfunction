# 005 start_here/m_gearbox, m_keystone
#area 66 -6 95 19
fill 66 64 -6 95 91 19 minecraft:air
fill 66 60 -6 95 62 19 minecraft:stone
fill 66 63 -6 95 63 19 minecraft:light_gray_concrete
fill 70 64 0 95 79 0 minecraft:light_gray_concrete
fill 70 64 0 70 79 13 minecraft:light_gray_concrete
setblock 71 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "005.1"}','{"text": "start_here"}','{"text": "m_gearbox"}','{"text": ""}']}}
setblock 72 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the crafting"}','{"text": "grid in JEI"}','{"text": ""}','{"text": ""}']}}
fill 80 64 0 80 79 13 minecraft:light_gray_concrete
setblock 75 64 5 minecraft:smooth_stone_slab
summon item_display 75.5 65.4 5.5 {item:{id:"kronwerke:stone_gearbox",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 81 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "005.2"}','{"text": "start_here"}','{"text": "m_keystone"}','{"text": ""}']}}
setblock 82 64 12 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Quellschlussstein"}','{"text": ""}','{"text": ""}']}}
fill 90 64 0 90 79 13 minecraft:light_gray_concrete
setblock 85 64 5 minecraft:smooth_stone_slab
summon item_display 85.5 65.4 5.5 {item:{id:"kronwerke:source_keystone",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
