# 052 mekanism_advanced/evap
#area 155 95 174 120
fill 155 64 95 174 95 120 minecraft:air
fill 155 60 95 174 62 120 minecraft:stone
fill 155 63 95 174 63 120 minecraft:light_gray_concrete
fill 159 64 101 174 83 101 minecraft:light_gray_concrete
fill 159 64 101 159 83 114 minecraft:light_gray_concrete
setblock 160 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 161 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 169 64 101 169 83 114 minecraft:light_gray_concrete
setblock 163 64 104 mekanism:thermal_evaporation_block
setblock 163 64 105 mekanism:thermal_evaporation_block
setblock 163 64 106 mekanism:thermal_evaporation_block
setblock 163 64 107 mekanism:thermal_evaporation_block
setblock 164 64 104 mekanism:thermal_evaporation_block
setblock 164 64 105 mekanism:thermal_evaporation_block
setblock 164 64 106 mekanism:thermal_evaporation_block
setblock 164 64 107 mekanism:thermal_evaporation_block
setblock 165 64 104 mekanism:thermal_evaporation_block
setblock 165 64 105 mekanism:thermal_evaporation_block
setblock 165 64 106 mekanism:thermal_evaporation_block
setblock 165 64 107 mekanism:thermal_evaporation_block
setblock 166 64 104 mekanism:thermal_evaporation_block
setblock 166 64 105 mekanism:thermal_evaporation_block
setblock 166 64 106 mekanism:thermal_evaporation_block
setblock 166 64 107 mekanism:thermal_evaporation_block
setblock 163 65 104 mekanism:thermal_evaporation_block
setblock 163 65 105 mekanism:thermal_evaporation_block
setblock 163 65 106 mekanism:thermal_evaporation_block
setblock 163 65 107 mekanism:thermal_evaporation_block
setblock 164 65 104 mekanism:thermal_evaporation_block
setblock 164 65 107 mekanism:thermal_evaporation_block
setblock 165 65 104 mekanism:thermal_evaporation_block
setblock 165 65 107 mekanism:thermal_evaporation_block
setblock 166 65 104 mekanism:thermal_evaporation_block
setblock 166 65 105 mekanism:thermal_evaporation_block
setblock 166 65 106 mekanism:thermal_evaporation_block
setblock 166 65 107 mekanism:thermal_evaporation_block
setblock 163 66 104 mekanism:thermal_evaporation_block
setblock 163 66 105 mekanism:thermal_evaporation_block
setblock 163 66 106 mekanism:thermal_evaporation_block
setblock 163 66 107 mekanism:thermal_evaporation_block
setblock 164 66 104 mekanism:thermal_evaporation_block
setblock 164 66 107 mekanism:thermal_evaporation_block
setblock 165 66 104 mekanism:thermal_evaporation_block
setblock 165 66 107 mekanism:thermal_evaporation_block
setblock 166 66 104 mekanism:thermal_evaporation_block
setblock 166 66 105 mekanism:thermal_evaporation_block
setblock 166 66 106 mekanism:thermal_evaporation_block
setblock 166 66 107 mekanism:thermal_evaporation_block
setblock 163 67 104 mekanism:thermal_evaporation_block
setblock 163 67 105 mekanism:thermal_evaporation_block
setblock 163 67 106 mekanism:thermal_evaporation_block
setblock 163 67 107 mekanism:thermal_evaporation_block
setblock 164 67 104 mekanism:thermal_evaporation_block
setblock 164 67 107 mekanism:thermal_evaporation_block
setblock 165 67 104 mekanism:thermal_evaporation_block
setblock 165 67 107 mekanism:thermal_evaporation_block
setblock 166 67 104 mekanism:thermal_evaporation_block
setblock 166 67 105 mekanism:thermal_evaporation_block
setblock 166 67 106 mekanism:thermal_evaporation_block
setblock 166 67 107 mekanism:thermal_evaporation_block
setblock 163 68 104 mekanism:thermal_evaporation_block
setblock 163 68 105 mekanism:thermal_evaporation_block
setblock 163 68 106 mekanism:thermal_evaporation_block
setblock 163 68 107 mekanism:thermal_evaporation_block
setblock 164 68 104 mekanism:thermal_evaporation_block
setblock 164 68 107 mekanism:thermal_evaporation_block
setblock 165 68 104 mekanism:thermal_evaporation_block
setblock 165 68 107 mekanism:thermal_evaporation_block
setblock 166 68 104 mekanism:thermal_evaporation_block
setblock 166 68 105 mekanism:thermal_evaporation_block
setblock 166 68 106 mekanism:thermal_evaporation_block
setblock 166 68 107 mekanism:thermal_evaporation_block
setblock 163 69 104 mekanism:thermal_evaporation_block
setblock 163 69 105 mekanism:thermal_evaporation_block
setblock 163 69 106 mekanism:thermal_evaporation_block
setblock 163 69 107 mekanism:thermal_evaporation_block
setblock 164 69 104 mekanism:thermal_evaporation_block
setblock 164 69 107 mekanism:thermal_evaporation_block
setblock 165 69 104 mekanism:thermal_evaporation_block
setblock 165 69 107 mekanism:thermal_evaporation_block
setblock 166 69 104 mekanism:thermal_evaporation_block
setblock 166 69 105 mekanism:thermal_evaporation_block
setblock 166 69 106 mekanism:thermal_evaporation_block
setblock 166 69 107 mekanism:thermal_evaporation_block
setblock 164 66 107 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 165 65 107 mekanism:thermal_evaporation_valve
setblock 166 65 106 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
