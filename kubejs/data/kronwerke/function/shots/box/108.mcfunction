# 108 ars_epic/breath
fill 382 63 148 393 63 161 minecraft:light_gray_concrete
fill 382 64 148 393 71 148 minecraft:light_gray_concrete
fill 382 64 148 382 71 161 minecraft:light_gray_concrete
setblock 383 64 160 minecraft:air
setblock 383 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108"}','{"text": "ars_epic"}','{"text": "breath"}','{"text": ""}']}}
setblock 384 64 160 minecraft:air
setblock 384 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "bottling dragon"}','{"text": "breath"}','{"text": "Im End:"}','{"text": "Drachenatem"}']}}
setblock 385 64 160 minecraft:air
setblock 385 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "abfüllen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 387.5 71 153.5 {text:'[{"text": "108  ", "color": "gold"}, {"text": "ars_epic/breath", "color": "gray"}, {"text": "\\nFüll Drachenatem ab", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 384 64 151 minecraft:dragon_head
setblock 391 64 157 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:glass_bottle",count:16}]}
