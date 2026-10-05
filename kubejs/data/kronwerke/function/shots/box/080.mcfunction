# 080 antimatter/reactor
fill 375 63 108 386 63 121 minecraft:light_gray_concrete
fill 375 64 108 386 71 108 minecraft:light_gray_concrete
fill 375 64 108 375 71 121 minecraft:light_gray_concrete
setblock 376 64 120 minecraft:air
setblock 376 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080"}','{"text": "antimatter"}','{"text": "reactor"}','{"text": ""}']}}
setblock 377 64 120 minecraft:air
setblock 377 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fission reactor"}','{"text": "GUI with fuel"}','{"text": "assemblies and"}','{"text": "control rods"}']}}
setblock 378 64 120 minecraft:air
setblock 378 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "GUI mit"}','{"text": "Brennstäben und"}','{"text": "Steuerstäben"}','{"text": ""}']}}
summon text_display 380.5 71 113.5 {text:'[{"text": "080  ", "color": "gold"}, {"text": "antimatter/reactor", "color": "gray"}, {"text": "\\nStarte den Spaltreaktor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 378 64 111 382 68 115 mekanismgenerators:fission_reactor_casing
fill 379 65 112 381 67 114 minecraft:air
fill 379 65 112 379 67 112 mekanismgenerators:fission_fuel_assembly
setblock 379 68 112 mekanismgenerators:control_rod_assembly
fill 381 65 112 381 67 112 mekanismgenerators:fission_fuel_assembly
setblock 381 68 112 mekanismgenerators:control_rod_assembly
fill 379 65 114 379 67 114 mekanismgenerators:fission_fuel_assembly
setblock 379 68 114 mekanismgenerators:control_rod_assembly
fill 381 65 114 381 67 114 mekanismgenerators:fission_fuel_assembly
setblock 381 68 114 mekanismgenerators:control_rod_assembly
fill 378 65 115 382 67 115 mekanismgenerators:reactor_glass
setblock 380 64 115 mekanismgenerators:fission_reactor_port
