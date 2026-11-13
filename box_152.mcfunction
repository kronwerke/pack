# 152 undergarden/arrival, infuser
#area 73 330 101 355
fill 73 64 330 101 91 355 minecraft:air
fill 73 60 330 101 62 355 minecraft:stone
fill 73 63 330 101 63 355 minecraft:light_gray_concrete
fill 77 64 336 101 79 336 minecraft:light_gray_concrete
fill 77 64 336 77 79 349 minecraft:light_gray_concrete
setblock 78 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 79 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 86 64 336 86 79 349 minecraft:light_gray_concrete
setblock 80 65 341 minecraft:stone_bricks
setblock 80 66 341 minecraft:stone_bricks
setblock 80 67 341 minecraft:stone_bricks
setblock 81 64 341 minecraft:stone_bricks
setblock 81 68 341 minecraft:stone_bricks
setblock 82 64 341 minecraft:stone_bricks
setblock 82 68 341 minecraft:stone_bricks
setblock 83 65 341 minecraft:stone_bricks
setblock 83 66 341 minecraft:stone_bricks
setblock 83 67 341 minecraft:stone_bricks
fill 81 65 341 82 67 341 undergarden:undergarden_portal[axis=x]
execute if block 81 66 341 undergarden:undergarden_portal
setblock 87 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.2"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 88 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 96 64 336 96 79 349 minecraft:light_gray_concrete
fill 90 63 340 92 63 342 undergarden:depthrock
setblock 91 64 341 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
