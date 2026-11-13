# 159 finale/tech
#area 117 355 138 382
fill 117 64 355 138 91 382 minecraft:air
fill 117 60 355 138 62 382 minecraft:stone
fill 117 63 355 138 63 382 minecraft:light_gray_concrete
fill 121 64 361 138 79 361 minecraft:light_gray_concrete
fill 121 64 361 121 79 376 minecraft:light_gray_concrete
setblock 122 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 123 64 375 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 133 64 361 133 79 376 minecraft:light_gray_concrete
setblock 127 64 367 draconicevolution:crafting_core
setblock 124 64 366 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 366 up draconicevolution:draconium_core
setblock 124 64 368 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 368 up draconicevolution:draconium_core
setblock 130 64 366 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 366 up draconicevolution:draconium_core
setblock 130 64 368 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 368 up draconicevolution:draconium_core
setblock 126 64 364 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 126 64 364 up botania:gaia_ingot
setblock 128 64 364 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 128 64 364 up botania:gaia_ingot
setblock 127 64 370 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 127 64 370 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
