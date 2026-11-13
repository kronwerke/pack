# 166 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
#area 115 319 194 348
fill 115 64 319 148 95 348 minecraft:air
fill 149 64 319 182 95 348 minecraft:air
fill 183 64 319 194 95 348 minecraft:air
fill 115 60 319 194 62 348 minecraft:stone
fill 115 63 319 194 63 348 minecraft:light_gray_concrete
fill 119 64 325 194 83 325 minecraft:light_gray_concrete
fill 119 64 325 119 83 342 minecraft:light_gray_concrete
setblock 120 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 121 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 129 64 325 129 83 342 minecraft:light_gray_concrete
setblock 123 64 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 330 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 331 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 330 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 123 65 331 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 330 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 330 pneumaticcraft:pressure_chamber_glass
setblock 124 64 331 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 65 329 pneumaticcraft:pressure_chamber_glass
setblock 124 65 331 pneumaticcraft:pressure_chamber_glass
setblock 124 66 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 66 330 pneumaticcraft:pressure_chamber_glass
setblock 124 66 331 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 330 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 331 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 330 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 125 65 331 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 330 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 331 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 123 65 331 up pneumaticcraft:pressure_chamber_wall
execute if block 125 65 330 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 130 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 131 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 139 64 325 139 83 342 minecraft:light_gray_concrete
setblock 134 64 329 pneumaticcraft:refinery[facing=south]
setblock 134 65 329 pneumaticcraft:refinery_output[facing=south]
setblock 134 66 329 pneumaticcraft:refinery_output[facing=south]
setblock 134 67 329 pneumaticcraft:refinery_output[facing=south]
setblock 134 68 329 pneumaticcraft:refinery_output[facing=south]
setblock 140 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 141 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 149 64 325 149 83 342 minecraft:light_gray_concrete
setblock 143 64 330 pneumaticcraft:pressure_tube
setblock 144 64 330 pneumaticcraft:pressure_tube
setblock 145 64 330 pneumaticcraft:vortex_tube[facing=east]
setblock 150 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 151 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 159 64 325 159 83 342 minecraft:light_gray_concrete
setblock 154 64 329 pneumaticcraft:elevator_base
fill 154 65 329 154 68 329 pneumaticcraft:elevator_frame
fill 155 64 329 155 67 329 minecraft:stone_bricks
setblock 155 68 329 pneumaticcraft:elevator_caller[facing=south]
setblock 160 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 161 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
fill 169 64 325 169 83 342 minecraft:light_gray_concrete
fill 163 64 330 165 64 330 pneumaticcraft:pressure_tube
kw testworld use 163 64 330 up pneumaticcraft:safety_tube_module
kw testworld use 165 64 330 up pneumaticcraft:pressure_gauge_module
setblock 170 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 171 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 179 64 325 179 83 342 minecraft:light_gray_concrete
setblock 174 64 330 minecraft:magma_block
setblock 174 65 330 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 180 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "166.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 181 64 341 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 189 64 325 189 83 342 minecraft:light_gray_concrete
setblock 184 64 330 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
