# 089 botania_runes/gourmaryllis
#area 152 143 171 168
fill 152 64 143 171 91 168 minecraft:air
fill 152 60 143 171 62 168 minecraft:stone
fill 152 63 143 171 63 168 minecraft:light_gray_concrete
fill 156 64 149 171 79 149 minecraft:light_gray_concrete
fill 156 64 149 156 79 162 minecraft:light_gray_concrete
setblock 157 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "botania_runes"}','{"text": "gourmaryllis"}','{"text": ""}']}}
setblock 158 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a belt dropping"}','{"text": "varied food"}','{"text": ""}','{"text": ""}']}}
fill 166 64 149 166 79 162 minecraft:light_gray_concrete
fill 159 63 153 163 63 155 minecraft:grass_block[snowy=false]
setblock 161 64 154 botania:gourmaryllis
summon item 160.5 64.2 155.5 {Item:{id:"minecraft:bread",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 155.5 {Item:{id:"minecraft:cooked_beef",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 160.5 64.2 153.5 {Item:{id:"minecraft:apple",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 162.5 64.2 153.5 {Item:{id:"minecraft:baked_potato",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
