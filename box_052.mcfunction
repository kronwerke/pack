# 052 mekanism_advanced/evap
#area 159 95 178 120
fill 159 64 95 178 95 120 minecraft:air
fill 159 60 95 178 62 120 minecraft:stone
fill 159 63 95 178 63 120 minecraft:light_gray_concrete
fill 163 64 101 178 83 101 minecraft:light_gray_concrete
fill 163 64 101 163 83 114 minecraft:light_gray_concrete
setblock 164 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 165 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 173 64 101 173 83 114 minecraft:light_gray_concrete
setblock 167 64 104 mekanism:thermal_evaporation_block
setblock 167 64 105 mekanism:thermal_evaporation_block
setblock 167 64 106 mekanism:thermal_evaporation_block
setblock 167 64 107 mekanism:thermal_evaporation_block
setblock 168 64 104 mekanism:thermal_evaporation_block
setblock 168 64 105 mekanism:thermal_evaporation_block
setblock 168 64 106 mekanism:thermal_evaporation_block
setblock 168 64 107 mekanism:thermal_evaporation_block
setblock 169 64 104 mekanism:thermal_evaporation_block
setblock 169 64 105 mekanism:thermal_evaporation_block
setblock 169 64 106 mekanism:thermal_evaporation_block
setblock 169 64 107 mekanism:thermal_evaporation_block
setblock 170 64 104 mekanism:thermal_evaporation_block
setblock 170 64 105 mekanism:thermal_evaporation_block
setblock 170 64 106 mekanism:thermal_evaporation_block
setblock 170 64 107 mekanism:thermal_evaporation_block
setblock 167 65 104 mekanism:thermal_evaporation_block
setblock 167 65 105 mekanism:thermal_evaporation_block
setblock 167 65 106 mekanism:thermal_evaporation_block
setblock 167 65 107 mekanism:thermal_evaporation_block
setblock 168 65 104 mekanism:thermal_evaporation_block
setblock 168 65 107 mekanism:thermal_evaporation_block
setblock 169 65 104 mekanism:thermal_evaporation_block
setblock 169 65 107 mekanism:thermal_evaporation_block
setblock 170 65 104 mekanism:thermal_evaporation_block
setblock 170 65 105 mekanism:thermal_evaporation_block
setblock 170 65 106 mekanism:thermal_evaporation_block
setblock 170 65 107 mekanism:thermal_evaporation_block
setblock 167 66 104 mekanism:thermal_evaporation_block
setblock 167 66 105 mekanism:thermal_evaporation_block
setblock 167 66 106 mekanism:thermal_evaporation_block
setblock 167 66 107 mekanism:thermal_evaporation_block
setblock 168 66 104 mekanism:thermal_evaporation_block
setblock 168 66 107 mekanism:thermal_evaporation_block
setblock 169 66 104 mekanism:thermal_evaporation_block
setblock 169 66 107 mekanism:thermal_evaporation_block
setblock 170 66 104 mekanism:thermal_evaporation_block
setblock 170 66 105 mekanism:thermal_evaporation_block
setblock 170 66 106 mekanism:thermal_evaporation_block
setblock 170 66 107 mekanism:thermal_evaporation_block
setblock 167 67 104 mekanism:thermal_evaporation_block
setblock 167 67 105 mekanism:thermal_evaporation_block
setblock 167 67 106 mekanism:thermal_evaporation_block
setblock 167 67 107 mekanism:thermal_evaporation_block
setblock 168 67 104 mekanism:thermal_evaporation_block
setblock 168 67 107 mekanism:thermal_evaporation_block
setblock 169 67 104 mekanism:thermal_evaporation_block
setblock 169 67 107 mekanism:thermal_evaporation_block
setblock 170 67 104 mekanism:thermal_evaporation_block
setblock 170 67 105 mekanism:thermal_evaporation_block
setblock 170 67 106 mekanism:thermal_evaporation_block
setblock 170 67 107 mekanism:thermal_evaporation_block
setblock 167 68 104 mekanism:thermal_evaporation_block
setblock 167 68 105 mekanism:thermal_evaporation_block
setblock 167 68 106 mekanism:thermal_evaporation_block
setblock 167 68 107 mekanism:thermal_evaporation_block
setblock 168 68 104 mekanism:thermal_evaporation_block
setblock 168 68 107 mekanism:thermal_evaporation_block
setblock 169 68 104 mekanism:thermal_evaporation_block
setblock 169 68 107 mekanism:thermal_evaporation_block
setblock 170 68 104 mekanism:thermal_evaporation_block
setblock 170 68 105 mekanism:thermal_evaporation_block
setblock 170 68 106 mekanism:thermal_evaporation_block
setblock 170 68 107 mekanism:thermal_evaporation_block
setblock 167 69 104 mekanism:thermal_evaporation_block
setblock 167 69 105 mekanism:thermal_evaporation_block
setblock 167 69 106 mekanism:thermal_evaporation_block
setblock 167 69 107 mekanism:thermal_evaporation_block
setblock 168 69 104 mekanism:thermal_evaporation_block
setblock 168 69 107 mekanism:thermal_evaporation_block
setblock 169 69 104 mekanism:thermal_evaporation_block
setblock 169 69 107 mekanism:thermal_evaporation_block
setblock 170 69 104 mekanism:thermal_evaporation_block
setblock 170 69 105 mekanism:thermal_evaporation_block
setblock 170 69 106 mekanism:thermal_evaporation_block
setblock 170 69 107 mekanism:thermal_evaporation_block
setblock 168 66 107 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 169 65 107 mekanism:thermal_evaporation_valve
setblock 170 65 106 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
