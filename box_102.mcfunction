# 102 hostile_networks/sim_chamber, scaling, data_center
#area 229 273 272 300
fill 229 64 273 264 95 300 minecraft:air
fill 265 64 273 272 95 300 minecraft:air
fill 229 60 273 272 62 300 minecraft:stone
fill 229 63 273 272 63 300 minecraft:light_gray_concrete
fill 233 64 279 272 83 279 minecraft:light_gray_concrete
fill 233 64 279 233 83 294 minecraft:light_gray_concrete
setblock 234 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.1"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 235 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 243 64 279 243 83 294 minecraft:light_gray_concrete
setblock 237 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 239 64 284 hostilenetworks:loot_fabricator[facing=south]
setblock 244 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.2"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 245 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 255 64 279 255 83 294 minecraft:light_gray_concrete
setblock 246 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 247 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 248 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 249 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 250 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 251 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 252 64 284 hostilenetworks:sim_chamber[facing=south]
setblock 249 64 286 hostilenetworks:loot_fabricator[facing=south]
setblock 256 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "102.3"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 257 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 267 64 279 267 83 294 minecraft:light_gray_concrete
fill 258 64 282 264 64 288 minecraft:obsidian
fill 258 70 282 264 70 288 minecraft:black_stained_glass
fill 258 65 282 258 69 282 minecraft:black_stained_glass
fill 258 65 283 258 69 283 minecraft:black_stained_glass
fill 258 65 284 258 69 284 minecraft:black_stained_glass
fill 258 65 285 258 69 285 minecraft:black_stained_glass
fill 258 65 286 258 69 286 minecraft:black_stained_glass
fill 258 65 287 258 69 287 minecraft:black_stained_glass
fill 258 65 288 258 69 288 minecraft:black_stained_glass
fill 259 65 282 259 69 282 minecraft:black_stained_glass
fill 259 65 288 259 69 288 minecraft:black_stained_glass
fill 260 65 282 260 69 282 minecraft:black_stained_glass
fill 260 65 288 260 69 288 minecraft:black_stained_glass
fill 261 65 282 261 69 282 minecraft:black_stained_glass
fill 261 65 288 261 69 288 minecraft:black_stained_glass
fill 262 65 282 262 69 282 minecraft:black_stained_glass
fill 262 65 288 262 69 288 minecraft:black_stained_glass
fill 263 65 282 263 69 282 minecraft:black_stained_glass
fill 263 65 288 263 69 288 minecraft:black_stained_glass
fill 264 65 282 264 69 282 minecraft:black_stained_glass
fill 264 65 283 264 69 283 minecraft:black_stained_glass
fill 264 65 284 264 69 284 minecraft:black_stained_glass
fill 264 65 285 264 69 285 minecraft:black_stained_glass
fill 264 65 286 264 69 286 minecraft:black_stained_glass
fill 264 65 287 264 69 287 minecraft:black_stained_glass
fill 264 65 288 264 69 288 minecraft:black_stained_glass
setblock 261 65 288 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
