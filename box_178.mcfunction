# 178 draconic/dust, injectors, stabilizer
#area -4 386 39 413
fill -4 64 386 36 91 413 minecraft:air
fill 37 64 386 39 91 413 minecraft:air
fill -4 60 386 39 62 413 minecraft:stone
fill -4 63 386 39 63 413 minecraft:light_gray_concrete
fill 0 64 392 39 79 392 minecraft:light_gray_concrete
fill 0 64 392 0 79 407 minecraft:light_gray_concrete
setblock 1 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "178.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 392 10 79 407 minecraft:light_gray_concrete
fill 4 64 396 6 65 397 minecraft:end_stone
setblock 5 64 397 draconicevolution:end_draconium_ore
setblock 6 65 397 draconicevolution:end_draconium_ore
setblock 4 65 396 draconicevolution:end_draconium_ore
setblock 11 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "178.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 392 22 79 407 minecraft:light_gray_concrete
setblock 16 64 398 draconicevolution:crafting_core
setblock 13 64 397 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 395 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 397 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 401 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 399 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 395 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 399 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 401 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "178.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 392 34 79 407 minecraft:light_gray_concrete
fill 27 64 397 29 66 399 draconicevolution:draconium_block
setblock 28 65 398 draconicevolution:energy_core
setblock 24 64 398 minecraft:polished_deepslate
setblock 24 65 398 draconicevolution:energy_core_stabilizer
setblock 32 64 398 minecraft:polished_deepslate
setblock 32 65 398 draconicevolution:energy_core_stabilizer
setblock 28 64 394 minecraft:polished_deepslate
setblock 28 65 394 draconicevolution:energy_core_stabilizer
setblock 28 64 402 minecraft:polished_deepslate
setblock 28 65 402 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
