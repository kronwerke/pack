# 057 mekanism/infuser
fill 0 63 108 11 63 121 minecraft:light_gray_concrete
fill 0 64 108 11 71 108 minecraft:light_gray_concrete
fill 0 64 108 0 71 121 minecraft:light_gray_concrete
setblock 1 64 120 minecraft:air
setblock 1 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057"}','{"text": "mekanism"}','{"text": "infuser"}','{"text": ""}']}}
setblock 2 64 120 minecraft:air
setblock 2 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "infuser GUI"}','{"text": "with the carbon"}','{"text": "bar and the"}','{"text": "electron tube"}']}}
setblock 3 64 120 minecraft:air
setblock 3 64 120 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "to circuit"}','{"text": "recipe"}','{"text": "GUI offen mit"}','{"text": "Kohle-Balken"}']}}
summon text_display 5.5 71 113.5 {text:'[{"text": "057  ", "color": "gold"}, {"text": "mekanism/infuser", "color": "gray"}, {"text": "\\nBau die Metallurgische Infusionsanlage", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 2 64 111 mekanism:metallurgic_infuser
setblock 9 64 117 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:16},{Slot:1b,id:"create:electron_tube",count:1}]}
