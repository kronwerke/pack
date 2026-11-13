# 055 occultism/spirit_fire
#area -4 123 15 148
fill -4 64 123 15 91 148 minecraft:air
fill -4 60 123 15 62 148 minecraft:stone
fill -4 63 123 15 63 148 minecraft:light_gray_concrete
fill 0 64 129 15 79 129 minecraft:light_gray_concrete
fill 0 64 129 0 79 142 minecraft:light_gray_concrete
setblock 1 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 141 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 129 10 79 142 minecraft:light_gray_concrete
setblock 5 64 134 occultism:spirit_fire[color=white]
summon item 5.5 65.5 134.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 135.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
