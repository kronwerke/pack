# 116 industrial/washing, conveyor, transporters
#area 88 214 129 239
fill 88 64 214 129 91 239 minecraft:air
fill 88 60 214 129 62 239 minecraft:stone
fill 88 63 214 129 63 239 minecraft:light_gray_concrete
fill 92 64 220 129 79 220 minecraft:light_gray_concrete
fill 92 64 220 92 79 233 minecraft:light_gray_concrete
setblock 93 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 94 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 95 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
fill 103 64 220 103 79 233 minecraft:light_gray_concrete
setblock 96 64 225 industrialforegoing:washing_factory[subfacing=south]
setblock 98 64 225 industrialforegoing:fermentation_station[subfacing=south]
setblock 100 64 225 industrialforegoing:fluid_sieving_machine[subfacing=south]
setblock 104 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 105 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
fill 114 64 220 114 79 233 minecraft:light_gray_concrete
setblock 106 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 107 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 108 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 109 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 110 64 225 industrialforegoing:conveyor[facing=east,type=flat]
setblock 111 64 225 industrialforegoing:conveyor[facing=east,type=flat]
summon item 107.5 64.4 225.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 109.5 64.4 225.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 110.5 64.4 225.5 {Item:{id:"minecraft:raw_iron",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 115 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.3"}','{"text": "industrial"}','{"text": "transporters"}','{"text": ""}']}}
setblock 116 64 232 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Inventare mit"}','{"text": "Transportern"}','{"text": ""}']}}
fill 124 64 220 124 79 233 minecraft:light_gray_concrete
setblock 117 64 225 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 121 64 225 minecraft:chest[facing=south,type=single,waterlogged=false]
kw testworld use 117 64 225 east industrialforegoing:transporter
kw testworld use 121 64 225 west industrialforegoing:transporter
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
