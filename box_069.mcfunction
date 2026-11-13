# 069 undergarden/arrival
#area 38 250 56 275
fill 38 64 250 56 91 275 minecraft:air
fill 38 60 250 56 62 275 minecraft:stone
fill 38 63 250 56 63 275 minecraft:light_gray_concrete
fill 42 64 256 56 79 256 minecraft:light_gray_concrete
fill 42 64 256 42 79 269 minecraft:light_gray_concrete
setblock 43 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 44 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 51 64 256 51 79 269 minecraft:light_gray_concrete
setblock 45 65 261 minecraft:stone_bricks
setblock 45 66 261 minecraft:stone_bricks
setblock 45 67 261 minecraft:stone_bricks
setblock 46 64 261 minecraft:stone_bricks
setblock 46 68 261 minecraft:stone_bricks
setblock 47 64 261 minecraft:stone_bricks
setblock 47 68 261 minecraft:stone_bricks
setblock 48 65 261 minecraft:stone_bricks
setblock 48 66 261 minecraft:stone_bricks
setblock 48 67 261 minecraft:stone_bricks
fill 46 65 261 47 67 261 undergarden:undergarden_portal[axis=x]
execute if block 46 66 261 undergarden:undergarden_portal
