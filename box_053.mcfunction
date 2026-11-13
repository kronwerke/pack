# 053 undergarden/arrival
#area 38 198 56 223
fill 38 64 198 56 91 223 minecraft:air
fill 38 60 198 56 62 223 minecraft:stone
fill 38 63 198 56 63 223 minecraft:light_gray_concrete
fill 42 64 204 56 79 204 minecraft:light_gray_concrete
fill 42 64 204 42 79 217 minecraft:light_gray_concrete
setblock 43 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "053"}','{"text": "undergarden"}','{"text": "arrival"}','{"text": ""}']}}
setblock 44 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Steig hinunter"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 51 64 204 51 79 217 minecraft:light_gray_concrete
setblock 45 65 209 minecraft:stone_bricks
setblock 45 66 209 minecraft:stone_bricks
setblock 45 67 209 minecraft:stone_bricks
setblock 46 64 209 minecraft:stone_bricks
setblock 46 68 209 minecraft:stone_bricks
setblock 47 64 209 minecraft:stone_bricks
setblock 47 68 209 minecraft:stone_bricks
setblock 48 65 209 minecraft:stone_bricks
setblock 48 66 209 minecraft:stone_bricks
setblock 48 67 209 minecraft:stone_bricks
fill 46 65 209 47 67 209 undergarden:undergarden_portal[axis=x]
execute if block 46 66 209 undergarden:undergarden_portal
