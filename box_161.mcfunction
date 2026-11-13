# 161 finale/tech
#area 117 380 138 407
fill 117 64 380 138 91 407 minecraft:air
fill 117 60 380 138 62 407 minecraft:stone
fill 117 63 380 138 63 407 minecraft:light_gray_concrete
fill 121 64 386 138 79 386 minecraft:light_gray_concrete
fill 121 64 386 121 79 401 minecraft:light_gray_concrete
setblock 122 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 123 64 400 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 133 64 386 133 79 401 minecraft:light_gray_concrete
setblock 127 64 392 draconicevolution:crafting_core
setblock 124 64 391 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 391 up draconicevolution:draconium_core
setblock 124 64 393 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 393 up draconicevolution:draconium_core
setblock 130 64 391 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 391 up draconicevolution:draconium_core
setblock 130 64 393 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 393 up draconicevolution:draconium_core
setblock 126 64 389 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 126 64 389 up botania:gaia_ingot
setblock 128 64 389 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 128 64 389 up botania:gaia_ingot
setblock 127 64 395 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 127 64 395 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
