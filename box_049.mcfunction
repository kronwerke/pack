# 049 mekanism_advanced/evap
#area 140 95 159 120
fill 140 64 95 159 95 120 minecraft:air
fill 140 60 95 159 62 120 minecraft:stone
fill 140 63 95 159 63 120 minecraft:light_gray_concrete
fill 144 64 101 159 83 101 minecraft:light_gray_concrete
fill 144 64 101 144 83 114 minecraft:light_gray_concrete
setblock 145 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "049"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 146 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 154 64 101 154 83 114 minecraft:light_gray_concrete
setblock 148 64 104 mekanism:thermal_evaporation_block
setblock 148 64 105 mekanism:thermal_evaporation_block
setblock 148 64 106 mekanism:thermal_evaporation_block
setblock 148 64 107 mekanism:thermal_evaporation_block
setblock 149 64 104 mekanism:thermal_evaporation_block
setblock 149 64 105 mekanism:thermal_evaporation_block
setblock 149 64 106 mekanism:thermal_evaporation_block
setblock 149 64 107 mekanism:thermal_evaporation_block
setblock 150 64 104 mekanism:thermal_evaporation_block
setblock 150 64 105 mekanism:thermal_evaporation_block
setblock 150 64 106 mekanism:thermal_evaporation_block
setblock 150 64 107 mekanism:thermal_evaporation_block
setblock 151 64 104 mekanism:thermal_evaporation_block
setblock 151 64 105 mekanism:thermal_evaporation_block
setblock 151 64 106 mekanism:thermal_evaporation_block
setblock 151 64 107 mekanism:thermal_evaporation_block
setblock 148 65 104 mekanism:thermal_evaporation_block
setblock 148 65 105 mekanism:thermal_evaporation_block
setblock 148 65 106 mekanism:thermal_evaporation_block
setblock 148 65 107 mekanism:thermal_evaporation_block
setblock 149 65 104 mekanism:thermal_evaporation_block
setblock 149 65 107 mekanism:thermal_evaporation_block
setblock 150 65 104 mekanism:thermal_evaporation_block
setblock 150 65 107 mekanism:thermal_evaporation_block
setblock 151 65 104 mekanism:thermal_evaporation_block
setblock 151 65 105 mekanism:thermal_evaporation_block
setblock 151 65 106 mekanism:thermal_evaporation_block
setblock 151 65 107 mekanism:thermal_evaporation_block
setblock 148 66 104 mekanism:thermal_evaporation_block
setblock 148 66 105 mekanism:thermal_evaporation_block
setblock 148 66 106 mekanism:thermal_evaporation_block
setblock 148 66 107 mekanism:thermal_evaporation_block
setblock 149 66 104 mekanism:thermal_evaporation_block
setblock 149 66 107 mekanism:thermal_evaporation_block
setblock 150 66 104 mekanism:thermal_evaporation_block
setblock 150 66 107 mekanism:thermal_evaporation_block
setblock 151 66 104 mekanism:thermal_evaporation_block
setblock 151 66 105 mekanism:thermal_evaporation_block
setblock 151 66 106 mekanism:thermal_evaporation_block
setblock 151 66 107 mekanism:thermal_evaporation_block
setblock 148 67 104 mekanism:thermal_evaporation_block
setblock 148 67 105 mekanism:thermal_evaporation_block
setblock 148 67 106 mekanism:thermal_evaporation_block
setblock 148 67 107 mekanism:thermal_evaporation_block
setblock 149 67 104 mekanism:thermal_evaporation_block
setblock 149 67 107 mekanism:thermal_evaporation_block
setblock 150 67 104 mekanism:thermal_evaporation_block
setblock 150 67 107 mekanism:thermal_evaporation_block
setblock 151 67 104 mekanism:thermal_evaporation_block
setblock 151 67 105 mekanism:thermal_evaporation_block
setblock 151 67 106 mekanism:thermal_evaporation_block
setblock 151 67 107 mekanism:thermal_evaporation_block
setblock 148 68 104 mekanism:thermal_evaporation_block
setblock 148 68 105 mekanism:thermal_evaporation_block
setblock 148 68 106 mekanism:thermal_evaporation_block
setblock 148 68 107 mekanism:thermal_evaporation_block
setblock 149 68 104 mekanism:thermal_evaporation_block
setblock 149 68 107 mekanism:thermal_evaporation_block
setblock 150 68 104 mekanism:thermal_evaporation_block
setblock 150 68 107 mekanism:thermal_evaporation_block
setblock 151 68 104 mekanism:thermal_evaporation_block
setblock 151 68 105 mekanism:thermal_evaporation_block
setblock 151 68 106 mekanism:thermal_evaporation_block
setblock 151 68 107 mekanism:thermal_evaporation_block
setblock 148 69 104 mekanism:thermal_evaporation_block
setblock 148 69 105 mekanism:thermal_evaporation_block
setblock 148 69 106 mekanism:thermal_evaporation_block
setblock 148 69 107 mekanism:thermal_evaporation_block
setblock 149 69 104 mekanism:thermal_evaporation_block
setblock 149 69 107 mekanism:thermal_evaporation_block
setblock 150 69 104 mekanism:thermal_evaporation_block
setblock 150 69 107 mekanism:thermal_evaporation_block
setblock 151 69 104 mekanism:thermal_evaporation_block
setblock 151 69 105 mekanism:thermal_evaporation_block
setblock 151 69 106 mekanism:thermal_evaporation_block
setblock 151 69 107 mekanism:thermal_evaporation_block
setblock 149 66 107 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 150 65 107 mekanism:thermal_evaporation_valve
setblock 151 65 106 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
