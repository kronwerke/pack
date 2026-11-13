# 060 mekanism_advanced/cnc_stamper
#area 240 97 259 122
fill 240 64 97 259 91 122 minecraft:air
fill 240 60 97 259 62 122 minecraft:stone
fill 240 63 97 259 63 122 minecraft:light_gray_concrete
fill 244 64 103 259 79 103 minecraft:light_gray_concrete
fill 244 64 103 244 79 116 minecraft:light_gray_concrete
setblock 245 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "060"}','{"text": "mekanism_advanced"}','{"text": "cnc_stamper"}','{"text": ""}']}}
setblock 246 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stamper GUI"}','{"text": "with the"}','{"text": "silicon press"}','{"text": ""}']}}
fill 254 64 103 254 79 116 minecraft:light_gray_concrete
setblock 248 64 108 minecraft:smooth_stone_slab
summon item_display 248.5 64.95 108.5 {item:{id:"mekmm:cnc_stamper",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 250 64 108 minecraft:smooth_stone_slab
summon item_display 250.5 64.95 108.5 {item:{id:"ae2:printed_silicon",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
