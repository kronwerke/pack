# 057 mekanism_advanced/evap
#area 191 97 210 122
fill 191 64 97 210 95 122 minecraft:air
fill 191 60 97 210 62 122 minecraft:stone
fill 191 63 97 210 63 122 minecraft:light_gray_concrete
fill 195 64 103 210 83 103 minecraft:light_gray_concrete
fill 195 64 103 195 83 116 minecraft:light_gray_concrete
setblock 196 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 197 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 205 64 103 205 83 116 minecraft:light_gray_concrete
setblock 199 64 106 mekanism:thermal_evaporation_block
setblock 199 64 107 mekanism:thermal_evaporation_block
setblock 199 64 108 mekanism:thermal_evaporation_block
setblock 199 64 109 mekanism:thermal_evaporation_block
setblock 200 64 106 mekanism:thermal_evaporation_block
setblock 200 64 107 mekanism:thermal_evaporation_block
setblock 200 64 108 mekanism:thermal_evaporation_block
setblock 200 64 109 mekanism:thermal_evaporation_block
setblock 201 64 106 mekanism:thermal_evaporation_block
setblock 201 64 107 mekanism:thermal_evaporation_block
setblock 201 64 108 mekanism:thermal_evaporation_block
setblock 201 64 109 mekanism:thermal_evaporation_block
setblock 202 64 106 mekanism:thermal_evaporation_block
setblock 202 64 107 mekanism:thermal_evaporation_block
setblock 202 64 108 mekanism:thermal_evaporation_block
setblock 202 64 109 mekanism:thermal_evaporation_block
setblock 199 65 106 mekanism:thermal_evaporation_block
setblock 199 65 107 mekanism:thermal_evaporation_block
setblock 199 65 108 mekanism:thermal_evaporation_block
setblock 199 65 109 mekanism:thermal_evaporation_block
setblock 200 65 106 mekanism:thermal_evaporation_block
setblock 200 65 109 mekanism:thermal_evaporation_block
setblock 201 65 106 mekanism:thermal_evaporation_block
setblock 201 65 109 mekanism:thermal_evaporation_block
setblock 202 65 106 mekanism:thermal_evaporation_block
setblock 202 65 107 mekanism:thermal_evaporation_block
setblock 202 65 108 mekanism:thermal_evaporation_block
setblock 202 65 109 mekanism:thermal_evaporation_block
setblock 199 66 106 mekanism:thermal_evaporation_block
setblock 199 66 107 mekanism:thermal_evaporation_block
setblock 199 66 108 mekanism:thermal_evaporation_block
setblock 199 66 109 mekanism:thermal_evaporation_block
setblock 200 66 106 mekanism:thermal_evaporation_block
setblock 200 66 109 mekanism:thermal_evaporation_block
setblock 201 66 106 mekanism:thermal_evaporation_block
setblock 201 66 109 mekanism:thermal_evaporation_block
setblock 202 66 106 mekanism:thermal_evaporation_block
setblock 202 66 107 mekanism:thermal_evaporation_block
setblock 202 66 108 mekanism:thermal_evaporation_block
setblock 202 66 109 mekanism:thermal_evaporation_block
setblock 199 67 106 mekanism:thermal_evaporation_block
setblock 199 67 107 mekanism:thermal_evaporation_block
setblock 199 67 108 mekanism:thermal_evaporation_block
setblock 199 67 109 mekanism:thermal_evaporation_block
setblock 200 67 106 mekanism:thermal_evaporation_block
setblock 200 67 109 mekanism:thermal_evaporation_block
setblock 201 67 106 mekanism:thermal_evaporation_block
setblock 201 67 109 mekanism:thermal_evaporation_block
setblock 202 67 106 mekanism:thermal_evaporation_block
setblock 202 67 107 mekanism:thermal_evaporation_block
setblock 202 67 108 mekanism:thermal_evaporation_block
setblock 202 67 109 mekanism:thermal_evaporation_block
setblock 199 68 106 mekanism:thermal_evaporation_block
setblock 199 68 107 mekanism:thermal_evaporation_block
setblock 199 68 108 mekanism:thermal_evaporation_block
setblock 199 68 109 mekanism:thermal_evaporation_block
setblock 200 68 106 mekanism:thermal_evaporation_block
setblock 200 68 109 mekanism:thermal_evaporation_block
setblock 201 68 106 mekanism:thermal_evaporation_block
setblock 201 68 109 mekanism:thermal_evaporation_block
setblock 202 68 106 mekanism:thermal_evaporation_block
setblock 202 68 107 mekanism:thermal_evaporation_block
setblock 202 68 108 mekanism:thermal_evaporation_block
setblock 202 68 109 mekanism:thermal_evaporation_block
setblock 199 69 106 mekanism:thermal_evaporation_block
setblock 199 69 107 mekanism:thermal_evaporation_block
setblock 199 69 108 mekanism:thermal_evaporation_block
setblock 199 69 109 mekanism:thermal_evaporation_block
setblock 200 69 106 mekanism:thermal_evaporation_block
setblock 200 69 109 mekanism:thermal_evaporation_block
setblock 201 69 106 mekanism:thermal_evaporation_block
setblock 201 69 109 mekanism:thermal_evaporation_block
setblock 202 69 106 mekanism:thermal_evaporation_block
setblock 202 69 107 mekanism:thermal_evaporation_block
setblock 202 69 108 mekanism:thermal_evaporation_block
setblock 202 69 109 mekanism:thermal_evaporation_block
setblock 200 66 109 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 201 65 109 mekanism:thermal_evaporation_valve
setblock 202 65 108 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
