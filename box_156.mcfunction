# 156 list_dimensions/d_mining, r_plates, r_enderio
#area 253 336 291 361
fill 253 64 336 291 91 361 minecraft:air
fill 253 60 336 291 62 361 minecraft:stone
fill 253 63 336 291 63 361 minecraft:light_gray_concrete
fill 257 64 342 291 79 342 minecraft:light_gray_concrete
fill 257 64 342 257 79 355 minecraft:light_gray_concrete
setblock 258 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 259 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 266 64 342 266 79 355 minecraft:light_gray_concrete
setblock 260 65 347 kronwerke:grubenrahmen
setblock 260 66 347 kronwerke:grubenrahmen
setblock 260 67 347 kronwerke:grubenrahmen
setblock 261 64 347 kronwerke:grubenrahmen
setblock 261 68 347 kronwerke:grubenrahmen
setblock 262 64 347 kronwerke:grubenrahmen
setblock 262 68 347 kronwerke:grubenrahmen
setblock 263 65 347 kronwerke:grubenrahmen
setblock 263 66 347 kronwerke:grubenrahmen
setblock 263 67 347 kronwerke:grubenrahmen
kw testworld use 261 64 347 up ars_nouveau:source_gem
setblock 267 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.2"}','{"text": "list_dimensions"}','{"text": "r_plates"}','{"text": ""}']}}
setblock 268 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit"}','{"text": "Warpplatten"}','{"text": ""}']}}
fill 276 64 342 276 79 355 minecraft:light_gray_concrete
setblock 269 64 347 waystones:warp_plate[status=idle]
setblock 273 64 347 waystones:warp_plate[status=idle]
setblock 277 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.3"}','{"text": "list_dimensions"}','{"text": "r_enderio"}','{"text": ""}']}}
setblock 278 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz Reiseanker"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 286 64 342 286 79 355 minecraft:light_gray_concrete
setblock 279 64 348 enderio:travel_anchor
fill 283 64 346 283 66 346 minecraft:stone_bricks
setblock 283 67 346 enderio:travel_anchor
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
