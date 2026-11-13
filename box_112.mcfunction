# 112 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 228 181 387 222
fill 228 64 181 245 106 222 minecraft:air
fill 246 64 181 263 106 222 minecraft:air
fill 264 64 181 281 106 222 minecraft:air
fill 282 64 181 299 106 222 minecraft:air
fill 300 64 181 317 106 222 minecraft:air
fill 318 64 181 335 106 222 minecraft:air
fill 336 64 181 353 106 222 minecraft:air
fill 354 64 181 371 106 222 minecraft:air
fill 372 64 181 387 106 222 minecraft:air
fill 228 60 181 387 62 222 minecraft:stone
fill 228 63 181 387 63 222 minecraft:light_gray_concrete
fill 232 64 187 387 94 187 minecraft:light_gray_concrete
fill 232 64 187 232 94 216 minecraft:light_gray_concrete
setblock 233 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 234 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 242 64 187 242 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 235 64 190 none
kw testworld use 237 65 192 south immersiveengineering:hammer
execute unless block 237 65 192 immersiveengineering:steel_fence
setblock 243 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 244 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 252 64 187 252 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 246 64 190 none
kw testworld use 247 65 190 south immersiveengineering:hammer
execute unless block 247 65 190 minecraft:piston
setblock 253 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 254 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 262 64 187 262 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 256 64 190 none
kw testworld use 257 65 191 south immersiveengineering:hammer
execute unless block 257 65 191 immersiveengineering:wooden_barrel
setblock 263 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 264 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 272 64 187 272 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 266 64 190 none
kw testworld use 267 65 191 south immersiveengineering:hammer
execute unless block 267 65 191 minecraft:cauldron
setblock 273 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 274 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 282 64 187 282 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 276 64 190 none
kw testworld use 277 65 191 south immersiveengineering:hammer
execute unless block 277 65 191 immersiveengineering:sheetmetal_iron
setblock 283 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 284 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 292 64 187 292 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 286 64 190 none
kw testworld use 287 65 191 south immersiveengineering:hammer
execute unless block 287 65 191 immersiveengineering:conveyor_basic
setblock 293 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 294 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 302 64 187 302 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 295 64 190 none
kw testworld use 297 64 194 south immersiveengineering:hammer
execute unless block 297 64 194 minecraft:cauldron
setblock 303 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 304 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 312 64 187 312 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 305 64 190 none
kw testworld use 307 65 192 south immersiveengineering:hammer
execute unless block 307 65 192 immersiveengineering:heavy_engineering
setblock 313 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 314 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 322 64 187 322 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 316 64 190 none
kw testworld use 317 65 194 south immersiveengineering:hammer
execute unless block 317 65 194 immersiveengineering:generator
setblock 323 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 324 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 332 64 187 332 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 325 64 190 none
kw testworld use 327 64 192 south immersiveengineering:hammer
execute unless block 327 64 192 immersiveengineering:sheetmetal_iron
setblock 333 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 334 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 342 64 187 342 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 336 64 190 none
kw testworld use 337 65 192 south immersiveengineering:hammer
execute unless block 337 65 192 immersiveengineering:conveyor_basic
setblock 343 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 344 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 352 64 187 352 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 346 64 190 none
kw testworld use 347 65 192 south immersiveengineering:hammer
execute unless block 347 65 192 immersiveengineering:slab_treated_wood_horizontal
setblock 353 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 354 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 362 64 187 362 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 356 64 190 none
kw testworld use 357 65 195 south immersiveengineering:hammer
execute unless block 357 65 195 immersiveengineering:heavy_engineering
setblock 363 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 364 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 372 64 187 372 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 366 64 190 none
kw testworld use 367 65 192 south immersiveengineering:hammer
execute unless block 367 65 192 immersiveengineering:light_engineering
setblock 373 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 374 64 215 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 382 64 187 382 94 216 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 375 64 190 none
kw testworld use 377 65 195 south immersiveengineering:hammer
execute unless block 377 65 195 immersiveengineering:rs_engineering
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
