# 092 undergarden/arrival
#area 53 269 71 294
fill 53 64 269 71 91 294 minecraft:air
fill 53 60 269 71 62 294 minecraft:stone
fill 53 63 269 71 63 294 minecraft:light_gray_concrete
fill 57 64 275 71 79 275 minecraft:light_gray_concrete
fill 57 64 275 57 79 288 minecraft:light_gray_concrete
setblock 58 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 59 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 66 64 275 66 79 288 minecraft:light_gray_concrete
setblock 60 65 280 minecraft:stone_bricks
setblock 60 66 280 minecraft:stone_bricks
setblock 60 67 280 minecraft:stone_bricks
setblock 61 64 280 minecraft:stone_bricks
setblock 61 68 280 minecraft:stone_bricks
setblock 62 64 280 minecraft:stone_bricks
setblock 62 68 280 minecraft:stone_bricks
setblock 63 65 280 minecraft:stone_bricks
setblock 63 66 280 minecraft:stone_bricks
setblock 63 67 280 minecraft:stone_bricks
fill 61 65 280 62 67 280 undergarden:undergarden_portal[axis=x]
execute if block 61 66 280 undergarden:undergarden_portal
