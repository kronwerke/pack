# 106 gaia/goal
#area 283 147 302 172
fill 283 64 147 302 91 172 minecraft:air
fill 283 60 147 302 62 172 minecraft:stone
fill 283 63 147 302 63 172 minecraft:light_gray_concrete
fill 287 64 153 302 79 153 minecraft:light_gray_concrete
fill 287 64 153 287 79 166 minecraft:light_gray_concrete
setblock 288 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "106"}','{"text": "gaia"}','{"text": "goal"}','{"text": ""}']}}
setblock 289 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a chest by the"}','{"text": "obelisk holding"}','{"text": "spirits"}','{"text": ""}']}}
fill 297 64 153 297 79 166 minecraft:light_gray_concrete
setblock 292 64 158 minecraft:smooth_stone_slab
summon item_display 292.5 65.4 158.5 {item:{id:"botania:gaia_spirit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
