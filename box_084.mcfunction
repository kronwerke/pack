# 084 pneumaticcraft/chamber
#area 63 231 82 256
fill 63 64 231 82 91 256 minecraft:air
fill 63 60 231 82 62 256 minecraft:stone
fill 63 63 231 82 63 256 minecraft:light_gray_concrete
fill 67 64 237 82 79 237 minecraft:light_gray_concrete
fill 67 64 237 67 79 250 minecraft:light_gray_concrete
setblock 68 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 69 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 77 64 237 77 79 250 minecraft:light_gray_concrete
setblock 71 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 65 242 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 71 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 71 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 64 242 pneumaticcraft:pressure_chamber_glass
setblock 72 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 65 241 pneumaticcraft:pressure_chamber_glass
setblock 72 65 243 pneumaticcraft:pressure_chamber_glass
setblock 72 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 72 66 242 pneumaticcraft:pressure_chamber_glass
setblock 72 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 65 242 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 73 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 73 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 71 65 243 up pneumaticcraft:pressure_chamber_wall
execute if block 73 65 242 pneumaticcraft:pressure_chamber_valve[formed=true]
