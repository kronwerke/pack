# 145 immersive_heavy/light, heavy
#area 253 219 282 244
fill 253 64 219 282 91 244 minecraft:air
fill 253 60 219 282 62 244 minecraft:stone
fill 253 63 219 282 63 244 minecraft:light_gray_concrete
fill 257 64 225 282 79 225 minecraft:light_gray_concrete
fill 257 64 225 257 79 238 minecraft:light_gray_concrete
setblock 258 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.1"}','{"text": "immersive_heavy"}','{"text": "light"}','{"text": ""}']}}
setblock 259 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Kronwerke"}','{"text": "recipes in the"}','{"text": "grid"}','{"text": ""}']}}
fill 267 64 225 267 79 238 minecraft:light_gray_concrete
setblock 262 64 230 minecraft:smooth_stone_slab
summon item_display 262.5 65.4 230.5 {item:{id:"immersiveengineering:light_engineering",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 268 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.2"}','{"text": "immersive_heavy"}','{"text": "heavy"}','{"text": ""}']}}
setblock 269 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Schwere"}','{"text": "Ingenieursbausteine"}','{"text": ""}','{"text": ""}']}}
fill 277 64 225 277 79 238 minecraft:light_gray_concrete
setblock 272 64 230 minecraft:smooth_stone_slab
summon item_display 272.5 65.4 230.5 {item:{id:"immersiveengineering:heavy_engineering",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
