# 058 occultism/spirit_fire
#area -4 142 15 167
fill -4 64 142 15 91 167 minecraft:air
fill -4 60 142 15 62 167 minecraft:stone
fill -4 63 142 15 63 167 minecraft:light_gray_concrete
fill 0 64 148 15 79 148 minecraft:light_gray_concrete
fill 0 64 148 0 79 161 minecraft:light_gray_concrete
setblock 1 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 160 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 148 10 79 161 minecraft:light_gray_concrete
setblock 5 64 153 occultism:spirit_fire[color=white]
summon item 5.5 65.5 153.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 154.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
