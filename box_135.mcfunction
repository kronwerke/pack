# 135 undergarden/arrival, infuser
#area 73 298 101 323
fill 73 64 298 101 91 323 minecraft:air
fill 73 60 298 101 62 323 minecraft:stone
fill 73 63 298 101 63 323 minecraft:light_gray_concrete
fill 77 64 304 101 79 304 minecraft:light_gray_concrete
fill 77 64 304 77 79 317 minecraft:light_gray_concrete
setblock 78 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 79 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 86 64 304 86 79 317 minecraft:light_gray_concrete
setblock 80 65 309 minecraft:stone_bricks
setblock 80 66 309 minecraft:stone_bricks
setblock 80 67 309 minecraft:stone_bricks
setblock 81 64 309 minecraft:stone_bricks
setblock 81 68 309 minecraft:stone_bricks
setblock 82 64 309 minecraft:stone_bricks
setblock 82 68 309 minecraft:stone_bricks
setblock 83 65 309 minecraft:stone_bricks
setblock 83 66 309 minecraft:stone_bricks
setblock 83 67 309 minecraft:stone_bricks
fill 81 65 309 82 67 309 undergarden:undergarden_portal[axis=x]
execute if block 81 66 309 undergarden:undergarden_portal
setblock 87 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.2"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 88 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 96 64 304 96 79 317 minecraft:light_gray_concrete
fill 90 63 308 92 63 310 undergarden:depthrock
setblock 91 64 309 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
