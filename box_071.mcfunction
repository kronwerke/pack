# 071 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 213 158 372 199
fill 213 64 158 230 106 199 minecraft:air
fill 231 64 158 248 106 199 minecraft:air
fill 249 64 158 266 106 199 minecraft:air
fill 267 64 158 284 106 199 minecraft:air
fill 285 64 158 302 106 199 minecraft:air
fill 303 64 158 320 106 199 minecraft:air
fill 321 64 158 338 106 199 minecraft:air
fill 339 64 158 356 106 199 minecraft:air
fill 357 64 158 372 106 199 minecraft:air
fill 213 60 158 372 62 199 minecraft:stone
fill 213 63 158 372 63 199 minecraft:light_gray_concrete
fill 217 64 164 372 94 164 minecraft:light_gray_concrete
fill 217 64 164 217 94 193 minecraft:light_gray_concrete
setblock 218 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 219 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 227 64 164 227 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 220 64 167 none
kw testworld use 222 65 169 south immersiveengineering:hammer
execute unless block 222 65 169 immersiveengineering:steel_fence
setblock 228 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 229 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 237 64 164 237 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 231 64 167 none
kw testworld use 232 65 167 south immersiveengineering:hammer
execute unless block 232 65 167 minecraft:piston
setblock 238 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 239 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 247 64 164 247 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 241 64 167 none
kw testworld use 242 65 168 south immersiveengineering:hammer
execute unless block 242 65 168 immersiveengineering:wooden_barrel
setblock 248 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 249 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 257 64 164 257 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 251 64 167 none
kw testworld use 252 65 168 south immersiveengineering:hammer
execute unless block 252 65 168 minecraft:cauldron
setblock 258 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 259 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 267 64 164 267 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 261 64 167 none
kw testworld use 262 65 168 south immersiveengineering:hammer
execute unless block 262 65 168 immersiveengineering:sheetmetal_iron
setblock 268 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 269 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 277 64 164 277 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 271 64 167 none
kw testworld use 272 65 168 south immersiveengineering:hammer
execute unless block 272 65 168 immersiveengineering:conveyor_basic
setblock 278 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 279 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 287 64 164 287 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 280 64 167 none
kw testworld use 282 64 171 south immersiveengineering:hammer
execute unless block 282 64 171 minecraft:cauldron
setblock 288 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 289 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 297 64 164 297 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 290 64 167 none
kw testworld use 292 65 169 south immersiveengineering:hammer
execute unless block 292 65 169 immersiveengineering:heavy_engineering
setblock 298 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 299 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 307 64 164 307 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 301 64 167 none
kw testworld use 302 65 171 south immersiveengineering:hammer
execute unless block 302 65 171 immersiveengineering:generator
setblock 308 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 309 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 317 64 164 317 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 310 64 167 none
kw testworld use 312 64 169 south immersiveengineering:hammer
execute unless block 312 64 169 immersiveengineering:sheetmetal_iron
setblock 318 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 319 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 327 64 164 327 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 321 64 167 none
kw testworld use 322 65 169 south immersiveengineering:hammer
execute unless block 322 65 169 immersiveengineering:conveyor_basic
setblock 328 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 329 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 337 64 164 337 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 331 64 167 none
kw testworld use 332 65 169 south immersiveengineering:hammer
execute unless block 332 65 169 immersiveengineering:slab_treated_wood_horizontal
setblock 338 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 339 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 347 64 164 347 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 341 64 167 none
kw testworld use 342 65 172 south immersiveengineering:hammer
execute unless block 342 65 172 immersiveengineering:heavy_engineering
setblock 348 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 349 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 357 64 164 357 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 351 64 167 none
kw testworld use 352 65 169 south immersiveengineering:hammer
execute unless block 352 65 169 immersiveengineering:light_engineering
setblock 358 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 359 64 192 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 367 64 164 367 94 193 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 360 64 167 none
kw testworld use 362 65 172 south immersiveengineering:hammer
execute unless block 362 65 172 immersiveengineering:rs_engineering
