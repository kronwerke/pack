# 156 exploration/e_compass, e_veins, e_lootr, e_campsite, e_yung_dungeon
#area 103 340 162 365
fill 103 64 340 147 91 365 minecraft:air
fill 148 64 340 162 91 365 minecraft:air
fill 103 60 340 162 62 365 minecraft:stone
fill 103 63 340 162 63 365 minecraft:light_gray_concrete
fill 107 64 346 162 79 346 minecraft:light_gray_concrete
fill 107 64 346 107 79 359 minecraft:light_gray_concrete
setblock 108 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.1"}','{"text": "exploration"}','{"text": "e_compass"}','{"text": ""}']}}
setblock 109 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Kompass"}','{"text": "der Natur"}','{"text": ""}','{"text": ""}']}}
fill 117 64 346 117 79 359 minecraft:light_gray_concrete
setblock 112 64 351 minecraft:smooth_stone_slab
summon item_display 112.5 65.4 351.5 {item:{id:"naturescompass:naturescompass",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 118 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.2"}','{"text": "exploration"}','{"text": "e_veins"}','{"text": ""}']}}
setblock 119 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde eine"}','{"text": "große Erzader"}','{"text": ""}','{"text": ""}']}}
fill 127 64 346 127 79 359 minecraft:light_gray_concrete
fill 120 64 350 124 68 351 minecraft:granite
setblock 120 64 351 minecraft:copper_ore
setblock 121 64 351 minecraft:copper_ore
setblock 121 65 351 minecraft:copper_ore
setblock 122 65 351 minecraft:copper_ore
setblock 123 66 351 minecraft:copper_ore
setblock 124 67 351 minecraft:copper_ore
setblock 124 68 351 minecraft:copper_ore
setblock 120 65 351 minecraft:copper_ore
setblock 123 67 351 minecraft:copper_ore
setblock 122 66 351 minecraft:raw_copper_block
setblock 123 68 351 minecraft:raw_copper_block
setblock 121 66 351 minecraft:raw_copper_block
setblock 128 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.3"}','{"text": "exploration"}','{"text": "e_lootr"}','{"text": ""}']}}
setblock 129 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Kisten"}','{"text": "stehen"}','{"text": ""}','{"text": ""}']}}
fill 137 64 346 137 79 359 minecraft:light_gray_concrete
fill 131 64 350 134 64 352 minecraft:mossy_cobblestone
fill 131 65 350 134 66 350 minecraft:mossy_stone_bricks
setblock 134 67 350 minecraft:cracked_stone_bricks
setblock 131 65 351 minecraft:cracked_stone_bricks
setblock 131 66 351 minecraft:mossy_stone_brick_slab
setblock 133 65 351 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 132 65 351 minecraft:lantern
setblock 138 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.4"}','{"text": "exploration"}','{"text": "e_campsite"}','{"text": ""}']}}
setblock 139 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Finde ein"}','{"text": "Höhlenlager"}','{"text": ""}','{"text": ""}']}}
fill 147 64 346 147 79 359 minecraft:light_gray_concrete
fill 140 64 349 144 64 353 minecraft:stone
fill 140 65 349 144 67 349 minecraft:stone
fill 140 65 350 140 67 353 minecraft:stone
fill 141 64 350 144 64 353 minecraft:oak_planks
setblock 142 65 352 minecraft:campfire[facing=south,lit=true]
setblock 141 65 350 minecraft:furnace[facing=south]
setblock 141 66 350 minecraft:cobblestone_wall
setblock 142 65 350 minecraft:crafting_table
setblock 143 65 350 lootr:lootr_chest[facing=south]{LootTable:"artifacts:chests/campsite_chest"}
setblock 144 65 350 minecraft:potted_red_tulip
setblock 144 65 351 minecraft:red_bed[facing=north,part=head]
setblock 144 65 352 minecraft:red_bed[facing=north,part=foot]
setblock 141 65 351 minecraft:lantern
setblock 148 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.5"}','{"text": "exploration"}','{"text": "e_yung_dungeon"}','{"text": ""}']}}
setblock 149 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Räum ein"}','{"text": "Verlies aus"}','{"text": ""}','{"text": ""}']}}
fill 157 64 346 157 79 359 minecraft:light_gray_concrete
fill 150 64 349 154 64 353 minecraft:mossy_cobblestone
fill 150 65 349 154 67 349 minecraft:cobblestone
fill 150 65 350 150 67 353 minecraft:mossy_cobblestone
setblock 152 66 349 minecraft:mossy_cobblestone
setblock 153 65 349 minecraft:mossy_cobblestone
setblock 152 65 351 minecraft:spawner{SpawnData:{entity:{id:"minecraft:skeleton"}}}
setblock 151 65 350 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 154 65 350 lootr:lootr_chest[facing=south]{LootTable:"minecraft:chests/simple_dungeon"}
setblock 153 65 350 minecraft:skeleton_skull[rotation=2]
setblock 151 65 352 minecraft:cobweb
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
