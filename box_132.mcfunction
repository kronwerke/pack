# 132 industrial/washing, conveyor
#area 88 252 119 277
fill 88 64 252 119 91 277 minecraft:air
fill 88 60 252 119 62 277 minecraft:stone
fill 88 63 252 119 63 277 minecraft:light_gray_concrete
fill 92 64 258 119 79 258 minecraft:light_gray_concrete
fill 92 64 258 92 79 271 minecraft:light_gray_concrete
setblock 93 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 94 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 95 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 103 64 258 103 79 271 minecraft:light_gray_concrete
setblock 96 64 263 industrialforegoing:washing_factory[subfacing=south]
setblock 98 64 263 industrialforegoing:fermentation_station[subfacing=south]
setblock 100 64 263 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 104 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 105 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 114 64 258 114 79 271 minecraft:light_gray_concrete
setblock 106 64 263 industrialforegoing:conveyor[facing=east,type=flat]
setblock 107 64 263 industrialforegoing:conveyor[facing=east,type=flat]
setblock 108 64 263 industrialforegoing:conveyor[facing=east,type=flat]
setblock 109 64 263 industrialforegoing:conveyor[facing=east,type=flat]
setblock 110 64 263 industrialforegoing:conveyor[facing=east,type=flat]
setblock 111 64 263 industrialforegoing:conveyor[facing=east,type=flat]
summon item 107.5 64.4 263.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 109.5 64.4 263.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 110.5 64.4 263.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
