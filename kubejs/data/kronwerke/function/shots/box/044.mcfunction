# 044 create_brass/pg_winding, pg_generator, pg_rheostat, pg_magnet
fill 0 63 77 41 63 90 minecraft:light_gray_concrete
fill 0 64 77 41 71 77 minecraft:light_gray_concrete
fill 0 64 77 0 71 90 minecraft:light_gray_concrete
setblock 1 64 89 minecraft:air
setblock 1 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044.1"}','{"text": "create_brass"}','{"text": "pg_winding"}','{"text": ""}']}}
setblock 2 64 89 minecraft:air
setblock 2 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the Power Grid"}','{"text": "parts, the full"}','{"text": "generator with"}','{"text": "a lamp, the"}']}}
setblock 3 64 89 minecraft:air
setblock 3 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "self excited"}','{"text": "wiring, the"}','{"text": "electromagnet"}','{"text": "over a depot"}']}}
setblock 4 64 89 minecraft:air
setblock 4 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Power Grid"}','{"text": "Teile, Lampe"}','{"text": "dran"}','{"text": ""}']}}
summon text_display 5.5 71 82.5 {text:'[{"text": "044.1  ", "color": "gold"}, {"text": "create_brass/pg_winding", "color": "gray"}, {"text": "\\nLeg Wicklungen um den Rotor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 2 64 80 powergrid:generator_induction_rotor
setblock 4 64 80 powergrid:generator_housing
setblock 6 64 80 powergrid:rheostat
setblock 8 64 80 powergrid:electromagnet
setblock 9 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"powergrid:copper_coil",count:1},{Slot:1b,id:"powergrid:wire_cutter",count:1}]}
setblock 11 64 89 minecraft:air
setblock 11 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044.2"}','{"text": "create_brass"}','{"text": "pg_generator"}','{"text": ""}']}}
setblock 12 64 89 minecraft:air
setblock 12 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Power Grid"}','{"text": "Teile, Lampe"}','{"text": "dran"}','{"text": ""}']}}
summon text_display 15.5 71 82.5 {text:'[{"text": "044.2  ", "color": "gold"}, {"text": "create_brass/pg_generator", "color": "gray"}, {"text": "\\nSchließ den Kollektor an", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 12 64 80 powergrid:generator_induction_rotor
setblock 14 64 80 powergrid:generator_housing
setblock 16 64 80 powergrid:rheostat
setblock 18 64 80 powergrid:electromagnet
setblock 19 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"powergrid:copper_coil",count:1},{Slot:1b,id:"powergrid:wire_cutter",count:1}]}
setblock 21 64 89 minecraft:air
setblock 21 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044.3"}','{"text": "create_brass"}','{"text": "pg_rheostat"}','{"text": ""}']}}
setblock 22 64 89 minecraft:air
setblock 22 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Power Grid"}','{"text": "Teile, Lampe"}','{"text": "dran"}','{"text": ""}']}}
summon text_display 25.5 71 82.5 {text:'[{"text": "044.3  ", "color": "gold"}, {"text": "create_brass/pg_rheostat", "color": "gray"}, {"text": "\\nLass den Generator sich selbst erregen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 22 64 80 powergrid:generator_induction_rotor
setblock 24 64 80 powergrid:generator_housing
setblock 26 64 80 powergrid:rheostat
setblock 28 64 80 powergrid:electromagnet
setblock 29 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"powergrid:copper_coil",count:1},{Slot:1b,id:"powergrid:wire_cutter",count:1}]}
setblock 31 64 89 minecraft:air
setblock 31 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "044.4"}','{"text": "create_brass"}','{"text": "pg_magnet"}','{"text": ""}']}}
setblock 32 64 89 minecraft:air
setblock 32 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Power Grid"}','{"text": "Teile, Lampe"}','{"text": "dran"}','{"text": ""}']}}
summon text_display 35.5 71 82.5 {text:'[{"text": "044.4  ", "color": "gold"}, {"text": "create_brass/pg_magnet", "color": "gray"}, {"text": "\\nMagnetisier Andesitlegierung", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 32 64 80 powergrid:generator_induction_rotor
setblock 34 64 80 powergrid:generator_housing
setblock 36 64 80 powergrid:rheostat
setblock 38 64 80 powergrid:electromagnet
setblock 39 64 86 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"powergrid:copper_coil",count:1},{Slot:1b,id:"powergrid:wire_cutter",count:1}]}
