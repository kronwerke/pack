# 113 finale/tech
#area 100 315 121 342
fill 100 64 315 121 91 342 minecraft:air
fill 100 60 315 121 62 342 minecraft:stone
fill 100 63 315 121 63 342 minecraft:light_gray_concrete
fill 104 64 321 121 79 321 minecraft:light_gray_concrete
fill 104 64 321 104 79 336 minecraft:light_gray_concrete
setblock 105 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "113"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 106 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 116 64 321 116 79 336 minecraft:light_gray_concrete
setblock 110 64 327 draconicevolution:crafting_core
setblock 107 64 326 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 107 64 326 up draconicevolution:draconium_core
setblock 107 64 328 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 107 64 328 up draconicevolution:draconium_core
setblock 113 64 326 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 113 64 326 up draconicevolution:draconium_core
setblock 113 64 328 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 113 64 328 up draconicevolution:draconium_core
setblock 109 64 324 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 109 64 324 up botania:gaia_ingot
setblock 111 64 324 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 111 64 324 up botania:gaia_ingot
setblock 110 64 330 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 110 64 330 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
