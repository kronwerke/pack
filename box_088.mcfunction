# 088 occultism/spirit_fire
#area -4 146 15 171
fill -4 64 146 15 91 171 minecraft:air
fill -4 60 146 15 62 171 minecraft:stone
fill -4 63 146 15 63 171 minecraft:light_gray_concrete
fill 0 64 152 15 79 152 minecraft:light_gray_concrete
fill 0 64 152 0 79 165 minecraft:light_gray_concrete
setblock 1 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 152 10 79 165 minecraft:light_gray_concrete
setblock 5 64 157 occultism:spirit_fire[color=white]
summon item 5.5 65.5 157.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 158.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
