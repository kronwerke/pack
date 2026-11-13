# 041 mekanism_advanced/evap
#area 140 65 159 90
fill 140 64 65 159 95 90 minecraft:air
fill 140 60 65 159 62 90 minecraft:stone
fill 140 63 65 159 63 90 minecraft:light_gray_concrete
fill 144 64 71 159 83 71 minecraft:light_gray_concrete
fill 144 64 71 144 83 84 minecraft:light_gray_concrete
setblock 145 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 146 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 154 64 71 154 83 84 minecraft:light_gray_concrete
setblock 148 64 74 mekanism:thermal_evaporation_block
setblock 148 64 75 mekanism:thermal_evaporation_block
setblock 148 64 76 mekanism:thermal_evaporation_block
setblock 148 64 77 mekanism:thermal_evaporation_block
setblock 149 64 74 mekanism:thermal_evaporation_block
setblock 149 64 75 mekanism:thermal_evaporation_block
setblock 149 64 76 mekanism:thermal_evaporation_block
setblock 149 64 77 mekanism:thermal_evaporation_block
setblock 150 64 74 mekanism:thermal_evaporation_block
setblock 150 64 75 mekanism:thermal_evaporation_block
setblock 150 64 76 mekanism:thermal_evaporation_block
setblock 150 64 77 mekanism:thermal_evaporation_block
setblock 151 64 74 mekanism:thermal_evaporation_block
setblock 151 64 75 mekanism:thermal_evaporation_block
setblock 151 64 76 mekanism:thermal_evaporation_block
setblock 151 64 77 mekanism:thermal_evaporation_block
setblock 148 65 74 mekanism:thermal_evaporation_block
setblock 148 65 75 mekanism:thermal_evaporation_block
setblock 148 65 76 mekanism:thermal_evaporation_block
setblock 148 65 77 mekanism:thermal_evaporation_block
setblock 149 65 74 mekanism:thermal_evaporation_block
setblock 149 65 77 mekanism:thermal_evaporation_block
setblock 150 65 74 mekanism:thermal_evaporation_block
setblock 150 65 77 mekanism:thermal_evaporation_block
setblock 151 65 74 mekanism:thermal_evaporation_block
setblock 151 65 75 mekanism:thermal_evaporation_block
setblock 151 65 76 mekanism:thermal_evaporation_block
setblock 151 65 77 mekanism:thermal_evaporation_block
setblock 148 66 74 mekanism:thermal_evaporation_block
setblock 148 66 75 mekanism:thermal_evaporation_block
setblock 148 66 76 mekanism:thermal_evaporation_block
setblock 148 66 77 mekanism:thermal_evaporation_block
setblock 149 66 74 mekanism:thermal_evaporation_block
setblock 149 66 77 mekanism:thermal_evaporation_block
setblock 150 66 74 mekanism:thermal_evaporation_block
setblock 150 66 77 mekanism:thermal_evaporation_block
setblock 151 66 74 mekanism:thermal_evaporation_block
setblock 151 66 75 mekanism:thermal_evaporation_block
setblock 151 66 76 mekanism:thermal_evaporation_block
setblock 151 66 77 mekanism:thermal_evaporation_block
setblock 148 67 74 mekanism:thermal_evaporation_block
setblock 148 67 75 mekanism:thermal_evaporation_block
setblock 148 67 76 mekanism:thermal_evaporation_block
setblock 148 67 77 mekanism:thermal_evaporation_block
setblock 149 67 74 mekanism:thermal_evaporation_block
setblock 149 67 77 mekanism:thermal_evaporation_block
setblock 150 67 74 mekanism:thermal_evaporation_block
setblock 150 67 77 mekanism:thermal_evaporation_block
setblock 151 67 74 mekanism:thermal_evaporation_block
setblock 151 67 75 mekanism:thermal_evaporation_block
setblock 151 67 76 mekanism:thermal_evaporation_block
setblock 151 67 77 mekanism:thermal_evaporation_block
setblock 148 68 74 mekanism:thermal_evaporation_block
setblock 148 68 75 mekanism:thermal_evaporation_block
setblock 148 68 76 mekanism:thermal_evaporation_block
setblock 148 68 77 mekanism:thermal_evaporation_block
setblock 149 68 74 mekanism:thermal_evaporation_block
setblock 149 68 77 mekanism:thermal_evaporation_block
setblock 150 68 74 mekanism:thermal_evaporation_block
setblock 150 68 77 mekanism:thermal_evaporation_block
setblock 151 68 74 mekanism:thermal_evaporation_block
setblock 151 68 75 mekanism:thermal_evaporation_block
setblock 151 68 76 mekanism:thermal_evaporation_block
setblock 151 68 77 mekanism:thermal_evaporation_block
setblock 148 69 74 mekanism:thermal_evaporation_block
setblock 148 69 75 mekanism:thermal_evaporation_block
setblock 148 69 76 mekanism:thermal_evaporation_block
setblock 148 69 77 mekanism:thermal_evaporation_block
setblock 149 69 74 mekanism:thermal_evaporation_block
setblock 149 69 77 mekanism:thermal_evaporation_block
setblock 150 69 74 mekanism:thermal_evaporation_block
setblock 150 69 77 mekanism:thermal_evaporation_block
setblock 151 69 74 mekanism:thermal_evaporation_block
setblock 151 69 75 mekanism:thermal_evaporation_block
setblock 151 69 76 mekanism:thermal_evaporation_block
setblock 151 69 77 mekanism:thermal_evaporation_block
setblock 149 66 77 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 150 65 77 mekanism:thermal_evaporation_valve
setblock 151 65 76 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
