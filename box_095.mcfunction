# 095 draconic_chaos/reactor
#area 37 288 56 313
fill 37 64 288 56 95 313 minecraft:air
fill 37 60 288 56 62 313 minecraft:stone
fill 37 63 288 56 63 313 minecraft:light_gray_concrete
fill 41 64 294 56 83 294 minecraft:light_gray_concrete
fill 41 64 294 41 83 307 minecraft:light_gray_concrete
setblock 42 64 306 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095"}','{"text": "draconic_chaos"}','{"text": "reactor"}','{"text": ""}']}}
setblock 43 64 306 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Drakonischen"}','{"text": "Reaktor"}','{"text": ""}']}}
fill 51 64 294 51 83 307 minecraft:light_gray_concrete
setblock 46 67 299 draconicevolution:reactor_core
setblock 42 67 299 minecraft:stone
kw testworld use 42 67 299 east draconicevolution:reactor_stabilizer
setblock 42 67 299 minecraft:air
setblock 50 67 299 minecraft:stone
kw testworld use 50 67 299 west draconicevolution:reactor_stabilizer
setblock 50 67 299 minecraft:air
setblock 46 67 295 minecraft:stone
kw testworld use 46 67 295 south draconicevolution:reactor_stabilizer
setblock 46 67 295 minecraft:air
setblock 46 67 303 minecraft:stone
kw testworld use 46 67 303 north draconicevolution:reactor_stabilizer
setblock 46 67 303 minecraft:air
setblock 46 71 299 minecraft:stone
kw testworld use 46 71 299 down draconicevolution:reactor_injector
setblock 46 71 299 minecraft:air
execute if block 43 67 299 draconicevolution:reactor_stabilizer
execute if block 46 70 299 draconicevolution:reactor_injector
