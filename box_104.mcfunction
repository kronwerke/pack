# 104 gaia/tiara
#area 235 147 254 172
fill 235 64 147 254 91 172 minecraft:air
fill 235 60 147 254 62 172 minecraft:stone
fill 235 63 147 254 63 172 minecraft:light_gray_concrete
fill 239 64 153 254 79 153 minecraft:light_gray_concrete
fill 239 64 153 239 79 166 minecraft:light_gray_concrete
setblock 240 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104"}','{"text": "gaia"}','{"text": "tiara"}','{"text": ""}']}}
setblock 241 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "flying with the"}','{"text": "flight bar"}','{"text": "visible"}','{"text": ""}']}}
fill 249 64 153 249 79 166 minecraft:light_gray_concrete
setblock 244 64 158 minecraft:smooth_stone_slab
summon item_display 244.5 65.4 158.5 {item:{id:"botania:flugel_tiara",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
