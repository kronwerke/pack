# 045 botania_runes/terrasteel
#area 154 86 175 111
fill 154 64 86 175 91 111 minecraft:air
fill 154 60 86 175 62 111 minecraft:stone
fill 154 63 86 175 63 111 minecraft:light_gray_concrete
fill 158 64 92 175 79 92 minecraft:light_gray_concrete
fill 158 64 92 158 79 105 minecraft:light_gray_concrete
setblock 159 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "045"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 160 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 170 64 92 170 79 105 minecraft:light_gray_concrete
setblock 163 64 96 botania:livingrock
setblock 163 64 97 minecraft:lapis_block
setblock 163 64 98 botania:livingrock
setblock 164 64 96 minecraft:lapis_block
setblock 164 64 97 botania:livingrock
setblock 164 64 98 minecraft:lapis_block
setblock 165 64 96 botania:livingrock
setblock 165 64 97 minecraft:lapis_block
setblock 165 64 98 botania:livingrock
setblock 164 65 97 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 164.5 66.25 97.5 {Tags:["kw_shot"]}
setblock 160 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 160.5 65.25 97.5 {Tags:["kw_shot"]}
setblock 168 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 168.5 65.25 97.5 {Tags:["kw_shot"]}
summon item 164.5 65.3 97.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 164.5 65.3 97.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 164.5 65.3 97.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
