# 022 create_brass/blaze_burner
#area 138 42 157 67
fill 138 64 42 157 91 67 minecraft:air
fill 138 60 42 157 62 67 minecraft:stone
fill 138 63 42 157 63 67 minecraft:light_gray_concrete
fill 142 64 48 157 79 48 minecraft:light_gray_concrete
fill 142 64 48 142 79 61 minecraft:light_gray_concrete
setblock 143 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create_brass"}','{"text": "blaze_burner"}','{"text": ""}']}}
setblock 144 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "catching a"}','{"text": "blaze with the"}','{"text": "empty burner"}','{"text": ""}']}}
fill 152 64 48 152 79 61 minecraft:light_gray_concrete
summon minecraft:blaze 146.5 64 53.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 149 64 53 minecraft:smooth_stone_slab
summon item_display 149.5 64.95 53.5 {item:{id:"create:empty_blaze_burner",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
