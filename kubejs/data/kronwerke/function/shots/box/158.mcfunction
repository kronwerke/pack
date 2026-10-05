# 158 hexerei/candles
fill 270 63 242 281 63 255 minecraft:light_gray_concrete
fill 270 64 242 281 71 242 minecraft:light_gray_concrete
fill 270 64 242 270 71 255 minecraft:light_gray_concrete
setblock 271 64 254 minecraft:air
setblock 271 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "158"}','{"text": "hexerei"}','{"text": "candles"}','{"text": ""}']}}
setblock 272 64 254 minecraft:air
setblock 272 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "candle dipper"}','{"text": "on a tallow"}','{"text": "cauldron with"}','{"text": "candles"}']}}
summon text_display 275.5 71 247.5 {text:'[{"text": "158  ", "color": "gold"}, {"text": "hexerei/candles", "color": "gray"}, {"text": "\\nZieh acht Kerzen", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 272 64 245 hexerei:candle_dipper
setblock 274 64 245 hexerei:mixing_cauldron
setblock 279 64 251 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"hexerei:tallow_impurity",count:16}]}
