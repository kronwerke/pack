# 078 ars_apprentice/ritual_scrying
#area 165 126 184 151
fill 165 64 126 184 91 151 minecraft:air
fill 165 60 126 184 62 151 minecraft:stone
fill 165 63 126 184 63 151 minecraft:light_gray_concrete
fill 169 64 132 184 79 132 minecraft:light_gray_concrete
fill 169 64 132 169 79 145 minecraft:light_gray_concrete
setblock 170 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "ars_apprentice"}','{"text": "ritual_scrying"}','{"text": ""}']}}
setblock 171 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "scrying"}','{"text": "particles"}','{"text": "through stone"}','{"text": ""}']}}
fill 179 64 132 179 79 145 minecraft:light_gray_concrete
setblock 174 64 137 minecraft:smooth_stone_slab
summon item_display 174.5 65.4 137.5 {item:{id:"ars_nouveau:ritual_scrying",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
