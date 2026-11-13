# 039 botania_runes/terrasteel
#area 120 86 141 111
fill 120 64 86 141 91 111 minecraft:air
fill 120 60 86 141 62 111 minecraft:stone
fill 120 63 86 141 63 111 minecraft:light_gray_concrete
fill 124 64 92 141 79 92 minecraft:light_gray_concrete
fill 124 64 92 124 79 105 minecraft:light_gray_concrete
setblock 125 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 126 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 136 64 92 136 79 105 minecraft:light_gray_concrete
setblock 129 64 96 botania:livingrock
setblock 129 64 97 minecraft:lapis_block
setblock 129 64 98 botania:livingrock
setblock 130 64 96 minecraft:lapis_block
setblock 130 64 97 botania:livingrock
setblock 130 64 98 minecraft:lapis_block
setblock 131 64 96 botania:livingrock
setblock 131 64 97 minecraft:lapis_block
setblock 131 64 98 botania:livingrock
setblock 130 65 97 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 130.5 66.25 97.5 {Tags:["kw_shot"]}
setblock 126 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 126.5 65.25 97.5 {Tags:["kw_shot"]}
setblock 134 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 134.5 65.25 97.5 {Tags:["kw_shot"]}
summon item 130.5 65.3 97.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 65.3 97.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 130.5 65.3 97.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
