# 088 industrial/washing, conveyor
#area 46 212 77 237
fill 46 64 212 77 91 237 minecraft:air
fill 46 60 212 77 62 237 minecraft:stone
fill 46 63 212 77 63 237 minecraft:light_gray_concrete
fill 50 64 218 77 79 218 minecraft:light_gray_concrete
fill 50 64 218 50 79 231 minecraft:light_gray_concrete
setblock 51 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 52 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 53 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 61 64 218 61 79 231 minecraft:light_gray_concrete
setblock 54 64 223 industrialforegoing:washing_factory[subfacing=south]
setblock 56 64 223 industrialforegoing:fermentation_station[subfacing=south]
setblock 58 64 223 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 62 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 63 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 72 64 218 72 79 231 minecraft:light_gray_concrete
setblock 64 64 223 industrialforegoing:conveyor[facing=east,type=flat]
setblock 65 64 223 industrialforegoing:conveyor[facing=east,type=flat]
setblock 66 64 223 industrialforegoing:conveyor[facing=east,type=flat]
setblock 67 64 223 industrialforegoing:conveyor[facing=east,type=flat]
setblock 68 64 223 industrialforegoing:conveyor[facing=east,type=flat]
setblock 69 64 223 industrialforegoing:conveyor[facing=east,type=flat]
summon item 65.5 64.4 223.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 67.5 64.4 223.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 68.5 64.4 223.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
