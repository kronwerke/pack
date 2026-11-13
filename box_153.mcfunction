# 153 undergarden/arrival, infuser
#area 73 336 101 361
fill 73 64 336 101 91 361 minecraft:air
fill 73 60 336 101 62 361 minecraft:stone
fill 73 63 336 101 63 361 minecraft:light_gray_concrete
fill 77 64 342 101 79 342 minecraft:light_gray_concrete
fill 77 64 342 77 79 355 minecraft:light_gray_concrete
setblock 78 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 79 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 86 64 342 86 79 355 minecraft:light_gray_concrete
setblock 80 65 347 minecraft:stone_bricks
setblock 80 66 347 minecraft:stone_bricks
setblock 80 67 347 minecraft:stone_bricks
setblock 81 64 347 minecraft:stone_bricks
setblock 81 68 347 minecraft:stone_bricks
setblock 82 64 347 minecraft:stone_bricks
setblock 82 68 347 minecraft:stone_bricks
setblock 83 65 347 minecraft:stone_bricks
setblock 83 66 347 minecraft:stone_bricks
setblock 83 67 347 minecraft:stone_bricks
fill 81 65 347 82 67 347 undergarden:undergarden_portal[axis=x]
execute if block 81 66 347 undergarden:undergarden_portal
setblock 87 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.2"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 88 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 96 64 342 96 79 355 minecraft:light_gray_concrete
fill 90 63 346 92 63 348 undergarden:depthrock
setblock 91 64 347 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
