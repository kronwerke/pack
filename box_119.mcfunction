# 119 occultism/satchel
#area 110 184 129 209
fill 110 64 184 129 91 209 minecraft:air
fill 110 60 184 129 62 209 minecraft:stone
fill 110 63 184 129 63 209 minecraft:light_gray_concrete
fill 114 64 190 129 79 190 minecraft:light_gray_concrete
fill 114 64 190 114 79 203 minecraft:light_gray_concrete
setblock 115 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "119"}','{"text": "occultism"}','{"text": "satchel"}','{"text": ""}']}}
setblock 116 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Dictionary"}','{"text": "pentacle"}','{"text": "preview in the"}','{"text": "world"}']}}
fill 124 64 190 124 79 203 minecraft:light_gray_concrete
setblock 119 64 195 minecraft:smooth_stone_slab
summon item_display 119.5 65.4 195.5 {item:{id:"occultism:ritual_satchel_t1",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
