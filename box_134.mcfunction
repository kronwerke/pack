# 134 hostile_networks/sim_chamber, scaling, data_center
#area 285 277 328 304
fill 285 64 277 320 95 304 minecraft:air
fill 321 64 277 328 95 304 minecraft:air
fill 285 60 277 328 62 304 minecraft:stone
fill 285 63 277 328 63 304 minecraft:light_gray_concrete
fill 289 64 283 328 83 283 minecraft:light_gray_concrete
fill 289 64 283 289 83 298 minecraft:light_gray_concrete
setblock 290 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134.1"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 291 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 299 64 283 299 83 298 minecraft:light_gray_concrete
setblock 293 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 295 64 288 hostilenetworks:loot_fabricator[facing=south]
setblock 300 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134.2"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 301 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 311 64 283 311 83 298 minecraft:light_gray_concrete
setblock 302 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 303 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 304 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 306 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 307 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 308 64 288 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 290 hostilenetworks:loot_fabricator[facing=south]
setblock 312 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "134.3"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 313 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 323 64 283 323 83 298 minecraft:light_gray_concrete
fill 314 64 286 320 64 292 minecraft:obsidian
fill 314 70 286 320 70 292 minecraft:black_stained_glass
fill 314 65 286 314 69 286 minecraft:black_stained_glass
fill 314 65 287 314 69 287 minecraft:black_stained_glass
fill 314 65 288 314 69 288 minecraft:black_stained_glass
fill 314 65 289 314 69 289 minecraft:black_stained_glass
fill 314 65 290 314 69 290 minecraft:black_stained_glass
fill 314 65 291 314 69 291 minecraft:black_stained_glass
fill 314 65 292 314 69 292 minecraft:black_stained_glass
fill 315 65 286 315 69 286 minecraft:black_stained_glass
fill 315 65 292 315 69 292 minecraft:black_stained_glass
fill 316 65 286 316 69 286 minecraft:black_stained_glass
fill 316 65 292 316 69 292 minecraft:black_stained_glass
fill 317 65 286 317 69 286 minecraft:black_stained_glass
fill 317 65 292 317 69 292 minecraft:black_stained_glass
fill 318 65 286 318 69 286 minecraft:black_stained_glass
fill 318 65 292 318 69 292 minecraft:black_stained_glass
fill 319 65 286 319 69 286 minecraft:black_stained_glass
fill 319 65 292 319 69 292 minecraft:black_stained_glass
fill 320 65 286 320 69 286 minecraft:black_stained_glass
fill 320 65 287 320 69 287 minecraft:black_stained_glass
fill 320 65 288 320 69 288 minecraft:black_stained_glass
fill 320 65 289 320 69 289 minecraft:black_stained_glass
fill 320 65 290 320 69 290 minecraft:black_stained_glass
fill 320 65 291 320 69 291 minecraft:black_stained_glass
fill 320 65 292 320 69 292 minecraft:black_stained_glass
setblock 317 65 292 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
