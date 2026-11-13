# 139 undergarden/arrival, infuser
#area 73 300 101 325
fill 73 64 300 101 91 325 minecraft:air
fill 73 60 300 101 62 325 minecraft:stone
fill 73 63 300 101 63 325 minecraft:light_gray_concrete
fill 77 64 306 101 79 306 minecraft:light_gray_concrete
fill 77 64 306 77 79 319 minecraft:light_gray_concrete
setblock 78 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 79 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 86 64 306 86 79 319 minecraft:light_gray_concrete
setblock 80 65 311 minecraft:stone_bricks
setblock 80 66 311 minecraft:stone_bricks
setblock 80 67 311 minecraft:stone_bricks
setblock 81 64 311 minecraft:stone_bricks
setblock 81 68 311 minecraft:stone_bricks
setblock 82 64 311 minecraft:stone_bricks
setblock 82 68 311 minecraft:stone_bricks
setblock 83 65 311 minecraft:stone_bricks
setblock 83 66 311 minecraft:stone_bricks
setblock 83 67 311 minecraft:stone_bricks
fill 81 65 311 82 67 311 undergarden:undergarden_portal[axis=x]
execute if block 81 66 311 undergarden:undergarden_portal
setblock 87 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139.2"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 88 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 96 64 306 96 79 319 minecraft:light_gray_concrete
fill 90 63 310 92 63 312 undergarden:depthrock
setblock 91 64 311 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
