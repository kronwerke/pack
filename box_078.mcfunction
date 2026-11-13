# 078 pneumaticcraft/chamber
#area 32 231 51 256
fill 32 64 231 51 91 256 minecraft:air
fill 32 60 231 51 62 256 minecraft:stone
fill 32 63 231 51 63 256 minecraft:light_gray_concrete
fill 36 64 237 51 79 237 minecraft:light_gray_concrete
fill 36 64 237 36 79 250 minecraft:light_gray_concrete
setblock 37 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 38 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 46 64 237 46 79 250 minecraft:light_gray_concrete
setblock 40 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 40 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 40 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 40 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 40 65 242 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 40 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 40 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 40 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 41 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 41 64 242 pneumaticcraft:pressure_chamber_glass
setblock 41 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 41 65 241 pneumaticcraft:pressure_chamber_glass
setblock 41 65 243 pneumaticcraft:pressure_chamber_glass
setblock 41 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 41 66 242 pneumaticcraft:pressure_chamber_glass
setblock 41 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 65 242 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 42 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 42 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 40 65 243 up pneumaticcraft:pressure_chamber_wall
execute if block 42 65 242 pneumaticcraft:pressure_chamber_valve[formed=true]
