# 135 industrial/addons, sower, bio, crusher
#area 262 240 311 265
fill 262 64 240 306 91 265 minecraft:air
fill 307 64 240 311 91 265 minecraft:air
fill 262 60 240 311 62 265 minecraft:stone
fill 262 63 240 311 63 265 minecraft:light_gray_concrete
fill 266 64 246 311 79 246 minecraft:light_gray_concrete
fill 266 64 246 266 79 259 minecraft:light_gray_concrete
setblock 267 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.1"}','{"text": "industrial"}','{"text": "addons"}','{"text": ""}']}}
setblock 268 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
fill 276 64 246 276 79 259 minecraft:light_gray_concrete
setblock 270 64 251 minecraft:smooth_stone_slab
summon item_display 270.5 64.95 251.5 {item:{id:"industrialforegoing:speed_addon_tier_1",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 272 64 251 minecraft:smooth_stone_slab
summon item_display 272.5 64.95 251.5 {item:{id:"industrialforegoing:efficiency_addon_tier_1",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 277 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.2"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 278 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Sämaschine auf"}','{"text": ""}','{"text": ""}']}}
fill 286 64 246 286 79 259 minecraft:light_gray_concrete
setblock 280 64 250 minecraft:oak_log[axis=y]
setblock 282 64 250 minecraft:oak_log[axis=y]
setblock 280 64 252 minecraft:oak_log[axis=y]
setblock 282 64 252 minecraft:oak_log[axis=y]
setblock 281 64 251 industrialforegoing:plant_sower[subfacing=south]
fill 280 65 250 282 65 252 minecraft:farmland[moisture=7]
fill 280 66 250 282 66 252 minecraft:wheat[age=7]
fill 281 64 249 281 65 249 minecraft:stone_bricks
setblock 281 66 249 industrialforegoing:plant_gatherer[subfacing=south]
setblock 287 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.3"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 288 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
fill 296 64 246 296 79 259 minecraft:light_gray_concrete
setblock 291 64 251 industrialforegoing:bioreactor[subfacing=south]
setblock 297 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.4"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 298 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
fill 306 64 246 306 79 259 minecraft:light_gray_concrete
setblock 299 64 250 minecraft:oak_fence
setblock 299 64 253 minecraft:oak_fence
setblock 300 64 250 minecraft:oak_fence
setblock 300 64 253 minecraft:oak_fence
setblock 301 64 250 minecraft:oak_fence
setblock 301 64 253 minecraft:oak_fence
setblock 302 64 250 minecraft:oak_fence
setblock 302 64 253 minecraft:oak_fence
setblock 303 64 250 minecraft:oak_fence
setblock 303 64 253 minecraft:oak_fence
setblock 299 64 251 minecraft:oak_fence
setblock 303 64 251 minecraft:oak_fence
setblock 299 64 252 minecraft:oak_fence
setblock 303 64 252 minecraft:oak_fence
summon minecraft:cow 300.5 64 251.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:cow 302.5 64 252.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 301 64 249 industrialforegoing:mob_crusher[subfacing=south]
setblock 304 64 251 industrialforegoing:mob_duplicator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
