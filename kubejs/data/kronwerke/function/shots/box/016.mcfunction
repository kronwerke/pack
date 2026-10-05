# 016 farms/lava_seeds
fill 98 63 31 109 63 44 minecraft:light_gray_concrete
fill 98 64 31 109 71 31 minecraft:light_gray_concrete
fill 98 64 31 98 71 44 minecraft:light_gray_concrete
setblock 99 64 43 minecraft:air
setblock 99 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "016"}','{"text": "farms"}','{"text": "lava_seeds"}','{"text": ""}']}}
setblock 100 64 43 minecraft:air
setblock 100 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fire seed"}','{"text": "field, the lava"}','{"text": "bucket recipe,"}','{"text": "item drain into"}']}}
setblock 101 64 43 minecraft:air
setblock 101 64 43 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fluid tanks"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
summon text_display 103.5 71 36.5 {text:'[{"text": "016  ", "color": "gold"}, {"text": "farms/lava_seeds", "color": "gray"}, {"text": "\\nZüchte Lava auf dem Feld", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 100 63 34 104 63 36 mysticalagriculture:inferium_farmland
fill 100 64 34 104 64 36 mysticalagriculture:fire_crop[age=7]
setblock 106 64 35 create:item_drain
setblock 106 64 37 create:fluid_tank
setblock 106 65 37 create:fluid_tank
