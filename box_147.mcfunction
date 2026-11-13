# 147 immersive_heavy/hv, duroplast, survey
#area 161 242 204 267
fill 161 64 242 199 95 267 minecraft:air
fill 200 64 242 204 95 267 minecraft:air
fill 161 60 242 204 62 267 minecraft:stone
fill 161 63 242 204 63 267 minecraft:light_gray_concrete
fill 165 64 248 204 83 248 minecraft:light_gray_concrete
fill 165 64 248 165 83 261 minecraft:light_gray_concrete
setblock 166 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.1"}','{"text": "immersive_heavy"}','{"text": "hv"}','{"text": ""}']}}
setblock 167 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "an HV line on"}','{"text": "steel posts,"}','{"text": "the bottling"}','{"text": "machine with"}']}}
setblock 168 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "resin, a core"}','{"text": "sample on the"}','{"text": "ground"}','{"text": ""}']}}
fill 179 64 248 179 83 261 minecraft:light_gray_concrete
kw testworld use 168 63 253 up immersiveengineering:steel_post
execute unless block 168 67 253 minecraft:air
kw testworld use 168 67 253 up immersiveengineering:connector_hv
kw testworld use 176 63 253 up immersiveengineering:steel_post
execute unless block 176 67 253 minecraft:air
kw testworld use 176 67 253 up immersiveengineering:connector_hv
kw testworld use 168 68 253 south immersiveengineering:wirecoil_steel
kw testworld use 176 68 253 south immersiveengineering:wirecoil_steel
setblock 180 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.2"}','{"text": "immersive_heavy"}','{"text": "duroplast"}','{"text": ""}']}}
setblock 181 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Gieß"}','{"text": "Duroplastplatten"}','{"text": ""}','{"text": ""}']}}
fill 189 64 248 189 83 261 minecraft:light_gray_concrete
setblock 184 64 253 minecraft:smooth_stone_slab
summon item_display 184.5 65.4 253.5 {item:{id:"immersiveengineering:plate_duroplast",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 190 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.3"}','{"text": "immersive_heavy"}','{"text": "survey"}','{"text": ""}']}}
setblock 191 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Such eine"}','{"text": "Mineralader"}','{"text": ""}','{"text": ""}']}}
fill 199 64 248 199 83 261 minecraft:light_gray_concrete
kw testworld use 194 63 253 up immersiveengineering:sample_drill
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
