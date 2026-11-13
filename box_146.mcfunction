# 146 finale/tech
#area 107 319 128 346
fill 107 64 319 128 91 346 minecraft:air
fill 107 60 319 128 62 346 minecraft:stone
fill 107 63 319 128 63 346 minecraft:light_gray_concrete
fill 111 64 325 128 79 325 minecraft:light_gray_concrete
fill 111 64 325 111 79 340 minecraft:light_gray_concrete
setblock 112 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 113 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 123 64 325 123 79 340 minecraft:light_gray_concrete
setblock 117 64 331 draconicevolution:crafting_core
setblock 114 64 330 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 114 64 330 up draconicevolution:draconium_core
setblock 114 64 332 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 114 64 332 up draconicevolution:draconium_core
setblock 120 64 330 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 120 64 330 up draconicevolution:draconium_core
setblock 120 64 332 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 120 64 332 up draconicevolution:draconium_core
setblock 116 64 328 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 116 64 328 up botania:gaia_ingot
setblock 118 64 328 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 118 64 328 up botania:gaia_ingot
setblock 117 64 334 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 117 64 334 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
