# 038 antimatter/waste
#area 207 65 228 90
fill 207 64 65 228 91 90 minecraft:air
fill 207 60 65 228 62 90 minecraft:stone
fill 207 63 65 228 63 90 minecraft:light_gray_concrete
fill 211 64 71 228 79 71 minecraft:light_gray_concrete
fill 211 64 71 211 79 84 minecraft:light_gray_concrete
setblock 212 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "038"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 213 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 223 64 71 223 79 84 minecraft:light_gray_concrete
setblock 214 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 216 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 218 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 220 64 76 mekanism:solar_neutron_activator[facing=south,active=false]
fill 214 64 75 220 64 75 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
