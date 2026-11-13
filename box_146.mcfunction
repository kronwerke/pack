# 146 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
#area 115 311 194 340
fill 115 64 311 148 95 340 minecraft:air
fill 149 64 311 182 95 340 minecraft:air
fill 183 64 311 194 95 340 minecraft:air
fill 115 60 311 194 62 340 minecraft:stone
fill 115 63 311 194 63 340 minecraft:light_gray_concrete
fill 119 64 317 194 83 317 minecraft:light_gray_concrete
fill 119 64 317 119 83 334 minecraft:light_gray_concrete
setblock 120 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 121 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 129 64 317 129 83 334 minecraft:light_gray_concrete
setblock 123 64 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 322 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 322 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 123 65 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 322 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 322 pneumaticcraft:pressure_chamber_glass
setblock 124 64 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 65 321 pneumaticcraft:pressure_chamber_glass
setblock 124 65 323 pneumaticcraft:pressure_chamber_glass
setblock 124 66 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 66 322 pneumaticcraft:pressure_chamber_glass
setblock 124 66 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 322 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 322 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 125 65 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 321 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 322 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 323 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 123 65 323 up pneumaticcraft:pressure_chamber_wall
execute if block 125 65 322 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 130 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 131 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 139 64 317 139 83 334 minecraft:light_gray_concrete
setblock 134 64 321 pneumaticcraft:refinery[facing=south]
setblock 134 65 321 pneumaticcraft:refinery_output[facing=south]
setblock 134 66 321 pneumaticcraft:refinery_output[facing=south]
setblock 134 67 321 pneumaticcraft:refinery_output[facing=south]
setblock 134 68 321 pneumaticcraft:refinery_output[facing=south]
setblock 140 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 141 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 149 64 317 149 83 334 minecraft:light_gray_concrete
setblock 143 64 322 pneumaticcraft:pressure_tube
setblock 144 64 322 pneumaticcraft:pressure_tube
setblock 145 64 322 pneumaticcraft:vortex_tube[facing=east]
setblock 150 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 151 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 159 64 317 159 83 334 minecraft:light_gray_concrete
setblock 154 64 321 pneumaticcraft:elevator_base
fill 154 65 321 154 68 321 pneumaticcraft:elevator_frame
fill 155 64 321 155 67 321 minecraft:stone_bricks
setblock 155 68 321 pneumaticcraft:elevator_caller[facing=south]
setblock 160 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 161 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
fill 169 64 317 169 83 334 minecraft:light_gray_concrete
fill 163 64 322 165 64 322 pneumaticcraft:pressure_tube
kw testworld use 163 64 322 up pneumaticcraft:safety_tube_module
kw testworld use 165 64 322 up pneumaticcraft:pressure_gauge_module
setblock 170 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 171 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 179 64 317 179 83 334 minecraft:light_gray_concrete
setblock 174 64 322 minecraft:magma_block
setblock 174 65 322 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 180 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 181 64 333 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 189 64 317 189 83 334 minecraft:light_gray_concrete
setblock 184 64 322 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
