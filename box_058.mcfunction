# 058 antimatter/waste
#area 255 95 276 120
fill 255 64 95 276 91 120 minecraft:air
fill 255 60 95 276 62 120 minecraft:stone
fill 255 63 95 276 63 120 minecraft:light_gray_concrete
fill 259 64 101 276 79 101 minecraft:light_gray_concrete
fill 259 64 101 259 79 114 minecraft:light_gray_concrete
setblock 260 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 261 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 271 64 101 271 79 114 minecraft:light_gray_concrete
setblock 262 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 264 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 266 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 268 64 106 mekanism:solar_neutron_activator[facing=south,active=false]
fill 262 64 105 268 64 105 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
