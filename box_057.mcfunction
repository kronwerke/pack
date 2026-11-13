# 057 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 201 158 360 199
fill 201 64 158 218 106 199 minecraft:air
fill 219 64 158 236 106 199 minecraft:air
fill 237 64 158 254 106 199 minecraft:air
fill 255 64 158 272 106 199 minecraft:air
fill 273 64 158 290 106 199 minecraft:air
fill 291 64 158 308 106 199 minecraft:air
fill 309 64 158 326 106 199 minecraft:air
fill 327 64 158 344 106 199 minecraft:air
fill 345 64 158 360 106 199 minecraft:air
fill 201 60 158 360 62 199 minecraft:stone
fill 201 63 158 360 63 199 minecraft:light_gray_concrete
fill 205 64 164 360 94 164 minecraft:light_gray_concrete
fill 205 64 164 205 94 193 minecraft:light_gray_concrete
setblock 206 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 207 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 215 64 164 215 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 208 64 167 none
kw testworld use 210 65 169 south immersiveengineering:hammer
execute unless block 210 65 169 immersiveengineering:steel_fence
setblock 216 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 217 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 225 64 164 225 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 219 64 167 none
kw testworld use 220 65 167 south immersiveengineering:hammer
execute unless block 220 65 167 minecraft:piston
setblock 226 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 227 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 235 64 164 235 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 229 64 167 none
kw testworld use 230 65 168 south immersiveengineering:hammer
execute unless block 230 65 168 immersiveengineering:wooden_barrel
setblock 236 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 237 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 245 64 164 245 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 239 64 167 none
kw testworld use 240 65 168 south immersiveengineering:hammer
execute unless block 240 65 168 minecraft:cauldron
setblock 246 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 247 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 255 64 164 255 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 249 64 167 none
kw testworld use 250 65 168 south immersiveengineering:hammer
execute unless block 250 65 168 immersiveengineering:sheetmetal_iron
setblock 256 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 257 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 265 64 164 265 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 259 64 167 none
kw testworld use 260 65 168 south immersiveengineering:hammer
execute unless block 260 65 168 immersiveengineering:conveyor_basic
setblock 266 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 267 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 275 64 164 275 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 268 64 167 none
kw testworld use 270 64 171 south immersiveengineering:hammer
execute unless block 270 64 171 minecraft:cauldron
setblock 276 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 277 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 285 64 164 285 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 278 64 167 none
kw testworld use 280 65 169 south immersiveengineering:hammer
execute unless block 280 65 169 immersiveengineering:heavy_engineering
setblock 286 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 287 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 295 64 164 295 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 289 64 167 none
kw testworld use 290 65 171 south immersiveengineering:hammer
execute unless block 290 65 171 immersiveengineering:generator
setblock 296 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 297 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 305 64 164 305 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 298 64 167 none
kw testworld use 300 64 169 south immersiveengineering:hammer
execute unless block 300 64 169 immersiveengineering:sheetmetal_iron
setblock 306 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 307 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 315 64 164 315 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 309 64 167 none
kw testworld use 310 65 169 south immersiveengineering:hammer
execute unless block 310 65 169 immersiveengineering:conveyor_basic
setblock 316 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 317 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 325 64 164 325 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 319 64 167 none
kw testworld use 320 65 169 south immersiveengineering:hammer
execute unless block 320 65 169 immersiveengineering:slab_treated_wood_horizontal
setblock 326 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 327 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 335 64 164 335 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 329 64 167 none
kw testworld use 330 65 172 south immersiveengineering:hammer
execute unless block 330 65 172 immersiveengineering:heavy_engineering
setblock 336 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 337 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 345 64 164 345 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 339 64 167 none
kw testworld use 340 65 169 south immersiveengineering:hammer
execute unless block 340 65 169 immersiveengineering:light_engineering
setblock 346 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 347 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 355 64 164 355 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 348 64 167 none
kw testworld use 350 65 172 south immersiveengineering:hammer
execute unless block 350 65 172 immersiveengineering:rs_engineering
