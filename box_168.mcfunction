# 168 hostile_networks/deep_learner, sim_chamber, scaling, data_center
#area 285 319 338 346
fill 285 64 319 320 95 346 minecraft:air
fill 321 64 319 338 95 346 minecraft:air
fill 285 60 319 338 62 346 minecraft:stone
fill 285 63 319 338 63 346 minecraft:light_gray_concrete
fill 289 64 325 338 83 325 minecraft:light_gray_concrete
fill 289 64 325 289 83 340 minecraft:light_gray_concrete
setblock 290 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "168.1"}','{"text": "hostile_networks"}','{"text": "deep_learner"}','{"text": ""}']}}
setblock 291 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Deep"}','{"text": "Learner"}','{"text": ""}','{"text": ""}']}}
fill 299 64 325 299 83 340 minecraft:light_gray_concrete
setblock 294 64 330 minecraft:smooth_stone_slab
summon item_display 294.5 65.4 330.5 {item:{id:"hostilenetworks:deep_learner",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 300 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "168.2"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 301 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 309 64 325 309 83 340 minecraft:light_gray_concrete
setblock 303 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 330 hostilenetworks:loot_fabricator[facing=south]
setblock 310 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "168.3"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 311 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 321 64 325 321 83 340 minecraft:light_gray_concrete
setblock 312 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 313 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 314 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 316 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 317 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 318 64 330 hostilenetworks:sim_chamber[facing=south]
setblock 315 64 332 hostilenetworks:loot_fabricator[facing=south]
setblock 322 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "168.4"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 323 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 333 64 325 333 83 340 minecraft:light_gray_concrete
fill 324 64 328 330 64 334 minecraft:obsidian
fill 324 70 328 330 70 334 minecraft:black_stained_glass
fill 324 65 328 324 69 328 minecraft:black_stained_glass
fill 324 65 329 324 69 329 minecraft:black_stained_glass
fill 324 65 330 324 69 330 minecraft:black_stained_glass
fill 324 65 331 324 69 331 minecraft:black_stained_glass
fill 324 65 332 324 69 332 minecraft:black_stained_glass
fill 324 65 333 324 69 333 minecraft:black_stained_glass
fill 324 65 334 324 69 334 minecraft:black_stained_glass
fill 325 65 328 325 69 328 minecraft:black_stained_glass
fill 325 65 334 325 69 334 minecraft:black_stained_glass
fill 326 65 328 326 69 328 minecraft:black_stained_glass
fill 326 65 334 326 69 334 minecraft:black_stained_glass
fill 327 65 328 327 69 328 minecraft:black_stained_glass
fill 327 65 334 327 69 334 minecraft:black_stained_glass
fill 328 65 328 328 69 328 minecraft:black_stained_glass
fill 328 65 334 328 69 334 minecraft:black_stained_glass
fill 329 65 328 329 69 328 minecraft:black_stained_glass
fill 329 65 334 329 69 334 minecraft:black_stained_glass
fill 330 65 328 330 69 328 minecraft:black_stained_glass
fill 330 65 329 330 69 329 minecraft:black_stained_glass
fill 330 65 330 330 69 330 minecraft:black_stained_glass
fill 330 65 331 330 69 331 minecraft:black_stained_glass
fill 330 65 332 330 69 332 minecraft:black_stained_glass
fill 330 65 333 330 69 333 minecraft:black_stained_glass
fill 330 65 334 330 69 334 minecraft:black_stained_glass
setblock 327 65 334 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
