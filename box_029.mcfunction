# 029 mekanism_advanced/evap
#area 107 63 126 88
fill 107 64 63 126 95 88 minecraft:air
fill 107 60 63 126 62 88 minecraft:stone
fill 107 63 63 126 63 88 minecraft:light_gray_concrete
fill 111 64 69 126 83 69 minecraft:light_gray_concrete
fill 111 64 69 111 83 82 minecraft:light_gray_concrete
setblock 112 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "029"}','{"text": "mekanism_advanced"}','{"text": "evap"}','{"text": ""}']}}
setblock 113 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "thermal"}','{"text": "evaporation"}','{"text": "tower"}','{"text": ""}']}}
fill 121 64 69 121 83 82 minecraft:light_gray_concrete
setblock 115 64 72 mekanism:thermal_evaporation_block
setblock 115 64 73 mekanism:thermal_evaporation_block
setblock 115 64 74 mekanism:thermal_evaporation_block
setblock 115 64 75 mekanism:thermal_evaporation_block
setblock 116 64 72 mekanism:thermal_evaporation_block
setblock 116 64 73 mekanism:thermal_evaporation_block
setblock 116 64 74 mekanism:thermal_evaporation_block
setblock 116 64 75 mekanism:thermal_evaporation_block
setblock 117 64 72 mekanism:thermal_evaporation_block
setblock 117 64 73 mekanism:thermal_evaporation_block
setblock 117 64 74 mekanism:thermal_evaporation_block
setblock 117 64 75 mekanism:thermal_evaporation_block
setblock 118 64 72 mekanism:thermal_evaporation_block
setblock 118 64 73 mekanism:thermal_evaporation_block
setblock 118 64 74 mekanism:thermal_evaporation_block
setblock 118 64 75 mekanism:thermal_evaporation_block
setblock 115 65 72 mekanism:thermal_evaporation_block
setblock 115 65 73 mekanism:thermal_evaporation_block
setblock 115 65 74 mekanism:thermal_evaporation_block
setblock 115 65 75 mekanism:thermal_evaporation_block
setblock 116 65 72 mekanism:thermal_evaporation_block
setblock 116 65 75 mekanism:thermal_evaporation_block
setblock 117 65 72 mekanism:thermal_evaporation_block
setblock 117 65 75 mekanism:thermal_evaporation_block
setblock 118 65 72 mekanism:thermal_evaporation_block
setblock 118 65 73 mekanism:thermal_evaporation_block
setblock 118 65 74 mekanism:thermal_evaporation_block
setblock 118 65 75 mekanism:thermal_evaporation_block
setblock 115 66 72 mekanism:thermal_evaporation_block
setblock 115 66 73 mekanism:thermal_evaporation_block
setblock 115 66 74 mekanism:thermal_evaporation_block
setblock 115 66 75 mekanism:thermal_evaporation_block
setblock 116 66 72 mekanism:thermal_evaporation_block
setblock 116 66 75 mekanism:thermal_evaporation_block
setblock 117 66 72 mekanism:thermal_evaporation_block
setblock 117 66 75 mekanism:thermal_evaporation_block
setblock 118 66 72 mekanism:thermal_evaporation_block
setblock 118 66 73 mekanism:thermal_evaporation_block
setblock 118 66 74 mekanism:thermal_evaporation_block
setblock 118 66 75 mekanism:thermal_evaporation_block
setblock 115 67 72 mekanism:thermal_evaporation_block
setblock 115 67 73 mekanism:thermal_evaporation_block
setblock 115 67 74 mekanism:thermal_evaporation_block
setblock 115 67 75 mekanism:thermal_evaporation_block
setblock 116 67 72 mekanism:thermal_evaporation_block
setblock 116 67 75 mekanism:thermal_evaporation_block
setblock 117 67 72 mekanism:thermal_evaporation_block
setblock 117 67 75 mekanism:thermal_evaporation_block
setblock 118 67 72 mekanism:thermal_evaporation_block
setblock 118 67 73 mekanism:thermal_evaporation_block
setblock 118 67 74 mekanism:thermal_evaporation_block
setblock 118 67 75 mekanism:thermal_evaporation_block
setblock 115 68 72 mekanism:thermal_evaporation_block
setblock 115 68 73 mekanism:thermal_evaporation_block
setblock 115 68 74 mekanism:thermal_evaporation_block
setblock 115 68 75 mekanism:thermal_evaporation_block
setblock 116 68 72 mekanism:thermal_evaporation_block
setblock 116 68 75 mekanism:thermal_evaporation_block
setblock 117 68 72 mekanism:thermal_evaporation_block
setblock 117 68 75 mekanism:thermal_evaporation_block
setblock 118 68 72 mekanism:thermal_evaporation_block
setblock 118 68 73 mekanism:thermal_evaporation_block
setblock 118 68 74 mekanism:thermal_evaporation_block
setblock 118 68 75 mekanism:thermal_evaporation_block
setblock 115 69 72 mekanism:thermal_evaporation_block
setblock 115 69 73 mekanism:thermal_evaporation_block
setblock 115 69 74 mekanism:thermal_evaporation_block
setblock 115 69 75 mekanism:thermal_evaporation_block
setblock 116 69 72 mekanism:thermal_evaporation_block
setblock 116 69 75 mekanism:thermal_evaporation_block
setblock 117 69 72 mekanism:thermal_evaporation_block
setblock 117 69 75 mekanism:thermal_evaporation_block
setblock 118 69 72 mekanism:thermal_evaporation_block
setblock 118 69 73 mekanism:thermal_evaporation_block
setblock 118 69 74 mekanism:thermal_evaporation_block
setblock 118 69 75 mekanism:thermal_evaporation_block
setblock 116 66 75 mekanism:thermal_evaporation_controller[facing=south,active=false]
setblock 117 65 75 mekanism:thermal_evaporation_valve
setblock 118 65 74 mekanism:thermal_evaporation_valve
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
