# 155 finale/tech
#area 107 349 128 376
fill 107 64 349 128 91 376 minecraft:air
fill 107 60 349 128 62 376 minecraft:stone
fill 107 63 349 128 63 376 minecraft:light_gray_concrete
fill 111 64 355 128 79 355 minecraft:light_gray_concrete
fill 111 64 355 111 79 370 minecraft:light_gray_concrete
setblock 112 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "155"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 113 64 369 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 123 64 355 123 79 370 minecraft:light_gray_concrete
setblock 117 64 361 draconicevolution:crafting_core
setblock 114 64 360 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 114 64 360 up draconicevolution:draconium_core
setblock 114 64 362 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 114 64 362 up draconicevolution:draconium_core
setblock 120 64 360 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 120 64 360 up draconicevolution:draconium_core
setblock 120 64 362 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 120 64 362 up draconicevolution:draconium_core
setblock 116 64 358 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 116 64 358 up botania:gaia_ingot
setblock 118 64 358 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 118 64 358 up botania:gaia_ingot
setblock 117 64 364 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 117 64 364 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
