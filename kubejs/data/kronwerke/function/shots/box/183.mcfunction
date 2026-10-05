# 183 industrial/addons, sower, gatherer, bio, slaughter, crusher, duplicator
fill 0 63 315 71 63 328 minecraft:light_gray_concrete
fill 0 64 315 71 71 315 minecraft:light_gray_concrete
fill 0 64 315 0 71 328 minecraft:light_gray_concrete
setblock 1 64 327 minecraft:air
setblock 1 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.1"}','{"text": "industrial"}','{"text": "addons"}','{"text": ""}']}}
setblock 2 64 327 minecraft:air
setblock 2 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the machines at"}','{"text": "work"}','{"text": ""}','{"text": ""}']}}
summon text_display 5.5 71 320.5 {text:'[{"text": "183.1  ", "color": "gold"}, {"text": "industrial/addons", "color": "gray"}, {"text": "\\nSteck Addons in deine Maschinen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 2 64 318 industrialforegoing:plant_sower
setblock 9 64 324 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"industrialforegoing:speed_addon_tier_1",count:1},{Slot:1b,id:"industrialforegoing:efficiency_addon_tier_1",count:1}]}
setblock 11 64 327 minecraft:air
setblock 11 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.2"}','{"text": "industrial"}','{"text": "sower"}','{"text": ""}']}}
setblock 12 64 327 minecraft:air
setblock 12 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Sämaschine auf"}','{"text": ""}','{"text": ""}']}}
summon text_display 15.5 71 320.5 {text:'[{"text": "183.2  ", "color": "gold"}, {"text": "industrial/sower", "color": "gray"}, {"text": "\\nStell eine Sämaschine auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 12 63 317 18 63 323 minecraft:farmland
fill 12 64 317 18 64 323 minecraft:wheat[age=7]
setblock 15 64 320 industrialforegoing:plant_sower
setblock 15 65 320 industrialforegoing:plant_gatherer
setblock 21 64 327 minecraft:air
setblock 21 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.3"}','{"text": "industrial"}','{"text": "gatherer"}','{"text": ""}']}}
setblock 22 64 327 minecraft:air
setblock 22 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell eine"}','{"text": "Erntemaschine"}','{"text": "auf"}','{"text": ""}']}}
summon text_display 25.5 71 320.5 {text:'[{"text": "183.3  ", "color": "gold"}, {"text": "industrial/gatherer", "color": "gray"}, {"text": "\\nStell eine Erntemaschine auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 22 63 317 28 63 323 minecraft:farmland
fill 22 64 317 28 64 323 minecraft:wheat[age=7]
setblock 25 64 320 industrialforegoing:plant_sower
setblock 25 65 320 industrialforegoing:plant_gatherer
setblock 31 64 327 minecraft:air
setblock 31 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.4"}','{"text": "industrial"}','{"text": "bio"}','{"text": ""}']}}
setblock 32 64 327 minecraft:air
setblock 32 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Betreib einen"}','{"text": "Biogenerator"}','{"text": ""}','{"text": ""}']}}
summon text_display 35.5 71 320.5 {text:'[{"text": "183.4  ", "color": "gold"}, {"text": "industrial/bio", "color": "gray"}, {"text": "\\nBetreib einen Biogenerator", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 32 64 318 industrialforegoing:bioreactor
setblock 34 64 318 industrialforegoing:biofuel_generator
setblock 41 64 327 minecraft:air
setblock 41 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.5"}','{"text": "industrial"}','{"text": "slaughter"}','{"text": ""}']}}
setblock 42 64 327 minecraft:air
setblock 42 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Fang Pinken"}','{"text": "Schleim auf"}','{"text": ""}','{"text": ""}']}}
summon text_display 45.5 71 320.5 {text:'[{"text": "183.5  ", "color": "gold"}, {"text": "industrial/slaughter", "color": "gray"}, {"text": "\\nFang Pinken Schleim auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 42 64 318 industrialforegoing:mob_slaughter_factory
summon minecraft:cow 43.5 64 322.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon minecraft:pig 46.5 64 322.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 51 64 327 minecraft:air
setblock 51 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.6"}','{"text": "industrial"}','{"text": "crusher"}','{"text": ""}']}}
setblock 52 64 327 minecraft:air
setblock 52 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterschnetzler"}','{"text": "auf"}','{"text": ""}']}}
summon text_display 55.5 71 320.5 {text:'[{"text": "183.6  ", "color": "gold"}, {"text": "industrial/crusher", "color": "gray"}, {"text": "\\nStell einen Monsterschnetzler auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 52 64 318 industrialforegoing:mob_crusher
summon minecraft:zombie 53.5 64 322.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
setblock 61 64 327 minecraft:air
setblock 61 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "183.7"}','{"text": "industrial"}','{"text": "duplicator"}','{"text": ""}']}}
setblock 62 64 327 minecraft:air
setblock 62 64 327 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Monsterspawner"}','{"text": "auf"}','{"text": ""}']}}
summon text_display 65.5 71 320.5 {text:'[{"text": "183.7  ", "color": "gold"}, {"text": "industrial/duplicator", "color": "gray"}, {"text": "\\nStell einen Monsterspawner auf", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 62 64 318 industrialforegoing:mob_duplicator
