# 186 oritech/cores, pipes, plastic, laser, atomic_forge, destroyer, fragment_forge, fragment, addons, addon_quarry, addon_crop, exo, reactor
fill 0 63 336 131 63 349 minecraft:light_gray_concrete
fill 0 64 336 131 71 336 minecraft:light_gray_concrete
fill 0 64 336 0 71 349 minecraft:light_gray_concrete
setblock 1 64 348 minecraft:air
setblock 1 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.1"}','{"text": "oritech"}','{"text": "cores"}','{"text": ""}']}}
setblock 2 64 348 minecraft:air
setblock 2 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau"}','{"text": "Maschinenkerne"}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 341.5 {text:'[{"text": "186.1  ", "color": "gold"}, {"text": "oritech/cores", "color": "gray"}, {"text": "\\nBau Maschinenkerne", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 2 63 338 8 63 341 minecraft:polished_deepslate
fill 2 64 338 8 67 338 minecraft:deepslate_tiles
fill 2 64 338 8 64 338 minecraft:polished_blackstone
fill 2 67 338 8 67 338 minecraft:polished_blackstone
setblock 2 64 341 minecraft:lantern
setblock 8 64 341 minecraft:lantern
setblock 3 64 340 oritech:machine_core_1
setblock 5 64 340 oritech:machine_core_2
setblock 11 64 348 minecraft:air
setblock 11 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.2"}','{"text": "oritech"}','{"text": "pipes"}','{"text": ""}']}}
setblock 12 64 348 minecraft:air
setblock 12 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg Rohre"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 15.5 71 341.5 {text:'[{"text": "186.2  ", "color": "gold"}, {"text": "oritech/pipes", "color": "gray"}, {"text": "\\nLeg Rohre", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 12 63 338 18 63 341 minecraft:polished_deepslate
fill 12 64 338 18 67 338 minecraft:deepslate_tiles
fill 12 64 338 18 64 338 minecraft:polished_blackstone
fill 12 67 338 18 67 338 minecraft:polished_blackstone
setblock 12 64 341 minecraft:lantern
setblock 18 64 341 minecraft:lantern
setblock 13 64 340 oritech:energy_pipe
setblock 15 64 340 oritech:item_pipe
summon glow_item_frame 14 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:wrench",count:1}}
setblock 21 64 348 minecraft:air
setblock 21 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.3"}','{"text": "oritech"}','{"text": "plastic"}','{"text": ""}']}}
setblock 22 64 348 minecraft:air
setblock 22 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach Plastik"}','{"text": "aus Weizen"}','{"text": ""}','{"text": ""}']}}
summon text_display 25.5 71 341.5 {text:'[{"text": "186.3  ", "color": "gold"}, {"text": "oritech/plastic", "color": "gray"}, {"text": "\\nMach Plastik aus Weizen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 22 63 338 28 63 341 minecraft:polished_deepslate
fill 22 64 338 28 67 338 minecraft:deepslate_tiles
fill 22 64 338 28 64 338 minecraft:polished_blackstone
fill 22 67 338 28 67 338 minecraft:polished_blackstone
setblock 22 64 341 minecraft:lantern
setblock 28 64 341 minecraft:lantern
setblock 24 64 340 oritech:machine_fluid_addon
summon glow_item_frame 24 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:plastic_sheet",count:1}}
setblock 31 64 348 minecraft:air
setblock 31 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.4"}','{"text": "oritech"}','{"text": "laser"}','{"text": ""}']}}
setblock 32 64 348 minecraft:air
setblock 32 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den"}','{"text": "Enderischen"}','{"text": "Laser"}','{"text": ""}']}}
summon text_display 35.5 71 341.5 {text:'[{"text": "186.4  ", "color": "gold"}, {"text": "oritech/laser", "color": "gray"}, {"text": "\\nBau den Enderischen Laser", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 32 63 338 38 63 341 minecraft:polished_deepslate
fill 32 64 338 38 67 338 minecraft:deepslate_tiles
fill 32 64 338 38 64 338 minecraft:polished_blackstone
fill 32 67 338 38 67 338 minecraft:polished_blackstone
setblock 32 64 341 minecraft:lantern
setblock 38 64 341 minecraft:lantern
setblock 34 64 340 oritech:laser_arm_block
summon glow_item_frame 33 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:target_designator",count:1}}
summon glow_item_frame 35 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:fluxite",count:1}}
setblock 41 64 348 minecraft:air
setblock 41 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.5"}','{"text": "oritech"}','{"text": "atomic_forge"}','{"text": ""}']}}
setblock 42 64 348 minecraft:air
setblock 42 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Speis eine"}','{"text": "Atomic Forge"}','{"text": ""}','{"text": ""}']}}
summon text_display 45.5 71 341.5 {text:'[{"text": "186.5  ", "color": "gold"}, {"text": "oritech/atomic_forge", "color": "gray"}, {"text": "\\nSpeis eine Atomic Forge", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 45 64 341 oritech:atomic_forge_block
setblock 44 64 340 oritech:machine_core_2
setblock 45 64 340 oritech:machine_core_2
setblock 46 64 340 oritech:machine_core_2
setblock 44 64 341 oritech:machine_core_2
setblock 46 64 341 oritech:machine_core_2
setblock 44 64 342 oritech:machine_core_2
setblock 45 64 342 oritech:machine_core_2
setblock 46 64 342 oritech:machine_core_2
setblock 45 64 344 oritech:laser_arm_block
setblock 51 64 348 minecraft:air
setblock 51 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.6"}','{"text": "oritech"}','{"text": "destroyer"}','{"text": ""}']}}
setblock 52 64 348 minecraft:air
setblock 52 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann einen"}','{"text": "Rahmen mit"}','{"text": "Zerstörer"}','{"text": ""}']}}
summon text_display 55.5 71 341.5 {text:'[{"text": "186.6  ", "color": "gold"}, {"text": "oritech/destroyer", "color": "gray"}, {"text": "\\nSpann einen Rahmen mit Zerstörer", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 52 63 338 58 63 341 minecraft:polished_deepslate
fill 52 64 338 58 67 338 minecraft:deepslate_tiles
fill 52 64 338 58 64 338 minecraft:polished_blackstone
fill 52 67 338 58 67 338 minecraft:polished_blackstone
setblock 52 64 341 minecraft:lantern
setblock 58 64 341 minecraft:lantern
setblock 53 64 340 oritech:machine_frame_block
setblock 55 64 340 oritech:destroyer_block
setblock 61 64 348 minecraft:air
setblock 61 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.7"}','{"text": "oritech"}','{"text": "fragment_forge"}','{"text": ""}']}}
setblock 62 64 348 minecraft:air
setblock 62 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Fragment Forge"}','{"text": ""}','{"text": ""}']}}
summon text_display 65.5 71 341.5 {text:'[{"text": "186.7  ", "color": "gold"}, {"text": "oritech/fragment_forge", "color": "gray"}, {"text": "\\nBau die Fragment Forge", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 62 63 338 68 63 341 minecraft:polished_deepslate
fill 62 64 338 68 67 338 minecraft:deepslate_tiles
fill 62 64 338 68 64 338 minecraft:polished_blackstone
fill 62 67 338 68 67 338 minecraft:polished_blackstone
setblock 62 64 341 minecraft:lantern
setblock 68 64 341 minecraft:lantern
setblock 64 64 340 oritech:fragment_forge_block
summon glow_item_frame 64 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:flux_gate",count:1}}
setblock 71 64 348 minecraft:air
setblock 71 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.8"}','{"text": "oritech"}','{"text": "fragment"}','{"text": ""}']}}
setblock 72 64 348 minecraft:air
setblock 72 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ die"}','{"text": "Erzstraße"}','{"text": ""}','{"text": ""}']}}
summon text_display 75.5 71 341.5 {text:'[{"text": "186.8  ", "color": "gold"}, {"text": "oritech/fragment", "color": "gray"}, {"text": "\\nSchließ die Erzstraße", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 72 63 338 78 63 341 minecraft:polished_deepslate
fill 72 64 338 78 67 338 minecraft:deepslate_tiles
fill 72 64 338 78 64 338 minecraft:polished_blackstone
fill 72 67 338 78 67 338 minecraft:polished_blackstone
setblock 72 64 341 minecraft:lantern
setblock 78 64 341 minecraft:lantern
summon glow_item_frame 74 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:iron_gem",count:1}}
setblock 81 64 348 minecraft:air
setblock 81 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.9"}','{"text": "oritech"}','{"text": "addons"}','{"text": ""}']}}
setblock 82 64 348 minecraft:air
setblock 82 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz ein Speed"}','{"text": "Addon an"}','{"text": ""}','{"text": ""}']}}
summon text_display 85.5 71 341.5 {text:'[{"text": "186.9  ", "color": "gold"}, {"text": "oritech/addons", "color": "gray"}, {"text": "\\nSetz ein Speed Addon an", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 82 63 338 88 63 341 minecraft:polished_deepslate
fill 82 64 338 88 67 338 minecraft:deepslate_tiles
fill 82 64 338 88 64 338 minecraft:polished_blackstone
fill 82 67 338 88 67 338 minecraft:polished_blackstone
setblock 82 64 341 minecraft:lantern
setblock 88 64 341 minecraft:lantern
setblock 84 64 340 oritech:machine_speed_addon
setblock 91 64 348 minecraft:air
setblock 91 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.10"}','{"text": "oritech"}','{"text": "addon_quarry"}','{"text": ""}']}}
setblock 92 64 348 minecraft:air
setblock 92 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Mach einen"}','{"text": "Steinbruch mit"}','{"text": "dem Mine-Add-On"}','{"text": ""}']}}
summon text_display 95.5 71 341.5 {text:'[{"text": "186.10  ", "color": "gold"}, {"text": "oritech/addon_quarry", "color": "gray"}, {"text": "\\nMach einen Steinbruch mit dem Mine-Add-On", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 92 63 338 98 63 341 minecraft:polished_deepslate
fill 92 64 338 98 67 338 minecraft:deepslate_tiles
fill 92 64 338 98 64 338 minecraft:polished_blackstone
fill 92 67 338 98 67 338 minecraft:polished_blackstone
setblock 92 64 341 minecraft:lantern
setblock 98 64 341 minecraft:lantern
setblock 94 64 340 oritech:quarry_addon
setblock 101 64 348 minecraft:air
setblock 101 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.11"}','{"text": "oritech"}','{"text": "addon_crop"}','{"text": ""}']}}
setblock 102 64 348 minecraft:air
setblock 102 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ernte nur"}','{"text": "Reifes mit dem"}','{"text": "Ernte-Filter"}','{"text": ""}']}}
summon text_display 105.5 71 341.5 {text:'[{"text": "186.11  ", "color": "gold"}, {"text": "oritech/addon_crop", "color": "gray"}, {"text": "\\nErnte nur Reifes mit dem Ernte-Filter", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 102 63 338 108 63 341 minecraft:polished_deepslate
fill 102 64 338 108 67 338 minecraft:deepslate_tiles
fill 102 64 338 108 64 338 minecraft:polished_blackstone
fill 102 67 338 108 67 338 minecraft:polished_blackstone
setblock 102 64 341 minecraft:lantern
setblock 108 64 341 minecraft:lantern
setblock 104 64 340 oritech:crop_filter_addon
setblock 111 64 348 minecraft:air
setblock 111 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.12"}','{"text": "oritech"}','{"text": "exo"}','{"text": ""}']}}
setblock 112 64 348 minecraft:air
setblock 112 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zieh die"}','{"text": "Exo-Rüstung an"}','{"text": ""}','{"text": ""}']}}
summon text_display 115.5 71 341.5 {text:'[{"text": "186.12  ", "color": "gold"}, {"text": "oritech/exo", "color": "gray"}, {"text": "\\nZieh die Exo-Rüstung an", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 112 63 338 118 63 341 minecraft:polished_deepslate
fill 112 64 338 118 67 338 minecraft:deepslate_tiles
fill 112 64 338 118 64 338 minecraft:polished_blackstone
fill 112 67 338 118 67 338 minecraft:polished_blackstone
setblock 112 64 341 minecraft:lantern
setblock 118 64 341 minecraft:lantern
summon glow_item_frame 113 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:exo_helmet",count:1}}
summon glow_item_frame 115 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:exo_chestplate",count:1}}
summon glow_item_frame 117 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:exo_leggings",count:1}}
summon glow_item_frame 118 66 339 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"oritech:exo_boots",count:1}}
setblock 121 64 348 minecraft:air
setblock 121 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "186.13"}','{"text": "oritech"}','{"text": "reactor"}','{"text": ""}']}}
setblock 122 64 348 minecraft:air
setblock 122 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Kernreaktor"}','{"text": ""}','{"text": ""}']}}
summon text_display 125.5 71 341.5 {text:'[{"text": "186.13  ", "color": "gold"}, {"text": "oritech/reactor", "color": "gray"}, {"text": "\\nBau einen Kernreaktor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 122 63 338 128 63 341 minecraft:polished_deepslate
fill 122 64 338 128 67 338 minecraft:deepslate_tiles
fill 122 64 338 128 64 338 minecraft:polished_blackstone
fill 122 67 338 128 67 338 minecraft:polished_blackstone
setblock 122 64 341 minecraft:lantern
setblock 128 64 341 minecraft:lantern
setblock 123 64 340 oritech:reactor_controller
setblock 125 64 340 oritech:reactor_wall
setblock 127 64 340 oritech:reactor_rod
setblock 129 64 340 oritech:reactor_vent
setblock 131 64 340 oritech:reactor_fuel_port
setblock 133 64 340 oritech:reactor_energy_port
