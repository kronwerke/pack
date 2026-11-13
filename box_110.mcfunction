# 110 draconic/dust, injectors, stabilizer
#area -4 315 39 342
fill -4 64 315 36 91 342 minecraft:air
fill 37 64 315 39 91 342 minecraft:air
fill -4 60 315 39 62 342 minecraft:stone
fill -4 63 315 39 63 342 minecraft:light_gray_concrete
fill 0 64 321 39 79 321 minecraft:light_gray_concrete
fill 0 64 321 0 79 336 minecraft:light_gray_concrete
setblock 1 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 321 10 79 336 minecraft:light_gray_concrete
fill 4 64 325 6 65 326 minecraft:end_stone
setblock 5 64 326 draconicevolution:end_draconium_ore
setblock 6 65 326 draconicevolution:end_draconium_ore
setblock 4 65 325 draconicevolution:end_draconium_ore
setblock 11 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 321 22 79 336 minecraft:light_gray_concrete
setblock 16 64 327 draconicevolution:crafting_core
setblock 13 64 326 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 324 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 326 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 330 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 328 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 324 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 328 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 330 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "110.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 321 34 79 336 minecraft:light_gray_concrete
fill 27 64 326 29 66 328 draconicevolution:draconium_block
setblock 28 65 327 draconicevolution:energy_core
setblock 24 64 327 minecraft:polished_deepslate
setblock 24 65 327 draconicevolution:energy_core_stabilizer
setblock 32 64 327 minecraft:polished_deepslate
setblock 32 65 327 draconicevolution:energy_core_stabilizer
setblock 28 64 323 minecraft:polished_deepslate
setblock 28 65 323 draconicevolution:energy_core_stabilizer
setblock 28 64 331 minecraft:polished_deepslate
setblock 28 65 331 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
