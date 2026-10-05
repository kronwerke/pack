# 143 occultism/foliot_janitor
fill 45 63 242 56 63 255 minecraft:light_gray_concrete
fill 45 64 242 56 71 242 minecraft:light_gray_concrete
fill 45 64 242 45 71 255 minecraft:light_gray_concrete
setblock 46 64 254 minecraft:air
setblock 46 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143"}','{"text": "occultism"}','{"text": "foliot_janitor"}','{"text": ""}']}}
setblock 47 64 254 minecraft:air
setblock 47 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "transporter,"}','{"text": "crusher and"}','{"text": "janitor working"}','{"text": "with chests"}']}}
summon text_display 50.5 71 247.5 {text:'[{"text": "143  ", "color": "gold"}, {"text": "occultism/foliot_janitor", "color": "gray"}, {"text": "\\nRuf einen Foliot Janitor", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 47 64 245 minecraft:chest
setblock 49 64 245 minecraft:chest
summon occultism:foliot 48.5 64 249.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon occultism:foliot 51.5 64 249.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
