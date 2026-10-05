# 078 mekanism_elite/fusion
fill 343 63 108 356 63 123 minecraft:light_gray_concrete
fill 343 64 108 356 71 108 minecraft:light_gray_concrete
fill 343 64 108 343 71 123 minecraft:light_gray_concrete
setblock 344 64 122 minecraft:air
setblock 344 64 122 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078"}','{"text": "mekanism_elite"}','{"text": "fusion"}','{"text": ""}']}}
setblock 345 64 122 minecraft:air
setblock 345 64 122 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fusion reactor"}','{"text": "with laser and"}','{"text": "amplifier"}','{"text": ""}']}}
summon text_display 349.5 71 114.5 {text:'[{"text": "078  ", "color": "gold"}, {"text": "mekanism_elite/fusion", "color": "gray"}, {"text": "\\nZünd den Fusionsreaktor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 346 64 111 350 68 115 mekanismgenerators:fusion_reactor_frame
fill 347 65 112 349 67 114 minecraft:air
setblock 348 68 113 mekanismgenerators:fusion_reactor_controller
setblock 348 66 116 mekanism:laser
setblock 348 66 118 mekanism:laser_amplifier
