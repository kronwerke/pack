# 054 create_trains/cargo
fill 220 63 77 231 63 90 minecraft:light_gray_concrete
fill 220 64 77 231 71 77 minecraft:light_gray_concrete
fill 220 64 77 220 71 90 minecraft:light_gray_concrete
setblock 221 64 89 minecraft:air
setblock 221 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "create_trains"}','{"text": "cargo"}','{"text": ""}']}}
setblock 222 64 89 minecraft:air
setblock 222 64 89 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a portable"}','{"text": "storage"}','{"text": "interface pair"}','{"text": "at a platform"}']}}
summon text_display 225.5 71 82.5 {text:'[{"text": "054  ", "color": "gold"}, {"text": "create_trains/cargo", "color": "gray"}, {"text": "\\nLad Fracht am Bahnsteig", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 221 63 82 229 63 82 minecraft:gravel
fill 221 64 82 229 64 82 create:track[shape=xo]
setblock 225 64 84 create:portable_storage_interface[facing=north]
setblock 225 64 85 minecraft:chest
