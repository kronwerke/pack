# 074 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 215 158 374 199
fill 215 64 158 232 106 199 minecraft:air
fill 233 64 158 250 106 199 minecraft:air
fill 251 64 158 268 106 199 minecraft:air
fill 269 64 158 286 106 199 minecraft:air
fill 287 64 158 304 106 199 minecraft:air
fill 305 64 158 322 106 199 minecraft:air
fill 323 64 158 340 106 199 minecraft:air
fill 341 64 158 358 106 199 minecraft:air
fill 359 64 158 374 106 199 minecraft:air
fill 215 60 158 374 62 199 minecraft:stone
fill 215 63 158 374 63 199 minecraft:light_gray_concrete
fill 219 64 164 374 94 164 minecraft:light_gray_concrete
fill 219 64 164 219 94 193 minecraft:light_gray_concrete
setblock 220 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 221 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 229 64 164 229 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 222 64 167 none
kw testworld use 224 65 169 south immersiveengineering:hammer
execute unless block 224 65 169 immersiveengineering:steel_fence
setblock 230 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 231 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 239 64 164 239 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 233 64 167 none
kw testworld use 234 65 167 south immersiveengineering:hammer
execute unless block 234 65 167 minecraft:piston
setblock 240 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 241 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 249 64 164 249 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 243 64 167 none
kw testworld use 244 65 168 south immersiveengineering:hammer
execute unless block 244 65 168 immersiveengineering:wooden_barrel
setblock 250 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 251 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 259 64 164 259 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 253 64 167 none
kw testworld use 254 65 168 south immersiveengineering:hammer
execute unless block 254 65 168 minecraft:cauldron
setblock 260 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 261 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 269 64 164 269 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 263 64 167 none
kw testworld use 264 65 168 south immersiveengineering:hammer
execute unless block 264 65 168 immersiveengineering:sheetmetal_iron
setblock 270 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 271 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 279 64 164 279 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 273 64 167 none
kw testworld use 274 65 168 south immersiveengineering:hammer
execute unless block 274 65 168 immersiveengineering:conveyor_basic
setblock 280 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 281 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 289 64 164 289 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 282 64 167 none
kw testworld use 284 64 171 south immersiveengineering:hammer
execute unless block 284 64 171 minecraft:cauldron
setblock 290 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 291 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 299 64 164 299 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 292 64 167 none
kw testworld use 294 65 169 south immersiveengineering:hammer
execute unless block 294 65 169 immersiveengineering:heavy_engineering
setblock 300 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 301 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 309 64 164 309 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 303 64 167 none
kw testworld use 304 65 171 south immersiveengineering:hammer
execute unless block 304 65 171 immersiveengineering:generator
setblock 310 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 311 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 319 64 164 319 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 312 64 167 none
kw testworld use 314 64 169 south immersiveengineering:hammer
execute unless block 314 64 169 immersiveengineering:sheetmetal_iron
setblock 320 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 321 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 329 64 164 329 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 323 64 167 none
kw testworld use 324 65 169 south immersiveengineering:hammer
execute unless block 324 65 169 immersiveengineering:conveyor_basic
setblock 330 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 331 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 339 64 164 339 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 333 64 167 none
kw testworld use 334 65 169 south immersiveengineering:hammer
execute unless block 334 65 169 immersiveengineering:slab_treated_wood_horizontal
setblock 340 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 341 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 349 64 164 349 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 343 64 167 none
kw testworld use 344 65 172 south immersiveengineering:hammer
execute unless block 344 65 172 immersiveengineering:heavy_engineering
setblock 350 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 351 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 359 64 164 359 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 353 64 167 none
kw testworld use 354 65 169 south immersiveengineering:hammer
execute unless block 354 65 169 immersiveengineering:light_engineering
setblock 360 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 361 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 369 64 164 369 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 362 64 167 none
kw testworld use 364 65 172 south immersiveengineering:hammer
execute unless block 364 65 172 immersiveengineering:rs_engineering
