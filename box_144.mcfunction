# 144 finale/tech
#area 112 317 133 344
fill 112 64 317 133 91 344 minecraft:air
fill 112 60 317 133 62 344 minecraft:stone
fill 112 63 317 133 63 344 minecraft:light_gray_concrete
fill 116 64 323 133 79 323 minecraft:light_gray_concrete
fill 116 64 323 116 79 338 minecraft:light_gray_concrete
setblock 117 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 118 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 128 64 323 128 79 338 minecraft:light_gray_concrete
setblock 122 64 329 draconicevolution:crafting_core
setblock 119 64 328 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 119 64 328 up draconicevolution:draconium_core
setblock 119 64 330 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 119 64 330 up draconicevolution:draconium_core
setblock 125 64 328 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 125 64 328 up draconicevolution:draconium_core
setblock 125 64 330 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 125 64 330 up draconicevolution:draconium_core
setblock 121 64 326 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 121 64 326 up botania:gaia_ingot
setblock 123 64 326 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 123 64 326 up botania:gaia_ingot
setblock 122 64 332 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 122 64 332 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
