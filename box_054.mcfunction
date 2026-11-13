# 054 list_dimensions/d_mining, d_aether, d_undergarden, d_otherside
#area 52 198 97 223
fill 52 64 198 96 91 223 minecraft:air
fill 97 64 198 97 91 223 minecraft:air
fill 52 60 198 97 62 223 minecraft:stone
fill 52 63 198 97 63 223 minecraft:light_gray_concrete
fill 56 64 204 97 79 204 minecraft:light_gray_concrete
fill 56 64 204 56 79 217 minecraft:light_gray_concrete
setblock 57 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 58 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 65 64 204 65 79 217 minecraft:light_gray_concrete
setblock 59 65 209 kronwerke:grubenrahmen
setblock 59 66 209 kronwerke:grubenrahmen
setblock 59 67 209 kronwerke:grubenrahmen
setblock 60 64 209 kronwerke:grubenrahmen
setblock 60 68 209 kronwerke:grubenrahmen
setblock 61 64 209 kronwerke:grubenrahmen
setblock 61 68 209 kronwerke:grubenrahmen
setblock 62 65 209 kronwerke:grubenrahmen
setblock 62 66 209 kronwerke:grubenrahmen
setblock 62 67 209 kronwerke:grubenrahmen
kw testworld use 60 64 209 up ars_nouveau:source_gem
setblock 66 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054.2"}','{"text": "list_dimensions"}','{"text": "d_aether"}','{"text": ""}']}}
setblock 67 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Aether-Portal"}','{"text": ""}','{"text": ""}']}}
fill 74 64 204 74 79 217 minecraft:light_gray_concrete
setblock 68 65 209 minecraft:glowstone
setblock 68 66 209 minecraft:glowstone
setblock 68 67 209 minecraft:glowstone
setblock 69 64 209 minecraft:glowstone
setblock 69 68 209 minecraft:glowstone
setblock 70 64 209 minecraft:glowstone
setblock 70 68 209 minecraft:glowstone
setblock 71 65 209 minecraft:glowstone
setblock 71 66 209 minecraft:glowstone
setblock 71 67 209 minecraft:glowstone
fill 69 65 209 70 67 209 aether:aether_portal[axis=x]
execute if block 69 66 209 aether:aether_portal
setblock 75 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054.3"}','{"text": "list_dimensions"}','{"text": "d_undergarden"}','{"text": ""}']}}
setblock 76 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne den"}','{"text": "Undergarden"}','{"text": ""}','{"text": ""}']}}
fill 83 64 204 83 79 217 minecraft:light_gray_concrete
setblock 77 65 209 minecraft:stone_bricks
setblock 77 66 209 minecraft:stone_bricks
setblock 77 67 209 minecraft:stone_bricks
setblock 78 64 209 minecraft:stone_bricks
setblock 78 68 209 minecraft:stone_bricks
setblock 79 64 209 minecraft:stone_bricks
setblock 79 68 209 minecraft:stone_bricks
setblock 80 65 209 minecraft:stone_bricks
setblock 80 66 209 minecraft:stone_bricks
setblock 80 67 209 minecraft:stone_bricks
fill 78 65 209 79 67 209 undergarden:undergarden_portal[axis=x]
execute if block 78 66 209 undergarden:undergarden_portal
setblock 84 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054.4"}','{"text": "list_dimensions"}','{"text": "d_otherside"}','{"text": ""}']}}
setblock 85 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne die"}','{"text": "Otherside"}','{"text": ""}','{"text": ""}']}}
fill 92 64 204 92 79 217 minecraft:light_gray_concrete
setblock 86 65 209 minecraft:reinforced_deepslate
setblock 86 66 209 minecraft:reinforced_deepslate
setblock 86 67 209 minecraft:reinforced_deepslate
setblock 87 64 209 minecraft:reinforced_deepslate
setblock 87 68 209 minecraft:reinforced_deepslate
setblock 88 64 209 minecraft:reinforced_deepslate
setblock 88 68 209 minecraft:reinforced_deepslate
setblock 89 65 209 minecraft:reinforced_deepslate
setblock 89 66 209 minecraft:reinforced_deepslate
setblock 89 67 209 minecraft:reinforced_deepslate
fill 87 65 209 88 67 209 deeperdarker:otherside_portal[axis=x]
execute if block 87 66 209 deeperdarker:otherside_portal
