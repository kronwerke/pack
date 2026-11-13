# 086 pneumaticcraft/chamber
#area 63 250 82 275
fill 63 64 250 82 91 275 minecraft:air
fill 63 60 250 82 62 275 minecraft:stone
fill 63 63 250 82 63 275 minecraft:light_gray_concrete
fill 67 64 256 82 79 256 minecraft:light_gray_concrete
fill 67 64 256 67 79 269 minecraft:light_gray_concrete
setblock 68 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 69 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 77 64 256 77 79 269 minecraft:light_gray_concrete
setblock 71 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 64 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 65 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 65 261 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 71 65 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 66 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 64 261 pneumaticcraft:pressure_chamber_glass
setblock 72 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 65 260 pneumaticcraft:pressure_chamber_glass
setblock 72 65 262 pneumaticcraft:pressure_chamber_glass
setblock 72 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 66 261 pneumaticcraft:pressure_chamber_glass
setblock 72 66 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 64 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 64 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 64 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 65 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 65 261 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 73 65 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 66 260 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 66 261 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 66 262 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 71 65 262 up pneumaticcraft:pressure_chamber_wall
execute if block 73 65 261 pneumaticcraft:pressure_chamber_valve[formed=true]
