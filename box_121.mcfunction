# 121 industrial/washing, conveyor
#area 88 216 119 241
fill 88 64 216 119 91 241 minecraft:air
fill 88 60 216 119 62 241 minecraft:stone
fill 88 63 216 119 63 241 minecraft:light_gray_concrete
fill 92 64 222 119 79 222 minecraft:light_gray_concrete
fill 92 64 222 92 79 235 minecraft:light_gray_concrete
setblock 93 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 94 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 95 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 103 64 222 103 79 235 minecraft:light_gray_concrete
setblock 96 64 227 industrialforegoing:washing_factory[subfacing=south]
setblock 98 64 227 industrialforegoing:fermentation_station[subfacing=south]
setblock 100 64 227 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 104 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "121.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 105 64 234 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 114 64 222 114 79 235 minecraft:light_gray_concrete
setblock 106 64 227 industrialforegoing:conveyor[facing=east,type=flat]
setblock 107 64 227 industrialforegoing:conveyor[facing=east,type=flat]
setblock 108 64 227 industrialforegoing:conveyor[facing=east,type=flat]
setblock 109 64 227 industrialforegoing:conveyor[facing=east,type=flat]
setblock 110 64 227 industrialforegoing:conveyor[facing=east,type=flat]
setblock 111 64 227 industrialforegoing:conveyor[facing=east,type=flat]
summon item 107.5 64.4 227.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 109.5 64.4 227.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 110.5 64.4 227.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
