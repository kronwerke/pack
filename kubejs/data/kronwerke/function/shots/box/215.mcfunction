# 215 nuclearcraft/reactor, irradiation, geiger
fill 116 63 467 149 63 482 minecraft:light_gray_concrete
fill 116 64 467 149 71 467 minecraft:light_gray_concrete
fill 116 64 467 116 71 482 minecraft:light_gray_concrete
setblock 117 64 481 minecraft:air
setblock 117 64 481 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "215.1"}','{"text": "nuclearcraft"}','{"text": "reactor"}','{"text": ""}']}}
setblock 118 64 481 minecraft:air
setblock 118 64 481 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Starte den"}','{"text": "ersten"}','{"text": "Spaltreaktor"}','{"text": ""}']}}
fill 119 64 470 125 70 476 nuclearcraft:fission_reactor_casing
fill 120 65 471 124 69 475 nuclearcraft:graphite_block
fill 121 65 472 121 69 472 nuclearcraft:fission_reactor_solid_fuel_cell
fill 121 65 474 121 69 474 nuclearcraft:fission_reactor_solid_fuel_cell
fill 123 65 472 123 69 472 nuclearcraft:fission_reactor_solid_fuel_cell
fill 123 65 474 123 69 474 nuclearcraft:fission_reactor_solid_fuel_cell
fill 120 65 476 124 69 476 nuclearcraft:fission_reactor_glass
setblock 122 64 476 nuclearcraft:fission_reactor_controller[facing=south]
setblock 119 67 473 nuclearcraft:fission_reactor_port
setblock 129 64 481 minecraft:air
setblock 129 64 481 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "215.2"}','{"text": "nuclearcraft"}','{"text": "irradiation"}','{"text": ""}']}}
setblock 130 64 481 minecraft:air
setblock 130 64 481 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bestrahl Stoffe"}','{"text": "im Reaktor"}','{"text": ""}','{"text": ""}']}}
setblock 130 64 471 nuclearcraft:fission_reactor_irradiation_chamber
setblock 132 64 471 nuclearcraft:irradiator
setblock 139 64 481 minecraft:air
setblock 139 64 481 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "215.3"}','{"text": "nuclearcraft"}','{"text": "geiger"}','{"text": ""}']}}
setblock 140 64 481 minecraft:air
setblock 140 64 481 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Geigerzähler"}','{"text": "und Dosimeter"}','{"text": ""}']}}
setblock 140 64 471 minecraft:polished_andesite
summon item_frame 140 64 472 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"nuclear_radiation:geiger_counter",count:1}}
setblock 142 64 471 minecraft:polished_andesite
summon item_frame 142 64 472 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"nuclear_radiation:dosimeter",count:1}}
