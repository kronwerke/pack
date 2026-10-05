# 202 pneumaticcraft_advanced/first_run, electrostatic, thermal, adv_air, first_program, frames, security_station, spawner_extractor, pressurized_spawner
fill 302 63 376 393 63 389 minecraft:light_gray_concrete
fill 302 64 376 393 71 376 minecraft:light_gray_concrete
fill 302 64 376 302 71 389 minecraft:light_gray_concrete
setblock 303 64 388 minecraft:air
setblock 303 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.1"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_run"}','{"text": ""}']}}
setblock 304 64 388 minecraft:air
setblock 304 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lass die Straße"}','{"text": "laufen"}','{"text": ""}','{"text": ""}']}}
summon text_display 307.5 71 381.5 {text:'[{"text": "202.1  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/first_run", "color": "gray"}, {"text": "\\nLass die Straße laufen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 304 63 378 310 63 381 minecraft:polished_deepslate
fill 304 64 378 310 67 378 minecraft:deepslate_tiles
fill 304 64 378 310 64 378 minecraft:polished_blackstone
fill 304 67 378 310 67 378 minecraft:polished_blackstone
setblock 304 64 381 minecraft:lantern
setblock 310 64 381 minecraft:lantern
setblock 306 64 380 pneumaticcraft:pressure_chamber_valve
summon glow_item_frame 306 66 379 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"pneumaticcraft:assembly_program_drill",count:1}}
setblock 313 64 388 minecraft:air
setblock 313 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.2"}','{"text": "pneumaticcraft_advanced"}','{"text": "electrostatic"}','{"text": ""}']}}
setblock 314 64 388 minecraft:air
setblock 314 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Electrostatic"}','{"text": "Compressor"}','{"text": ""}']}}
summon text_display 317.5 71 381.5 {text:'[{"text": "202.2  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/electrostatic", "color": "gray"}, {"text": "\\nBau einen Electrostatic Compressor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 314 63 378 320 63 381 minecraft:polished_deepslate
fill 314 64 378 320 67 378 minecraft:deepslate_tiles
fill 314 64 378 320 64 378 minecraft:polished_blackstone
fill 314 67 378 320 67 378 minecraft:polished_blackstone
setblock 314 64 381 minecraft:lantern
setblock 320 64 381 minecraft:lantern
setblock 316 64 380 pneumaticcraft:electrostatic_compressor
setblock 323 64 388 minecraft:air
setblock 323 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.3"}','{"text": "pneumaticcraft_advanced"}','{"text": "thermal"}','{"text": ""}']}}
setblock 324 64 388 minecraft:air
setblock 324 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Thermal"}','{"text": "Compressor"}','{"text": ""}']}}
summon text_display 327.5 71 381.5 {text:'[{"text": "202.3  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/thermal", "color": "gray"}, {"text": "\\nBau einen Thermal Compressor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 324 63 378 330 63 381 minecraft:polished_deepslate
fill 324 64 378 330 67 378 minecraft:deepslate_tiles
fill 324 64 378 330 64 378 minecraft:polished_blackstone
fill 324 67 378 330 67 378 minecraft:polished_blackstone
setblock 324 64 381 minecraft:lantern
setblock 330 64 381 minecraft:lantern
setblock 326 64 380 pneumaticcraft:thermal_compressor
setblock 333 64 388 minecraft:air
setblock 333 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.4"}','{"text": "pneumaticcraft_advanced"}','{"text": "adv_air"}','{"text": ""}']}}
setblock 334 64 388 minecraft:air
setblock 334 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Advanced Air"}','{"text": "Compressor"}','{"text": ""}']}}
summon text_display 337.5 71 381.5 {text:'[{"text": "202.4  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/adv_air", "color": "gray"}, {"text": "\\nBau einen Advanced Air Compressor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 334 63 378 340 63 381 minecraft:polished_deepslate
fill 334 64 378 340 67 378 minecraft:deepslate_tiles
fill 334 64 378 340 64 378 minecraft:polished_blackstone
fill 334 67 378 340 67 378 minecraft:polished_blackstone
setblock 334 64 381 minecraft:lantern
setblock 340 64 381 minecraft:lantern
setblock 336 64 380 pneumaticcraft:advanced_air_compressor
setblock 343 64 388 minecraft:air
setblock 343 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.5"}','{"text": "pneumaticcraft_advanced"}','{"text": "first_program"}','{"text": ""}']}}
setblock 344 64 388 minecraft:air
setblock 344 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Programmiere"}','{"text": "deine erste"}','{"text": "Drohne"}','{"text": ""}']}}
summon text_display 347.5 71 381.5 {text:'[{"text": "202.5  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/first_program", "color": "gray"}, {"text": "\\nProgrammiere deine erste Drohne", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 344 63 378 350 63 381 minecraft:polished_deepslate
fill 344 64 378 350 67 378 minecraft:deepslate_tiles
fill 344 64 378 350 64 378 minecraft:polished_blackstone
fill 344 67 378 350 67 378 minecraft:polished_blackstone
setblock 344 64 381 minecraft:lantern
setblock 350 64 381 minecraft:lantern
summon glow_item_frame 346 66 379 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"pneumaticcraft:drone",count:1}}
setblock 353 64 388 minecraft:air
setblock 353 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.6"}','{"text": "pneumaticcraft_advanced"}','{"text": "frames"}','{"text": ""}']}}
setblock 354 64 388 minecraft:air
setblock 354 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Logistics"}','{"text": "Frames"}','{"text": ""}','{"text": ""}']}}
summon text_display 357.5 71 381.5 {text:'[{"text": "202.6  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/frames", "color": "gray"}, {"text": "\\nBau Logistics Frames", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 354 63 378 360 63 381 minecraft:polished_deepslate
fill 354 64 378 360 67 378 minecraft:deepslate_tiles
fill 354 64 378 360 64 378 minecraft:polished_blackstone
fill 354 67 378 360 67 378 minecraft:polished_blackstone
setblock 354 64 381 minecraft:lantern
setblock 360 64 381 minecraft:lantern
summon glow_item_frame 355 66 379 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"pneumaticcraft:logistics_frame_passive_provider",count:1}}
summon glow_item_frame 357 66 379 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"pneumaticcraft:logistics_frame_requester",count:1}}
setblock 363 64 388 minecraft:air
setblock 363 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.7"}','{"text": "pneumaticcraft_advanced"}','{"text": "security_station"}','{"text": ""}']}}
setblock 364 64 388 minecraft:air
setblock 364 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Security"}','{"text": "Station"}','{"text": ""}']}}
summon text_display 367.5 71 381.5 {text:'[{"text": "202.7  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/security_station", "color": "gray"}, {"text": "\\nBau eine Security Station", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 364 63 378 370 63 381 minecraft:polished_deepslate
fill 364 64 378 370 67 378 minecraft:deepslate_tiles
fill 364 64 378 370 64 378 minecraft:polished_blackstone
fill 364 67 378 370 67 378 minecraft:polished_blackstone
setblock 364 64 381 minecraft:lantern
setblock 370 64 381 minecraft:lantern
setblock 366 64 380 pneumaticcraft:security_station
setblock 373 64 388 minecraft:air
setblock 373 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.8"}','{"text": "pneumaticcraft_advanced"}','{"text": "spawner_extractor"}','{"text": ""}']}}
setblock 374 64 388 minecraft:air
setblock 374 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spawner"}','{"text": "Extractor"}','{"text": ""}']}}
summon text_display 377.5 71 381.5 {text:'[{"text": "202.8  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/spawner_extractor", "color": "gray"}, {"text": "\\nBau einen Spawner Extractor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 374 63 378 380 63 381 minecraft:polished_deepslate
fill 374 64 378 380 67 378 minecraft:deepslate_tiles
fill 374 64 378 380 64 378 minecraft:polished_blackstone
fill 374 67 378 380 67 378 minecraft:polished_blackstone
setblock 374 64 381 minecraft:lantern
setblock 380 64 381 minecraft:lantern
setblock 376 64 380 pneumaticcraft:spawner_extractor
setblock 383 64 388 minecraft:air
setblock 383 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "202.9"}','{"text": "pneumaticcraft_advanced"}','{"text": "pressurized_spawner"}','{"text": ""}']}}
setblock 384 64 388 minecraft:air
setblock 384 64 388 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Pressurized"}','{"text": "Spawner"}','{"text": ""}']}}
summon text_display 387.5 71 381.5 {text:'[{"text": "202.9  ", "color": "gold"}, {"text": "pneumaticcraft_advanced/pressurized_spawner", "color": "gray"}, {"text": "\\nBau einen Pressurized Spawner", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 384 63 378 390 63 381 minecraft:polished_deepslate
fill 384 64 378 390 67 378 minecraft:deepslate_tiles
fill 384 64 378 390 64 378 minecraft:polished_blackstone
fill 384 67 378 390 67 378 minecraft:polished_blackstone
setblock 384 64 381 minecraft:lantern
setblock 390 64 381 minecraft:lantern
setblock 386 64 380 pneumaticcraft:pressurized_spawner
