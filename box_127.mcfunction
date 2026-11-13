# 127 draconic/dust, injectors, stabilizer
#area -4 317 39 344
fill -4 64 317 36 91 344 minecraft:air
fill 37 64 317 39 91 344 minecraft:air
fill -4 60 317 39 62 344 minecraft:stone
fill -4 63 317 39 63 344 minecraft:light_gray_concrete
fill 0 64 323 39 79 323 minecraft:light_gray_concrete
fill 0 64 323 0 79 338 minecraft:light_gray_concrete
setblock 1 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 323 10 79 338 minecraft:light_gray_concrete
fill 4 64 327 6 65 328 minecraft:end_stone
setblock 5 64 328 draconicevolution:end_draconium_ore
setblock 6 65 328 draconicevolution:end_draconium_ore
setblock 4 65 327 draconicevolution:end_draconium_ore
setblock 11 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 323 22 79 338 minecraft:light_gray_concrete
setblock 16 64 329 draconicevolution:crafting_core
setblock 13 64 328 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 326 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 328 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 332 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 330 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 326 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 330 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 332 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 323 34 79 338 minecraft:light_gray_concrete
fill 27 64 328 29 66 330 draconicevolution:draconium_block
setblock 28 65 329 draconicevolution:energy_core
setblock 24 64 329 minecraft:polished_deepslate
setblock 24 65 329 draconicevolution:energy_core_stabilizer
setblock 32 64 329 minecraft:polished_deepslate
setblock 32 65 329 draconicevolution:energy_core_stabilizer
setblock 28 64 325 minecraft:polished_deepslate
setblock 28 65 325 draconicevolution:energy_core_stabilizer
setblock 28 64 333 minecraft:polished_deepslate
setblock 28 65 333 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
