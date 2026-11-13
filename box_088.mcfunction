# 088 pneumaticcraft/chamber, refinery
#area 96 250 125 275
fill 96 64 250 125 91 275 minecraft:air
fill 96 60 250 125 62 275 minecraft:stone
fill 96 63 250 125 63 275 minecraft:light_gray_concrete
fill 100 64 256 125 79 256 minecraft:light_gray_concrete
fill 100 64 256 100 79 269 minecraft:light_gray_concrete
setblock 101 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 102 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 110 64 256 110 79 269 minecraft:light_gray_concrete
setblock 104 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 104 64 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 104 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 104 65 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 104 65 261 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 104 65 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 104 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 104 66 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 105 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 105 64 261 pneumaticcraft:pressure_chamber_glass
setblock 105 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 105 65 260 pneumaticcraft:pressure_chamber_glass
setblock 105 65 262 pneumaticcraft:pressure_chamber_glass
setblock 105 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 105 66 261 pneumaticcraft:pressure_chamber_glass
setblock 105 66 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 64 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 65 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 65 261 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 106 65 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 66 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 106 66 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 104 65 262 up pneumaticcraft:pressure_chamber_wall
execute if block 106 65 261 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 111 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 112 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 120 64 256 120 79 269 minecraft:light_gray_concrete
setblock 115 64 261 pneumaticcraft:refinery[facing=south]
setblock 115 65 261 pneumaticcraft:refinery_output[facing=south]
setblock 115 66 261 pneumaticcraft:refinery_output[facing=south]
setblock 115 67 261 pneumaticcraft:refinery_output[facing=south]
setblock 115 68 261 pneumaticcraft:refinery_output[facing=south]
