# 091 pneumaticcraft_advanced/first_run, electrostatic, thermal, adv_air, security_station, spawner_extractor, pressurized_spawner
#area 154 254 233 279
fill 154 64 254 198 91 279 minecraft:air
fill 199 64 254 233 91 279 minecraft:air
fill 154 60 254 233 62 279 minecraft:stone
fill 154 63 254 233 63 279 minecraft:light_gray_concrete
fill 158 64 260 233 79 260 minecraft:light_gray_concrete
fill 158 64 260 158 79 273 minecraft:light_gray_concrete
setblock 159 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.1"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_run"}','{"text": ""}']}}
setblock 160 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Straße"}','{"text": "laufen"}','{"text": ""}','{"text": ""}']}}
fill 168 64 260 168 79 273 minecraft:light_gray_concrete
setblock 163 64 265 pneumaticcraft:assembly_platform
setblock 162 64 265 pneumaticcraft:assembly_drill
setblock 164 64 265 pneumaticcraft:assembly_laser
setblock 163 64 264 pneumaticcraft:assembly_io_unit_import
setblock 163 64 266 pneumaticcraft:assembly_io_unit_export
setblock 163 64 263 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 163 64 267 minecraft:chest[facing=south,type=single,waterlogged=false]
setblock 165 64 265 pneumaticcraft:assembly_controller
setblock 169 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.2"}','{"text": "pneumaticcraft_advanced"}','{"text": "electrostatic"}','{"text": ""}']}}
setblock 170 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Electrostatic"}','{"text": "Compressor"}','{"text": ""}']}}
fill 178 64 260 178 79 273 minecraft:light_gray_concrete
setblock 173 64 265 pneumaticcraft:electrostatic_compressor
fill 173 65 265 173 68 265 minecraft:iron_bars
setblock 173 69 265 minecraft:lightning_rod[facing=up,powered=false]
setblock 179 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.3"}','{"text": "pneumaticcraft_advanced"}','{"text": "thermal"}','{"text": ""}']}}
setblock 180 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermal"}','{"text": "Compressor"}','{"text": ""}']}}
fill 188 64 260 188 79 273 minecraft:light_gray_concrete
setblock 182 64 265 minecraft:magma_block
setblock 183 64 265 pneumaticcraft:thermal_compressor
setblock 184 64 265 minecraft:blue_ice
setblock 189 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.4"}','{"text": "pneumaticcraft_advanced"}','{"text": "adv_air"}','{"text": ""}']}}
setblock 190 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Advanced Air"}','{"text": "Compressor"}','{"text": ""}']}}
fill 198 64 260 198 79 273 minecraft:light_gray_concrete
setblock 193 64 265 pneumaticcraft:advanced_air_compressor[facing=south,on=true]
setblock 199 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.5"}','{"text": "pneumaticcraft_advanced"}','{"text": "security_station"}','{"text": ""}']}}
setblock 200 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Security"}','{"text": "Station"}','{"text": ""}']}}
fill 208 64 260 208 79 273 minecraft:light_gray_concrete
setblock 203 64 265 pneumaticcraft:security_station[facing=south]
setblock 209 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.6"}','{"text": "pneumaticcraft_advanced"}','{"text": "spawner_extractor"}','{"text": ""}']}}
setblock 210 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spawner"}','{"text": "Extractor"}','{"text": ""}']}}
fill 218 64 260 218 79 273 minecraft:light_gray_concrete
setblock 213 64 265 minecraft:spawner
setblock 213 65 265 pneumaticcraft:spawner_extractor
setblock 219 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091.7"}','{"text": "pneumaticcraft_advanced"}','{"text": "pressurized_spawner"}','{"text": ""}']}}
setblock 220 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Pressurized"}','{"text": "Spawner"}','{"text": ""}']}}
fill 228 64 260 228 79 273 minecraft:light_gray_concrete
setblock 223 64 265 pneumaticcraft:pressurized_spawner
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
