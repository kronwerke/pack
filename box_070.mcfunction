# 070 list_dimensions/d_mining, d_aether, d_undergarden, d_otherside
#area 52 250 97 275
fill 52 64 250 96 91 275 minecraft:air
fill 97 64 250 97 91 275 minecraft:air
fill 52 60 250 97 62 275 minecraft:stone
fill 52 63 250 97 63 275 minecraft:light_gray_concrete
fill 56 64 256 97 79 256 minecraft:light_gray_concrete
fill 56 64 256 56 79 269 minecraft:light_gray_concrete
setblock 57 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 58 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 65 64 256 65 79 269 minecraft:light_gray_concrete
setblock 59 65 261 kronwerke:grubenrahmen
setblock 59 66 261 kronwerke:grubenrahmen
setblock 59 67 261 kronwerke:grubenrahmen
setblock 60 64 261 kronwerke:grubenrahmen
setblock 60 68 261 kronwerke:grubenrahmen
setblock 61 64 261 kronwerke:grubenrahmen
setblock 61 68 261 kronwerke:grubenrahmen
setblock 62 65 261 kronwerke:grubenrahmen
setblock 62 66 261 kronwerke:grubenrahmen
setblock 62 67 261 kronwerke:grubenrahmen
kw testworld use 60 64 261 up ars_nouveau:source_gem
setblock 66 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.2"}','{"text": "list_dimensions"}','{"text": "d_aether"}','{"text": ""}']}}
setblock 67 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Aether-Portal"}','{"text": ""}','{"text": ""}']}}
fill 74 64 256 74 79 269 minecraft:light_gray_concrete
setblock 68 65 261 minecraft:glowstone
setblock 68 66 261 minecraft:glowstone
setblock 68 67 261 minecraft:glowstone
setblock 69 64 261 minecraft:glowstone
setblock 69 68 261 minecraft:glowstone
setblock 70 64 261 minecraft:glowstone
setblock 70 68 261 minecraft:glowstone
setblock 71 65 261 minecraft:glowstone
setblock 71 66 261 minecraft:glowstone
setblock 71 67 261 minecraft:glowstone
fill 69 65 261 70 67 261 aether:aether_portal[axis=x]
execute if block 69 66 261 aether:aether_portal
setblock 75 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.3"}','{"text": "list_dimensions"}','{"text": "d_undergarden"}','{"text": ""}']}}
setblock 76 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne den"}','{"text": "Undergarden"}','{"text": ""}','{"text": ""}']}}
fill 83 64 256 83 79 269 minecraft:light_gray_concrete
setblock 77 65 261 minecraft:stone_bricks
setblock 77 66 261 minecraft:stone_bricks
setblock 77 67 261 minecraft:stone_bricks
setblock 78 64 261 minecraft:stone_bricks
setblock 78 68 261 minecraft:stone_bricks
setblock 79 64 261 minecraft:stone_bricks
setblock 79 68 261 minecraft:stone_bricks
setblock 80 65 261 minecraft:stone_bricks
setblock 80 66 261 minecraft:stone_bricks
setblock 80 67 261 minecraft:stone_bricks
fill 78 65 261 79 67 261 undergarden:undergarden_portal[axis=x]
execute if block 78 66 261 undergarden:undergarden_portal
setblock 84 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "070.4"}','{"text": "list_dimensions"}','{"text": "d_otherside"}','{"text": ""}']}}
setblock 85 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne die"}','{"text": "Otherside"}','{"text": ""}','{"text": ""}']}}
fill 92 64 256 92 79 269 minecraft:light_gray_concrete
setblock 86 65 261 minecraft:reinforced_deepslate
setblock 86 66 261 minecraft:reinforced_deepslate
setblock 86 67 261 minecraft:reinforced_deepslate
setblock 87 64 261 minecraft:reinforced_deepslate
setblock 87 68 261 minecraft:reinforced_deepslate
setblock 88 64 261 minecraft:reinforced_deepslate
setblock 88 68 261 minecraft:reinforced_deepslate
setblock 89 65 261 minecraft:reinforced_deepslate
setblock 89 66 261 minecraft:reinforced_deepslate
setblock 89 67 261 minecraft:reinforced_deepslate
fill 87 65 261 88 67 261 deeperdarker:otherside_portal[axis=x]
execute if block 87 66 261 deeperdarker:otherside_portal
