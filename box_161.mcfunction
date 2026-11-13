# 161 finale/tech
#area 117 357 138 384
fill 117 64 357 138 91 384 minecraft:air
fill 117 60 357 138 62 384 minecraft:stone
fill 117 63 357 138 63 384 minecraft:light_gray_concrete
fill 121 64 363 138 79 363 minecraft:light_gray_concrete
fill 121 64 363 121 79 378 minecraft:light_gray_concrete
setblock 122 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 123 64 377 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 133 64 363 133 79 378 minecraft:light_gray_concrete
setblock 127 64 369 draconicevolution:crafting_core
setblock 124 64 368 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 368 up draconicevolution:draconium_core
setblock 124 64 370 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 370 up draconicevolution:draconium_core
setblock 130 64 368 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 368 up draconicevolution:draconium_core
setblock 130 64 370 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 370 up draconicevolution:draconium_core
setblock 126 64 366 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 126 64 366 up botania:gaia_ingot
setblock 128 64 366 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 128 64 366 up botania:gaia_ingot
setblock 127 64 372 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 127 64 372 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
