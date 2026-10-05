# 139 alfheim/elementium_armor
fill 30 63 223 41 63 236 minecraft:light_gray_concrete
fill 30 64 223 41 71 223 minecraft:light_gray_concrete
fill 30 64 223 30 71 236 minecraft:light_gray_concrete
setblock 31 64 235 minecraft:air
setblock 31 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "139"}','{"text": "alfheim"}','{"text": "elementium_armor"}','{"text": ""}']}}
setblock 32 64 235 minecraft:air
setblock 32 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pixie"}','{"text": "attacking a mob"}','{"text": "Elementium-Rüstung"}','{"text": "an, Mob"}']}}
setblock 33 64 235 minecraft:air
setblock 33 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "angreifen"}','{"text": "lassen"}','{"text": ""}','{"text": ""}']}}
summon text_display 35.5 71 228.5 {text:'[{"text": "139  ", "color": "gold"}, {"text": "alfheim/elementium_armor", "color": "gray"}, {"text": "\\nTrag Elementiumrüstung", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 39 64 232 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"botania:elementium_chestplate",count:1}]}
summon minecraft:zombie 33.5 64 230.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
