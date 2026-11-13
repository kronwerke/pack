# 032 botania_runes/mana_pearl
#area 56 86 75 111
fill 56 64 86 75 91 111 minecraft:air
fill 56 60 86 75 62 111 minecraft:stone
fill 56 63 86 75 63 111 minecraft:light_gray_concrete
fill 60 64 92 75 79 92 minecraft:light_gray_concrete
fill 60 64 92 60 79 105 minecraft:light_gray_concrete
setblock 61 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "032"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 62 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 70 64 92 70 79 105 minecraft:light_gray_concrete
setblock 65 64 97 create:brass_casing
setblock 65 65 97 botania:mana_pool{mana:1000000}
summon item 65.5 66 97.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
