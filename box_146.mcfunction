# 146 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
#area 115 313 194 342
fill 115 64 313 148 95 342 minecraft:air
fill 149 64 313 182 95 342 minecraft:air
fill 183 64 313 194 95 342 minecraft:air
fill 115 60 313 194 62 342 minecraft:stone
fill 115 63 313 194 63 342 minecraft:light_gray_concrete
fill 119 64 319 194 83 319 minecraft:light_gray_concrete
fill 119 64 319 119 83 336 minecraft:light_gray_concrete
setblock 120 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 121 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 129 64 319 129 83 336 minecraft:light_gray_concrete
setblock 123 64 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 324 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 325 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 324 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 123 65 325 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 324 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 324 pneumaticcraft:pressure_chamber_glass
setblock 124 64 325 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 65 323 pneumaticcraft:pressure_chamber_glass
setblock 124 65 325 pneumaticcraft:pressure_chamber_glass
setblock 124 66 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 66 324 pneumaticcraft:pressure_chamber_glass
setblock 124 66 325 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 324 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 325 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 324 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 125 65 325 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 324 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 325 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 123 65 325 up pneumaticcraft:pressure_chamber_wall
execute if block 125 65 324 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 130 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 131 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 139 64 319 139 83 336 minecraft:light_gray_concrete
setblock 134 64 323 pneumaticcraft:refinery[facing=south]
setblock 134 65 323 pneumaticcraft:refinery_output[facing=south]
setblock 134 66 323 pneumaticcraft:refinery_output[facing=south]
setblock 134 67 323 pneumaticcraft:refinery_output[facing=south]
setblock 134 68 323 pneumaticcraft:refinery_output[facing=south]
setblock 140 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 141 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 149 64 319 149 83 336 minecraft:light_gray_concrete
setblock 143 64 324 pneumaticcraft:pressure_tube
setblock 144 64 324 pneumaticcraft:pressure_tube
setblock 145 64 324 pneumaticcraft:vortex_tube[facing=east]
setblock 150 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 151 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 159 64 319 159 83 336 minecraft:light_gray_concrete
setblock 154 64 323 pneumaticcraft:elevator_base
fill 154 65 323 154 68 323 pneumaticcraft:elevator_frame
fill 155 64 323 155 67 323 minecraft:stone_bricks
setblock 155 68 323 pneumaticcraft:elevator_caller[facing=south]
setblock 160 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 161 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
fill 169 64 319 169 83 336 minecraft:light_gray_concrete
fill 163 64 324 165 64 324 pneumaticcraft:pressure_tube
kw testworld use 163 64 324 up pneumaticcraft:safety_tube_module
kw testworld use 165 64 324 up pneumaticcraft:pressure_gauge_module
setblock 170 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 171 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 179 64 319 179 83 336 minecraft:light_gray_concrete
setblock 174 64 324 minecraft:magma_block
setblock 174 65 324 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 180 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 181 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 189 64 319 189 83 336 minecraft:light_gray_concrete
setblock 184 64 324 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
