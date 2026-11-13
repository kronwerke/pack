# 145 draconic/dust, injectors, stabilizer
#area -4 319 39 346
fill -4 64 319 36 91 346 minecraft:air
fill 37 64 319 39 91 346 minecraft:air
fill -4 60 319 39 62 346 minecraft:stone
fill -4 63 319 39 63 346 minecraft:light_gray_concrete
fill 0 64 325 39 79 325 minecraft:light_gray_concrete
fill 0 64 325 0 79 340 minecraft:light_gray_concrete
setblock 1 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 325 10 79 340 minecraft:light_gray_concrete
fill 4 64 329 6 65 330 minecraft:end_stone
setblock 5 64 330 draconicevolution:end_draconium_ore
setblock 6 65 330 draconicevolution:end_draconium_ore
setblock 4 65 329 draconicevolution:end_draconium_ore
setblock 11 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 325 22 79 340 minecraft:light_gray_concrete
setblock 16 64 331 draconicevolution:crafting_core
setblock 13 64 330 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 328 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 330 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 334 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 332 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 328 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 332 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 334 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 325 34 79 340 minecraft:light_gray_concrete
fill 27 64 330 29 66 332 draconicevolution:draconium_block
setblock 28 65 331 draconicevolution:energy_core
setblock 24 64 331 minecraft:polished_deepslate
setblock 24 65 331 draconicevolution:energy_core_stabilizer
setblock 32 64 331 minecraft:polished_deepslate
setblock 32 65 331 draconicevolution:energy_core_stabilizer
setblock 28 64 327 minecraft:polished_deepslate
setblock 28 65 327 draconicevolution:energy_core_stabilizer
setblock 28 64 335 minecraft:polished_deepslate
setblock 28 65 335 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
