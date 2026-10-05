# 123 botania_runes/thermalily
fill 156 63 186 167 63 199 minecraft:light_gray_concrete
fill 156 64 186 167 71 186 minecraft:light_gray_concrete
fill 156 64 186 156 71 199 minecraft:light_gray_concrete
setblock 157 64 198 minecraft:air
setblock 157 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "123"}','{"text": "botania_runes"}','{"text": "thermalily"}','{"text": ""}']}}
setblock 158 64 198 minecraft:air
setblock 158 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a hose pulley"}','{"text": "feeding lava"}','{"text": "next to the"}','{"text": "lily"}']}}
summon text_display 161.5 71 191.5 {text:'[{"text": "123  ", "color": "gold"}, {"text": "botania_runes/thermalily", "color": "gray"}, {"text": "\\nPflanz eine Thermalilie", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 161 64 191 botania:thermalily
setblock 161 66 191 create:hose_pulley[facing=south]
setblock 161 64 189 botania:mana_spreader
