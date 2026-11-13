# 098 occultism/spirit_fire
#area -4 176 15 201
fill -4 64 176 15 91 201 minecraft:air
fill -4 60 176 15 62 201 minecraft:stone
fill -4 63 176 15 63 201 minecraft:light_gray_concrete
fill 0 64 182 15 79 182 minecraft:light_gray_concrete
fill 0 64 182 0 79 195 minecraft:light_gray_concrete
setblock 1 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "098"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 194 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 182 10 79 195 minecraft:light_gray_concrete
setblock 5 64 187 occultism:spirit_fire[color=white]
summon item 5.5 65.5 187.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 188.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
