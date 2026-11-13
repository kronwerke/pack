# 098 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 218 179 377 220
fill 218 64 179 235 106 220 minecraft:air
fill 236 64 179 253 106 220 minecraft:air
fill 254 64 179 271 106 220 minecraft:air
fill 272 64 179 289 106 220 minecraft:air
fill 290 64 179 307 106 220 minecraft:air
fill 308 64 179 325 106 220 minecraft:air
fill 326 64 179 343 106 220 minecraft:air
fill 344 64 179 361 106 220 minecraft:air
fill 362 64 179 377 106 220 minecraft:air
fill 218 60 179 377 62 220 minecraft:stone
fill 218 63 179 377 63 220 minecraft:light_gray_concrete
fill 222 64 185 377 94 185 minecraft:light_gray_concrete
fill 222 64 185 222 94 214 minecraft:light_gray_concrete
setblock 223 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 224 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 232 64 185 232 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 225 64 188 none
kw testworld use 227 65 190 south immersiveengineering:hammer
execute unless block 227 65 190 immersiveengineering:steel_fence
setblock 233 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 234 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 242 64 185 242 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 236 64 188 none
kw testworld use 237 65 188 south immersiveengineering:hammer
execute unless block 237 65 188 minecraft:piston
setblock 243 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 244 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 252 64 185 252 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 246 64 188 none
kw testworld use 247 65 189 south immersiveengineering:hammer
execute unless block 247 65 189 immersiveengineering:wooden_barrel
setblock 253 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 254 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 262 64 185 262 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 256 64 188 none
kw testworld use 257 65 189 south immersiveengineering:hammer
execute unless block 257 65 189 minecraft:cauldron
setblock 263 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 264 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 272 64 185 272 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 266 64 188 none
kw testworld use 267 65 189 south immersiveengineering:hammer
execute unless block 267 65 189 immersiveengineering:sheetmetal_iron
setblock 273 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 274 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 282 64 185 282 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 276 64 188 none
kw testworld use 277 65 189 south immersiveengineering:hammer
execute unless block 277 65 189 immersiveengineering:conveyor_basic
setblock 283 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 284 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 292 64 185 292 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 285 64 188 none
kw testworld use 287 64 192 south immersiveengineering:hammer
execute unless block 287 64 192 minecraft:cauldron
setblock 293 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 294 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 302 64 185 302 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 295 64 188 none
kw testworld use 297 65 190 south immersiveengineering:hammer
execute unless block 297 65 190 immersiveengineering:heavy_engineering
setblock 303 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 304 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 312 64 185 312 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 306 64 188 none
kw testworld use 307 65 192 south immersiveengineering:hammer
execute unless block 307 65 192 immersiveengineering:generator
setblock 313 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 314 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 322 64 185 322 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 315 64 188 none
kw testworld use 317 64 190 south immersiveengineering:hammer
execute unless block 317 64 190 immersiveengineering:sheetmetal_iron
setblock 323 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 324 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 332 64 185 332 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 326 64 188 none
kw testworld use 327 65 190 south immersiveengineering:hammer
execute unless block 327 65 190 immersiveengineering:conveyor_basic
setblock 333 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 334 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 342 64 185 342 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 336 64 188 none
kw testworld use 337 65 190 south immersiveengineering:hammer
execute unless block 337 65 190 immersiveengineering:slab_treated_wood_horizontal
setblock 343 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 344 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 352 64 185 352 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 346 64 188 none
kw testworld use 347 65 193 south immersiveengineering:hammer
execute unless block 347 65 193 immersiveengineering:heavy_engineering
setblock 353 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 354 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 362 64 185 362 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 356 64 188 none
kw testworld use 357 65 190 south immersiveengineering:hammer
execute unless block 357 65 190 immersiveengineering:light_engineering
setblock 363 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 364 64 213 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 372 64 185 372 94 214 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 365 64 188 none
kw testworld use 367 65 193 south immersiveengineering:hammer
execute unless block 367 65 193 immersiveengineering:rs_engineering
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
