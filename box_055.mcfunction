# 055 antimatter/waste
#area 240 95 261 120
fill 240 64 95 261 91 120 minecraft:air
fill 240 60 95 261 62 120 minecraft:stone
fill 240 63 95 261 63 120 minecraft:light_gray_concrete
fill 244 64 101 261 79 101 minecraft:light_gray_concrete
fill 244 64 101 244 79 114 minecraft:light_gray_concrete
setblock 245 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 246 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 256 64 101 256 79 114 minecraft:light_gray_concrete
setblock 247 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 249 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 251 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 253 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
fill 247 64 105 253 64 105 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
