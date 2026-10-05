# 131 gaia/tiara
fill 286 63 186 297 63 199 minecraft:light_gray_concrete
fill 286 64 186 297 71 186 minecraft:light_gray_concrete
fill 286 64 186 286 71 199 minecraft:light_gray_concrete
setblock 287 64 198 minecraft:air
setblock 287 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131"}','{"text": "gaia"}','{"text": "tiara"}','{"text": ""}']}}
setblock 288 64 198 minecraft:air
setblock 288 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "flying with the"}','{"text": "flight bar"}','{"text": "visible"}','{"text": "Fliegen mit"}']}}
setblock 289 64 198 minecraft:air
setblock 289 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Flugleiste"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 291.5 71 191.5 {text:'[{"text": "131  ", "color": "gold"}, {"text": "gaia/tiara", "color": "gray"}, {"text": "\\nCrafte die Flügel-Tiara", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 295 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:flugel_tiara",count:1}]}
