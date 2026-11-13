# 171 exploration/e_compass, e_veins, e_lootr, e_campsite, e_yung_dungeon
#area 103 342 162 367
fill 103 64 342 147 91 367 minecraft:air
fill 148 64 342 162 91 367 minecraft:air
fill 103 60 342 162 62 367 minecraft:stone
fill 103 63 342 162 63 367 minecraft:light_gray_concrete
fill 107 64 348 162 79 348 minecraft:light_gray_concrete
fill 107 64 348 107 79 361 minecraft:light_gray_concrete
setblock 108 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "171.1"}','{"text": "exploration"}','{"text": "e_compass"}','{"text": ""}']}}
setblock 109 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Kompass"}','{"text": "der Natur"}','{"text": ""}','{"text": ""}']}}
fill 117 64 348 117 79 361 minecraft:light_gray_concrete
setblock 112 64 353 minecraft:smooth_stone_slab
summon item_display 112.5 65.4 353.5 {item:{id:"naturescompass:naturescompass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 118 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "171.2"}','{"text": "exploration"}','{"text": "e_veins"}','{"text": ""}']}}
setblock 119 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde eine"}','{"text": "große Erzader"}','{"text": ""}','{"text": ""}']}}
fill 127 64 348 127 79 361 minecraft:light_gray_concrete
fill 120 64 352 124 68 353 minecraft:granite
setblock 120 64 353 minecraft:copper_ore
setblock 121 64 353 minecraft:copper_ore
setblock 121 65 353 minecraft:copper_ore
setblock 122 65 353 minecraft:copper_ore
setblock 123 66 353 minecraft:copper_ore
setblock 124 67 353 minecraft:copper_ore
setblock 124 68 353 minecraft:copper_ore
setblock 120 65 353 minecraft:copper_ore
setblock 123 67 353 minecraft:copper_ore
setblock 122 66 353 minecraft:raw_copper_block
setblock 123 68 353 minecraft:raw_copper_block
setblock 121 66 353 minecraft:raw_copper_block
setblock 128 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "171.3"}','{"text": "exploration"}','{"text": "e_lootr"}','{"text": ""}']}}
setblock 129 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Kisten"}','{"text": "stehen"}','{"text": ""}','{"text": ""}']}}
fill 137 64 348 137 79 361 minecraft:light_gray_concrete
fill 131 64 352 134 64 354 minecraft:mossy_cobblestone
fill 131 65 352 134 66 352 minecraft:mossy_stone_bricks
setblock 134 67 352 minecraft:cracked_stone_bricks
setblock 131 65 353 minecraft:cracked_stone_bricks
setblock 131 66 353 minecraft:mossy_stone_brick_slab
setblock 133 65 353 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 132 65 353 minecraft:lantern
setblock 138 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "171.4"}','{"text": "exploration"}','{"text": "e_campsite"}','{"text": ""}']}}
setblock 139 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde ein"}','{"text": "Höhlenlager"}','{"text": ""}','{"text": ""}']}}
fill 147 64 348 147 79 361 minecraft:light_gray_concrete
fill 140 64 351 144 64 355 minecraft:stone
fill 140 65 351 144 67 351 minecraft:stone
fill 140 65 352 140 67 355 minecraft:stone
fill 141 64 352 144 64 355 minecraft:oak_planks
setblock 142 65 354 minecraft:campfire[facing=south,lit=true]
setblock 141 65 352 minecraft:furnace[facing=south]
setblock 141 66 352 minecraft:cobblestone_wall
setblock 142 65 352 minecraft:crafting_table
setblock 143 65 352 lootr:lootr_chest[facing=south]{LootTable:"artifacts:chests/campsite_chest"}
setblock 144 65 352 minecraft:potted_red_tulip
setblock 144 65 353 minecraft:red_bed[facing=north,part=head]
setblock 144 65 354 minecraft:red_bed[facing=north,part=foot]
setblock 141 65 353 minecraft:lantern
setblock 148 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "171.5"}','{"text": "exploration"}','{"text": "e_yung_dungeon"}','{"text": ""}']}}
setblock 149 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Räum ein"}','{"text": "Verlies aus"}','{"text": ""}','{"text": ""}']}}
fill 157 64 348 157 79 361 minecraft:light_gray_concrete
fill 150 64 351 154 64 355 minecraft:mossy_cobblestone
fill 150 65 351 154 67 351 minecraft:cobblestone
fill 150 65 352 150 67 355 minecraft:mossy_cobblestone
setblock 152 66 351 minecraft:mossy_cobblestone
setblock 153 65 351 minecraft:mossy_cobblestone
setblock 152 65 353 minecraft:spawner{SpawnData:{entity:{id:"minecraft:skeleton"}}}
setblock 151 65 352 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 154 65 352 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 153 65 352 minecraft:skeleton_skull[rotation=2]
setblock 151 65 354 minecraft:cobweb
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
