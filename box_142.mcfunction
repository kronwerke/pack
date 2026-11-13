# 142 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
#area 115 307 194 336
fill 115 64 307 148 95 336 minecraft:air
fill 149 64 307 182 95 336 minecraft:air
fill 183 64 307 194 95 336 minecraft:air
fill 115 60 307 194 62 336 minecraft:stone
fill 115 63 307 194 63 336 minecraft:light_gray_concrete
fill 119 64 313 194 83 313 minecraft:light_gray_concrete
fill 119 64 313 119 83 330 minecraft:light_gray_concrete
setblock 120 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 121 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 129 64 313 129 83 330 minecraft:light_gray_concrete
setblock 123 64 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 318 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 319 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 318 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 123 65 319 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 318 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 318 pneumaticcraft:pressure_chamber_glass
setblock 124 64 319 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 65 317 pneumaticcraft:pressure_chamber_glass
setblock 124 65 319 pneumaticcraft:pressure_chamber_glass
setblock 124 66 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 66 318 pneumaticcraft:pressure_chamber_glass
setblock 124 66 319 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 318 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 319 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 318 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 125 65 319 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 317 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 318 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 319 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 123 65 319 up pneumaticcraft:pressure_chamber_wall
execute if block 125 65 318 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 130 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 131 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 139 64 313 139 83 330 minecraft:light_gray_concrete
setblock 134 64 317 pneumaticcraft:refinery[facing=south]
setblock 134 65 317 pneumaticcraft:refinery_output[facing=south]
setblock 134 66 317 pneumaticcraft:refinery_output[facing=south]
setblock 134 67 317 pneumaticcraft:refinery_output[facing=south]
setblock 134 68 317 pneumaticcraft:refinery_output[facing=south]
setblock 140 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 141 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 149 64 313 149 83 330 minecraft:light_gray_concrete
setblock 143 64 318 pneumaticcraft:pressure_tube
setblock 144 64 318 pneumaticcraft:pressure_tube
setblock 145 64 318 pneumaticcraft:vortex_tube[facing=east]
setblock 150 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 151 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 159 64 313 159 83 330 minecraft:light_gray_concrete
setblock 154 64 317 pneumaticcraft:elevator_base
fill 154 65 317 154 68 317 pneumaticcraft:elevator_frame
fill 155 64 317 155 67 317 minecraft:stone_bricks
setblock 155 68 317 pneumaticcraft:elevator_caller[facing=south]
setblock 160 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 161 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
fill 169 64 313 169 83 330 minecraft:light_gray_concrete
fill 163 64 318 165 64 318 pneumaticcraft:pressure_tube
kw testworld use 163 64 318 up pneumaticcraft:safety_tube_module
kw testworld use 165 64 318 up pneumaticcraft:pressure_gauge_module
setblock 170 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 171 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 179 64 313 179 83 330 minecraft:light_gray_concrete
setblock 174 64 318 minecraft:magma_block
setblock 174 65 318 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 180 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 181 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 189 64 313 189 83 330 minecraft:light_gray_concrete
setblock 184 64 318 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
