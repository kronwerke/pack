# 163 draconic/dust, injectors, stabilizer
#area -4 384 39 411
fill -4 64 384 36 91 411 minecraft:air
fill 37 64 384 39 91 411 minecraft:air
fill -4 60 384 39 62 411 minecraft:stone
fill -4 63 384 39 63 411 minecraft:light_gray_concrete
fill 0 64 390 39 79 390 minecraft:light_gray_concrete
fill 0 64 390 0 79 405 minecraft:light_gray_concrete
setblock 1 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 390 10 79 405 minecraft:light_gray_concrete
fill 4 64 394 6 65 395 minecraft:end_stone
setblock 5 64 395 draconicevolution:end_draconium_ore
setblock 6 65 395 draconicevolution:end_draconium_ore
setblock 4 65 394 draconicevolution:end_draconium_ore
setblock 11 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 390 22 79 405 minecraft:light_gray_concrete
setblock 16 64 396 draconicevolution:crafting_core
setblock 13 64 395 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 393 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 395 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 399 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 397 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 393 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 397 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 399 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "163.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 390 34 79 405 minecraft:light_gray_concrete
fill 27 64 395 29 66 397 draconicevolution:draconium_block
setblock 28 65 396 draconicevolution:energy_core
setblock 24 64 396 minecraft:polished_deepslate
setblock 24 65 396 draconicevolution:energy_core_stabilizer
setblock 32 64 396 minecraft:polished_deepslate
setblock 32 65 396 draconicevolution:energy_core_stabilizer
setblock 28 64 392 minecraft:polished_deepslate
setblock 28 65 392 draconicevolution:energy_core_stabilizer
setblock 28 64 400 minecraft:polished_deepslate
setblock 28 65 400 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
