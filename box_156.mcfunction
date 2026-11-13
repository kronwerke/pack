# 156 draconic/dust, injectors, stabilizer
#area -4 355 39 382
fill -4 64 355 36 91 382 minecraft:air
fill 37 64 355 39 91 382 minecraft:air
fill -4 60 355 39 62 382 minecraft:stone
fill -4 63 355 39 63 382 minecraft:light_gray_concrete
fill 0 64 361 39 79 361 minecraft:light_gray_concrete
fill 0 64 361 0 79 376 minecraft:light_gray_concrete
setblock 1 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 361 10 79 376 minecraft:light_gray_concrete
fill 4 64 365 6 65 366 minecraft:end_stone
setblock 5 64 366 draconicevolution:end_draconium_ore
setblock 6 65 366 draconicevolution:end_draconium_ore
setblock 4 65 365 draconicevolution:end_draconium_ore
setblock 11 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 361 22 79 376 minecraft:light_gray_concrete
setblock 16 64 367 draconicevolution:crafting_core
setblock 13 64 366 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 364 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 366 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 370 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 368 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 364 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 368 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 370 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "156.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 361 34 79 376 minecraft:light_gray_concrete
fill 27 64 366 29 66 368 draconicevolution:draconium_block
setblock 28 65 367 draconicevolution:energy_core
setblock 24 64 367 minecraft:polished_deepslate
setblock 24 65 367 draconicevolution:energy_core_stabilizer
setblock 32 64 367 minecraft:polished_deepslate
setblock 32 65 367 draconicevolution:energy_core_stabilizer
setblock 28 64 363 minecraft:polished_deepslate
setblock 28 65 363 draconicevolution:energy_core_stabilizer
setblock 28 64 371 minecraft:polished_deepslate
setblock 28 65 371 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
