# 076 ars_apprentice/collector
#area 135 126 154 151
fill 135 64 126 154 91 151 minecraft:air
fill 135 60 126 154 62 151 minecraft:stone
fill 135 63 126 154 63 151 minecraft:light_gray_concrete
fill 139 64 132 154 79 132 minecraft:light_gray_concrete
fill 139 64 132 139 79 145 minecraft:light_gray_concrete
setblock 140 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "ars_apprentice"}','{"text": "collector"}','{"text": ""}']}}
setblock 141 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "collector at"}','{"text": "the link farm,"}','{"text": "depositor at"}','{"text": "the workshop"}']}}
fill 149 64 132 149 79 145 minecraft:light_gray_concrete
setblock 143 64 137 minecraft:smooth_stone_slab
summon item_display 143.5 64.95 137.5 {item:{id:"ars_nouveau:relay_collector",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 145 64 137 minecraft:smooth_stone_slab
summon item_display 145.5 64.95 137.5 {item:{id:"ars_nouveau:relay_deposit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
