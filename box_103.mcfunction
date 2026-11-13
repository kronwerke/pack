# 103 finale/tech
#area 100 296 121 323
fill 100 64 296 121 91 323 minecraft:air
fill 100 60 296 121 62 323 minecraft:stone
fill 100 63 296 121 63 323 minecraft:light_gray_concrete
fill 104 64 302 121 79 302 minecraft:light_gray_concrete
fill 104 64 302 104 79 317 minecraft:light_gray_concrete
setblock 105 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "103"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 106 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 116 64 302 116 79 317 minecraft:light_gray_concrete
setblock 110 64 308 draconicevolution:crafting_core
setblock 107 64 307 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 107 64 307 up draconicevolution:draconium_core
setblock 107 64 309 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 107 64 309 up draconicevolution:draconium_core
setblock 113 64 307 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 113 64 307 up draconicevolution:draconium_core
setblock 113 64 309 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 113 64 309 up draconicevolution:draconium_core
setblock 109 64 305 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 109 64 305 up botania:gaia_ingot
setblock 111 64 305 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 111 64 305 up botania:gaia_ingot
setblock 110 64 311 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 110 64 311 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
