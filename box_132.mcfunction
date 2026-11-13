# 132 immersive_heavy/hv, duroplast, survey
#area 161 240 204 265
fill 161 64 240 199 95 265 minecraft:air
fill 200 64 240 204 95 265 minecraft:air
fill 161 60 240 204 62 265 minecraft:stone
fill 161 63 240 204 63 265 minecraft:light_gray_concrete
fill 165 64 246 204 83 246 minecraft:light_gray_concrete
fill 165 64 246 165 83 259 minecraft:light_gray_concrete
setblock 166 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.1"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 167 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 168 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 179 64 246 179 83 259 minecraft:light_gray_concrete
kw testworld use 168 63 251 up immersiveengineering:steel_post
execute unless block 168 67 251 minecraft:air
kw testworld use 168 67 251 up immersiveengineering:connector_hv
kw testworld use 176 63 251 up immersiveengineering:steel_post
execute unless block 176 67 251 minecraft:air
kw testworld use 176 67 251 up immersiveengineering:connector_hv
kw testworld use 168 68 251 south immersiveengineering:wirecoil_steel
kw testworld use 176 68 251 south immersiveengineering:wirecoil_steel
setblock 180 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.2"}','{"text": "immersive_heavy"}','{"text": "duroplast"}','{"text": ""}']}}
setblock 181 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Gieß"}','{"text": "Duroplastplatten"}','{"text": ""}','{"text": ""}']}}
fill 189 64 246 189 83 259 minecraft:light_gray_concrete
setblock 184 64 251 minecraft:smooth_stone_slab
summon item_display 184.5 65.4 251.5 {item:{id:"immersiveengineering:plate_duroplast",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 190 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.3"}','{"text": "immersive_heavy"}','{"text": "survey"}','{"text": ""}']}}
setblock 191 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Such eine"}','{"text": "Mineralader"}','{"text": ""}','{"text": ""}']}}
fill 199 64 246 199 83 259 minecraft:light_gray_concrete
kw testworld use 194 63 251 up immersiveengineering:sample_drill
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
