# 092 hostile_networks/sim_chamber, scaling, data_center
#area 229 254 272 281
fill 229 64 254 264 95 281 minecraft:air
fill 265 64 254 272 95 281 minecraft:air
fill 229 60 254 272 62 281 minecraft:stone
fill 229 63 254 272 63 281 minecraft:light_gray_concrete
fill 233 64 260 272 83 260 minecraft:light_gray_concrete
fill 233 64 260 233 83 275 minecraft:light_gray_concrete
setblock 234 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.1"}','{"text": "hostile_networks"}','{"text": "sim_chamber"}','{"text": ""}']}}
setblock 235 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die"}','{"text": "Simulationskammer"}','{"text": ""}','{"text": ""}']}}
fill 243 64 260 243 83 275 minecraft:light_gray_concrete
setblock 237 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 239 64 265 hostilenetworks:loot_fabricator[facing=south]
setblock 244 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.2"}','{"text": "hostile_networks"}','{"text": "scaling"}','{"text": ""}']}}
setblock 245 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Viele Kammern,"}','{"text": "ein Modell je"}','{"text": "Kammer"}','{"text": ""}']}}
fill 255 64 260 255 83 275 minecraft:light_gray_concrete
setblock 246 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 247 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 248 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 249 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 250 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 251 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 252 64 265 hostilenetworks:sim_chamber[facing=south]
setblock 249 64 267 hostilenetworks:loot_fabricator[facing=south]
setblock 256 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092.3"}','{"text": "hostile_networks"}','{"text": "data_center"}','{"text": ""}']}}
setblock 257 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Das"}','{"text": "Rechenzentrum"}','{"text": ""}','{"text": ""}']}}
fill 267 64 260 267 83 275 minecraft:light_gray_concrete
fill 258 64 263 264 64 269 minecraft:obsidian
fill 258 70 263 264 70 269 minecraft:black_stained_glass
fill 258 65 263 258 69 263 minecraft:black_stained_glass
fill 258 65 264 258 69 264 minecraft:black_stained_glass
fill 258 65 265 258 69 265 minecraft:black_stained_glass
fill 258 65 266 258 69 266 minecraft:black_stained_glass
fill 258 65 267 258 69 267 minecraft:black_stained_glass
fill 258 65 268 258 69 268 minecraft:black_stained_glass
fill 258 65 269 258 69 269 minecraft:black_stained_glass
fill 259 65 263 259 69 263 minecraft:black_stained_glass
fill 259 65 269 259 69 269 minecraft:black_stained_glass
fill 260 65 263 260 69 263 minecraft:black_stained_glass
fill 260 65 269 260 69 269 minecraft:black_stained_glass
fill 261 65 263 261 69 263 minecraft:black_stained_glass
fill 261 65 269 261 69 269 minecraft:black_stained_glass
fill 262 65 263 262 69 263 minecraft:black_stained_glass
fill 262 65 269 262 69 269 minecraft:black_stained_glass
fill 263 65 263 263 69 263 minecraft:black_stained_glass
fill 263 65 269 263 69 269 minecraft:black_stained_glass
fill 264 65 263 264 69 263 minecraft:black_stained_glass
fill 264 65 264 264 69 264 minecraft:black_stained_glass
fill 264 65 265 264 69 265 minecraft:black_stained_glass
fill 264 65 266 264 69 266 minecraft:black_stained_glass
fill 264 65 267 264 69 267 minecraft:black_stained_glass
fill 264 65 268 264 69 268 minecraft:black_stained_glass
fill 264 65 269 264 69 269 minecraft:black_stained_glass
setblock 261 65 269 hostilenetworks:data_center[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
