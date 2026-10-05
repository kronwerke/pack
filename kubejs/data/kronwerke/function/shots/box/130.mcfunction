# 130 gaia/fight
fill 267 63 186 282 63 203 minecraft:light_gray_concrete
fill 267 64 186 282 71 186 minecraft:light_gray_concrete
fill 267 64 186 267 71 203 minecraft:light_gray_concrete
setblock 268 64 202 minecraft:air
setblock 268 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130"}','{"text": "gaia"}','{"text": "fight"}','{"text": ""}']}}
setblock 269 64 202 minecraft:air
setblock 269 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the guardian"}','{"text": "with the purple"}','{"text": "traps"}','{"text": "Von oben:"}']}}
setblock 270 64 202 minecraft:air
setblock 270 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Leuchtfeuer mit"}','{"text": "vier Pylonen"}','{"text": ""}','{"text": ""}']}}
summon text_display 274.5 71 193.5 {text:'[{"text": "130  ", "color": "gold"}, {"text": "gaia/fight", "color": "gray"}, {"text": "\\nBesiege den Wächter von Gaia", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template botania:gaia_ritual 269 64 188 none
setblock 280 64 199 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:gaia_spirit",count:1},{Slot:1b,id:"botania:terrasteel_ingot",count:1}]}
