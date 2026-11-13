# 131 industrial/washing, conveyor
#area 88 246 119 271
fill 88 64 246 119 91 271 minecraft:air
fill 88 60 246 119 62 271 minecraft:stone
fill 88 63 246 119 63 271 minecraft:light_gray_concrete
fill 92 64 252 119 79 252 minecraft:light_gray_concrete
fill 92 64 252 92 79 265 minecraft:light_gray_concrete
setblock 93 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 94 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 95 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 103 64 252 103 79 265 minecraft:light_gray_concrete
setblock 96 64 257 industrialforegoing:washing_factory[subfacing=south]
setblock 98 64 257 industrialforegoing:fermentation_station[subfacing=south]
setblock 100 64 257 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 104 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 105 64 264 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 114 64 252 114 79 265 minecraft:light_gray_concrete
setblock 106 64 257 industrialforegoing:conveyor[facing=east,type=flat]
setblock 107 64 257 industrialforegoing:conveyor[facing=east,type=flat]
setblock 108 64 257 industrialforegoing:conveyor[facing=east,type=flat]
setblock 109 64 257 industrialforegoing:conveyor[facing=east,type=flat]
setblock 110 64 257 industrialforegoing:conveyor[facing=east,type=flat]
setblock 111 64 257 industrialforegoing:conveyor[facing=east,type=flat]
summon item 107.5 64.4 257.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 109.5 64.4 257.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 110.5 64.4 257.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
