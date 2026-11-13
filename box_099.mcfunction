# 099 occultism/spirit_fire
#area -4 182 15 207
fill -4 64 182 15 91 207 minecraft:air
fill -4 60 182 15 62 207 minecraft:stone
fill -4 63 182 15 63 207 minecraft:light_gray_concrete
fill 0 64 188 15 79 188 minecraft:light_gray_concrete
fill 0 64 188 0 79 201 minecraft:light_gray_concrete
setblock 1 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 200 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 188 10 79 201 minecraft:light_gray_concrete
setblock 5 64 193 occultism:spirit_fire[color=white]
summon item 5.5 65.5 193.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 194.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
