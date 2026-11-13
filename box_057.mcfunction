# 057 botania_runes/gourmaryllis
#area 152 105 171 130
fill 152 64 105 171 91 130 minecraft:air
fill 152 60 105 171 62 130 minecraft:stone
fill 152 63 105 171 63 130 minecraft:light_gray_concrete
fill 156 64 111 171 79 111 minecraft:light_gray_concrete
fill 156 64 111 156 79 124 minecraft:light_gray_concrete
setblock 157 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 158 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": ""}','{"text": ""}']}}
fill 166 64 111 166 79 124 minecraft:light_gray_concrete
fill 159 63 115 163 63 117 minecraft:grass_block[snowy=false]
setblock 161 64 116 botania:gourmaryllis
summon item 160.5 64.2 117.5 {Item:{id:"minecraft:bread",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 117.5 {Item:{id:"minecraft:cooked_beef",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 160.5 64.2 115.5 {Item:{id:"minecraft:apple",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 115.5 {Item:{id:"minecraft:baked_potato",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
