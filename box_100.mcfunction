# 100 draconic/dust, injectors, stabilizer
#area -4 296 39 323
fill -4 64 296 36 91 323 minecraft:air
fill 37 64 296 39 91 323 minecraft:air
fill -4 60 296 39 62 323 minecraft:stone
fill -4 63 296 39 63 323 minecraft:light_gray_concrete
fill 0 64 302 39 79 302 minecraft:light_gray_concrete
fill 0 64 302 0 79 317 minecraft:light_gray_concrete
setblock 1 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.1"}','{"text": "draconic"}','{"text": "dust"}','{"text": ""}']}}
setblock 2 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Draconium"}','{"text": "im End ab"}','{"text": ""}','{"text": ""}']}}
fill 10 64 302 10 79 317 minecraft:light_gray_concrete
fill 4 64 306 6 65 307 minecraft:end_stone
setblock 5 64 307 draconicevolution:end_draconium_ore
setblock 6 65 307 draconicevolution:end_draconium_ore
setblock 4 65 306 draconicevolution:end_draconium_ore
setblock 11 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.2"}','{"text": "draconic"}','{"text": "injectors"}','{"text": ""}']}}
setblock 12 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell acht"}','{"text": "Draconium-Injektoren"}','{"text": "auf"}','{"text": ""}']}}
fill 22 64 302 22 79 317 minecraft:light_gray_concrete
setblock 16 64 308 draconicevolution:crafting_core
setblock 13 64 307 draconicevolution:basic_crafting_injector[facing=east]
setblock 15 64 305 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 307 draconicevolution:basic_crafting_injector[facing=west]
setblock 15 64 311 draconicevolution:basic_crafting_injector[facing=north]
setblock 13 64 309 draconicevolution:basic_crafting_injector[facing=east]
setblock 17 64 305 draconicevolution:basic_crafting_injector[facing=south]
setblock 19 64 309 draconicevolution:basic_crafting_injector[facing=west]
setblock 17 64 311 draconicevolution:basic_crafting_injector[facing=north]
setblock 23 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.3"}','{"text": "draconic"}','{"text": "stabilizer"}','{"text": ""}']}}
setblock 24 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau vier"}','{"text": "Stabilisatoren"}','{"text": "mit Gaia"}','{"text": ""}']}}
fill 34 64 302 34 79 317 minecraft:light_gray_concrete
fill 27 64 307 29 66 309 draconicevolution:draconium_block
setblock 28 65 308 draconicevolution:energy_core
setblock 24 64 308 minecraft:polished_deepslate
setblock 24 65 308 draconicevolution:energy_core_stabilizer
setblock 32 64 308 minecraft:polished_deepslate
setblock 32 65 308 draconicevolution:energy_core_stabilizer
setblock 28 64 304 minecraft:polished_deepslate
setblock 28 65 304 draconicevolution:energy_core_stabilizer
setblock 28 64 312 minecraft:polished_deepslate
setblock 28 65 312 draconicevolution:energy_core_stabilizer
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
