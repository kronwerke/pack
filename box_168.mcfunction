# 168 finale/tech
#area 167 384 188 411
fill 167 64 384 188 91 411 minecraft:air
fill 167 60 384 188 62 411 minecraft:stone
fill 167 63 384 188 63 411 minecraft:light_gray_concrete
fill 171 64 390 188 79 390 minecraft:light_gray_concrete
fill 171 64 390 171 79 405 minecraft:light_gray_concrete
setblock 172 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "168"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 173 64 404 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 183 64 390 183 79 405 minecraft:light_gray_concrete
setblock 177 64 396 draconicevolution:crafting_core
setblock 174 64 395 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 174 64 395 up draconicevolution:draconium_core
setblock 174 64 397 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 174 64 397 up draconicevolution:draconium_core
setblock 180 64 395 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 180 64 395 up draconicevolution:draconium_core
setblock 180 64 397 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 180 64 397 up draconicevolution:draconium_core
setblock 176 64 393 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 176 64 393 up botania:gaia_ingot
setblock 178 64 393 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 178 64 393 up botania:gaia_ingot
setblock 177 64 399 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 177 64 399 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
