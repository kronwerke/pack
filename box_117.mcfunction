# 117 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
#area 115 275 194 304
fill 115 64 275 148 95 304 minecraft:air
fill 149 64 275 182 95 304 minecraft:air
fill 183 64 275 194 95 304 minecraft:air
fill 115 60 275 194 62 304 minecraft:stone
fill 115 63 275 194 63 304 minecraft:light_gray_concrete
fill 119 64 281 194 83 281 minecraft:light_gray_concrete
fill 119 64 281 119 83 298 minecraft:light_gray_concrete
setblock 120 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 121 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 129 64 281 129 83 298 minecraft:light_gray_concrete
setblock 123 64 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 286 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 286 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 123 65 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 286 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 286 pneumaticcraft:pressure_chamber_glass
setblock 124 64 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 65 285 pneumaticcraft:pressure_chamber_glass
setblock 124 65 287 pneumaticcraft:pressure_chamber_glass
setblock 124 66 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 66 286 pneumaticcraft:pressure_chamber_glass
setblock 124 66 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 286 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 286 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 125 65 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 286 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 123 65 287 up pneumaticcraft:pressure_chamber_wall
execute if block 125 65 286 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 130 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 131 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 139 64 281 139 83 298 minecraft:light_gray_concrete
setblock 134 64 285 pneumaticcraft:refinery[facing=south]
setblock 134 65 285 pneumaticcraft:refinery_output[facing=south]
setblock 134 66 285 pneumaticcraft:refinery_output[facing=south]
setblock 134 67 285 pneumaticcraft:refinery_output[facing=south]
setblock 134 68 285 pneumaticcraft:refinery_output[facing=south]
setblock 140 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 141 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 149 64 281 149 83 298 minecraft:light_gray_concrete
setblock 143 64 286 pneumaticcraft:pressure_tube
setblock 144 64 286 pneumaticcraft:pressure_tube
setblock 145 64 286 pneumaticcraft:vortex_tube[facing=east]
setblock 150 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 151 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 159 64 281 159 83 298 minecraft:light_gray_concrete
setblock 154 64 285 pneumaticcraft:elevator_base
fill 154 65 285 154 68 285 pneumaticcraft:elevator_frame
fill 155 64 285 155 67 285 minecraft:stone_bricks
setblock 155 68 285 pneumaticcraft:elevator_caller[facing=south]
setblock 160 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 161 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
fill 169 64 281 169 83 298 minecraft:light_gray_concrete
fill 163 64 286 165 64 286 pneumaticcraft:pressure_tube
kw testworld use 163 64 286 up pneumaticcraft:safety_tube_module
kw testworld use 165 64 286 up pneumaticcraft:pressure_gauge_module
setblock 170 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 171 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 179 64 281 179 83 298 minecraft:light_gray_concrete
setblock 174 64 286 minecraft:magma_block
setblock 174 65 286 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 180 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "117.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 181 64 297 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 189 64 281 189 83 298 minecraft:light_gray_concrete
setblock 184 64 286 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
