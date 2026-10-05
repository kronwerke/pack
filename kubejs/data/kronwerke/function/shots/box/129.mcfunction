# 129 gaia/arena
fill 248 63 186 263 63 203 minecraft:light_gray_concrete
fill 248 64 186 263 71 186 minecraft:light_gray_concrete
fill 248 64 186 248 71 203 minecraft:light_gray_concrete
setblock 249 64 202 minecraft:air
setblock 249 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "129"}','{"text": "gaia"}','{"text": "arena"}','{"text": ""}']}}
setblock 250 64 202 minecraft:air
setblock 250 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "beacon with"}','{"text": "four pylons"}','{"text": "from above"}','{"text": "Von oben:"}']}}
setblock 251 64 202 minecraft:air
setblock 251 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leuchtfeuer mit"}','{"text": "vier Pylonen"}','{"text": ""}','{"text": ""}']}}
summon text_display 255.5 71 193.5 {text:'[{"text": "129  ", "color": "gold"}, {"text": "gaia/arena", "color": "gray"}, {"text": "\\nBau die Arena", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template botania:gaia_ritual 250 64 188 none
setblock 261 64 199 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:gaia_spirit",count:1},{Slot:1b,id:"botania:terrasteel_ingot",count:1}]}
