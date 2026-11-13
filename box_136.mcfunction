# 136 pneumaticcraft_advanced/first_run, electrostatic, thermal, adv_air, first_program, frames, security_station, spawner_extractor, pressurized_spawner
#area 190 277 289 302
fill 190 64 277 234 91 302 minecraft:air
fill 235 64 277 279 91 302 minecraft:air
fill 280 64 277 289 91 302 minecraft:air
fill 190 60 277 289 62 302 minecraft:stone
fill 190 63 277 289 63 302 minecraft:light_gray_concrete
fill 194 64 283 289 79 283 minecraft:light_gray_concrete
fill 194 64 283 194 79 296 minecraft:light_gray_concrete
setblock 195 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.1"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_run"}','{"text": ""}']}}
setblock 196 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Straße"}','{"text": "laufen"}','{"text": ""}','{"text": ""}']}}
fill 204 64 283 204 79 296 minecraft:light_gray_concrete
setblock 199 64 288 pneumaticcraft:assembly_platform
setblock 198 64 288 pneumaticcraft:assembly_drill
setblock 200 64 288 pneumaticcraft:assembly_laser
setblock 199 64 287 pneumaticcraft:assembly_io_unit_import
setblock 199 64 289 pneumaticcraft:assembly_io_unit_export
setblock 199 64 286 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 199 64 290 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 201 64 288 pneumaticcraft:assembly_controller
setblock 205 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.2"}','{"text": "pneumaticcraft_advanced"}','{"text": "electrostatic"}','{"text": ""}']}}
setblock 206 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Electrostatic"}','{"text": "Compressor"}','{"text": ""}']}}
fill 214 64 283 214 79 296 minecraft:light_gray_concrete
setblock 209 64 288 pneumaticcraft:electrostatic_compressor
fill 209 65 288 209 68 288 minecraft:iron_bars
setblock 209 69 288 minecraft:lightning_rod[facing=up,powered=false]
setblock 215 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.3"}','{"text": "pneumaticcraft_advanced"}','{"text": "thermal"}','{"text": ""}']}}
setblock 216 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermal"}','{"text": "Compressor"}','{"text": ""}']}}
fill 224 64 283 224 79 296 minecraft:light_gray_concrete
setblock 218 64 288 minecraft:magma_block
setblock 219 64 288 pneumaticcraft:thermal_compressor
setblock 220 64 288 minecraft:blue_ice
setblock 225 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.4"}','{"text": "pneumaticcraft_advanced"}','{"text": "adv_air"}','{"text": ""}']}}
setblock 226 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Advanced Air"}','{"text": "Compressor"}','{"text": ""}']}}
fill 234 64 283 234 79 296 minecraft:light_gray_concrete
setblock 229 64 288 pneumaticcraft:advanced_air_compressor[facing=south,on=true]
setblock 235 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.5"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_program"}','{"text": ""}']}}
setblock 236 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Programmiere"}','{"text": "deine erste"}','{"text": "Drohne"}','{"text": ""}']}}
fill 244 64 283 244 79 296 minecraft:light_gray_concrete
setblock 238 64 288 pneumaticcraft:programmer[facing=south]
setblock 240 64 288 minecraft:smooth_stone_slab
summon item_display 240.5 64.95 288.5 {item:{id:"pneumaticcraft:drone",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 245 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.6"}','{"text": "pneumaticcraft_advanced"}','{"text": "frames"}','{"text": ""}']}}
setblock 246 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Logistics"}','{"text": "Frames"}','{"text": ""}','{"text": ""}']}}
fill 254 64 283 254 79 296 minecraft:light_gray_concrete
setblock 247 64 288 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 251 64 288 minecraft:chest[facing=south,type=single,waterlogged=false]
kw testworld use 247 64 288 south pneumaticcraft:logistics_frame_passive_provider
kw testworld use 251 64 288 south pneumaticcraft:logistics_frame_requester
setblock 255 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.7"}','{"text": "pneumaticcraft_advanced"}','{"text": "security_station"}','{"text": ""}']}}
setblock 256 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Security"}','{"text": "Station"}','{"text": ""}']}}
fill 264 64 283 264 79 296 minecraft:light_gray_concrete
setblock 259 64 288 pneumaticcraft:security_station[facing=south]
setblock 265 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.8"}','{"text": "pneumaticcraft_advanced"}','{"text": "spawner_extractor"}','{"text": ""}']}}
setblock 266 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spawner"}','{"text": "Extractor"}','{"text": ""}']}}
fill 274 64 283 274 79 296 minecraft:light_gray_concrete
setblock 269 64 288 minecraft:spawner
setblock 269 65 288 pneumaticcraft:spawner_extractor
setblock 275 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "136.9"}','{"text": "pneumaticcraft_advanced"}','{"text": "pressurized_spawner"}','{"text": ""}']}}
setblock 276 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Pressurized"}','{"text": "Spawner"}','{"text": ""}']}}
fill 284 64 283 284 79 296 minecraft:light_gray_concrete
setblock 279 64 288 pneumaticcraft:pressurized_spawner
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
