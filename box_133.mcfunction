# 133 pneumaticcraft/chamber, refinery, vortex, elevator, safety, plastic, etching
#area 115 277 194 306
fill 115 64 277 148 95 306 minecraft:air
fill 149 64 277 182 95 306 minecraft:air
fill 183 64 277 194 95 306 minecraft:air
fill 115 60 277 194 62 306 minecraft:stone
fill 115 63 277 194 63 306 minecraft:light_gray_concrete
fill 119 64 283 194 83 283 minecraft:light_gray_concrete
fill 119 64 283 119 83 300 minecraft:light_gray_concrete
setblock 120 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 121 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 129 64 283 129 83 300 minecraft:light_gray_concrete
setblock 123 64 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 288 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 64 289 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 65 288 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 123 65 289 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 123 66 288 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 64 288 pneumaticcraft:pressure_chamber_glass
setblock 124 64 289 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 65 287 pneumaticcraft:pressure_chamber_glass
setblock 124 65 289 pneumaticcraft:pressure_chamber_glass
setblock 124 66 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 124 66 288 pneumaticcraft:pressure_chamber_glass
setblock 124 66 289 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 288 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 64 289 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 65 288 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 125 65 289 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 287 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 288 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 125 66 289 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 123 65 289 up pneumaticcraft:pressure_chamber_wall
execute if block 125 65 288 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 130 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 131 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 139 64 283 139 83 300 minecraft:light_gray_concrete
setblock 134 64 287 pneumaticcraft:refinery[facing=south]
setblock 134 65 287 pneumaticcraft:refinery_output[facing=south]
setblock 134 66 287 pneumaticcraft:refinery_output[facing=south]
setblock 134 67 287 pneumaticcraft:refinery_output[facing=south]
setblock 134 68 287 pneumaticcraft:refinery_output[facing=south]
setblock 140 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 141 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 149 64 283 149 83 300 minecraft:light_gray_concrete
setblock 143 64 288 pneumaticcraft:pressure_tube
setblock 144 64 288 pneumaticcraft:pressure_tube
setblock 145 64 288 pneumaticcraft:vortex_tube[facing=east]
setblock 150 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 151 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 159 64 283 159 83 300 minecraft:light_gray_concrete
setblock 154 64 287 pneumaticcraft:elevator_base
fill 154 65 287 154 68 287 pneumaticcraft:elevator_frame
fill 155 64 287 155 67 287 minecraft:stone_bricks
setblock 155 68 287 pneumaticcraft:elevator_caller[facing=south]
setblock 160 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.5"}','{"text": "pneumaticcraft"}','{"text": "safety"}','{"text": ""}']}}
setblock 161 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein"}','{"text": "Sicherheitsventil"}','{"text": ""}','{"text": ""}']}}
fill 169 64 283 169 83 300 minecraft:light_gray_concrete
fill 163 64 288 165 64 288 pneumaticcraft:pressure_tube
kw testworld use 163 64 288 up pneumaticcraft:safety_tube_module
kw testworld use 165 64 288 up pneumaticcraft:pressure_gauge_module
setblock 170 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.6"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 171 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 179 64 283 179 83 300 minecraft:light_gray_concrete
setblock 174 64 288 minecraft:magma_block
setblock 174 65 288 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 180 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.7"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 181 64 299 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 189 64 283 189 83 300 minecraft:light_gray_concrete
setblock 184 64 288 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
