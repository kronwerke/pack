# 090 pneumaticcraft/chamber, refinery, vortex, elevator, plastic, etching
#area 89 254 158 283
fill 89 64 254 122 95 283 minecraft:air
fill 123 64 254 156 95 283 minecraft:air
fill 157 64 254 158 95 283 minecraft:air
fill 89 60 254 158 62 283 minecraft:stone
fill 89 63 254 158 63 283 minecraft:light_gray_concrete
fill 93 64 260 158 83 260 minecraft:light_gray_concrete
fill 93 64 260 93 83 277 minecraft:light_gray_concrete
setblock 94 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 95 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 103 64 260 103 83 277 minecraft:light_gray_concrete
setblock 97 64 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 64 265 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 64 266 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 65 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 65 265 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 97 65 266 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 66 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 66 265 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 64 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 64 265 pneumaticcraft:pressure_chamber_glass
setblock 98 64 266 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 65 264 pneumaticcraft:pressure_chamber_glass
setblock 98 65 266 pneumaticcraft:pressure_chamber_glass
setblock 98 66 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 66 265 pneumaticcraft:pressure_chamber_glass
setblock 98 66 266 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 64 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 64 265 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 64 266 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 65 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 65 265 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 99 65 266 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 66 264 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 66 265 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 66 266 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 97 65 266 up pneumaticcraft:pressure_chamber_wall
execute if block 99 65 265 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 104 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 105 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 113 64 260 113 83 277 minecraft:light_gray_concrete
setblock 108 64 264 pneumaticcraft:refinery[facing=south]
setblock 108 65 264 pneumaticcraft:refinery_output[facing=south]
setblock 108 66 264 pneumaticcraft:refinery_output[facing=south]
setblock 108 67 264 pneumaticcraft:refinery_output[facing=south]
setblock 108 68 264 pneumaticcraft:refinery_output[facing=south]
setblock 114 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 115 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 123 64 260 123 83 277 minecraft:light_gray_concrete
setblock 117 64 265 pneumaticcraft:pressure_tube
setblock 118 64 265 pneumaticcraft:pressure_tube
setblock 119 64 265 pneumaticcraft:vortex_tube[facing=east]
setblock 124 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 125 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 133 64 260 133 83 277 minecraft:light_gray_concrete
setblock 128 64 264 pneumaticcraft:elevator_base
fill 128 65 264 128 68 264 pneumaticcraft:elevator_frame
fill 129 64 264 129 67 264 minecraft:stone_bricks
setblock 129 68 264 pneumaticcraft:elevator_caller[facing=south]
setblock 134 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.5"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 135 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 143 64 260 143 83 277 minecraft:light_gray_concrete
setblock 138 64 265 minecraft:magma_block
setblock 138 65 265 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 144 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.6"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 145 64 276 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 153 64 260 153 83 277 minecraft:light_gray_concrete
setblock 148 64 265 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
