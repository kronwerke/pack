# 083 botania_runes/mana_pearl
#area 107 139 126 164
fill 107 64 139 126 91 164 minecraft:air
fill 107 60 139 126 62 164 minecraft:stone
fill 107 63 139 126 63 164 minecraft:light_gray_concrete
fill 111 64 145 126 79 145 minecraft:light_gray_concrete
fill 111 64 145 111 79 158 minecraft:light_gray_concrete
setblock 112 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083"}','{"text": "botania_runes"}','{"text": "mana_pearl"}','{"text": ""}']}}
setblock 113 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pool on a"}','{"text": "brass casing"}','{"text": "with a pearl in"}','{"text": "it"}']}}
fill 121 64 145 121 79 158 minecraft:light_gray_concrete
setblock 116 64 150 create:brass_casing
setblock 116 65 150 botania:mana_pool{mana:1000000}
summon item 116.5 66 150.5 {Item:{id:"minecraft:ender_pearl",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
