# 151 exploration/e_compass, e_veins, e_lootr, e_campsite, e_yung_dungeon
#area 103 336 162 361
fill 103 64 336 147 91 361 minecraft:air
fill 148 64 336 162 91 361 minecraft:air
fill 103 60 336 162 62 361 minecraft:stone
fill 103 63 336 162 63 361 minecraft:light_gray_concrete
fill 107 64 342 162 79 342 minecraft:light_gray_concrete
fill 107 64 342 107 79 355 minecraft:light_gray_concrete
setblock 108 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.1"}','{"text": "exploration"}','{"text": "e_compass"}','{"text": ""}']}}
setblock 109 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Kompass"}','{"text": "der Natur"}','{"text": ""}','{"text": ""}']}}
fill 117 64 342 117 79 355 minecraft:light_gray_concrete
setblock 112 64 347 minecraft:smooth_stone_slab
summon item_display 112.5 65.4 347.5 {item:{id:"naturescompass:naturescompass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 118 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.2"}','{"text": "exploration"}','{"text": "e_veins"}','{"text": ""}']}}
setblock 119 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde eine"}','{"text": "große Erzader"}','{"text": ""}','{"text": ""}']}}
fill 127 64 342 127 79 355 minecraft:light_gray_concrete
fill 120 64 346 124 68 347 minecraft:granite
setblock 120 64 347 minecraft:copper_ore
setblock 121 64 347 minecraft:copper_ore
setblock 121 65 347 minecraft:copper_ore
setblock 122 65 347 minecraft:copper_ore
setblock 123 66 347 minecraft:copper_ore
setblock 124 67 347 minecraft:copper_ore
setblock 124 68 347 minecraft:copper_ore
setblock 120 65 347 minecraft:copper_ore
setblock 123 67 347 minecraft:copper_ore
setblock 122 66 347 minecraft:raw_copper_block
setblock 123 68 347 minecraft:raw_copper_block
setblock 121 66 347 minecraft:raw_copper_block
setblock 128 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.3"}','{"text": "exploration"}','{"text": "e_lootr"}','{"text": ""}']}}
setblock 129 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Kisten"}','{"text": "stehen"}','{"text": ""}','{"text": ""}']}}
fill 137 64 342 137 79 355 minecraft:light_gray_concrete
fill 131 64 346 134 64 348 minecraft:mossy_cobblestone
fill 131 65 346 134 66 346 minecraft:mossy_stone_bricks
setblock 134 67 346 minecraft:cracked_stone_bricks
setblock 131 65 347 minecraft:cracked_stone_bricks
setblock 131 66 347 minecraft:mossy_stone_brick_slab
setblock 133 65 347 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 132 65 347 minecraft:lantern
setblock 138 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.4"}','{"text": "exploration"}','{"text": "e_campsite"}','{"text": ""}']}}
setblock 139 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde ein"}','{"text": "Höhlenlager"}','{"text": ""}','{"text": ""}']}}
fill 147 64 342 147 79 355 minecraft:light_gray_concrete
fill 140 64 345 144 64 349 minecraft:stone
fill 140 65 345 144 67 345 minecraft:stone
fill 140 65 346 140 67 349 minecraft:stone
fill 141 64 346 144 64 349 minecraft:oak_planks
setblock 142 65 348 minecraft:campfire[facing=south,lit=true]
setblock 141 65 346 minecraft:furnace[facing=south]
setblock 141 66 346 minecraft:cobblestone_wall
setblock 142 65 346 minecraft:crafting_table
setblock 143 65 346 lootr:lootr_chest[facing=south]{LootTable:"artifacts:chests/campsite_chest"}
setblock 144 65 346 minecraft:potted_red_tulip
setblock 144 65 347 minecraft:red_bed[facing=north,part=head]
setblock 144 65 348 minecraft:red_bed[facing=north,part=foot]
setblock 141 65 347 minecraft:lantern
setblock 148 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.5"}','{"text": "exploration"}','{"text": "e_yung_dungeon"}','{"text": ""}']}}
setblock 149 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Räum ein"}','{"text": "Verlies aus"}','{"text": ""}','{"text": ""}']}}
fill 157 64 342 157 79 355 minecraft:light_gray_concrete
fill 150 64 345 154 64 349 minecraft:mossy_cobblestone
fill 150 65 345 154 67 345 minecraft:cobblestone
fill 150 65 346 150 67 349 minecraft:mossy_cobblestone
setblock 152 66 345 minecraft:mossy_cobblestone
setblock 153 65 345 minecraft:mossy_cobblestone
setblock 152 65 347 minecraft:spawner{SpawnData:{entity:{id:"minecraft:skeleton"}}}
setblock 151 65 346 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 154 65 346 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 153 65 346 minecraft:skeleton_skull[rotation=2]
setblock 151 65 348 minecraft:cobweb
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
