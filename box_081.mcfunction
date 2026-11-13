# 081 list_dimensions/d_mining, d_aether, d_undergarden, d_otherside
#area 67 250 112 275
fill 67 64 250 111 91 275 minecraft:air
fill 112 64 250 112 91 275 minecraft:air
fill 67 60 250 112 62 275 minecraft:stone
fill 67 63 250 112 63 275 minecraft:light_gray_concrete
fill 71 64 256 112 79 256 minecraft:light_gray_concrete
fill 71 64 256 71 79 269 minecraft:light_gray_concrete
setblock 72 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 73 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 80 64 256 80 79 269 minecraft:light_gray_concrete
setblock 74 65 261 kronwerke:grubenrahmen
setblock 74 66 261 kronwerke:grubenrahmen
setblock 74 67 261 kronwerke:grubenrahmen
setblock 75 64 261 kronwerke:grubenrahmen
setblock 75 68 261 kronwerke:grubenrahmen
setblock 76 64 261 kronwerke:grubenrahmen
setblock 76 68 261 kronwerke:grubenrahmen
setblock 77 65 261 kronwerke:grubenrahmen
setblock 77 66 261 kronwerke:grubenrahmen
setblock 77 67 261 kronwerke:grubenrahmen
kw testworld use 75 64 261 up ars_nouveau:source_gem
setblock 81 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.2"}','{"text": "list_dimensions"}','{"text": "d_aether"}','{"text": ""}']}}
setblock 82 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Aether-Portal"}','{"text": ""}','{"text": ""}']}}
fill 89 64 256 89 79 269 minecraft:light_gray_concrete
setblock 83 65 261 minecraft:glowstone
setblock 83 66 261 minecraft:glowstone
setblock 83 67 261 minecraft:glowstone
setblock 84 64 261 minecraft:glowstone
setblock 84 68 261 minecraft:glowstone
setblock 85 64 261 minecraft:glowstone
setblock 85 68 261 minecraft:glowstone
setblock 86 65 261 minecraft:glowstone
setblock 86 66 261 minecraft:glowstone
setblock 86 67 261 minecraft:glowstone
fill 84 65 261 85 67 261 aether:aether_portal[axis=x]
execute if block 84 66 261 aether:aether_portal
setblock 90 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.3"}','{"text": "list_dimensions"}','{"text": "d_undergarden"}','{"text": ""}']}}
setblock 91 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne den"}','{"text": "Undergarden"}','{"text": ""}','{"text": ""}']}}
fill 98 64 256 98 79 269 minecraft:light_gray_concrete
setblock 92 65 261 minecraft:stone_bricks
setblock 92 66 261 minecraft:stone_bricks
setblock 92 67 261 minecraft:stone_bricks
setblock 93 64 261 minecraft:stone_bricks
setblock 93 68 261 minecraft:stone_bricks
setblock 94 64 261 minecraft:stone_bricks
setblock 94 68 261 minecraft:stone_bricks
setblock 95 65 261 minecraft:stone_bricks
setblock 95 66 261 minecraft:stone_bricks
setblock 95 67 261 minecraft:stone_bricks
fill 93 65 261 94 67 261 undergarden:undergarden_portal[axis=x]
execute if block 93 66 261 undergarden:undergarden_portal
setblock 99 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081.4"}','{"text": "list_dimensions"}','{"text": "d_otherside"}','{"text": ""}']}}
setblock 100 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne die"}','{"text": "Otherside"}','{"text": ""}','{"text": ""}']}}
fill 107 64 256 107 79 269 minecraft:light_gray_concrete
setblock 101 65 261 minecraft:reinforced_deepslate
setblock 101 66 261 minecraft:reinforced_deepslate
setblock 101 67 261 minecraft:reinforced_deepslate
setblock 102 64 261 minecraft:reinforced_deepslate
setblock 102 68 261 minecraft:reinforced_deepslate
setblock 103 64 261 minecraft:reinforced_deepslate
setblock 103 68 261 minecraft:reinforced_deepslate
setblock 104 65 261 minecraft:reinforced_deepslate
setblock 104 66 261 minecraft:reinforced_deepslate
setblock 104 67 261 minecraft:reinforced_deepslate
fill 102 65 261 103 67 261 deeperdarker:otherside_portal[axis=x]
execute if block 102 66 261 deeperdarker:otherside_portal
