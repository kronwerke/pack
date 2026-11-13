# 125 finale/tech
#area 97 319 118 346
fill 97 64 319 118 91 346 minecraft:air
fill 97 60 319 118 62 346 minecraft:stone
fill 97 63 319 118 63 346 minecraft:light_gray_concrete
fill 101 64 325 118 79 325 minecraft:light_gray_concrete
fill 101 64 325 101 79 340 minecraft:light_gray_concrete
setblock 102 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "125"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 103 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 113 64 325 113 79 340 minecraft:light_gray_concrete
setblock 107 64 331 draconicevolution:crafting_core
setblock 104 64 330 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 104 64 330 up draconicevolution:draconium_core
setblock 104 64 332 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 104 64 332 up draconicevolution:draconium_core
setblock 110 64 330 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 110 64 330 up draconicevolution:draconium_core
setblock 110 64 332 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 110 64 332 up draconicevolution:draconium_core
setblock 106 64 328 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 106 64 328 up botania:gaia_ingot
setblock 108 64 328 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 108 64 328 up botania:gaia_ingot
setblock 107 64 334 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 107 64 334 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
