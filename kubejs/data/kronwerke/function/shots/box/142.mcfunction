# 142 occultism/foliot_crusher
fill 30 63 242 41 63 255 minecraft:light_gray_concrete
fill 30 64 242 41 71 242 minecraft:light_gray_concrete
fill 30 64 242 30 71 255 minecraft:light_gray_concrete
setblock 31 64 254 minecraft:air
setblock 31 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142"}','{"text": "occultism"}','{"text": "foliot_crusher"}','{"text": ""}']}}
setblock 32 64 254 minecraft:air
setblock 32 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Foliot crusher"}','{"text": "next to a pile"}','{"text": "of dust"}','{"text": ""}']}}
summon text_display 35.5 71 247.5 {text:'[{"text": "142  ", "color": "gold"}, {"text": "occultism/foliot_crusher", "color": "gray"}, {"text": "\\nRuf einen Foliot Crusher", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 39 64 251 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"occultism:iron_dust",count:32}]}
summon occultism:foliot 33.5 64 249.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
