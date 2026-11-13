# 047 botania_runes/terrasteel
#area 169 86 190 111
fill 169 64 86 190 91 111 minecraft:air
fill 169 60 86 190 62 111 minecraft:stone
fill 169 63 86 190 63 111 minecraft:light_gray_concrete
fill 173 64 92 190 79 92 minecraft:light_gray_concrete
fill 173 64 92 173 79 105 minecraft:light_gray_concrete
setblock 174 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "047"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 175 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 185 64 92 185 79 105 minecraft:light_gray_concrete
setblock 178 64 96 botania:livingrock
setblock 178 64 97 minecraft:lapis_block
setblock 178 64 98 botania:livingrock
setblock 179 64 96 minecraft:lapis_block
setblock 179 64 97 botania:livingrock
setblock 179 64 98 minecraft:lapis_block
setblock 180 64 96 botania:livingrock
setblock 180 64 97 minecraft:lapis_block
setblock 180 64 98 botania:livingrock
setblock 179 65 97 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 179.5 66.25 97.5 {Tags:["kw_shot"]}
setblock 175 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 175.5 65.25 97.5 {Tags:["kw_shot"]}
setblock 183 64 97 botania:mana_pool{mana:1000000}
summon botania:mana_spark 183.5 65.25 97.5 {Tags:["kw_shot"]}
summon item 179.5 65.3 97.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 179.5 65.3 97.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 179.5 65.3 97.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
