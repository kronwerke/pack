# 118 pneumaticcraft_advanced/first_run, electrostatic, thermal, adv_air, first_program, frames, security_station, spawner_extractor, pressurized_spawner
#area 190 275 289 300
fill 190 64 275 234 91 300 minecraft:air
fill 235 64 275 279 91 300 minecraft:air
fill 280 64 275 289 91 300 minecraft:air
fill 190 60 275 289 62 300 minecraft:stone
fill 190 63 275 289 63 300 minecraft:light_gray_concrete
fill 194 64 281 289 79 281 minecraft:light_gray_concrete
fill 194 64 281 194 79 294 minecraft:light_gray_concrete
setblock 195 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.1"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_run"}','{"text": ""}']}}
setblock 196 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Straße"}','{"text": "laufen"}','{"text": ""}','{"text": ""}']}}
fill 204 64 281 204 79 294 minecraft:light_gray_concrete
setblock 199 64 286 pneumaticcraft:assembly_platform
setblock 198 64 286 pneumaticcraft:assembly_drill
setblock 200 64 286 pneumaticcraft:assembly_laser
setblock 199 64 285 pneumaticcraft:assembly_io_unit_import
setblock 199 64 287 pneumaticcraft:assembly_io_unit_export
setblock 199 64 284 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 199 64 288 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 201 64 286 pneumaticcraft:assembly_controller
setblock 205 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.2"}','{"text": "pneumaticcraft_advanced"}','{"text": "electrostatic"}','{"text": ""}']}}
setblock 206 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Electrostatic"}','{"text": "Compressor"}','{"text": ""}']}}
fill 214 64 281 214 79 294 minecraft:light_gray_concrete
setblock 209 64 286 pneumaticcraft:electrostatic_compressor
fill 209 65 286 209 68 286 minecraft:iron_bars
setblock 209 69 286 minecraft:lightning_rod[facing=up,powered=false]
setblock 215 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.3"}','{"text": "pneumaticcraft_advanced"}','{"text": "thermal"}','{"text": ""}']}}
setblock 216 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermal"}','{"text": "Compressor"}','{"text": ""}']}}
fill 224 64 281 224 79 294 minecraft:light_gray_concrete
setblock 218 64 286 minecraft:magma_block
setblock 219 64 286 pneumaticcraft:thermal_compressor
setblock 220 64 286 minecraft:blue_ice
setblock 225 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.4"}','{"text": "pneumaticcraft_advanced"}','{"text": "adv_air"}','{"text": ""}']}}
setblock 226 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Advanced Air"}','{"text": "Compressor"}','{"text": ""}']}}
fill 234 64 281 234 79 294 minecraft:light_gray_concrete
setblock 229 64 286 pneumaticcraft:advanced_air_compressor[facing=south,on=true]
setblock 235 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.5"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_program"}','{"text": ""}']}}
setblock 236 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Programmiere"}','{"text": "deine erste"}','{"text": "Drohne"}','{"text": ""}']}}
fill 244 64 281 244 79 294 minecraft:light_gray_concrete
setblock 238 64 286 pneumaticcraft:programmer[facing=south]
setblock 240 64 286 minecraft:smooth_stone_slab
summon item_display 240.5 64.95 286.5 {item:{id:"pneumaticcraft:drone",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 245 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.6"}','{"text": "pneumaticcraft_advanced"}','{"text": "frames"}','{"text": ""}']}}
setblock 246 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Logistics"}','{"text": "Frames"}','{"text": ""}','{"text": ""}']}}
fill 254 64 281 254 79 294 minecraft:light_gray_concrete
setblock 247 64 286 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 251 64 286 minecraft:chest[facing=south,type=single,waterlogged=false]
kw testworld use 247 64 286 south pneumaticcraft:logistics_frame_passive_provider
kw testworld use 251 64 286 south pneumaticcraft:logistics_frame_requester
setblock 255 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.7"}','{"text": "pneumaticcraft_advanced"}','{"text": "security_station"}','{"text": ""}']}}
setblock 256 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Security"}','{"text": "Station"}','{"text": ""}']}}
fill 264 64 281 264 79 294 minecraft:light_gray_concrete
setblock 259 64 286 pneumaticcraft:security_station[facing=south]
setblock 265 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.8"}','{"text": "pneumaticcraft_advanced"}','{"text": "spawner_extractor"}','{"text": ""}']}}
setblock 266 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spawner"}','{"text": "Extractor"}','{"text": ""}']}}
fill 274 64 281 274 79 294 minecraft:light_gray_concrete
setblock 269 64 286 minecraft:spawner
setblock 269 65 286 pneumaticcraft:spawner_extractor
setblock 275 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.9"}','{"text": "pneumaticcraft_advanced"}','{"text": "pressurized_spawner"}','{"text": ""}']}}
setblock 276 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Pressurized"}','{"text": "Spawner"}','{"text": ""}']}}
fill 284 64 281 284 79 294 minecraft:light_gray_concrete
setblock 279 64 286 pneumaticcraft:pressurized_spawner
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
