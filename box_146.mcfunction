# 146 pneumaticcraft_advanced/first_run, electrostatic, thermal, adv_air, first_program, frames, security_station, spawner_extractor, pressurized_spawner
#area 190 307 289 332
fill 190 64 307 234 91 332 minecraft:air
fill 235 64 307 279 91 332 minecraft:air
fill 280 64 307 289 91 332 minecraft:air
fill 190 60 307 289 62 332 minecraft:stone
fill 190 63 307 289 63 332 minecraft:light_gray_concrete
fill 194 64 313 289 79 313 minecraft:light_gray_concrete
fill 194 64 313 194 79 326 minecraft:light_gray_concrete
setblock 195 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.1"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_run"}','{"text": ""}']}}
setblock 196 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Straße"}','{"text": "laufen"}','{"text": ""}','{"text": ""}']}}
fill 204 64 313 204 79 326 minecraft:light_gray_concrete
setblock 199 64 318 pneumaticcraft:assembly_platform
setblock 198 64 318 pneumaticcraft:assembly_drill
setblock 200 64 318 pneumaticcraft:assembly_laser
setblock 199 64 317 pneumaticcraft:assembly_io_unit_import
setblock 199 64 319 pneumaticcraft:assembly_io_unit_export
setblock 199 64 316 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 199 64 320 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 201 64 318 pneumaticcraft:assembly_controller
setblock 205 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.2"}','{"text": "pneumaticcraft_advanced"}','{"text": "electrostatic"}','{"text": ""}']}}
setblock 206 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Electrostatic"}','{"text": "Compressor"}','{"text": ""}']}}
fill 214 64 313 214 79 326 minecraft:light_gray_concrete
setblock 209 64 318 pneumaticcraft:electrostatic_compressor
fill 209 65 318 209 68 318 minecraft:iron_bars
setblock 209 69 318 minecraft:lightning_rod[facing=up,powered=false]
setblock 215 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.3"}','{"text": "pneumaticcraft_advanced"}','{"text": "thermal"}','{"text": ""}']}}
setblock 216 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermal"}','{"text": "Compressor"}','{"text": ""}']}}
fill 224 64 313 224 79 326 minecraft:light_gray_concrete
setblock 218 64 318 minecraft:magma_block
setblock 219 64 318 pneumaticcraft:thermal_compressor
setblock 220 64 318 minecraft:blue_ice
setblock 225 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.4"}','{"text": "pneumaticcraft_advanced"}','{"text": "adv_air"}','{"text": ""}']}}
setblock 226 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Advanced Air"}','{"text": "Compressor"}','{"text": ""}']}}
fill 234 64 313 234 79 326 minecraft:light_gray_concrete
setblock 229 64 318 pneumaticcraft:advanced_air_compressor[facing=south,on=true]
setblock 235 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.5"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_program"}','{"text": ""}']}}
setblock 236 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Programmiere"}','{"text": "deine erste"}','{"text": "Drohne"}','{"text": ""}']}}
fill 244 64 313 244 79 326 minecraft:light_gray_concrete
setblock 238 64 318 pneumaticcraft:programmer[facing=south]
setblock 240 64 318 minecraft:smooth_stone_slab
summon item_display 240.5 64.95 318.5 {item:{id:"pneumaticcraft:drone",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 245 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.6"}','{"text": "pneumaticcraft_advanced"}','{"text": "frames"}','{"text": ""}']}}
setblock 246 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Logistics"}','{"text": "Frames"}','{"text": ""}','{"text": ""}']}}
fill 254 64 313 254 79 326 minecraft:light_gray_concrete
setblock 247 64 318 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 251 64 318 minecraft:chest[facing=south,type=single,waterlogged=false]
kw testworld use 247 64 318 south pneumaticcraft:logistics_frame_passive_provider
kw testworld use 251 64 318 south pneumaticcraft:logistics_frame_requester
setblock 255 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.7"}','{"text": "pneumaticcraft_advanced"}','{"text": "security_station"}','{"text": ""}']}}
setblock 256 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Security"}','{"text": "Station"}','{"text": ""}']}}
fill 264 64 313 264 79 326 minecraft:light_gray_concrete
setblock 259 64 318 pneumaticcraft:security_station[facing=south]
setblock 265 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.8"}','{"text": "pneumaticcraft_advanced"}','{"text": "spawner_extractor"}','{"text": ""}']}}
setblock 266 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spawner"}','{"text": "Extractor"}','{"text": ""}']}}
fill 274 64 313 274 79 326 minecraft:light_gray_concrete
setblock 269 64 318 minecraft:spawner
setblock 269 65 318 pneumaticcraft:spawner_extractor
setblock 275 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.9"}','{"text": "pneumaticcraft_advanced"}','{"text": "pressurized_spawner"}','{"text": ""}']}}
setblock 276 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Pressurized"}','{"text": "Spawner"}','{"text": ""}']}}
fill 284 64 313 284 79 326 minecraft:light_gray_concrete
setblock 279 64 318 pneumaticcraft:pressurized_spawner
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
