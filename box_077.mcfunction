# 077 immersive_heavy/crusher, press, squeezer, fermenter, mixer, bottling, arc, refinery, diesel, sawmill, assembler, auto_workbench, excavator, lightning_rod, radio_tower
#area 215 177 374 218
fill 215 64 177 232 106 218 minecraft:air
fill 233 64 177 250 106 218 minecraft:air
fill 251 64 177 268 106 218 minecraft:air
fill 269 64 177 286 106 218 minecraft:air
fill 287 64 177 304 106 218 minecraft:air
fill 305 64 177 322 106 218 minecraft:air
fill 323 64 177 340 106 218 minecraft:air
fill 341 64 177 358 106 218 minecraft:air
fill 359 64 177 374 106 218 minecraft:air
fill 215 60 177 374 62 218 minecraft:stone
fill 215 63 177 374 63 218 minecraft:light_gray_concrete
fill 219 64 183 374 94 183 minecraft:light_gray_concrete
fill 219 64 183 219 94 212 minecraft:light_gray_concrete
setblock 220 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.1"}','{"text": "immersive_heavy"}','{"text": "crusher"}','{"text": ""}']}}
setblock 221 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "each formed"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 229 64 183 229 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/crusher 222 64 186 none
kw testworld use 224 65 188 south immersiveengineering:hammer
execute unless block 224 65 188 immersiveengineering:steel_fence
setblock 230 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.2"}','{"text": "immersive_heavy"}','{"text": "press"}','{"text": ""}']}}
setblock 231 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Metallpresse"}','{"text": ""}','{"text": ""}']}}
fill 239 64 183 239 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/metal_press 233 64 186 none
kw testworld use 234 65 186 south immersiveengineering:hammer
execute unless block 234 65 186 minecraft:piston
setblock 240 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.3"}','{"text": "immersive_heavy"}','{"text": "squeezer"}','{"text": ""}']}}
setblock 241 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Industriepresse"}','{"text": ""}','{"text": ""}']}}
fill 249 64 183 249 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/squeezer 243 64 186 none
kw testworld use 244 65 187 south immersiveengineering:hammer
execute unless block 244 65 187 immersiveengineering:wooden_barrel
setblock 250 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.4"}','{"text": "immersive_heavy"}','{"text": "fermenter"}','{"text": ""}']}}
setblock 251 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Industriefermenter"}','{"text": ""}','{"text": ""}']}}
fill 259 64 183 259 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/fermenter 253 64 186 none
kw testworld use 254 65 187 south immersiveengineering:hammer
execute unless block 254 65 187 minecraft:cauldron
setblock 260 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.5"}','{"text": "immersive_heavy"}','{"text": "mixer"}','{"text": ""}']}}
setblock 261 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Mischer"}','{"text": ""}','{"text": ""}']}}
fill 269 64 183 269 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/mixer 263 64 186 none
kw testworld use 264 65 187 south immersiveengineering:hammer
execute unless block 264 65 187 immersiveengineering:sheetmetal_iron
setblock 270 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.6"}','{"text": "immersive_heavy"}','{"text": "bottling"}','{"text": ""}']}}
setblock 271 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Abfüllanlage"}','{"text": ""}','{"text": ""}']}}
fill 279 64 183 279 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/bottling_machine 273 64 186 none
kw testworld use 274 65 187 south immersiveengineering:hammer
execute unless block 274 65 187 immersiveengineering:conveyor_basic
setblock 280 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.7"}','{"text": "immersive_heavy"}','{"text": "arc"}','{"text": ""}']}}
setblock 281 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Lichtbogenofen"}','{"text": ""}','{"text": ""}']}}
fill 289 64 183 289 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/arcfurnace 282 64 186 none
kw testworld use 284 64 190 south immersiveengineering:hammer
execute unless block 284 64 190 minecraft:cauldron
setblock 290 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.8"}','{"text": "immersive_heavy"}','{"text": "refinery"}','{"text": ""}']}}
setblock 291 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form eine"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 299 64 183 299 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/refinery 292 64 186 none
kw testworld use 294 65 188 south immersiveengineering:hammer
execute unless block 294 65 188 immersiveengineering:heavy_engineering
setblock 300 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.9"}','{"text": "immersive_heavy"}','{"text": "diesel"}','{"text": ""}']}}
setblock 301 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Dieselgenerator"}','{"text": ""}','{"text": ""}']}}
fill 309 64 183 309 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/diesel_generator 303 64 186 none
kw testworld use 304 65 190 south immersiveengineering:hammer
execute unless block 304 65 190 immersiveengineering:generator
setblock 310 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.10"}','{"text": "immersive_heavy"}','{"text": "sawmill"}','{"text": ""}']}}
setblock 311 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form ein"}','{"text": "Sägewerk"}','{"text": ""}','{"text": ""}']}}
fill 319 64 183 319 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/sawmill 312 64 186 none
kw testworld use 314 64 188 south immersiveengineering:hammer
execute unless block 314 64 188 immersiveengineering:sheetmetal_iron
setblock 320 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.11"}','{"text": "immersive_heavy"}','{"text": "assembler"}','{"text": ""}']}}
setblock 321 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Monteur"}','{"text": ""}','{"text": ""}']}}
fill 329 64 183 329 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/assembler 323 64 186 none
kw testworld use 324 65 188 south immersiveengineering:hammer
execute unless block 324 65 188 immersiveengineering:conveyor_basic
setblock 330 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.12"}','{"text": "immersive_heavy"}','{"text": "auto_workbench"}','{"text": ""}']}}
setblock 331 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Automatisierten"}','{"text": "Arbeitstisch"}','{"text": ""}']}}
fill 339 64 183 339 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/auto_workbench 333 64 186 none
kw testworld use 334 65 188 south immersiveengineering:hammer
execute unless block 334 65 188 immersiveengineering:slab_treated_wood_horizontal
setblock 340 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.13"}','{"text": "immersive_heavy"}','{"text": "excavator"}','{"text": ""}']}}
setblock 341 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Bagger"}','{"text": ""}','{"text": ""}']}}
fill 349 64 183 349 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/excavator 343 64 186 none
kw testworld use 344 65 191 south immersiveengineering:hammer
execute unless block 344 65 191 immersiveengineering:heavy_engineering
setblock 350 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.14"}','{"text": "immersive_heavy"}','{"text": "lightning_rod"}','{"text": ""}']}}
setblock 351 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Blitzableiter"}','{"text": ""}','{"text": ""}']}}
fill 359 64 183 359 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/lightning_rod 353 64 186 none
kw testworld use 354 65 188 south immersiveengineering:hammer
execute unless block 354 65 188 immersiveengineering:light_engineering
setblock 360 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "077.15"}','{"text": "immersive_heavy"}','{"text": "radio_tower"}','{"text": ""}']}}
setblock 361 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Form einen"}','{"text": "Funkturm"}','{"text": ""}','{"text": ""}']}}
fill 369 64 183 369 94 212 minecraft:light_gray_concrete
place template immersiveengineering:multiblocks/radio_tower 362 64 186 none
kw testworld use 364 65 191 south immersiveengineering:hammer
execute unless block 364 65 191 immersiveengineering:rs_engineering
