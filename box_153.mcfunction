# 153 undergarden/arrival, infuser
#area 73 334 101 359
fill 73 64 334 101 91 359 minecraft:air
fill 73 60 334 101 62 359 minecraft:stone
fill 73 63 334 101 63 359 minecraft:light_gray_concrete
fill 77 64 340 101 79 340 minecraft:light_gray_concrete
fill 77 64 340 77 79 353 minecraft:light_gray_concrete
setblock 78 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 79 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 86 64 340 86 79 353 minecraft:light_gray_concrete
setblock 80 65 345 minecraft:stone_bricks
setblock 80 66 345 minecraft:stone_bricks
setblock 80 67 345 minecraft:stone_bricks
setblock 81 64 345 minecraft:stone_bricks
setblock 81 68 345 minecraft:stone_bricks
setblock 82 64 345 minecraft:stone_bricks
setblock 82 68 345 minecraft:stone_bricks
setblock 83 65 345 minecraft:stone_bricks
setblock 83 66 345 minecraft:stone_bricks
setblock 83 67 345 minecraft:stone_bricks
fill 81 65 345 82 67 345 undergarden:undergarden_portal[axis=x]
execute if block 81 66 345 undergarden:undergarden_portal
setblock 87 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "153.2"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 88 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 96 64 340 96 79 353 minecraft:light_gray_concrete
fill 90 63 344 92 63 346 undergarden:depthrock
setblock 91 64 345 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
