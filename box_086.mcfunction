# 086 botania_runes/mana_pearl
#area 107 143 126 168
fill 107 64 143 126 91 168 minecraft:air
fill 107 60 143 126 62 168 minecraft:stone
fill 107 63 143 126 63 168 minecraft:light_gray_concrete
fill 111 64 149 126 79 149 minecraft:light_gray_concrete
fill 111 64 149 111 79 162 minecraft:light_gray_concrete
setblock 112 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 149 121 79 162 minecraft:light_gray_concrete
setblock 116 64 154 create:brass_casing
setblock 116 65 154 botania:mana_pool{mana:1000000}
summon item 116.5 66 154.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
