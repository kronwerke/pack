# 070 ars_nouveau/scribes_table
#area 43 126 62 151
fill 43 64 126 62 91 151 minecraft:air
fill 43 60 126 62 62 151 minecraft:stone
fill 43 63 126 62 63 151 minecraft:light_gray_concrete
fill 47 64 132 62 79 132 minecraft:light_gray_concrete
fill 47 64 132 47 79 145 minecraft:light_gray_concrete
setblock 48 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070"}','{"text": "ars_nouveau"}','{"text": "scribes_table"}','{"text": ""}']}}
setblock 49 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the glyph"}','{"text": "selection"}','{"text": "screen with"}','{"text": "ingredients"}']}}
setblock 50 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "over the table"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 57 64 132 57 79 145 minecraft:light_gray_concrete
setblock 52 64 137 minecraft:smooth_stone_slab
summon item_display 52.5 65.4 137.5 {item:{id:"ars_nouveau:scribes_table",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
