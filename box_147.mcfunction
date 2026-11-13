# 147 hostile_networks/sim_chamber, scaling, data_center
#area 285 307 328 334
fill 285 64 307 320 95 334 minecraft:air
fill 321 64 307 328 95 334 minecraft:air
fill 285 60 307 328 62 334 minecraft:stone
fill 285 63 307 328 63 334 minecraft:light_gray_concrete
fill 289 64 313 328 83 313 minecraft:light_gray_concrete
fill 289 64 313 289 83 328 minecraft:light_gray_concrete
setblock 290 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.1"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 291 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 299 64 313 299 83 328 minecraft:light_gray_concrete
setblock 293 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 295 64 318 hostilenetworks:loot_fabricator[facing=south]
setblock 300 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.2"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 301 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 311 64 313 311 83 328 minecraft:light_gray_concrete
setblock 302 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 303 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 304 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 306 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 307 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 308 64 318 hostilenetworks:sim_chamber[facing=south]
setblock 305 64 320 hostilenetworks:loot_fabricator[facing=south]
setblock 312 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.3"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 313 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 323 64 313 323 83 328 minecraft:light_gray_concrete
fill 314 64 316 320 64 322 minecraft:obsidian
fill 314 70 316 320 70 322 minecraft:black_stained_glass
fill 314 65 316 314 69 316 minecraft:black_stained_glass
fill 314 65 317 314 69 317 minecraft:black_stained_glass
fill 314 65 318 314 69 318 minecraft:black_stained_glass
fill 314 65 319 314 69 319 minecraft:black_stained_glass
fill 314 65 320 314 69 320 minecraft:black_stained_glass
fill 314 65 321 314 69 321 minecraft:black_stained_glass
fill 314 65 322 314 69 322 minecraft:black_stained_glass
fill 315 65 316 315 69 316 minecraft:black_stained_glass
fill 315 65 322 315 69 322 minecraft:black_stained_glass
fill 316 65 316 316 69 316 minecraft:black_stained_glass
fill 316 65 322 316 69 322 minecraft:black_stained_glass
fill 317 65 316 317 69 316 minecraft:black_stained_glass
fill 317 65 322 317 69 322 minecraft:black_stained_glass
fill 318 65 316 318 69 316 minecraft:black_stained_glass
fill 318 65 322 318 69 322 minecraft:black_stained_glass
fill 319 65 316 319 69 316 minecraft:black_stained_glass
fill 319 65 322 319 69 322 minecraft:black_stained_glass
fill 320 65 316 320 69 316 minecraft:black_stained_glass
fill 320 65 317 320 69 317 minecraft:black_stained_glass
fill 320 65 318 320 69 318 minecraft:black_stained_glass
fill 320 65 319 320 69 319 minecraft:black_stained_glass
fill 320 65 320 320 69 320 minecraft:black_stained_glass
fill 320 65 321 320 69 321 minecraft:black_stained_glass
fill 320 65 322 320 69 322 minecraft:black_stained_glass
setblock 317 65 322 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
