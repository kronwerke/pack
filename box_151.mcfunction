# 151 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
#area 115 317 194 346
fill 115 64 317 148 95 346 minecraft:air
fill 149 64 317 182 95 346 minecraft:air
fill 183 64 317 194 95 346 minecraft:air
fill 115 60 317 194 62 346 minecraft:stone
fill 115 63 317 194 63 346 minecraft:light_gray_concrete
fill 119 64 323 194 83 323 minecraft:light_gray_concrete
fill 119 64 323 119 83 340 minecraft:light_gray_concrete
setblock 120 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 121 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 129 64 323 129 83 340 minecraft:light_gray_concrete
setblock 123 64 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 328 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 328 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 123 65 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 328 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 328 pneumaticcraft:pressure_chamber_glass
setblock 124 64 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 65 327 pneumaticcraft:pressure_chamber_glass
setblock 124 65 329 pneumaticcraft:pressure_chamber_glass
setblock 124 66 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 66 328 pneumaticcraft:pressure_chamber_glass
setblock 124 66 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 328 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 328 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 125 65 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 327 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 328 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 329 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 123 65 329 up pneumaticcraft:pressure_chamber_wall
execute if block 125 65 328 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 130 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 131 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 139 64 323 139 83 340 minecraft:light_gray_concrete
setblock 134 64 327 pneumaticcraft:refinery[facing=south]
setblock 134 65 327 pneumaticcraft:refinery_output[facing=south]
setblock 134 66 327 pneumaticcraft:refinery_output[facing=south]
setblock 134 67 327 pneumaticcraft:refinery_output[facing=south]
setblock 134 68 327 pneumaticcraft:refinery_output[facing=south]
setblock 140 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 141 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 149 64 323 149 83 340 minecraft:light_gray_concrete
setblock 143 64 328 pneumaticcraft:pressure_tube
setblock 144 64 328 pneumaticcraft:pressure_tube
setblock 145 64 328 pneumaticcraft:vortex_tube[facing=east]
setblock 150 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 151 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 159 64 323 159 83 340 minecraft:light_gray_concrete
setblock 154 64 327 pneumaticcraft:elevator_base
fill 154 65 327 154 68 327 pneumaticcraft:elevator_frame
fill 155 64 327 155 67 327 minecraft:stone_bricks
setblock 155 68 327 pneumaticcraft:elevator_caller[facing=south]
setblock 160 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 161 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
fill 169 64 323 169 83 340 minecraft:light_gray_concrete
fill 163 64 328 165 64 328 pneumaticcraft:pressure_tube
kw testworld use 163 64 328 up pneumaticcraft:safety_tube_module
kw testworld use 165 64 328 up pneumaticcraft:pressure_gauge_module
setblock 170 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 171 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 179 64 323 179 83 340 minecraft:light_gray_concrete
setblock 174 64 328 minecraft:magma_block
setblock 174 65 328 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 180 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 181 64 339 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 189 64 323 189 83 340 minecraft:light_gray_concrete
setblock 184 64 328 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
