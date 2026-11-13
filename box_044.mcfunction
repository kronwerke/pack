# 044 antimatter/waste
#area 225 65 246 90
fill 225 64 65 246 91 90 minecraft:air
fill 225 60 65 246 62 90 minecraft:stone
fill 225 63 65 246 63 90 minecraft:light_gray_concrete
fill 229 64 71 246 79 71 minecraft:light_gray_concrete
fill 229 64 71 229 79 84 minecraft:light_gray_concrete
setblock 230 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 231 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 241 64 71 241 79 84 minecraft:light_gray_concrete
setblock 232 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 234 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 236 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 238 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
fill 232 64 75 238 64 75 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
