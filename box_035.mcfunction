# 035 botania_runes/terrasteel
#area 101 86 122 111
fill 101 64 86 122 91 111 minecraft:air
fill 101 60 86 122 62 111 minecraft:stone
fill 101 63 86 122 63 111 minecraft:light_gray_concrete
fill 105 64 92 122 79 92 minecraft:light_gray_concrete
fill 105 64 92 105 79 105 minecraft:light_gray_concrete
setblock 106 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 107 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 117 64 92 117 79 105 minecraft:light_gray_concrete
setblock 110 64 96 botania:livingrock
setblock 110 64 97 minecraft:lapis_block
setblock 110 64 98 botania:livingrock
setblock 111 64 96 minecraft:lapis_block
setblock 111 64 97 botania:livingrock
setblock 111 64 98 minecraft:lapis_block
setblock 112 64 96 botania:livingrock
setblock 112 64 97 minecraft:lapis_block
setblock 112 64 98 botania:livingrock
setblock 111 65 97 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 111.5 66.25 97.5 {Tags:["kw_shot"]}
setblock 107 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 107.5 65.25 97.5 {Tags:["kw_shot"]}
setblock 115 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 115.5 65.25 97.5 {Tags:["kw_shot"]}
summon item 111.5 65.3 97.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 111.5 65.3 97.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 111.5 65.3 97.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
