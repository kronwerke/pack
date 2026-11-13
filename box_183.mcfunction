# 183 finale/tech
#area 167 386 188 413
fill 167 64 386 188 91 413 minecraft:air
fill 167 60 386 188 62 413 minecraft:stone
fill 167 63 386 188 63 413 minecraft:light_gray_concrete
fill 171 64 392 188 79 392 minecraft:light_gray_concrete
fill 171 64 392 171 79 407 minecraft:light_gray_concrete
setblock 172 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183"}','{"text": "finale"}','{"text": "tech"}','{"text": ""}']}}
setblock 173 64 406 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fusioniere"}','{"text": "Erwachtes"}','{"text": "Draconium"}','{"text": ""}']}}
fill 183 64 392 183 79 407 minecraft:light_gray_concrete
setblock 177 64 398 draconicevolution:crafting_core
setblock 174 64 397 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 174 64 397 up draconicevolution:draconium_core
setblock 174 64 399 draconicevolution:wyvern_crafting_injector[facing=east]
kw testworld use 174 64 399 up draconicevolution:draconium_core
setblock 180 64 397 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 180 64 397 up draconicevolution:draconium_core
setblock 180 64 399 draconicevolution:wyvern_crafting_injector[facing=west]
kw testworld use 180 64 399 up draconicevolution:draconium_core
setblock 176 64 395 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 176 64 395 up botania:gaia_ingot
setblock 178 64 395 draconicevolution:wyvern_crafting_injector[facing=south]
kw testworld use 178 64 395 up botania:gaia_ingot
setblock 177 64 401 draconicevolution:wyvern_crafting_injector[facing=north]
kw testworld use 177 64 401 up draconicevolution:dragon_heart
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
