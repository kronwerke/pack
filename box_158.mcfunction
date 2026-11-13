# 158 draconic/dust, injectors, stabilizer
#area -4 357 39 384
fill -4 64 357 36 91 384 minecraft:air
fill 37 64 357 39 91 384 minecraft:air
fill -4 60 357 39 62 384 minecraft:stone
fill -4 63 357 39 63 384 minecraft:light_gray_concrete
fill 0 64 363 39 79 363 minecraft:light_gray_concrete
fill 0 64 363 0 79 378 minecraft:light_gray_concrete
setblock 1 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 363 10 79 378 minecraft:light_gray_concrete
fill 4 64 367 6 65 368 minecraft:end_stone
setblock 5 64 368 draconicevolution:end_draconium_ore
setblock 6 65 368 draconicevolution:end_draconium_ore
setblock 4 65 367 draconicevolution:end_draconium_ore
setblock 11 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 363 22 79 378 minecraft:light_gray_concrete
setblock 16 64 369 draconicevolution:crafting_core
setblock 13 64 368 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 366 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 368 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 372 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 370 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 366 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 370 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 372 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 363 34 79 378 minecraft:light_gray_concrete
fill 27 64 368 29 66 370 draconicevolution:draconium_block
setblock 28 65 369 draconicevolution:energy_core
setblock 24 64 369 minecraft:polished_deepslate
setblock 24 65 369 draconicevolution:energy_core_stabilizer
setblock 32 64 369 minecraft:polished_deepslate
setblock 32 65 369 draconicevolution:energy_core_stabilizer
setblock 28 64 365 minecraft:polished_deepslate
setblock 28 65 365 draconicevolution:energy_core_stabilizer
setblock 28 64 373 minecraft:polished_deepslate
setblock 28 65 373 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
