# 064 antimatter/waste
#area 306 97 327 122
fill 306 64 97 327 91 122 minecraft:air
fill 306 60 97 327 62 122 minecraft:stone
fill 306 63 97 327 63 122 minecraft:light_gray_concrete
fill 310 64 103 327 79 103 minecraft:light_gray_concrete
fill 310 64 103 310 79 116 minecraft:light_gray_concrete
setblock 311 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 312 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 322 64 103 322 79 116 minecraft:light_gray_concrete
setblock 313 64 108 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 315 64 108 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 317 64 108 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 319 64 108 mekanism:solar_neutron_activator[facing=south,active=false]
fill 313 64 107 319 64 107 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
