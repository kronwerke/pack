# 215 nuclearcraft/reactor, irradiation, geiger
fill 116 63 485 149 63 500 minecraft:light_gray_concrete
fill 116 64 485 149 71 485 minecraft:light_gray_concrete
fill 116 64 485 116 71 500 minecraft:light_gray_concrete
setblock 117 64 499 minecraft:air
setblock 117 64 499 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "215.1"}','{"text": "nuclearcraft"}','{"text": "reactor"}','{"text": ""}']}}
setblock 118 64 499 minecraft:air
setblock 118 64 499 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Starte den"}','{"text": "ersten"}','{"text": "Spaltreaktor"}','{"text": ""}']}}
summon text_display 122.5 71 491.5 {text:'[{"text": "215.1  ", "color": "gold"}, {"text": "nuclearcraft/reactor", "color": "gray"}, {"text": "\\nStarte den ersten Spaltreaktor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 119 64 488 125 70 494 nuclearcraft:fission_reactor_casing
fill 120 65 489 124 69 493 nuclearcraft:graphite_block
fill 121 65 490 121 69 490 nuclearcraft:fission_reactor_solid_fuel_cell
fill 121 65 492 121 69 492 nuclearcraft:fission_reactor_solid_fuel_cell
fill 123 65 490 123 69 490 nuclearcraft:fission_reactor_solid_fuel_cell
fill 123 65 492 123 69 492 nuclearcraft:fission_reactor_solid_fuel_cell
fill 120 65 494 124 69 494 nuclearcraft:fission_reactor_glass
setblock 122 64 494 nuclearcraft:fission_reactor_controller[facing=south]
setblock 119 67 491 nuclearcraft:fission_reactor_port
setblock 129 64 499 minecraft:air
setblock 129 64 499 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "215.2"}','{"text": "nuclearcraft"}','{"text": "irradiation"}','{"text": ""}']}}
setblock 130 64 499 minecraft:air
setblock 130 64 499 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bestrahl Stoffe"}','{"text": "im Reaktor"}','{"text": ""}','{"text": ""}']}}
summon text_display 133.5 71 490.5 {text:'[{"text": "215.2  ", "color": "gold"}, {"text": "nuclearcraft/irradiation", "color": "gray"}, {"text": "\\nBestrahl Stoffe im Reaktor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 130 63 487 136 63 490 minecraft:polished_deepslate
fill 130 64 487 136 67 487 minecraft:deepslate_tiles
fill 130 64 487 136 64 487 minecraft:polished_blackstone
fill 130 67 487 136 67 487 minecraft:polished_blackstone
setblock 130 64 490 minecraft:lantern
setblock 136 64 490 minecraft:lantern
setblock 131 64 489 nuclearcraft:fission_reactor_irradiation_chamber
setblock 133 64 489 nuclearcraft:irradiator
setblock 139 64 499 minecraft:air
setblock 139 64 499 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "215.3"}','{"text": "nuclearcraft"}','{"text": "geiger"}','{"text": ""}']}}
setblock 140 64 499 minecraft:air
setblock 140 64 499 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Geigerzähler"}','{"text": "und Dosimeter"}','{"text": ""}']}}
summon text_display 143.5 71 490.5 {text:'[{"text": "215.3  ", "color": "gold"}, {"text": "nuclearcraft/geiger", "color": "gray"}, {"text": "\\nBau Geigerzähler und Dosimeter", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 140 63 487 146 63 490 minecraft:polished_deepslate
fill 140 64 487 146 67 487 minecraft:deepslate_tiles
fill 140 64 487 146 64 487 minecraft:polished_blackstone
fill 140 67 487 146 67 487 minecraft:polished_blackstone
setblock 140 64 490 minecraft:lantern
setblock 146 64 490 minecraft:lantern
summon glow_item_frame 141 66 488 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"nuclear_radiation:geiger_counter",count:1}}
summon glow_item_frame 143 66 488 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"nuclear_radiation:dosimeter",count:1}}
