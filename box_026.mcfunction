# 026 create_brass/blaze_burner
#area 154 44 173 69
fill 154 64 44 173 91 69 minecraft:air
fill 154 60 44 173 62 69 minecraft:stone
fill 154 63 44 173 63 69 minecraft:light_gray_concrete
fill 158 64 50 173 79 50 minecraft:light_gray_concrete
fill 158 64 50 158 79 63 minecraft:light_gray_concrete
setblock 159 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "create_brass"}','{"text": "blaze_burner"}','{"text": ""}']}}
setblock 160 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "catching a"}','{"text": "blaze with the"}','{"text": "empty burner"}','{"text": ""}']}}
fill 168 64 50 168 79 63 minecraft:light_gray_concrete
summon minecraft:blaze 162.5 64 55.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 165 64 55 minecraft:smooth_stone_slab
summon item_display 165.5 64.95 55.5 {item:{id:"create:empty_blaze_burner",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
