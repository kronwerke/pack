# 092 draconic_chaos/reactor
#area 37 269 58 296
fill 37 64 269 58 97 296 minecraft:air
fill 37 60 269 58 62 296 minecraft:stone
fill 37 63 269 58 63 296 minecraft:light_gray_concrete
fill 41 64 275 58 85 275 minecraft:light_gray_concrete
fill 41 64 275 41 85 290 minecraft:light_gray_concrete
setblock 42 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "draconic_chaos"}','{"text": "reactor"}','{"text": ""}']}}
setblock 43 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Drakonischen"}','{"text": "Reaktor"}','{"text": ""}']}}
fill 53 64 275 53 85 290 minecraft:light_gray_concrete
setblock 47 67 281 draconicevolution:reactor_core
setblock 42 67 281 minecraft:stone
kw testworld use 42 67 281 east draconicevolution:reactor_stabilizer
setblock 42 67 281 minecraft:air
setblock 52 67 281 minecraft:stone
kw testworld use 52 67 281 west draconicevolution:reactor_stabilizer
setblock 52 67 281 minecraft:air
setblock 47 67 276 minecraft:stone
kw testworld use 47 67 276 south draconicevolution:reactor_stabilizer
setblock 47 67 276 minecraft:air
setblock 47 67 286 minecraft:stone
kw testworld use 47 67 286 north draconicevolution:reactor_stabilizer
setblock 47 67 286 minecraft:air
setblock 47 72 281 minecraft:stone
kw testworld use 47 72 281 down draconicevolution:reactor_injector
setblock 47 72 281 minecraft:air
execute if block 43 67 281 draconicevolution:reactor_stabilizer
execute if block 47 71 281 draconicevolution:reactor_injector
