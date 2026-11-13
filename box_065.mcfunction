# 065 pneumaticcraft/chamber
#area -4 231 15 256
fill -4 64 231 15 91 256 minecraft:air
fill -4 60 231 15 62 256 minecraft:stone
fill -4 63 231 15 63 256 minecraft:light_gray_concrete
fill 0 64 237 15 79 237 minecraft:light_gray_concrete
fill 0 64 237 0 79 250 minecraft:light_gray_concrete
setblock 1 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "065"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 2 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 10 64 237 10 79 250 minecraft:light_gray_concrete
setblock 4 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 4 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 4 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 4 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 4 65 242 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 4 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 4 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 4 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 5 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 5 64 242 pneumaticcraft:pressure_chamber_glass
setblock 5 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 5 65 241 pneumaticcraft:pressure_chamber_glass
setblock 5 65 243 pneumaticcraft:pressure_chamber_glass
setblock 5 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 5 66 242 pneumaticcraft:pressure_chamber_glass
setblock 5 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 65 242 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 6 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 6 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 4 65 243 up pneumaticcraft:pressure_chamber_wall
execute if block 6 65 242 pneumaticcraft:pressure_chamber_valve[formed=true]
