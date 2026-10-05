# 185 industrial/washing, conveyor, transporters
fill 116 63 315 151 63 328 minecraft:light_gray_concrete
fill 116 64 315 151 71 315 minecraft:light_gray_concrete
fill 116 64 315 116 71 328 minecraft:light_gray_concrete
setblock 117 64 327 minecraft:air
setblock 117 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "185.1"}','{"text": "industrial"}','{"text": "washing"}','{"text": ""}']}}
setblock 118 64 327 minecraft:air
setblock 118 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the ore meat"}','{"text": "machines in a"}','{"text": "row, conveyors"}','{"text": "with upgrades,"}']}}
setblock 119 64 327 minecraft:air
setblock 119 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "two"}','{"text": "transporters"}','{"text": ""}','{"text": ""}']}}
summon text_display 121.5 71 320.5 {text:'[{"text": "185.1  ", "color": "gold"}, {"text": "industrial/washing", "color": "gray"}, {"text": "\\nBau eine Waschfabrik", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 118 64 318 industrialforegoing:washing_factory
setblock 120 64 318 industrialforegoing:fermentation_station
setblock 122 64 318 industrialforegoing:fluid_sieving_machine
setblock 127 64 327 minecraft:air
setblock 127 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "185.2"}','{"text": "industrial"}','{"text": "conveyor"}','{"text": ""}']}}
setblock 128 64 327 minecraft:air
setblock 128 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leg"}','{"text": "Förderbänder"}','{"text": ""}','{"text": ""}']}}
summon text_display 132.5 71 320.5 {text:'[{"text": "185.2  ", "color": "gold"}, {"text": "industrial/conveyor", "color": "gray"}, {"text": "\\nLeg Förderbänder", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 128 64 320 136 64 320 industrialforegoing:conveyor[facing=east]
setblock 137 64 324 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"industrialforegoing:conveyor_insertion_upgrade",count:1},{Slot:1b,id:"industrialforegoing:conveyor_extraction_upgrade",count:1},{Slot:2b,id:"industrialforegoing:conveyor_detection_upgrade",count:1}]}
setblock 139 64 327 minecraft:air
setblock 139 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "185.3"}','{"text": "industrial"}','{"text": "transporters"}','{"text": ""}']}}
setblock 140 64 327 minecraft:air
setblock 140 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Inventare mit"}','{"text": "Transportern"}','{"text": ""}']}}
summon text_display 144.5 71 320.5 {text:'[{"text": "185.3  ", "color": "gold"}, {"text": "industrial/transporters", "color": "gray"}, {"text": "\\nVerbinde zwei Inventare mit Transportern", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 140 64 320 148 64 320 industrialforegoing:conveyor[facing=east]
setblock 149 64 324 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"industrialforegoing:conveyor_insertion_upgrade",count:1},{Slot:1b,id:"industrialforegoing:conveyor_extraction_upgrade",count:1},{Slot:2b,id:"industrialforegoing:conveyor_detection_upgrade",count:1}]}
