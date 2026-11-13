# 152 industrial/washing, conveyor, transporters
#area 322 242 363 267
fill 322 64 242 363 91 267 minecraft:air
fill 322 60 242 363 62 267 minecraft:stone
fill 322 63 242 363 63 267 minecraft:light_gray_concrete
fill 326 64 248 363 79 248 minecraft:light_gray_concrete
fill 326 64 248 326 79 261 minecraft:light_gray_concrete
setblock 327 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 328 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 329 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 337 64 248 337 79 261 minecraft:light_gray_concrete
setblock 330 64 253 industrialforegoing:washing_factory[subfacing=south]
setblock 332 64 253 industrialforegoing:fermentation_station[subfacing=south]
setblock 334 64 253 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 338 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 339 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 348 64 248 348 79 261 minecraft:light_gray_concrete
setblock 340 64 253 industrialforegoing:conveyor[facing=east,type=flat]
setblock 341 64 253 industrialforegoing:conveyor[facing=east,type=flat]
setblock 342 64 253 industrialforegoing:conveyor[facing=east,type=flat]
setblock 343 64 253 industrialforegoing:conveyor[facing=east,type=flat]
setblock 344 64 253 industrialforegoing:conveyor[facing=east,type=flat]
setblock 345 64 253 industrialforegoing:conveyor[facing=east,type=flat]
summon item 341.5 64.4 253.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 343.5 64.4 253.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 344.5 64.4 253.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 349 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "152.3"}','{"text": "industrial"}','{"text": "transporters"}','{"text": ""}']}}
setblock 350 64 260 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Inventare mit"}','{"text": "Transportern"}','{"text": ""}']}}
fill 358 64 248 358 79 261 minecraft:light_gray_concrete
setblock 352 64 253 minecraft:smooth_stone_slab
summon item_display 352.5 64.95 253.5 {item:{id:"industrialforegoing:item_transporter_type",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 354 64 253 minecraft:smooth_stone_slab
summon item_display 354.5 64.95 253.5 {item:{id:"industrialforegoing:fluid_transporter_type",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
