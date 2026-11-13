# 137 industrial/washing, conveyor
#area 322 240 353 265
fill 322 64 240 353 91 265 minecraft:air
fill 322 60 240 353 62 265 minecraft:stone
fill 322 63 240 353 63 265 minecraft:light_gray_concrete
fill 326 64 246 353 79 246 minecraft:light_gray_concrete
fill 326 64 246 326 79 259 minecraft:light_gray_concrete
setblock 327 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "137.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 328 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 329 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 337 64 246 337 79 259 minecraft:light_gray_concrete
setblock 330 64 251 industrialforegoing:washing_factory[subfacing=south]
setblock 332 64 251 industrialforegoing:fermentation_station[subfacing=south]
setblock 334 64 251 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 338 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "137.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 339 64 258 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 348 64 246 348 79 259 minecraft:light_gray_concrete
setblock 340 64 251 industrialforegoing:conveyor[facing=east,type=flat]
setblock 341 64 251 industrialforegoing:conveyor[facing=east,type=flat]
setblock 342 64 251 industrialforegoing:conveyor[facing=east,type=flat]
setblock 343 64 251 industrialforegoing:conveyor[facing=east,type=flat]
setblock 344 64 251 industrialforegoing:conveyor[facing=east,type=flat]
setblock 345 64 251 industrialforegoing:conveyor[facing=east,type=flat]
summon item 341.5 64.4 251.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 343.5 64.4 251.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 344.5 64.4 251.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
