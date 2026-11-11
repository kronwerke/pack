# 010 botania_runes/terrasteel
#area 26 51 47 76
fill 26 64 51 47 91 76 minecraft:air
fill 26 60 51 47 62 76 minecraft:stone
fill 26 63 51 47 63 76 minecraft:light_gray_concrete
fill 30 64 57 47 79 57 minecraft:light_gray_concrete
fill 30 64 57 30 79 70 minecraft:light_gray_concrete
setblock 31 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 32 64 69 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
summon text_display 36.5 71 62.5 {text:'[{"text": "010  ", "color": "gold"}, {"text": "botania_runes/terrasteel", "color": "gray"}, {"text": "\\nSchmied Terrastahl", "color": "white"}]',billboard:"center",background:1275068416,Tags:["kw_shot"],alignment:"center",line_width:200,transformation:{scale:[1.6f,1.6f,1.6f],translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]}}
fill 42 64 57 42 79 66 minecraft:light_gray_concrete
setblock 35 64 61 botania:livingrock
setblock 35 64 62 minecraft:lapis_block
setblock 35 64 63 botania:livingrock
setblock 36 64 61 minecraft:lapis_block
setblock 36 64 62 botania:livingrock
setblock 36 64 63 minecraft:lapis_block
setblock 37 64 61 botania:livingrock
setblock 37 64 62 minecraft:lapis_block
setblock 37 64 63 botania:livingrock
setblock 36 65 62 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 36.5 66.25 62.5 {Tags:["kw_shot"]}
setblock 32 64 62 botania:mana_pool{mana:1000000}
summon botania:mana_spark 32.5 65.25 62.5 {Tags:["kw_shot"]}
setblock 40 64 62 botania:mana_pool{mana:1000000}
summon botania:mana_spark 40.5 65.25 62.5 {Tags:["kw_shot"]}
summon item 36.5 65.3 62.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 36.5 65.3 62.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 36.5 65.3 62.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
