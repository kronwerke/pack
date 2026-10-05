# 026 create/alloy_mixing
fill 102 63 52 117 63 65 minecraft:light_gray_concrete
fill 102 64 52 117 71 52 minecraft:light_gray_concrete
fill 102 64 52 102 71 65 minecraft:light_gray_concrete
setblock 103 64 64 minecraft:air
setblock 103 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "create"}','{"text": "alloy_mixing"}','{"text": ""}']}}
setblock 104 64 64 minecraft:air
setblock 104 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the whole"}','{"text": "andesite alloy"}','{"text": "line with"}','{"text": "belts, funnels,"}']}}
setblock 105 64 64 minecraft:air
setblock 105 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "mixer and"}','{"text": "output chest"}','{"text": "Andesitlegierung:"}','{"text": "Andesit und"}']}}
setblock 106 64 64 minecraft:air
setblock 106 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Eisennugget ins"}','{"text": "Becken"}','{"text": ""}','{"text": ""}']}}
summon text_display 109.5 71 57.5 {text:'[{"text": "026  ", "color": "gold"}, {"text": "create/alloy_mixing", "color": "gray"}, {"text": "\\nMisch Legierung am Band", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
place template create:gametest/processing/brass_mixing 104 64 54 none
setblock 115 64 61 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:andesite",count:64},{Slot:1b,id:"minecraft:iron_nugget",count:64}]}
