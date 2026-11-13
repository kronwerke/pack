# 130 finale/tech
#area 97 317 118 344
fill 97 64 317 118 91 344 minecraft:air
fill 97 60 317 118 62 344 minecraft:stone
fill 97 63 317 118 63 344 minecraft:light_gray_concrete
fill 101 64 323 118 79 323 minecraft:light_gray_concrete
fill 101 64 323 101 79 338 minecraft:light_gray_concrete
setblock 102 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 103 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 113 64 323 113 79 338 minecraft:light_gray_concrete
setblock 107 64 329 draconicevolution:crafting_core
setblock 104 64 328 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 104 64 328 up draconicevolution:draconium_core
setblock 104 64 330 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 104 64 330 up draconicevolution:draconium_core
setblock 110 64 328 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 110 64 328 up draconicevolution:draconium_core
setblock 110 64 330 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 110 64 330 up draconicevolution:draconium_core
setblock 106 64 326 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 106 64 326 up botania:gaia_ingot
setblock 108 64 326 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 108 64 326 up botania:gaia_ingot
setblock 107 64 332 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 107 64 332 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
