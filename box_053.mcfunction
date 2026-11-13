# 053 botania_runes/terrasteel
#area 169 105 190 130
fill 169 64 105 190 91 130 minecraft:air
fill 169 60 105 190 62 130 minecraft:stone
fill 169 63 105 190 63 130 minecraft:light_gray_concrete
fill 173 64 111 190 79 111 minecraft:light_gray_concrete
fill 173 64 111 173 79 124 minecraft:light_gray_concrete
setblock 174 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "053"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 175 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 185 64 111 185 79 124 minecraft:light_gray_concrete
setblock 178 64 115 botania:livingrock
setblock 178 64 116 minecraft:lapis_block
setblock 178 64 117 botania:livingrock
setblock 179 64 115 minecraft:lapis_block
setblock 179 64 116 botania:livingrock
setblock 179 64 117 minecraft:lapis_block
setblock 180 64 115 botania:livingrock
setblock 180 64 116 minecraft:lapis_block
setblock 180 64 117 botania:livingrock
setblock 179 65 116 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 179.5 66.25 116.5 {Tags:["kw_shot"]}
setblock 175 64 116 botania:mana_pool{mana:1000000}
summon botania:mana_spark 175.5 65.25 116.5 {Tags:["kw_shot"]}
setblock 183 64 116 botania:mana_pool{mana:1000000}
summon botania:mana_spark 183.5 65.25 116.5 {Tags:["kw_shot"]}
summon item 179.5 65.3 116.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 179.5 65.3 116.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 179.5 65.3 116.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
