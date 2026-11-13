# 088 pneumaticcraft/chamber, refinery, elevator
#area 118 250 157 275
fill 118 64 250 156 95 275 minecraft:air
fill 157 64 250 157 95 275 minecraft:air
fill 118 60 250 157 62 275 minecraft:stone
fill 118 63 250 157 63 275 minecraft:light_gray_concrete
fill 122 64 256 157 83 256 minecraft:light_gray_concrete
fill 122 64 256 122 83 269 minecraft:light_gray_concrete
setblock 123 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 124 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 132 64 256 132 83 269 minecraft:light_gray_concrete
setblock 126 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 126 64 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 126 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 126 65 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 126 65 261 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 126 65 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 126 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 126 66 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 127 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 127 64 261 pneumaticcraft:pressure_chamber_glass
setblock 127 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 127 65 260 pneumaticcraft:pressure_chamber_glass
setblock 127 65 262 pneumaticcraft:pressure_chamber_glass
setblock 127 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 127 66 261 pneumaticcraft:pressure_chamber_glass
setblock 127 66 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 64 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 65 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 65 261 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 128 65 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 66 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 128 66 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 126 65 262 up pneumaticcraft:pressure_chamber_wall
execute if block 128 65 261 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 133 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 134 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 142 64 256 142 83 269 minecraft:light_gray_concrete
setblock 137 64 261 pneumaticcraft:refinery[facing=south]
setblock 137 65 261 pneumaticcraft:refinery_output[facing=south]
setblock 137 66 261 pneumaticcraft:refinery_output[facing=south]
setblock 137 67 261 pneumaticcraft:refinery_output[facing=south]
setblock 137 68 261 pneumaticcraft:refinery_output[facing=south]
setblock 143 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088.3"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 144 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 152 64 256 152 83 269 minecraft:light_gray_concrete
setblock 147 64 261 pneumaticcraft:elevator_base
fill 147 65 261 147 68 261 pneumaticcraft:elevator_frame
fill 148 64 261 148 67 261 minecraft:stone_bricks
setblock 148 68 261 pneumaticcraft:elevator_caller[facing=south]
