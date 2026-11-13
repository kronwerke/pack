# 053 mekanism_ores/full
#area 125 97 144 122
fill 125 64 97 144 91 122 minecraft:air
fill 125 60 97 144 62 122 minecraft:stone
fill 125 63 97 144 63 122 minecraft:light_gray_concrete
fill 129 64 103 144 79 103 minecraft:light_gray_concrete
fill 129 64 103 129 79 116 minecraft:light_gray_concrete
setblock 130 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "053"}','{"text": "mekanism_ores"}','{"text": "full"}','{"text": ""}']}}
setblock 131 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a machine GUI"}','{"text": "with 8 speed"}','{"text": "and 8 energy"}','{"text": "upgrades"}']}}
fill 139 64 103 139 79 116 minecraft:light_gray_concrete
setblock 133 64 108 minecraft:smooth_stone_slab
summon item_display 133.5 64.95 108.5 {item:{id:"mekanism:upgrade_speed",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 135 64 108 minecraft:smooth_stone_slab
summon item_display 135.5 64.95 108.5 {item:{id:"mekanism:upgrade_energy",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
