# 155 draconic/dust, injectors, stabilizer
#area -4 349 39 376
fill -4 64 349 36 91 376 minecraft:air
fill 37 64 349 39 91 376 minecraft:air
fill -4 60 349 39 62 376 minecraft:stone
fill -4 63 349 39 63 376 minecraft:light_gray_concrete
fill 0 64 355 39 79 355 minecraft:light_gray_concrete
fill 0 64 355 0 79 370 minecraft:light_gray_concrete
setblock 1 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 355 10 79 370 minecraft:light_gray_concrete
fill 4 64 359 6 65 360 minecraft:end_stone
setblock 5 64 360 draconicevolution:end_draconium_ore
setblock 6 65 360 draconicevolution:end_draconium_ore
setblock 4 65 359 draconicevolution:end_draconium_ore
setblock 11 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 355 22 79 370 minecraft:light_gray_concrete
setblock 16 64 361 draconicevolution:crafting_core
setblock 13 64 360 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 358 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 360 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 364 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 362 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 358 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 362 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 364 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 355 34 79 370 minecraft:light_gray_concrete
fill 27 64 360 29 66 362 draconicevolution:draconium_block
setblock 28 65 361 draconicevolution:energy_core
setblock 24 64 361 minecraft:polished_deepslate
setblock 24 65 361 draconicevolution:energy_core_stabilizer
setblock 32 64 361 minecraft:polished_deepslate
setblock 32 65 361 draconicevolution:energy_core_stabilizer
setblock 28 64 357 minecraft:polished_deepslate
setblock 28 65 357 draconicevolution:energy_core_stabilizer
setblock 28 64 365 minecraft:polished_deepslate
setblock 28 65 365 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
