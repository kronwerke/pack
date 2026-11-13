# 095 list_dimensions/d_mining, d_aether, d_undergarden, d_otherside, r_mekanism
#area 67 271 122 296
fill 67 64 271 111 91 296 minecraft:air
fill 112 64 271 122 91 296 minecraft:air
fill 67 60 271 122 62 296 minecraft:stone
fill 67 63 271 122 63 296 minecraft:light_gray_concrete
fill 71 64 277 122 79 277 minecraft:light_gray_concrete
fill 71 64 277 71 79 290 minecraft:light_gray_concrete
setblock 72 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095.1"}','{"text": "list_dimensions"}','{"text": "d_mining"}','{"text": ""}']}}
setblock 73 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Die Farmwelt"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 80 64 277 80 79 290 minecraft:light_gray_concrete
setblock 74 65 282 kronwerke:grubenrahmen
setblock 74 66 282 kronwerke:grubenrahmen
setblock 74 67 282 kronwerke:grubenrahmen
setblock 75 64 282 kronwerke:grubenrahmen
setblock 75 68 282 kronwerke:grubenrahmen
setblock 76 64 282 kronwerke:grubenrahmen
setblock 76 68 282 kronwerke:grubenrahmen
setblock 77 65 282 kronwerke:grubenrahmen
setblock 77 66 282 kronwerke:grubenrahmen
setblock 77 67 282 kronwerke:grubenrahmen
kw testworld use 75 64 282 up ars_nouveau:source_gem
setblock 81 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095.2"}','{"text": "list_dimensions"}','{"text": "d_aether"}','{"text": ""}']}}
setblock 82 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Aether-Portal"}','{"text": ""}','{"text": ""}']}}
fill 89 64 277 89 79 290 minecraft:light_gray_concrete
setblock 83 65 282 minecraft:glowstone
setblock 83 66 282 minecraft:glowstone
setblock 83 67 282 minecraft:glowstone
setblock 84 64 282 minecraft:glowstone
setblock 84 68 282 minecraft:glowstone
setblock 85 64 282 minecraft:glowstone
setblock 85 68 282 minecraft:glowstone
setblock 86 65 282 minecraft:glowstone
setblock 86 66 282 minecraft:glowstone
setblock 86 67 282 minecraft:glowstone
fill 84 65 282 85 67 282 aether:aether_portal[axis=x]
execute if block 84 66 282 aether:aether_portal
setblock 90 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095.3"}','{"text": "list_dimensions"}','{"text": "d_undergarden"}','{"text": ""}']}}
setblock 91 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne den"}','{"text": "Undergarden"}','{"text": ""}','{"text": ""}']}}
fill 98 64 277 98 79 290 minecraft:light_gray_concrete
setblock 92 65 282 minecraft:stone_bricks
setblock 92 66 282 minecraft:stone_bricks
setblock 92 67 282 minecraft:stone_bricks
setblock 93 64 282 minecraft:stone_bricks
setblock 93 68 282 minecraft:stone_bricks
setblock 94 64 282 minecraft:stone_bricks
setblock 94 68 282 minecraft:stone_bricks
setblock 95 65 282 minecraft:stone_bricks
setblock 95 66 282 minecraft:stone_bricks
setblock 95 67 282 minecraft:stone_bricks
fill 93 65 282 94 67 282 undergarden:undergarden_portal[axis=x]
execute if block 93 66 282 undergarden:undergarden_portal
setblock 99 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095.4"}','{"text": "list_dimensions"}','{"text": "d_otherside"}','{"text": ""}']}}
setblock 100 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Öffne die"}','{"text": "Otherside"}','{"text": ""}','{"text": ""}']}}
fill 107 64 277 107 79 290 minecraft:light_gray_concrete
setblock 101 65 282 minecraft:reinforced_deepslate
setblock 101 66 282 minecraft:reinforced_deepslate
setblock 101 67 282 minecraft:reinforced_deepslate
setblock 102 64 282 minecraft:reinforced_deepslate
setblock 102 68 282 minecraft:reinforced_deepslate
setblock 103 64 282 minecraft:reinforced_deepslate
setblock 103 68 282 minecraft:reinforced_deepslate
setblock 104 65 282 minecraft:reinforced_deepslate
setblock 104 66 282 minecraft:reinforced_deepslate
setblock 104 67 282 minecraft:reinforced_deepslate
fill 102 65 282 103 67 282 deeperdarker:otherside_portal[axis=x]
execute if block 102 66 282 deeperdarker:otherside_portal
setblock 108 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095.5"}','{"text": "list_dimensions"}','{"text": "r_mekanism"}','{"text": ""}']}}
setblock 109 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Teleporter"}','{"text": ""}','{"text": ""}']}}
fill 117 64 277 117 79 290 minecraft:light_gray_concrete
setblock 112 64 282 mekanism:teleporter
setblock 111 64 282 mekanism:teleporter_frame
setblock 113 64 282 mekanism:teleporter_frame
setblock 111 65 282 mekanism:teleporter_frame
setblock 113 65 282 mekanism:teleporter_frame
setblock 111 66 282 mekanism:teleporter_frame
setblock 113 66 282 mekanism:teleporter_frame
setblock 111 67 282 mekanism:teleporter_frame
setblock 113 67 282 mekanism:teleporter_frame
setblock 112 67 282 mekanism:teleporter_frame
