# 041 botania_runes/mana_pearl
#area 92 86 111 111
fill 92 64 86 111 91 111 minecraft:air
fill 92 60 86 111 62 111 minecraft:stone
fill 92 63 86 111 63 111 minecraft:light_gray_concrete
fill 96 64 92 111 79 92 minecraft:light_gray_concrete
fill 96 64 92 96 79 105 minecraft:light_gray_concrete
setblock 97 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "041"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 98 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 106 64 92 106 79 105 minecraft:light_gray_concrete
setblock 101 64 97 create:brass_casing
setblock 101 65 97 botania:mana_pool{mana:1000000}
summon item 101.5 66 97.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
