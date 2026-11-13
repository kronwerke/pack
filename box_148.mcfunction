# 148 hostile_networks/deep_learner, sim_chamber, scaling, data_center
#area 285 311 338 338
fill 285 64 311 320 95 338 minecraft:air
fill 321 64 311 338 95 338 minecraft:air
fill 285 60 311 338 62 338 minecraft:stone
fill 285 63 311 338 63 338 minecraft:light_gray_concrete
fill 289 64 317 338 83 317 minecraft:light_gray_concrete
fill 289 64 317 289 83 332 minecraft:light_gray_concrete
setblock 290 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.1"}','{"text": "hostile_networks"}','{"text": "deep_learner"}','{"text": ""}']}}
setblock 291 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Deep"}','{"text": "Learner"}','{"text": ""}','{"text": ""}']}}
fill 299 64 317 299 83 332 minecraft:light_gray_concrete
setblock 294 64 322 minecraft:smooth_stone_slab
summon item_display 294.5 64.95 322.5 {item:{id:"hostilenetworks:deep_learner",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 300 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.2"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 301 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 309 64 317 309 83 332 minecraft:light_gray_concrete
setblock 303 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 322 hostilenetworks:loot_fabricator[facing=south]
setblock 310 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.3"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 311 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 321 64 317 321 83 332 minecraft:light_gray_concrete
setblock 312 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 313 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 314 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 316 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 317 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 318 64 322 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 324 hostilenetworks:loot_fabricator[facing=south]
setblock 322 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.4"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 323 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 333 64 317 333 83 332 minecraft:light_gray_concrete
fill 324 64 320 330 64 326 minecraft:obsidian
fill 324 70 320 330 70 326 minecraft:black_stained_glass
fill 324 65 320 324 69 320 minecraft:black_stained_glass
fill 324 65 321 324 69 321 minecraft:black_stained_glass
fill 324 65 322 324 69 322 minecraft:black_stained_glass
fill 324 65 323 324 69 323 minecraft:black_stained_glass
fill 324 65 324 324 69 324 minecraft:black_stained_glass
fill 324 65 325 324 69 325 minecraft:black_stained_glass
fill 324 65 326 324 69 326 minecraft:black_stained_glass
fill 325 65 320 325 69 320 minecraft:black_stained_glass
fill 325 65 326 325 69 326 minecraft:black_stained_glass
fill 326 65 320 326 69 320 minecraft:black_stained_glass
fill 326 65 326 326 69 326 minecraft:black_stained_glass
fill 327 65 320 327 69 320 minecraft:black_stained_glass
fill 327 65 326 327 69 326 minecraft:black_stained_glass
fill 328 65 320 328 69 320 minecraft:black_stained_glass
fill 328 65 326 328 69 326 minecraft:black_stained_glass
fill 329 65 320 329 69 320 minecraft:black_stained_glass
fill 329 65 326 329 69 326 minecraft:black_stained_glass
fill 330 65 320 330 69 320 minecraft:black_stained_glass
fill 330 65 321 330 69 321 minecraft:black_stained_glass
fill 330 65 322 330 69 322 minecraft:black_stained_glass
fill 330 65 323 330 69 323 minecraft:black_stained_glass
fill 330 65 324 330 69 324 minecraft:black_stained_glass
fill 330 65 325 330 69 325 minecraft:black_stained_glass
fill 330 65 326 330 69 326 minecraft:black_stained_glass
setblock 327 65 326 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
