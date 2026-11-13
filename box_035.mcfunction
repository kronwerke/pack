# 035 mekanism_advanced/evap
#area 125 65 144 90
fill 125 64 65 144 95 90 minecraft:air
fill 125 60 65 144 62 90 minecraft:stone
fill 125 63 65 144 63 90 minecraft:light_gray_concrete
fill 129 64 71 144 83 71 minecraft:light_gray_concrete
fill 129 64 71 129 83 84 minecraft:light_gray_concrete
setblock 130 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 131 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 139 64 71 139 83 84 minecraft:light_gray_concrete
setblock 133 64 74 mekanism:thermal_evaporation_block
setblock 133 64 75 mekanism:thermal_evaporation_block
setblock 133 64 76 mekanism:thermal_evaporation_block
setblock 133 64 77 mekanism:thermal_evaporation_block
setblock 134 64 74 mekanism:thermal_evaporation_block
setblock 134 64 75 mekanism:thermal_evaporation_block
setblock 134 64 76 mekanism:thermal_evaporation_block
setblock 134 64 77 mekanism:thermal_evaporation_block
setblock 135 64 74 mekanism:thermal_evaporation_block
setblock 135 64 75 mekanism:thermal_evaporation_block
setblock 135 64 76 mekanism:thermal_evaporation_block
setblock 135 64 77 mekanism:thermal_evaporation_block
setblock 136 64 74 mekanism:thermal_evaporation_block
setblock 136 64 75 mekanism:thermal_evaporation_block
setblock 136 64 76 mekanism:thermal_evaporation_block
setblock 136 64 77 mekanism:thermal_evaporation_block
setblock 133 65 74 mekanism:thermal_evaporation_block
setblock 133 65 75 mekanism:thermal_evaporation_block
setblock 133 65 76 mekanism:thermal_evaporation_block
setblock 133 65 77 mekanism:thermal_evaporation_block
setblock 134 65 74 mekanism:thermal_evaporation_block
setblock 134 65 77 mekanism:thermal_evaporation_block
setblock 135 65 74 mekanism:thermal_evaporation_block
setblock 135 65 77 mekanism:thermal_evaporation_block
setblock 136 65 74 mekanism:thermal_evaporation_block
setblock 136 65 75 mekanism:thermal_evaporation_block
setblock 136 65 76 mekanism:thermal_evaporation_block
setblock 136 65 77 mekanism:thermal_evaporation_block
setblock 133 66 74 mekanism:thermal_evaporation_block
setblock 133 66 75 mekanism:thermal_evaporation_block
setblock 133 66 76 mekanism:thermal_evaporation_block
setblock 133 66 77 mekanism:thermal_evaporation_block
setblock 134 66 74 mekanism:thermal_evaporation_block
setblock 134 66 77 mekanism:thermal_evaporation_block
setblock 135 66 74 mekanism:thermal_evaporation_block
setblock 135 66 77 mekanism:thermal_evaporation_block
setblock 136 66 74 mekanism:thermal_evaporation_block
setblock 136 66 75 mekanism:thermal_evaporation_block
setblock 136 66 76 mekanism:thermal_evaporation_block
setblock 136 66 77 mekanism:thermal_evaporation_block
setblock 133 67 74 mekanism:thermal_evaporation_block
setblock 133 67 75 mekanism:thermal_evaporation_block
setblock 133 67 76 mekanism:thermal_evaporation_block
setblock 133 67 77 mekanism:thermal_evaporation_block
setblock 134 67 74 mekanism:thermal_evaporation_block
setblock 134 67 77 mekanism:thermal_evaporation_block
setblock 135 67 74 mekanism:thermal_evaporation_block
setblock 135 67 77 mekanism:thermal_evaporation_block
setblock 136 67 74 mekanism:thermal_evaporation_block
setblock 136 67 75 mekanism:thermal_evaporation_block
setblock 136 67 76 mekanism:thermal_evaporation_block
setblock 136 67 77 mekanism:thermal_evaporation_block
setblock 133 68 74 mekanism:thermal_evaporation_block
setblock 133 68 75 mekanism:thermal_evaporation_block
setblock 133 68 76 mekanism:thermal_evaporation_block
setblock 133 68 77 mekanism:thermal_evaporation_block
setblock 134 68 74 mekanism:thermal_evaporation_block
setblock 134 68 77 mekanism:thermal_evaporation_block
setblock 135 68 74 mekanism:thermal_evaporation_block
setblock 135 68 77 mekanism:thermal_evaporation_block
setblock 136 68 74 mekanism:thermal_evaporation_block
setblock 136 68 75 mekanism:thermal_evaporation_block
setblock 136 68 76 mekanism:thermal_evaporation_block
setblock 136 68 77 mekanism:thermal_evaporation_block
setblock 133 69 74 mekanism:thermal_evaporation_block
setblock 133 69 75 mekanism:thermal_evaporation_block
setblock 133 69 76 mekanism:thermal_evaporation_block
setblock 133 69 77 mekanism:thermal_evaporation_block
setblock 134 69 74 mekanism:thermal_evaporation_block
setblock 134 69 77 mekanism:thermal_evaporation_block
setblock 135 69 74 mekanism:thermal_evaporation_block
setblock 135 69 77 mekanism:thermal_evaporation_block
setblock 136 69 74 mekanism:thermal_evaporation_block
setblock 136 69 75 mekanism:thermal_evaporation_block
setblock 136 69 76 mekanism:thermal_evaporation_block
setblock 136 69 77 mekanism:thermal_evaporation_block
setblock 134 66 77 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 135 65 77 mekanism:thermal_evaporation_valve
setblock 136 65 76 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
