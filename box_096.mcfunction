# 096 draconic_chaos/reactor
#area 37 290 56 315
fill 37 64 290 56 95 315 minecraft:air
fill 37 60 290 56 62 315 minecraft:stone
fill 37 63 290 56 63 315 minecraft:light_gray_concrete
fill 41 64 296 56 83 296 minecraft:light_gray_concrete
fill 41 64 296 41 83 309 minecraft:light_gray_concrete
setblock 42 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "draconic_chaos"}','{"text": "reactor"}','{"text": ""}']}}
setblock 43 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Drakonischen"}','{"text": "Reaktor"}','{"text": ""}']}}
fill 51 64 296 51 83 309 minecraft:light_gray_concrete
setblock 46 67 301 draconicevolution:reactor_core
setblock 42 67 301 minecraft:stone
kw testworld use 42 67 301 east draconicevolution:reactor_stabilizer
setblock 42 67 301 minecraft:air
setblock 50 67 301 minecraft:stone
kw testworld use 50 67 301 west draconicevolution:reactor_stabilizer
setblock 50 67 301 minecraft:air
setblock 46 67 297 minecraft:stone
kw testworld use 46 67 297 south draconicevolution:reactor_stabilizer
setblock 46 67 297 minecraft:air
setblock 46 67 305 minecraft:stone
kw testworld use 46 67 305 north draconicevolution:reactor_stabilizer
setblock 46 67 305 minecraft:air
setblock 46 71 301 minecraft:stone
kw testworld use 46 71 301 down draconicevolution:reactor_injector
setblock 46 71 301 minecraft:air
execute if block 43 67 301 draconicevolution:reactor_stabilizer
execute if block 46 70 301 draconicevolution:reactor_injector
