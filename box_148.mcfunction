# 148 hostile_networks/deep_learner, sim_chamber, scaling, data_center
#area 285 313 338 340
fill 285 64 313 320 95 340 minecraft:air
fill 321 64 313 338 95 340 minecraft:air
fill 285 60 313 338 62 340 minecraft:stone
fill 285 63 313 338 63 340 minecraft:light_gray_concrete
fill 289 64 319 338 83 319 minecraft:light_gray_concrete
fill 289 64 319 289 83 334 minecraft:light_gray_concrete
setblock 290 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.1"}','{"text": "hostile_networks"}','{"text": "deep_learner"}','{"text": ""}']}}
setblock 291 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Deep"}','{"text": "Learner"}','{"text": ""}','{"text": ""}']}}
fill 299 64 319 299 83 334 minecraft:light_gray_concrete
setblock 294 64 324 minecraft:smooth_stone_slab
summon item_display 294.5 65.4 324.5 {item:{id:"hostilenetworks:deep_learner",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 300 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.2"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 301 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 309 64 319 309 83 334 minecraft:light_gray_concrete
setblock 303 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 324 hostilenetworks:loot_fabricator[facing=south]
setblock 310 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.3"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 311 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 321 64 319 321 83 334 minecraft:light_gray_concrete
setblock 312 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 313 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 314 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 316 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 317 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 318 64 324 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 326 hostilenetworks:loot_fabricator[facing=south]
setblock 322 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "148.4"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 323 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 333 64 319 333 83 334 minecraft:light_gray_concrete
fill 324 64 322 330 64 328 minecraft:obsidian
fill 324 70 322 330 70 328 minecraft:black_stained_glass
fill 324 65 322 324 69 322 minecraft:black_stained_glass
fill 324 65 323 324 69 323 minecraft:black_stained_glass
fill 324 65 324 324 69 324 minecraft:black_stained_glass
fill 324 65 325 324 69 325 minecraft:black_stained_glass
fill 324 65 326 324 69 326 minecraft:black_stained_glass
fill 324 65 327 324 69 327 minecraft:black_stained_glass
fill 324 65 328 324 69 328 minecraft:black_stained_glass
fill 325 65 322 325 69 322 minecraft:black_stained_glass
fill 325 65 328 325 69 328 minecraft:black_stained_glass
fill 326 65 322 326 69 322 minecraft:black_stained_glass
fill 326 65 328 326 69 328 minecraft:black_stained_glass
fill 327 65 322 327 69 322 minecraft:black_stained_glass
fill 327 65 328 327 69 328 minecraft:black_stained_glass
fill 328 65 322 328 69 322 minecraft:black_stained_glass
fill 328 65 328 328 69 328 minecraft:black_stained_glass
fill 329 65 322 329 69 322 minecraft:black_stained_glass
fill 329 65 328 329 69 328 minecraft:black_stained_glass
fill 330 65 322 330 69 322 minecraft:black_stained_glass
fill 330 65 323 330 69 323 minecraft:black_stained_glass
fill 330 65 324 330 69 324 minecraft:black_stained_glass
fill 330 65 325 330 69 325 minecraft:black_stained_glass
fill 330 65 326 330 69 326 minecraft:black_stained_glass
fill 330 65 327 330 69 327 minecraft:black_stained_glass
fill 330 65 328 330 69 328 minecraft:black_stained_glass
setblock 327 65 328 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
