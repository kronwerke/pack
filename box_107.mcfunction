# 107 undergarden/arrival, infuser
#area 73 296 101 321
fill 73 64 296 101 91 321 minecraft:air
fill 73 60 296 101 62 321 minecraft:stone
fill 73 63 296 101 63 321 minecraft:light_gray_concrete
fill 77 64 302 101 79 302 minecraft:light_gray_concrete
fill 77 64 302 77 79 315 minecraft:light_gray_concrete
setblock 78 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.1"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 79 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 86 64 302 86 79 315 minecraft:light_gray_concrete
setblock 80 65 307 minecraft:stone_bricks
setblock 80 66 307 minecraft:stone_bricks
setblock 80 67 307 minecraft:stone_bricks
setblock 81 64 307 minecraft:stone_bricks
setblock 81 68 307 minecraft:stone_bricks
setblock 82 64 307 minecraft:stone_bricks
setblock 82 68 307 minecraft:stone_bricks
setblock 83 65 307 minecraft:stone_bricks
setblock 83 66 307 minecraft:stone_bricks
setblock 83 67 307 minecraft:stone_bricks
fill 81 65 307 82 67 307 undergarden:undergarden_portal[axis=x]
execute if block 81 66 307 undergarden:undergarden_portal
setblock 87 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.2"}','{"text": "undergarden"}','{"text": "infuser"}','{"text": ""}']}}
setblock 88 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Infusionstisch"}','{"text": ""}','{"text": ""}']}}
fill 96 64 302 96 79 315 minecraft:light_gray_concrete
fill 90 63 306 92 63 308 undergarden:depthrock
setblock 91 64 307 undergarden:infuser[state=infusing_utherium]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
