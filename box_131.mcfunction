# 131 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower, resonanz
#area -4 240 165 281
fill -4 64 240 13 106 281 minecraft:air
fill 14 64 240 31 106 281 minecraft:air
fill 32 64 240 49 106 281 minecraft:air
fill 50 64 240 67 106 281 minecraft:air
fill 68 64 240 85 106 281 minecraft:air
fill 86 64 240 103 106 281 minecraft:air
fill 104 64 240 121 106 281 minecraft:air
fill 122 64 240 139 106 281 minecraft:air
fill 140 64 240 157 106 281 minecraft:air
fill 158 64 240 165 106 281 minecraft:air
fill -4 60 240 165 62 281 minecraft:stone
fill -4 63 240 165 63 281 minecraft:light_gray_concrete
fill 0 64 246 165 94 246 minecraft:light_gray_concrete
fill 0 64 246 0 94 275 minecraft:light_gray_concrete
setblock 1 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 2 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 246 10 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 3 64 249 none
kw testworld use 5 65 251 south immersiveengineering:hammer
execute unless block 5 65 251 immersiveengineering:steel_fence
setblock 11 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 12 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 20 64 246 20 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 14 64 249 none
kw testworld use 15 65 249 south immersiveengineering:hammer
execute unless block 15 65 249 minecraft:piston
setblock 21 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 22 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 30 64 246 30 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 24 64 249 none
kw testworld use 25 65 250 south immersiveengineering:hammer
execute unless block 25 65 250 immersiveengineering:wooden_barrel
setblock 31 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 32 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 40 64 246 40 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 34 64 249 none
kw testworld use 35 65 250 south immersiveengineering:hammer
execute unless block 35 65 250 minecraft:cauldron
setblock 41 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 42 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 50 64 246 50 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 44 64 249 none
kw testworld use 45 65 250 south immersiveengineering:hammer
execute unless block 45 65 250 immersiveengineering:sheetmetal_iron
setblock 51 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 52 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 60 64 246 60 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 54 64 249 none
kw testworld use 55 65 250 south immersiveengineering:hammer
execute unless block 55 65 250 immersiveengineering:conveyor_basic
setblock 61 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 62 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 70 64 246 70 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 63 64 249 none
kw testworld use 65 64 253 south immersiveengineering:hammer
execute unless block 65 64 253 minecraft:cauldron
setblock 71 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 72 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 80 64 246 80 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 73 64 249 none
kw testworld use 75 65 251 south immersiveengineering:hammer
execute unless block 75 65 251 immersiveengineering:heavy_engineering
setblock 81 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 82 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 90 64 246 90 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 84 64 249 none
kw testworld use 85 65 253 south immersiveengineering:hammer
execute unless block 85 65 253 immersiveengineering:generator
setblock 91 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 92 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 100 64 246 100 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 93 64 249 none
kw testworld use 95 64 251 south immersiveengineering:hammer
execute unless block 95 64 251 immersiveengineering:sheetmetal_iron
setblock 101 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 102 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 110 64 246 110 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 104 64 249 none
kw testworld use 105 65 251 south immersiveengineering:hammer
execute unless block 105 65 251 immersiveengineering:conveyor_basic
setblock 111 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 112 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 120 64 246 120 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 114 64 249 none
kw testworld use 115 65 251 south immersiveengineering:hammer
execute unless block 115 65 251 immersiveengineering:slab_treated_wood_horizontal
setblock 121 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 122 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 130 64 246 130 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 124 64 249 none
kw testworld use 125 65 254 south immersiveengineering:hammer
execute unless block 125 65 254 immersiveengineering:heavy_engineering
setblock 131 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 132 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 140 64 246 140 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 134 64 249 none
kw testworld use 135 65 251 south immersiveengineering:hammer
execute unless block 135 65 251 immersiveengineering:light_engineering
setblock 141 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 142 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 150 64 246 150 94 275 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 143 64 249 none
kw testworld use 145 65 254 south immersiveengineering:hammer
execute unless block 145 65 254 immersiveengineering:rs_engineering
setblock 151 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.16"}','{"text": "immersive_heavy"}','{"text": "resonanz"}','{"text": ""}']}}
setblock 152 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Resonanz-Beobachter"}','{"text": ""}','{"text": ""}']}}
fill 160 64 246 160 94 275 minecraft:light_gray_concrete
setblock 155 64 251 minecraft:smooth_stone_slab
summon item_display 155.5 65.4 251.5 {item:{id:"immersiveengineering:resonanz_engineering",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.0f,2.0f,2.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
