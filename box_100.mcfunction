# 100 pneumaticcraft/chamber, refinery, vortex, elevator, plastic, etching
#area 89 273 158 302
fill 89 64 273 122 95 302 minecraft:air
fill 123 64 273 156 95 302 minecraft:air
fill 157 64 273 158 95 302 minecraft:air
fill 89 60 273 158 62 302 minecraft:stone
fill 89 63 273 158 63 302 minecraft:light_gray_concrete
fill 93 64 279 158 83 279 minecraft:light_gray_concrete
fill 93 64 279 93 83 296 minecraft:light_gray_concrete
setblock 94 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.1"}','{"text": "pneumaticcraft"}','{"text": "chamber"}','{"text": ""}']}}
setblock 95 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz die"}','{"text": "Druckkammer"}','{"text": "zusammen"}','{"text": ""}']}}
fill 103 64 279 103 83 296 minecraft:light_gray_concrete
setblock 97 64 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 64 284 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 64 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 65 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 65 284 pneumaticcraft:pressure_chamber_interface[facing=west]
setblock 97 65 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 66 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 97 66 284 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 64 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 64 284 pneumaticcraft:pressure_chamber_glass
setblock 98 64 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 65 283 pneumaticcraft:pressure_chamber_glass
setblock 98 65 285 pneumaticcraft:pressure_chamber_glass
setblock 98 66 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 98 66 284 pneumaticcraft:pressure_chamber_glass
setblock 98 66 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 64 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 64 284 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 64 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 65 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 65 284 pneumaticcraft:pressure_chamber_valve[facing=east,formed=false]
setblock 99 65 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 66 283 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 66 284 pneumaticcraft:pressure_chamber_wall[wall_state=none]
setblock 99 66 285 pneumaticcraft:pressure_chamber_wall[wall_state=none]
kw testworld use 97 65 285 up pneumaticcraft:pressure_chamber_wall
execute if block 99 65 284 pneumaticcraft:pressure_chamber_valve[formed=true]
setblock 104 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.2"}','{"text": "pneumaticcraft"}','{"text": "refinery"}','{"text": ""}']}}
setblock 105 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Raffinerie"}','{"text": ""}','{"text": ""}']}}
fill 113 64 279 113 83 296 minecraft:light_gray_concrete
setblock 108 64 283 pneumaticcraft:refinery[facing=south]
setblock 108 65 283 pneumaticcraft:refinery_output[facing=south]
setblock 108 66 283 pneumaticcraft:refinery_output[facing=south]
setblock 108 67 283 pneumaticcraft:refinery_output[facing=south]
setblock 108 68 283 pneumaticcraft:refinery_output[facing=south]
setblock 114 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.3"}','{"text": "pneumaticcraft"}','{"text": "vortex"}','{"text": ""}']}}
setblock 115 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wirbelrohr"}','{"text": ""}','{"text": ""}']}}
fill 123 64 279 123 83 296 minecraft:light_gray_concrete
setblock 117 64 284 pneumaticcraft:pressure_tube
setblock 118 64 284 pneumaticcraft:pressure_tube
setblock 119 64 284 pneumaticcraft:vortex_tube[facing=east]
setblock 124 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.4"}','{"text": "pneumaticcraft"}','{"text": "elevator"}','{"text": ""}']}}
setblock 125 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Aufzug"}','{"text": ""}','{"text": ""}']}}
fill 133 64 279 133 83 296 minecraft:light_gray_concrete
setblock 128 64 283 pneumaticcraft:elevator_base
fill 128 65 283 128 68 283 pneumaticcraft:elevator_frame
fill 129 64 283 129 67 283 minecraft:stone_bricks
setblock 129 68 283 pneumaticcraft:elevator_caller[facing=south]
setblock 134 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.5"}','{"text": "pneumaticcraft"}','{"text": "plastic"}','{"text": ""}']}}
setblock 135 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Koch Kunststoff"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 143 64 279 143 83 296 minecraft:light_gray_concrete
setblock 138 64 284 minecraft:magma_block
setblock 138 65 284 pneumaticcraft:thermopneumatic_processing_plant[facing=south]
setblock 144 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "100.6"}','{"text": "pneumaticcraft"}','{"text": "etching"}','{"text": ""}']}}
setblock 145 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ätze die"}','{"text": "Platine"}','{"text": ""}','{"text": ""}']}}
fill 153 64 279 153 83 296 minecraft:light_gray_concrete
setblock 148 64 284 pneumaticcraft:etching_tank
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
