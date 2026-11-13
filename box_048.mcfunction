# 048 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 101 144 260 185
fill 101 64 144 118 106 185 minecraft:air
fill 119 64 144 136 106 185 minecraft:air
fill 137 64 144 154 106 185 minecraft:air
fill 155 64 144 172 106 185 minecraft:air
fill 173 64 144 190 106 185 minecraft:air
fill 191 64 144 208 106 185 minecraft:air
fill 209 64 144 226 106 185 minecraft:air
fill 227 64 144 244 106 185 minecraft:air
fill 245 64 144 260 106 185 minecraft:air
fill 101 60 144 260 62 185 minecraft:stone
fill 101 63 144 260 63 185 minecraft:light_gray_concrete
fill 105 64 150 260 94 150 minecraft:light_gray_concrete
fill 105 64 150 105 94 179 minecraft:light_gray_concrete
setblock 106 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 107 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 115 64 150 115 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 108 64 153 none
kw testworld use 110 65 155 south immersiveengineering:hammer
execute unless block 110 65 155 immersiveengineering:steel_fence
setblock 116 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 117 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 125 64 150 125 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 119 64 153 none
kw testworld use 120 65 153 south immersiveengineering:hammer
execute unless block 120 65 153 minecraft:piston
setblock 126 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 127 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 135 64 150 135 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 129 64 153 none
kw testworld use 130 65 154 south immersiveengineering:hammer
execute unless block 130 65 154 immersiveengineering:wooden_barrel
setblock 136 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 137 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 145 64 150 145 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 139 64 153 none
kw testworld use 140 65 154 south immersiveengineering:hammer
execute unless block 140 65 154 minecraft:cauldron
setblock 146 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 147 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 155 64 150 155 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 149 64 153 none
kw testworld use 150 65 154 south immersiveengineering:hammer
execute unless block 150 65 154 immersiveengineering:sheetmetal_iron
setblock 156 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 157 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 165 64 150 165 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 159 64 153 none
kw testworld use 160 65 154 south immersiveengineering:hammer
execute unless block 160 65 154 immersiveengineering:conveyor_basic
setblock 166 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 167 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 175 64 150 175 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 168 64 153 none
kw testworld use 170 64 157 south immersiveengineering:hammer
execute unless block 170 64 157 minecraft:cauldron
setblock 176 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 177 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 185 64 150 185 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 178 64 153 none
kw testworld use 180 65 155 south immersiveengineering:hammer
execute unless block 180 65 155 immersiveengineering:heavy_engineering
setblock 186 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 187 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 195 64 150 195 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 189 64 153 none
kw testworld use 190 65 157 south immersiveengineering:hammer
execute unless block 190 65 157 immersiveengineering:generator
setblock 196 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 197 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 205 64 150 205 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 198 64 153 none
kw testworld use 200 64 155 south immersiveengineering:hammer
execute unless block 200 64 155 immersiveengineering:sheetmetal_iron
setblock 206 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 207 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 215 64 150 215 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 209 64 153 none
kw testworld use 210 65 155 south immersiveengineering:hammer
execute unless block 210 65 155 immersiveengineering:conveyor_basic
setblock 216 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 217 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 225 64 150 225 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 219 64 153 none
kw testworld use 220 65 155 south immersiveengineering:hammer
execute unless block 220 65 155 immersiveengineering:slab_treated_wood_horizontal
setblock 226 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 227 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 235 64 150 235 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 229 64 153 none
kw testworld use 230 65 158 south immersiveengineering:hammer
execute unless block 230 65 158 immersiveengineering:heavy_engineering
setblock 236 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 237 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 245 64 150 245 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 239 64 153 none
kw testworld use 240 65 155 south immersiveengineering:hammer
execute unless block 240 65 155 immersiveengineering:light_engineering
setblock 246 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 247 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 255 64 150 255 94 179 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 248 64 153 none
kw testworld use 250 65 158 south immersiveengineering:hammer
execute unless block 250 65 158 immersiveengineering:rs_engineering
