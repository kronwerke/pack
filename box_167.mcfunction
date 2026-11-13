# 167 mahou_tsukai/cloth, fay_sight, staff
#area 132 384 171 409
fill 132 64 384 171 91 409 minecraft:air
fill 132 60 384 171 62 409 minecraft:stone
fill 132 63 384 171 63 409 minecraft:light_gray_concrete
fill 136 64 390 171 79 390 minecraft:light_gray_concrete
fill 136 64 390 136 79 403 minecraft:light_gray_concrete
setblock 137 64 402 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "167.1"}','{"text": "mahou_tsukai"}','{"text": "cloth"}','{"text": ""}']}}
setblock 138 64 402 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schneid"}','{"text": "Zaubertuch"}','{"text": ""}','{"text": ""}']}}
fill 146 64 390 146 79 403 minecraft:light_gray_concrete
setblock 140 64 395 minecraft:smooth_stone_slab
summon item_display 140.5 64.95 395.5 {item:{id:"mahoutsukai:dagger",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 142 64 395 minecraft:smooth_stone_slab
summon item_display 142.5 64.95 395.5 {item:{id:"mahoutsukai:spell_cloth",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 147 64 402 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "167.2"}','{"text": "mahou_tsukai"}','{"text": "fay_sight"}','{"text": ""}']}}
setblock 148 64 402 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne die"}','{"text": "Feensicht"}','{"text": ""}','{"text": ""}']}}
fill 156 64 390 156 79 403 minecraft:light_gray_concrete
setblock 151 64 395 minecraft:smooth_stone_slab
summon item_display 151.5 65.4 395.5 {item:{id:"mahoutsukai:scroll_fay_sight",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 157 64 402 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "167.3"}','{"text": "mahou_tsukai"}','{"text": "staff"}','{"text": ""}']}}
setblock 158 64 402 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ruf einen"}','{"text": "Mystischen Stab"}','{"text": ""}','{"text": ""}']}}
fill 166 64 390 166 79 403 minecraft:light_gray_concrete
setblock 161 64 395 minecraft:smooth_stone_slab
summon item_display 161.5 65.4 395.5 {item:{id:"mahoutsukai:mystic_staff",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
