# 125 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 228 211 387 252
fill 228 64 211 245 106 252 minecraft:air
fill 246 64 211 263 106 252 minecraft:air
fill 264 64 211 281 106 252 minecraft:air
fill 282 64 211 299 106 252 minecraft:air
fill 300 64 211 317 106 252 minecraft:air
fill 318 64 211 335 106 252 minecraft:air
fill 336 64 211 353 106 252 minecraft:air
fill 354 64 211 371 106 252 minecraft:air
fill 372 64 211 387 106 252 minecraft:air
fill 228 60 211 387 62 252 minecraft:stone
fill 228 63 211 387 63 252 minecraft:light_gray_concrete
fill 232 64 217 387 94 217 minecraft:light_gray_concrete
fill 232 64 217 232 94 246 minecraft:light_gray_concrete
setblock 233 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 234 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 242 64 217 242 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 235 64 220 none
kw testworld use 237 65 222 south immersiveengineering:hammer
execute unless block 237 65 222 immersiveengineering:steel_fence
setblock 243 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 244 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 252 64 217 252 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 246 64 220 none
kw testworld use 247 65 220 south immersiveengineering:hammer
execute unless block 247 65 220 minecraft:piston
setblock 253 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 254 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 262 64 217 262 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 256 64 220 none
kw testworld use 257 65 221 south immersiveengineering:hammer
execute unless block 257 65 221 immersiveengineering:wooden_barrel
setblock 263 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 264 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 272 64 217 272 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 266 64 220 none
kw testworld use 267 65 221 south immersiveengineering:hammer
execute unless block 267 65 221 minecraft:cauldron
setblock 273 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 274 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 282 64 217 282 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 276 64 220 none
kw testworld use 277 65 221 south immersiveengineering:hammer
execute unless block 277 65 221 immersiveengineering:sheetmetal_iron
setblock 283 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 284 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 292 64 217 292 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 286 64 220 none
kw testworld use 287 65 221 south immersiveengineering:hammer
execute unless block 287 65 221 immersiveengineering:conveyor_basic
setblock 293 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 294 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 302 64 217 302 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 295 64 220 none
kw testworld use 297 64 224 south immersiveengineering:hammer
execute unless block 297 64 224 minecraft:cauldron
setblock 303 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 304 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 312 64 217 312 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 305 64 220 none
kw testworld use 307 65 222 south immersiveengineering:hammer
execute unless block 307 65 222 immersiveengineering:heavy_engineering
setblock 313 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 314 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 322 64 217 322 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 316 64 220 none
kw testworld use 317 65 224 south immersiveengineering:hammer
execute unless block 317 65 224 immersiveengineering:generator
setblock 323 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 324 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 332 64 217 332 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 325 64 220 none
kw testworld use 327 64 222 south immersiveengineering:hammer
execute unless block 327 64 222 immersiveengineering:sheetmetal_iron
setblock 333 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 334 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 342 64 217 342 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 336 64 220 none
kw testworld use 337 65 222 south immersiveengineering:hammer
execute unless block 337 65 222 immersiveengineering:conveyor_basic
setblock 343 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 344 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 352 64 217 352 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 346 64 220 none
kw testworld use 347 65 222 south immersiveengineering:hammer
execute unless block 347 65 222 immersiveengineering:slab_treated_wood_horizontal
setblock 353 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 354 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 362 64 217 362 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 356 64 220 none
kw testworld use 357 65 225 south immersiveengineering:hammer
execute unless block 357 65 225 immersiveengineering:heavy_engineering
setblock 363 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 364 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 372 64 217 372 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 366 64 220 none
kw testworld use 367 65 222 south immersiveengineering:hammer
execute unless block 367 65 222 immersiveengineering:light_engineering
setblock 373 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 374 64 245 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 382 64 217 382 94 246 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 375 64 220 none
kw testworld use 377 65 225 south immersiveengineering:hammer
execute unless block 377 65 225 immersiveengineering:rs_engineering
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
