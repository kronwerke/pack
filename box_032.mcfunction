# 032 mekanism_advanced/evap
#area 107 65 126 90
fill 107 64 65 126 95 90 minecraft:air
fill 107 60 65 126 62 90 minecraft:stone
fill 107 63 65 126 63 90 minecraft:light_gray_concrete
fill 111 64 71 126 83 71 minecraft:light_gray_concrete
fill 111 64 71 111 83 84 minecraft:light_gray_concrete
setblock 112 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 113 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 121 64 71 121 83 84 minecraft:light_gray_concrete
setblock 115 64 74 mekanism:thermal_evaporation_block
setblock 115 64 75 mekanism:thermal_evaporation_block
setblock 115 64 76 mekanism:thermal_evaporation_block
setblock 115 64 77 mekanism:thermal_evaporation_block
setblock 116 64 74 mekanism:thermal_evaporation_block
setblock 116 64 75 mekanism:thermal_evaporation_block
setblock 116 64 76 mekanism:thermal_evaporation_block
setblock 116 64 77 mekanism:thermal_evaporation_block
setblock 117 64 74 mekanism:thermal_evaporation_block
setblock 117 64 75 mekanism:thermal_evaporation_block
setblock 117 64 76 mekanism:thermal_evaporation_block
setblock 117 64 77 mekanism:thermal_evaporation_block
setblock 118 64 74 mekanism:thermal_evaporation_block
setblock 118 64 75 mekanism:thermal_evaporation_block
setblock 118 64 76 mekanism:thermal_evaporation_block
setblock 118 64 77 mekanism:thermal_evaporation_block
setblock 115 65 74 mekanism:thermal_evaporation_block
setblock 115 65 75 mekanism:thermal_evaporation_block
setblock 115 65 76 mekanism:thermal_evaporation_block
setblock 115 65 77 mekanism:thermal_evaporation_block
setblock 116 65 74 mekanism:thermal_evaporation_block
setblock 116 65 77 mekanism:thermal_evaporation_block
setblock 117 65 74 mekanism:thermal_evaporation_block
setblock 117 65 77 mekanism:thermal_evaporation_block
setblock 118 65 74 mekanism:thermal_evaporation_block
setblock 118 65 75 mekanism:thermal_evaporation_block
setblock 118 65 76 mekanism:thermal_evaporation_block
setblock 118 65 77 mekanism:thermal_evaporation_block
setblock 115 66 74 mekanism:thermal_evaporation_block
setblock 115 66 75 mekanism:thermal_evaporation_block
setblock 115 66 76 mekanism:thermal_evaporation_block
setblock 115 66 77 mekanism:thermal_evaporation_block
setblock 116 66 74 mekanism:thermal_evaporation_block
setblock 116 66 77 mekanism:thermal_evaporation_block
setblock 117 66 74 mekanism:thermal_evaporation_block
setblock 117 66 77 mekanism:thermal_evaporation_block
setblock 118 66 74 mekanism:thermal_evaporation_block
setblock 118 66 75 mekanism:thermal_evaporation_block
setblock 118 66 76 mekanism:thermal_evaporation_block
setblock 118 66 77 mekanism:thermal_evaporation_block
setblock 115 67 74 mekanism:thermal_evaporation_block
setblock 115 67 75 mekanism:thermal_evaporation_block
setblock 115 67 76 mekanism:thermal_evaporation_block
setblock 115 67 77 mekanism:thermal_evaporation_block
setblock 116 67 74 mekanism:thermal_evaporation_block
setblock 116 67 77 mekanism:thermal_evaporation_block
setblock 117 67 74 mekanism:thermal_evaporation_block
setblock 117 67 77 mekanism:thermal_evaporation_block
setblock 118 67 74 mekanism:thermal_evaporation_block
setblock 118 67 75 mekanism:thermal_evaporation_block
setblock 118 67 76 mekanism:thermal_evaporation_block
setblock 118 67 77 mekanism:thermal_evaporation_block
setblock 115 68 74 mekanism:thermal_evaporation_block
setblock 115 68 75 mekanism:thermal_evaporation_block
setblock 115 68 76 mekanism:thermal_evaporation_block
setblock 115 68 77 mekanism:thermal_evaporation_block
setblock 116 68 74 mekanism:thermal_evaporation_block
setblock 116 68 77 mekanism:thermal_evaporation_block
setblock 117 68 74 mekanism:thermal_evaporation_block
setblock 117 68 77 mekanism:thermal_evaporation_block
setblock 118 68 74 mekanism:thermal_evaporation_block
setblock 118 68 75 mekanism:thermal_evaporation_block
setblock 118 68 76 mekanism:thermal_evaporation_block
setblock 118 68 77 mekanism:thermal_evaporation_block
setblock 115 69 74 mekanism:thermal_evaporation_block
setblock 115 69 75 mekanism:thermal_evaporation_block
setblock 115 69 76 mekanism:thermal_evaporation_block
setblock 115 69 77 mekanism:thermal_evaporation_block
setblock 116 69 74 mekanism:thermal_evaporation_block
setblock 116 69 77 mekanism:thermal_evaporation_block
setblock 117 69 74 mekanism:thermal_evaporation_block
setblock 117 69 77 mekanism:thermal_evaporation_block
setblock 118 69 74 mekanism:thermal_evaporation_block
setblock 118 69 75 mekanism:thermal_evaporation_block
setblock 118 69 76 mekanism:thermal_evaporation_block
setblock 118 69 77 mekanism:thermal_evaporation_block
setblock 116 66 77 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 117 65 77 mekanism:thermal_evaporation_valve
setblock 118 65 76 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
