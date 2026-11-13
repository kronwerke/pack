# 058 antimatter/waste
#area 259 95 280 120
fill 259 64 95 280 91 120 minecraft:air
fill 259 60 95 280 62 120 minecraft:stone
fill 259 63 95 280 63 120 minecraft:light_gray_concrete
fill 263 64 101 280 79 101 minecraft:light_gray_concrete
fill 263 64 101 263 79 114 minecraft:light_gray_concrete
setblock 264 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 265 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 275 64 101 275 79 114 minecraft:light_gray_concrete
setblock 266 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 268 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 270 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 272 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
fill 266 64 105 272 64 105 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
