# 075 pneumaticcraft/chamber
#area 12 231 31 256
fill 12 64 231 31 91 256 minecraft:air
fill 12 60 231 31 62 256 minecraft:stone
fill 12 63 231 31 63 256 minecraft:light_gray_concrete
fill 16 64 237 31 79 237 minecraft:light_gray_concrete
fill 16 64 237 16 79 250 minecraft:light_gray_concrete
setblock 17 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "075"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 18 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 26 64 237 26 79 250 minecraft:light_gray_concrete
setblock 20 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 20 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 20 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 20 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 20 65 242 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 20 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 20 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 20 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 21 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 21 64 242 pneumaticcraft:pressure_chamber_glass
setblock 21 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 21 65 241 pneumaticcraft:pressure_chamber_glass
setblock 21 65 243 pneumaticcraft:pressure_chamber_glass
setblock 21 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 21 66 242 pneumaticcraft:pressure_chamber_glass
setblock 21 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 64 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 64 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 64 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 65 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 65 242 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 22 65 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 66 241 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 66 242 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 22 66 243 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 20 65 243 up pneumaticcraft:pressure_chamber_wall
execute if block 22 65 242 pneumaticcraft:pressure_chamber_valve[formed=true]
