# 094 undergarden/arrival
#area 53 271 71 296
fill 53 64 271 71 91 296 minecraft:air
fill 53 60 271 71 62 296 minecraft:stone
fill 53 63 271 71 63 296 minecraft:light_gray_concrete
fill 57 64 277 71 79 277 minecraft:light_gray_concrete
fill 57 64 277 57 79 290 minecraft:light_gray_concrete
setblock 58 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "094"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 59 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 66 64 277 66 79 290 minecraft:light_gray_concrete
setblock 60 65 282 minecraft:stone_bricks
setblock 60 66 282 minecraft:stone_bricks
setblock 60 67 282 minecraft:stone_bricks
setblock 61 64 282 minecraft:stone_bricks
setblock 61 68 282 minecraft:stone_bricks
setblock 62 64 282 minecraft:stone_bricks
setblock 62 68 282 minecraft:stone_bricks
setblock 63 65 282 minecraft:stone_bricks
setblock 63 66 282 minecraft:stone_bricks
setblock 63 67 282 minecraft:stone_bricks
fill 61 65 282 62 67 282 undergarden:undergarden_portal[axis=x]
execute if block 61 66 282 undergarden:undergarden_portal
