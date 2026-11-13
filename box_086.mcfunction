# 086 botania_runes/mana_pearl
#area 107 145 126 170
fill 107 64 145 126 91 170 minecraft:air
fill 107 60 145 126 62 170 minecraft:stone
fill 107 63 145 126 63 170 minecraft:light_gray_concrete
fill 111 64 151 126 79 151 minecraft:light_gray_concrete
fill 111 64 151 111 79 164 minecraft:light_gray_concrete
setblock 112 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 151 121 79 164 minecraft:light_gray_concrete
setblock 116 64 156 create:brass_casing
setblock 116 65 156 botania:mana_pool{mana:1000000}
summon item 116.5 66 156.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
