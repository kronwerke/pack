# 140 occultism/spirit_fire
fill 0 63 242 11 63 255 minecraft:light_gray_concrete
fill 0 64 242 11 71 242 minecraft:light_gray_concrete
fill 0 64 242 0 71 255 minecraft:light_gray_concrete
setblock 1 64 254 minecraft:air
setblock 1 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 254 minecraft:air
setblock 2 64 254 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
summon text_display 5.5 71 247.5 {text:'[{"text": "140  ", "color": "gold"}, {"text": "occultism/spirit_fire", "color": "gray"}, {"text": "\\nZünde Spiritfire", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
setblock 5 63 247 minecraft:netherrack
setblock 5 64 247 occultism:spirit_fire
setblock 9 64 251 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:andesite",count:32}]}
