# 076 undergarden/arrival
#area 53 250 71 275
fill 53 64 250 71 91 275 minecraft:air
fill 53 60 250 71 62 275 minecraft:stone
fill 53 63 250 71 63 275 minecraft:light_gray_concrete
fill 57 64 256 71 79 256 minecraft:light_gray_concrete
fill 57 64 256 57 79 269 minecraft:light_gray_concrete
setblock 58 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 59 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 66 64 256 66 79 269 minecraft:light_gray_concrete
setblock 60 65 261 minecraft:stone_bricks
setblock 60 66 261 minecraft:stone_bricks
setblock 60 67 261 minecraft:stone_bricks
setblock 61 64 261 minecraft:stone_bricks
setblock 61 68 261 minecraft:stone_bricks
setblock 62 64 261 minecraft:stone_bricks
setblock 62 68 261 minecraft:stone_bricks
setblock 63 65 261 minecraft:stone_bricks
setblock 63 66 261 minecraft:stone_bricks
setblock 63 67 261 minecraft:stone_bricks
fill 61 65 261 62 67 261 undergarden:undergarden_portal[axis=x]
execute if block 61 66 261 undergarden:undergarden_portal
