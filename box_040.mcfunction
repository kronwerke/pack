# 040 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 76 144 235 185
fill 76 64 144 93 106 185 minecraft:air
fill 94 64 144 111 106 185 minecraft:air
fill 112 64 144 129 106 185 minecraft:air
fill 130 64 144 147 106 185 minecraft:air
fill 148 64 144 165 106 185 minecraft:air
fill 166 64 144 183 106 185 minecraft:air
fill 184 64 144 201 106 185 minecraft:air
fill 202 64 144 219 106 185 minecraft:air
fill 220 64 144 235 106 185 minecraft:air
fill 76 60 144 235 62 185 minecraft:stone
fill 76 63 144 235 63 185 minecraft:light_gray_concrete
fill 80 64 150 235 94 150 minecraft:light_gray_concrete
fill 80 64 150 80 94 179 minecraft:light_gray_concrete
setblock 81 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 82 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 90 64 150 90 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 83 64 153 none
kw testworld use 85 65 155 south immersiveengineering:hammer
execute unless block 85 65 155 immersiveengineering:steel_fence
setblock 91 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 92 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 100 64 150 100 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 94 64 153 none
kw testworld use 95 65 153 south immersiveengineering:hammer
execute unless block 95 65 153 minecraft:piston
setblock 101 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 102 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 110 64 150 110 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 104 64 153 none
kw testworld use 105 65 154 south immersiveengineering:hammer
execute unless block 105 65 154 immersiveengineering:wooden_barrel
setblock 111 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 112 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 120 64 150 120 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 114 64 153 none
kw testworld use 115 65 154 south immersiveengineering:hammer
execute unless block 115 65 154 minecraft:cauldron
setblock 121 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 122 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 130 64 150 130 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 124 64 153 none
kw testworld use 125 65 154 south immersiveengineering:hammer
execute unless block 125 65 154 immersiveengineering:sheetmetal_iron
setblock 131 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 132 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 140 64 150 140 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 134 64 153 none
kw testworld use 135 65 154 south immersiveengineering:hammer
execute unless block 135 65 154 immersiveengineering:conveyor_basic
setblock 141 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 142 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 150 64 150 150 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 143 64 153 none
kw testworld use 145 64 157 south immersiveengineering:hammer
execute unless block 145 64 157 minecraft:cauldron
setblock 151 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 152 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 160 64 150 160 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 153 64 153 none
kw testworld use 155 65 155 south immersiveengineering:hammer
execute unless block 155 65 155 immersiveengineering:heavy_engineering
setblock 161 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 162 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 170 64 150 170 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 164 64 153 none
kw testworld use 165 65 157 south immersiveengineering:hammer
execute unless block 165 65 157 immersiveengineering:generator
setblock 171 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 172 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 180 64 150 180 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 173 64 153 none
kw testworld use 175 64 155 south immersiveengineering:hammer
execute unless block 175 64 155 immersiveengineering:sheetmetal_iron
setblock 181 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 182 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 190 64 150 190 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 184 64 153 none
kw testworld use 185 65 155 south immersiveengineering:hammer
execute unless block 185 65 155 immersiveengineering:conveyor_basic
setblock 191 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 192 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 200 64 150 200 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 194 64 153 none
kw testworld use 195 65 155 south immersiveengineering:hammer
execute unless block 195 65 155 immersiveengineering:slab_treated_wood_horizontal
setblock 201 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 202 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 210 64 150 210 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 204 64 153 none
kw testworld use 205 65 158 south immersiveengineering:hammer
execute unless block 205 65 158 immersiveengineering:heavy_engineering
setblock 211 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 212 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 220 64 150 220 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 214 64 153 none
kw testworld use 215 65 155 south immersiveengineering:hammer
execute unless block 215 65 155 immersiveengineering:light_engineering
setblock 221 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "040.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 222 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 230 64 150 230 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 223 64 153 none
kw testworld use 225 65 158 south immersiveengineering:hammer
execute unless block 225 65 158 immersiveengineering:rs_engineering
