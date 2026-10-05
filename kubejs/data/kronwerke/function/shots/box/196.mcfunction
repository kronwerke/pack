# 196 list_power/steam_engine, mek_heat, ie_thermo, alternator, powah_reactor, flux, mekmm_large, nc_passive, draconic_core
fill 0 63 376 99 63 395 minecraft:light_gray_concrete
fill 0 64 376 99 71 376 minecraft:light_gray_concrete
fill 0 64 376 0 71 395 minecraft:light_gray_concrete
setblock 1 64 394 minecraft:air
setblock 1 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.1"}','{"text": "list_power"}','{"text": "steam_engine"}','{"text": ""}']}}
setblock 2 64 394 minecraft:air
setblock 2 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Heiz einen"}','{"text": "Dampfkessel an"}','{"text": ""}','{"text": ""}']}}
summon text_display 6.5 71 381.5 {text:'[{"text": "196.1  ", "color": "gold"}, {"text": "list_power/steam_engine", "color": "gray"}, {"text": "\\nHeiz einen Dampfkessel an", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/fluids/steam_engine 2 64 378 none
setblock 13 64 394 minecraft:air
setblock 13 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.2"}','{"text": "list_power"}','{"text": "mek_heat"}','{"text": ""}']}}
setblock 14 64 394 minecraft:air
setblock 14 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Wärmegenerator"}','{"text": "in Lava"}','{"text": ""}']}}
summon text_display 17.5 71 381.5 {text:'[{"text": "196.2  ", "color": "gold"}, {"text": "list_power/mek_heat", "color": "gray"}, {"text": "\\nStell einen Wärmegenerator in Lava", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 14 63 378 20 63 381 minecraft:polished_deepslate
fill 14 64 378 20 67 378 minecraft:deepslate_tiles
fill 14 64 378 20 64 378 minecraft:polished_blackstone
fill 14 67 378 20 67 378 minecraft:polished_blackstone
setblock 14 64 381 minecraft:lantern
setblock 20 64 381 minecraft:lantern
summon glow_item_frame 16 66 379 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:lava_bucket",count:1}}
setblock 23 64 394 minecraft:air
setblock 23 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.3"}','{"text": "list_power"}','{"text": "ie_thermo"}','{"text": ""}']}}
setblock 24 64 394 minecraft:air
setblock 24 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann Lava"}','{"text": "gegen Wasser"}','{"text": ""}','{"text": ""}']}}
summon text_display 27.5 71 381.5 {text:'[{"text": "196.3  ", "color": "gold"}, {"text": "list_power/ie_thermo", "color": "gray"}, {"text": "\\nSpann Lava gegen Wasser", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 24 63 378 30 63 381 minecraft:polished_deepslate
fill 24 64 378 30 67 378 minecraft:deepslate_tiles
fill 24 64 378 30 64 378 minecraft:polished_blackstone
fill 24 67 378 30 67 378 minecraft:polished_blackstone
setblock 24 64 381 minecraft:lantern
setblock 30 64 381 minecraft:lantern
setblock 26 64 380 minecraft:lightning_rod
setblock 33 64 394 minecraft:air
setblock 33 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.4"}','{"text": "list_power"}','{"text": "alternator"}','{"text": ""}']}}
setblock 34 64 394 minecraft:air
setblock 34 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach aus"}','{"text": "Rotation Strom"}','{"text": ""}','{"text": ""}']}}
summon text_display 37.5 71 381.5 {text:'[{"text": "196.4  ", "color": "gold"}, {"text": "list_power/alternator", "color": "gray"}, {"text": "\\nMach aus Rotation Strom", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 34 63 378 40 63 381 minecraft:polished_deepslate
fill 34 64 378 40 67 378 minecraft:deepslate_tiles
fill 34 64 378 40 64 378 minecraft:polished_blackstone
fill 34 67 378 40 67 378 minecraft:polished_blackstone
setblock 34 64 381 minecraft:lantern
setblock 40 64 381 minecraft:lantern
setblock 36 64 380 create:cogwheel
setblock 43 64 394 minecraft:air
setblock 43 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.5"}','{"text": "list_power"}','{"text": "powah_reactor"}','{"text": ""}']}}
setblock 44 64 394 minecraft:air
setblock 44 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den"}','{"text": "Powah-Reaktor"}','{"text": ""}','{"text": ""}']}}
summon text_display 47.5 71 381.5 {text:'[{"text": "196.5  ", "color": "gold"}, {"text": "list_power/powah_reactor", "color": "gray"}, {"text": "\\nZünde den Powah-Reaktor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 44 63 378 50 63 381 minecraft:polished_deepslate
fill 44 64 378 50 67 378 minecraft:deepslate_tiles
fill 44 64 378 50 64 378 minecraft:polished_blackstone
fill 44 67 378 50 67 378 minecraft:polished_blackstone
setblock 44 64 381 minecraft:lantern
setblock 50 64 381 minecraft:lantern
summon glow_item_frame 46 66 379 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:water_bucket",count:1}}
setblock 53 64 394 minecraft:air
setblock 53 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.6"}','{"text": "list_power"}','{"text": "flux"}','{"text": ""}']}}
setblock 54 64 394 minecraft:air
setblock 54 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Flux-Netzwerk"}','{"text": ""}','{"text": ""}']}}
summon text_display 57.5 71 381.5 {text:'[{"text": "196.6  ", "color": "gold"}, {"text": "list_power/flux", "color": "gray"}, {"text": "\\nBau ein Flux-Netzwerk", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 54 63 378 60 63 381 minecraft:polished_deepslate
fill 54 64 378 60 67 378 minecraft:deepslate_tiles
fill 54 64 378 60 64 378 minecraft:polished_blackstone
fill 54 67 378 60 67 378 minecraft:polished_blackstone
setblock 54 64 381 minecraft:lantern
setblock 60 64 381 minecraft:lantern
summon glow_item_frame 56 66 379 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"ars_nouveau:source_gem",count:1}}
setblock 63 64 394 minecraft:air
setblock 63 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.7"}','{"text": "list_power"}','{"text": "mekmm_large"}','{"text": ""}']}}
setblock 64 64 394 minecraft:air
setblock 64 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell die"}','{"text": "großen"}','{"text": "Generatoren"}','{"text": ""}']}}
summon text_display 67.5 71 381.5 {text:'[{"text": "196.7  ", "color": "gold"}, {"text": "list_power/mekmm_large", "color": "gray"}, {"text": "\\nStell die großen Generatoren", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 64 63 378 70 63 381 minecraft:polished_deepslate
fill 64 64 378 70 67 378 minecraft:deepslate_tiles
fill 64 64 378 70 64 378 minecraft:polished_blackstone
fill 64 67 378 70 67 378 minecraft:polished_blackstone
setblock 64 64 381 minecraft:lantern
setblock 70 64 381 minecraft:lantern
setblock 66 64 380 create:encased_fan
setblock 73 64 394 minecraft:air
setblock 73 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.8"}','{"text": "list_power"}','{"text": "nc_passive"}','{"text": ""}']}}
setblock 74 64 394 minecraft:air
setblock 74 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Solarzellen"}','{"text": "und RTGs"}','{"text": ""}','{"text": ""}']}}
summon text_display 77.5 71 381.5 {text:'[{"text": "196.8  ", "color": "gold"}, {"text": "list_power/nc_passive", "color": "gray"}, {"text": "\\nLeg Solarzellen und RTGs", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 74 63 378 80 63 381 minecraft:polished_deepslate
fill 74 64 378 80 67 378 minecraft:deepslate_tiles
fill 74 64 378 80 64 378 minecraft:polished_blackstone
fill 74 67 378 80 67 378 minecraft:polished_blackstone
setblock 74 64 381 minecraft:lantern
setblock 80 64 381 minecraft:lantern
setblock 76 64 380 minecraft:daylight_detector
setblock 83 64 394 minecraft:air
setblock 83 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "196.9"}','{"text": "list_power"}','{"text": "draconic_core"}','{"text": ""}']}}
setblock 84 64 394 minecraft:air
setblock 84 64 394 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Build Guide im"}','{"text": "Kern zeigt die"}','{"text": "Hülle"}','{"text": ""}']}}
summon text_display 90.5 71 384.5 {text:'[{"text": "196.9  ", "color": "gold"}, {"text": "list_power/draconic_core", "color": "gray"}, {"text": "\\nBau den Energiekern", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 90 66 384 draconicevolution:energy_core
setblock 90 66 378 draconicevolution:energy_core_stabilizer
setblock 90 66 390 draconicevolution:energy_core_stabilizer
setblock 84 66 384 draconicevolution:energy_core_stabilizer
setblock 96 66 384 draconicevolution:energy_core_stabilizer
setblock 97 64 391 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"draconicevolution:draconium_block",count:16},{Slot:1b,id:"minecraft:redstone_block",count:16}]}
