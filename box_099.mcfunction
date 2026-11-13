# 099 industrial/washing, conveyor
#area 71 214 102 239
fill 71 64 214 102 91 239 minecraft:air
fill 71 60 214 102 62 239 minecraft:stone
fill 71 63 214 102 63 239 minecraft:light_gray_concrete
fill 75 64 220 102 79 220 minecraft:light_gray_concrete
fill 75 64 220 75 79 233 minecraft:light_gray_concrete
setblock 76 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 77 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 78 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 86 64 220 86 79 233 minecraft:light_gray_concrete
setblock 79 64 225 industrialforegoing:washing_factory[subfacing=south]
setblock 81 64 225 industrialforegoing:fermentation_station[subfacing=south]
setblock 83 64 225 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 87 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 88 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 97 64 220 97 79 233 minecraft:light_gray_concrete
setblock 89 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 90 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 91 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 92 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 93 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 94 64 225 industrialforegoing:conveyor[facing=east,type=flat]
summon item 90.5 64.4 225.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 92.5 64.4 225.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 93.5 64.4 225.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
