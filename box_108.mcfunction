# 108 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 228 179 387 220
fill 228 64 179 245 106 220 minecraft:air
fill 246 64 179 263 106 220 minecraft:air
fill 264 64 179 281 106 220 minecraft:air
fill 282 64 179 299 106 220 minecraft:air
fill 300 64 179 317 106 220 minecraft:air
fill 318 64 179 335 106 220 minecraft:air
fill 336 64 179 353 106 220 minecraft:air
fill 354 64 179 371 106 220 minecraft:air
fill 372 64 179 387 106 220 minecraft:air
fill 228 60 179 387 62 220 minecraft:stone
fill 228 63 179 387 63 220 minecraft:light_gray_concrete
fill 232 64 185 387 94 185 minecraft:light_gray_concrete
fill 232 64 185 232 94 214 minecraft:light_gray_concrete
setblock 233 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 234 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 242 64 185 242 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 235 64 188 none
kw testworld use 237 65 190 south immersiveengineering:hammer
execute unless block 237 65 190 immersiveengineering:steel_fence
setblock 243 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 244 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 252 64 185 252 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 246 64 188 none
kw testworld use 247 65 188 south immersiveengineering:hammer
execute unless block 247 65 188 minecraft:piston
setblock 253 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 254 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 262 64 185 262 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 256 64 188 none
kw testworld use 257 65 189 south immersiveengineering:hammer
execute unless block 257 65 189 immersiveengineering:wooden_barrel
setblock 263 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 264 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 272 64 185 272 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 266 64 188 none
kw testworld use 267 65 189 south immersiveengineering:hammer
execute unless block 267 65 189 minecraft:cauldron
setblock 273 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 274 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 282 64 185 282 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 276 64 188 none
kw testworld use 277 65 189 south immersiveengineering:hammer
execute unless block 277 65 189 immersiveengineering:sheetmetal_iron
setblock 283 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 284 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 292 64 185 292 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 286 64 188 none
kw testworld use 287 65 189 south immersiveengineering:hammer
execute unless block 287 65 189 immersiveengineering:conveyor_basic
setblock 293 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 294 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 302 64 185 302 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 295 64 188 none
kw testworld use 297 64 192 south immersiveengineering:hammer
execute unless block 297 64 192 minecraft:cauldron
setblock 303 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 304 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 312 64 185 312 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 305 64 188 none
kw testworld use 307 65 190 south immersiveengineering:hammer
execute unless block 307 65 190 immersiveengineering:heavy_engineering
setblock 313 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 314 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 322 64 185 322 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 316 64 188 none
kw testworld use 317 65 192 south immersiveengineering:hammer
execute unless block 317 65 192 immersiveengineering:generator
setblock 323 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 324 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 332 64 185 332 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 325 64 188 none
kw testworld use 327 64 190 south immersiveengineering:hammer
execute unless block 327 64 190 immersiveengineering:sheetmetal_iron
setblock 333 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 334 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 342 64 185 342 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 336 64 188 none
kw testworld use 337 65 190 south immersiveengineering:hammer
execute unless block 337 65 190 immersiveengineering:conveyor_basic
setblock 343 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 344 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 352 64 185 352 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 346 64 188 none
kw testworld use 347 65 190 south immersiveengineering:hammer
execute unless block 347 65 190 immersiveengineering:slab_treated_wood_horizontal
setblock 353 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 354 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 362 64 185 362 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 356 64 188 none
kw testworld use 357 65 193 south immersiveengineering:hammer
execute unless block 357 65 193 immersiveengineering:heavy_engineering
setblock 363 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 364 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 372 64 185 372 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 366 64 188 none
kw testworld use 367 65 190 south immersiveengineering:hammer
execute unless block 367 65 190 immersiveengineering:light_engineering
setblock 373 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 374 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 382 64 185 382 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 375 64 188 none
kw testworld use 377 65 193 south immersiveengineering:hammer
execute unless block 377 65 193 immersiveengineering:rs_engineering
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
