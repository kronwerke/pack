# 035 antimatter/waste
#area 207 63 228 88
fill 207 64 63 228 91 88 minecraft:air
fill 207 60 63 228 62 88 minecraft:stone
fill 207 63 63 228 63 88 minecraft:light_gray_concrete
fill 211 64 69 228 79 69 minecraft:light_gray_concrete
fill 211 64 69 211 79 82 minecraft:light_gray_concrete
setblock 212 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "antimatter"}','{"text": "waste"}','{"text": ""}']}}
setblock 213 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "row of solar"}','{"text": "neutron"}','{"text": "activators"}','{"text": "under open sky"}']}}
fill 223 64 69 223 79 82 minecraft:light_gray_concrete
setblock 214 64 74 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 216 64 74 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 218 64 74 mekanism:solar_neutron_activator[facing=south,active=false]
setblock 220 64 74 mekanism:solar_neutron_activator[facing=south,active=false]
fill 214 64 73 220 64 73 mekanism:basic_pressurized_tube
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
