# 150 industrial/addons, sower, bio, crusher
#area 262 242 311 267
fill 262 64 242 306 91 267 minecraft:air
fill 307 64 242 311 91 267 minecraft:air
fill 262 60 242 311 62 267 minecraft:stone
fill 262 63 242 311 63 267 minecraft:light_gray_concrete
fill 266 64 248 311 79 248 minecraft:light_gray_concrete
fill 266 64 248 266 79 261 minecraft:light_gray_concrete
setblock 267 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.1"}','{"text": "industrial"}','{"text": "addons"}','{"text": ""}']}}
setblock 268 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 276 64 248 276 79 261 minecraft:light_gray_concrete
setblock 270 64 253 minecraft:smooth_stone_slab
summon item_display 270.5 64.95 253.5 {item:{id:"industrialforegoing:speed_addon_tier_1",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 272 64 253 minecraft:smooth_stone_slab
summon item_display 272.5 64.95 253.5 {item:{id:"industrialforegoing:efficiency_addon_tier_1",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 277 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.2"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 278 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Sämaschine auf"}','{"text": ""}','{"text": ""}']}}
fill 286 64 248 286 79 261 minecraft:light_gray_concrete
setblock 280 64 252 minecraft:oak_log[axis=y]
setblock 282 64 252 minecraft:oak_log[axis=y]
setblock 280 64 254 minecraft:oak_log[axis=y]
setblock 282 64 254 minecraft:oak_log[axis=y]
setblock 281 64 253 industrialforegoing:plant_sower[subfacing=south]
fill 280 65 252 282 65 254 minecraft:farmland[moisture=7]
fill 280 66 252 282 66 254 minecraft:wheat[age=7]
fill 281 64 251 281 65 251 minecraft:stone_bricks
setblock 281 66 251 industrialforegoing:plant_gatherer[subfacing=south]
setblock 287 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.3"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 288 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 296 64 248 296 79 261 minecraft:light_gray_concrete
setblock 291 64 253 industrialforegoing:bioreactor[subfacing=south]
setblock 297 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.4"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 298 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 306 64 248 306 79 261 minecraft:light_gray_concrete
setblock 299 64 252 minecraft:oak_fence
setblock 299 64 255 minecraft:oak_fence
setblock 300 64 252 minecraft:oak_fence
setblock 300 64 255 minecraft:oak_fence
setblock 301 64 252 minecraft:oak_fence
setblock 301 64 255 minecraft:oak_fence
setblock 302 64 252 minecraft:oak_fence
setblock 302 64 255 minecraft:oak_fence
setblock 303 64 252 minecraft:oak_fence
setblock 303 64 255 minecraft:oak_fence
setblock 299 64 253 minecraft:oak_fence
setblock 303 64 253 minecraft:oak_fence
setblock 299 64 254 minecraft:oak_fence
setblock 303 64 254 minecraft:oak_fence
summon minecraft:cow 300.5 64 253.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 302.5 64 254.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 301 64 251 industrialforegoing:mob_crusher[subfacing=south]
setblock 304 64 253 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
