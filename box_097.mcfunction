# 097 undergarden/arrival, infuser
#area 73 277 101 302
fill 73 64 277 101 91 302 minecraft:air
fill 73 60 277 101 62 302 minecraft:stone
fill 73 63 277 101 63 302 minecraft:light_gray_concrete
fill 77 64 283 101 79 283 minecraft:light_gray_concrete
fill 77 64 283 77 79 296 minecraft:light_gray_concrete
setblock 78 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 79 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 86 64 283 86 79 296 minecraft:light_gray_concrete
setblock 80 65 288 minecraft:stone_bricks
setblock 80 66 288 minecraft:stone_bricks
setblock 80 67 288 minecraft:stone_bricks
setblock 81 64 288 minecraft:stone_bricks
setblock 81 68 288 minecraft:stone_bricks
setblock 82 64 288 minecraft:stone_bricks
setblock 82 68 288 minecraft:stone_bricks
setblock 83 65 288 minecraft:stone_bricks
setblock 83 66 288 minecraft:stone_bricks
setblock 83 67 288 minecraft:stone_bricks
fill 81 65 288 82 67 288 undergarden:undergarden_portal[axis=x]
execute if block 81 66 288 undergarden:undergarden_portal
setblock 87 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "097.2"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 88 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 96 64 283 96 79 296 minecraft:light_gray_concrete
fill 90 63 287 92 63 289 undergarden:depthrock
setblock 91 64 288 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
