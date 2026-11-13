# 050 botania_runes/mana_pearl
#area 107 105 126 130
fill 107 64 105 126 91 130 minecraft:air
fill 107 60 105 126 62 130 minecraft:stone
fill 107 63 105 126 63 130 minecraft:light_gray_concrete
fill 111 64 111 126 79 111 minecraft:light_gray_concrete
fill 111 64 111 111 79 124 minecraft:light_gray_concrete
setblock 112 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 111 121 79 124 minecraft:light_gray_concrete
setblock 116 64 116 create:brass_casing
setblock 116 65 116 botania:mana_pool{mana:1000000}
summon item 116.5 66 116.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
