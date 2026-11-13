# 099 botania_runes/gourmaryllis
#area 152 147 171 172
fill 152 64 147 171 91 172 minecraft:air
fill 152 60 147 171 62 172 minecraft:stone
fill 152 63 147 171 63 172 minecraft:light_gray_concrete
fill 156 64 153 171 79 153 minecraft:light_gray_concrete
fill 156 64 153 156 79 166 minecraft:light_gray_concrete
setblock 157 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 158 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": ""}','{"text": ""}']}}
fill 166 64 153 166 79 166 minecraft:light_gray_concrete
fill 159 63 157 163 63 159 minecraft:grass_block[snowy=false]
setblock 161 64 158 botania:gourmaryllis
summon item 160.5 64.2 159.5 {Item:{id:"minecraft:bread",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 159.5 {Item:{id:"minecraft:cooked_beef",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 160.5 64.2 157.5 {Item:{id:"minecraft:apple",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 157.5 {Item:{id:"minecraft:baked_potato",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
