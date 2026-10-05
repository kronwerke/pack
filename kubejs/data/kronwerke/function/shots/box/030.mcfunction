# 030 create/frogport
fill 168 63 52 183 63 65 minecraft:light_gray_concrete
fill 168 64 52 183 71 52 minecraft:light_gray_concrete
fill 168 64 52 168 71 65 minecraft:light_gray_concrete
setblock 169 64 64 minecraft:air
setblock 169 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "create"}','{"text": "frogport"}','{"text": ""}']}}
setblock 170 64 64 minecraft:air
setblock 170 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain conveyor"}','{"text": "with a frogport"}','{"text": "carrying a"}','{"text": "package"}']}}
setblock 171 64 64 minecraft:air
setblock 171 64 64 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Kette zwischen"}','{"text": "den Förderern"}','{"text": "ziehen, Frosch"}','{"text": "anhängen"}']}}
summon text_display 175.5 71 57.5 {text:'[{"text": "030  ", "color": "gold"}, {"text": "create/frogport", "color": "gray"}, {"text": "\\nSchick Pakete per Kette", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 171 64 57 create:shaft[axis=y]
setblock 171 65 57 create:chain_conveyor
setblock 179 64 57 create:shaft[axis=y]
setblock 179 65 57 create:chain_conveyor
setblock 173 64 59 create:package_frogport
setblock 181 64 61 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:chain",count:1},{Slot:1b,id:"create:package_frogport",count:1},{Slot:2b,id:"create:cardboard_block",count:1}]}
