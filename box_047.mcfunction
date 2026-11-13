# 047 antimatter/waste
#area 240 65 261 90
fill 240 64 65 261 91 90 minecraft:air
fill 240 60 65 261 62 90 minecraft:stone
fill 240 63 65 261 63 90 minecraft:light_gray_concrete
fill 244 64 71 261 79 71 minecraft:light_gray_concrete
fill 244 64 71 244 79 84 minecraft:light_gray_concrete
setblock 245 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 246 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 256 64 71 256 79 84 minecraft:light_gray_concrete
setblock 247 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 249 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 251 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 253 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
fill 247 64 75 253 64 75 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
