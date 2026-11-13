# 158 draconic/dust, injectors, stabilizer
#area -4 380 39 407
fill -4 64 380 36 91 407 minecraft:air
fill 37 64 380 39 91 407 minecraft:air
fill -4 60 380 39 62 407 minecraft:stone
fill -4 63 380 39 63 407 minecraft:light_gray_concrete
fill 0 64 386 39 79 386 minecraft:light_gray_concrete
fill 0 64 386 0 79 401 minecraft:light_gray_concrete
setblock 1 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 386 10 79 401 minecraft:light_gray_concrete
fill 4 64 390 6 65 391 minecraft:end_stone
setblock 5 64 391 draconicevolution:end_draconium_ore
setblock 6 65 391 draconicevolution:end_draconium_ore
setblock 4 65 390 draconicevolution:end_draconium_ore
setblock 11 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 386 22 79 401 minecraft:light_gray_concrete
setblock 16 64 392 draconicevolution:crafting_core
setblock 13 64 391 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 389 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 391 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 395 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 393 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 389 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 393 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 395 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 386 34 79 401 minecraft:light_gray_concrete
fill 27 64 391 29 66 393 draconicevolution:draconium_block
setblock 28 65 392 draconicevolution:energy_core
setblock 24 64 392 minecraft:polished_deepslate
setblock 24 65 392 draconicevolution:energy_core_stabilizer
setblock 32 64 392 minecraft:polished_deepslate
setblock 32 65 392 draconicevolution:energy_core_stabilizer
setblock 28 64 388 minecraft:polished_deepslate
setblock 28 65 388 draconicevolution:energy_core_stabilizer
setblock 28 64 396 minecraft:polished_deepslate
setblock 28 65 396 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
