# 018 occultism/spirit_fire
#area -4 78 15 103
fill -4 64 78 15 91 103 minecraft:air
fill -4 60 78 15 62 103 minecraft:stone
fill -4 63 78 15 63 103 minecraft:light_gray_concrete
fill 0 64 84 15 79 84 minecraft:light_gray_concrete
fill 0 64 84 0 79 97 minecraft:light_gray_concrete
setblock 1 64 96 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 96 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
summon text_display 5.5 71 89.5 {text:'[{"text": "018  ", "color": "gold"}, {"text": "occultism/spirit_fire", "color": "gray"}, {"text": "\\nZünde Spiritfire", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 10 64 84 10 79 97 minecraft:light_gray_concrete
setblock 5 64 89 occultism:spirit_fire[color=white]
summon item 5.5 65.5 89.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 90.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
