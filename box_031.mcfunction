# 031 botania_runes/terrasteel
#area 101 84 122 109
fill 101 64 84 122 91 109 minecraft:air
fill 101 60 84 122 62 109 minecraft:stone
fill 101 63 84 122 63 109 minecraft:light_gray_concrete
fill 105 64 90 122 79 90 minecraft:light_gray_concrete
fill 105 64 90 105 79 103 minecraft:light_gray_concrete
setblock 106 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "botania_runes"}','{"text": "terrasteel"}','{"text": ""}']}}
setblock 107 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the plate mid"}','{"text": "craft"}','{"text": ""}','{"text": ""}']}}
fill 117 64 90 117 79 103 minecraft:light_gray_concrete
setblock 110 64 94 botania:livingrock
setblock 110 64 95 minecraft:lapis_block
setblock 110 64 96 botania:livingrock
setblock 111 64 94 minecraft:lapis_block
setblock 111 64 95 botania:livingrock
setblock 111 64 96 minecraft:lapis_block
setblock 112 64 94 botania:livingrock
setblock 112 64 95 minecraft:lapis_block
setblock 112 64 96 botania:livingrock
setblock 111 65 95 botania:terrestrial_agglomeration_plate
summon botania:mana_spark 111.5 66.25 95.5 {Tags:["kw_shot"]}
setblock 107 64 95 botania:mana_pool{mana:1000000}
summon botania:mana_spark 107.5 65.25 95.5 {Tags:["kw_shot"]}
setblock 115 64 95 botania:mana_pool{mana:1000000}
summon botania:mana_spark 115.5 65.25 95.5 {Tags:["kw_shot"]}
summon item 111.5 65.3 95.5 {Item:{id:"botania:manasteel_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 111.5 65.3 95.5 {Item:{id:"botania:mana_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 111.5 65.3 95.5 {Item:{id:"botania:mana_diamond",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
