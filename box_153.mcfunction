# 153 hostile_networks/deep_learner, sim_chamber, scaling, data_center
#area 285 317 338 344
fill 285 64 317 320 95 344 minecraft:air
fill 321 64 317 338 95 344 minecraft:air
fill 285 60 317 338 62 344 minecraft:stone
fill 285 63 317 338 63 344 minecraft:light_gray_concrete
fill 289 64 323 338 83 323 minecraft:light_gray_concrete
fill 289 64 323 289 83 338 minecraft:light_gray_concrete
setblock 290 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.1"}','{"text": "hostile_networks"}','{"text": "deep_learner"}','{"text": ""}']}}
setblock 291 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Deep"}','{"text": "Learner"}','{"text": ""}','{"text": ""}']}}
fill 299 64 323 299 83 338 minecraft:light_gray_concrete
setblock 294 64 328 minecraft:smooth_stone_slab
summon item_display 294.5 65.4 328.5 {item:{id:"hostilenetworks:deep_learner",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 300 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.2"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 301 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 309 64 323 309 83 338 minecraft:light_gray_concrete
setblock 303 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 328 hostilenetworks:loot_fabricator[facing=south]
setblock 310 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.3"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 311 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 321 64 323 321 83 338 minecraft:light_gray_concrete
setblock 312 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 313 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 314 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 316 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 317 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 318 64 328 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 330 hostilenetworks:loot_fabricator[facing=south]
setblock 322 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.4"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 323 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 333 64 323 333 83 338 minecraft:light_gray_concrete
fill 324 64 326 330 64 332 minecraft:obsidian
fill 324 70 326 330 70 332 minecraft:black_stained_glass
fill 324 65 326 324 69 326 minecraft:black_stained_glass
fill 324 65 327 324 69 327 minecraft:black_stained_glass
fill 324 65 328 324 69 328 minecraft:black_stained_glass
fill 324 65 329 324 69 329 minecraft:black_stained_glass
fill 324 65 330 324 69 330 minecraft:black_stained_glass
fill 324 65 331 324 69 331 minecraft:black_stained_glass
fill 324 65 332 324 69 332 minecraft:black_stained_glass
fill 325 65 326 325 69 326 minecraft:black_stained_glass
fill 325 65 332 325 69 332 minecraft:black_stained_glass
fill 326 65 326 326 69 326 minecraft:black_stained_glass
fill 326 65 332 326 69 332 minecraft:black_stained_glass
fill 327 65 326 327 69 326 minecraft:black_stained_glass
fill 327 65 332 327 69 332 minecraft:black_stained_glass
fill 328 65 326 328 69 326 minecraft:black_stained_glass
fill 328 65 332 328 69 332 minecraft:black_stained_glass
fill 329 65 326 329 69 326 minecraft:black_stained_glass
fill 329 65 332 329 69 332 minecraft:black_stained_glass
fill 330 65 326 330 69 326 minecraft:black_stained_glass
fill 330 65 327 330 69 327 minecraft:black_stained_glass
fill 330 65 328 330 69 328 minecraft:black_stained_glass
fill 330 65 329 330 69 329 minecraft:black_stained_glass
fill 330 65 330 330 69 330 minecraft:black_stained_glass
fill 330 65 331 330 69 331 minecraft:black_stained_glass
fill 330 65 332 330 69 332 minecraft:black_stained_glass
setblock 327 65 332 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
