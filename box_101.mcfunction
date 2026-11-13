# 101 pneumaticcraft_advanced/first_run, electrostatic, thermal, adv_air, security_station, spawner_extractor, pressurized_spawner
#area 154 273 233 298
fill 154 64 273 198 91 298 minecraft:air
fill 199 64 273 233 91 298 minecraft:air
fill 154 60 273 233 62 298 minecraft:stone
fill 154 63 273 233 63 298 minecraft:light_gray_concrete
fill 158 64 279 233 79 279 minecraft:light_gray_concrete
fill 158 64 279 158 79 292 minecraft:light_gray_concrete
setblock 159 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.1"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_run"}','{"text": ""}']}}
setblock 160 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Straße"}','{"text": "laufen"}','{"text": ""}','{"text": ""}']}}
fill 168 64 279 168 79 292 minecraft:light_gray_concrete
setblock 163 64 284 pneumaticcraft:assembly_platform
setblock 162 64 284 pneumaticcraft:assembly_drill
setblock 164 64 284 pneumaticcraft:assembly_laser
setblock 163 64 283 pneumaticcraft:assembly_io_unit_import
setblock 163 64 285 pneumaticcraft:assembly_io_unit_export
setblock 163 64 282 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 163 64 286 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 165 64 284 pneumaticcraft:assembly_controller
setblock 169 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.2"}','{"text": "pneumaticcraft_advanced"}','{"text": "electrostatic"}','{"text": ""}']}}
setblock 170 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Electrostatic"}','{"text": "Compressor"}','{"text": ""}']}}
fill 178 64 279 178 79 292 minecraft:light_gray_concrete
setblock 173 64 284 pneumaticcraft:electrostatic_compressor
fill 173 65 284 173 68 284 minecraft:iron_bars
setblock 173 69 284 minecraft:lightning_rod[facing=up,powered=false]
setblock 179 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.3"}','{"text": "pneumaticcraft_advanced"}','{"text": "thermal"}','{"text": ""}']}}
setblock 180 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermal"}','{"text": "Compressor"}','{"text": ""}']}}
fill 188 64 279 188 79 292 minecraft:light_gray_concrete
setblock 182 64 284 minecraft:magma_block
setblock 183 64 284 pneumaticcraft:thermal_compressor
setblock 184 64 284 minecraft:blue_ice
setblock 189 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.4"}','{"text": "pneumaticcraft_advanced"}','{"text": "adv_air"}','{"text": ""}']}}
setblock 190 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Advanced Air"}','{"text": "Compressor"}','{"text": ""}']}}
fill 198 64 279 198 79 292 minecraft:light_gray_concrete
setblock 193 64 284 pneumaticcraft:advanced_air_compressor[facing=south,on=true]
setblock 199 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.5"}','{"text": "pneumaticcraft_advanced"}','{"text": "security_station"}','{"text": ""}']}}
setblock 200 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Security"}','{"text": "Station"}','{"text": ""}']}}
fill 208 64 279 208 79 292 minecraft:light_gray_concrete
setblock 203 64 284 pneumaticcraft:security_station[facing=south]
setblock 209 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.6"}','{"text": "pneumaticcraft_advanced"}','{"text": "spawner_extractor"}','{"text": ""}']}}
setblock 210 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spawner"}','{"text": "Extractor"}','{"text": ""}']}}
fill 218 64 279 218 79 292 minecraft:light_gray_concrete
setblock 213 64 284 minecraft:spawner
setblock 213 65 284 pneumaticcraft:spawner_extractor
setblock 219 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.7"}','{"text": "pneumaticcraft_advanced"}','{"text": "pressurized_spawner"}','{"text": ""}']}}
setblock 220 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Pressurized"}','{"text": "Spawner"}','{"text": ""}']}}
fill 228 64 279 228 79 292 minecraft:light_gray_concrete
setblock 223 64 284 pneumaticcraft:pressurized_spawner
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
