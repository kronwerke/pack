# 132 hostile_networks/sim_chamber, scaling, data_center
#area 285 275 328 302
fill 285 64 275 320 95 302 minecraft:air
fill 321 64 275 328 95 302 minecraft:air
fill 285 60 275 328 62 302 minecraft:stone
fill 285 63 275 328 63 302 minecraft:light_gray_concrete
fill 289 64 281 328 83 281 minecraft:light_gray_concrete
fill 289 64 281 289 83 296 minecraft:light_gray_concrete
setblock 290 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.1"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 291 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 299 64 281 299 83 296 minecraft:light_gray_concrete
setblock 293 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 295 64 286 hostilenetworks:loot_fabricator[facing=south]
setblock 300 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.2"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 301 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 311 64 281 311 83 296 minecraft:light_gray_concrete
setblock 302 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 303 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 304 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 306 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 307 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 308 64 286 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 288 hostilenetworks:loot_fabricator[facing=south]
setblock 312 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.3"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 313 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 323 64 281 323 83 296 minecraft:light_gray_concrete
fill 314 64 284 320 64 290 minecraft:obsidian
fill 314 70 284 320 70 290 minecraft:black_stained_glass
fill 314 65 284 314 69 284 minecraft:black_stained_glass
fill 314 65 285 314 69 285 minecraft:black_stained_glass
fill 314 65 286 314 69 286 minecraft:black_stained_glass
fill 314 65 287 314 69 287 minecraft:black_stained_glass
fill 314 65 288 314 69 288 minecraft:black_stained_glass
fill 314 65 289 314 69 289 minecraft:black_stained_glass
fill 314 65 290 314 69 290 minecraft:black_stained_glass
fill 315 65 284 315 69 284 minecraft:black_stained_glass
fill 315 65 290 315 69 290 minecraft:black_stained_glass
fill 316 65 284 316 69 284 minecraft:black_stained_glass
fill 316 65 290 316 69 290 minecraft:black_stained_glass
fill 317 65 284 317 69 284 minecraft:black_stained_glass
fill 317 65 290 317 69 290 minecraft:black_stained_glass
fill 318 65 284 318 69 284 minecraft:black_stained_glass
fill 318 65 290 318 69 290 minecraft:black_stained_glass
fill 319 65 284 319 69 284 minecraft:black_stained_glass
fill 319 65 290 319 69 290 minecraft:black_stained_glass
fill 320 65 284 320 69 284 minecraft:black_stained_glass
fill 320 65 285 320 69 285 minecraft:black_stained_glass
fill 320 65 286 320 69 286 minecraft:black_stained_glass
fill 320 65 287 320 69 287 minecraft:black_stained_glass
fill 320 65 288 320 69 288 minecraft:black_stained_glass
fill 320 65 289 320 69 289 minecraft:black_stained_glass
fill 320 65 290 320 69 290 minecraft:black_stained_glass
setblock 317 65 290 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
