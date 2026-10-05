# 124 botania_runes/gourmaryllis
fill 171 63 186 184 63 199 minecraft:light_gray_concrete
fill 171 64 186 184 71 186 minecraft:light_gray_concrete
fill 171 64 186 171 71 199 minecraft:light_gray_concrete
setblock 172 64 198 minecraft:air
setblock 172 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "124"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 173 64 198 minecraft:air
setblock 173 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": "Riemen über die"}','{"text": "Blume,"}']}}
setblock 174 64 198 minecraft:air
setblock 174 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "verschiedene"}','{"text": "Essen"}','{"text": ""}','{"text": ""}']}}
summon text_display 177.5 71 191.5 {text:'[{"text": "124  ", "color": "gold"}, {"text": "botania_runes/gourmaryllis", "color": "gray"}, {"text": "\\nPflanz eine Gourmaryllis", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 176 64 191 botania:gourmaryllis
setblock 182 64 195 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:bread",count:16},{Slot:1b,id:"minecraft:cooked_beef",count:16},{Slot:2b,id:"minecraft:baked_potato",count:16},{Slot:3b,id:"farmersdelight:tomato",count:16},{Slot:4b,id:"create:belt_connector",count:1}]}
