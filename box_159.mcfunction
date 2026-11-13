# 159 finale/tech
#area 117 353 138 380
fill 117 64 353 138 91 380 minecraft:air
fill 117 60 353 138 62 380 minecraft:stone
fill 117 63 353 138 63 380 minecraft:light_gray_concrete
fill 121 64 359 138 79 359 minecraft:light_gray_concrete
fill 121 64 359 121 79 374 minecraft:light_gray_concrete
setblock 122 64 373 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "159"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 123 64 373 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 133 64 359 133 79 374 minecraft:light_gray_concrete
setblock 127 64 365 draconicevolution:crafting_core
setblock 124 64 364 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 364 up draconicevolution:draconium_core
setblock 124 64 366 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 124 64 366 up draconicevolution:draconium_core
setblock 130 64 364 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 364 up draconicevolution:draconium_core
setblock 130 64 366 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 130 64 366 up draconicevolution:draconium_core
setblock 126 64 362 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 126 64 362 up botania:gaia_ingot
setblock 128 64 362 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 128 64 362 up botania:gaia_ingot
setblock 127 64 368 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 127 64 368 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
