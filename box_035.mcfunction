# 035 occultism/spirit_fire
#area -4 109 15 134
fill -4 64 109 15 91 134 minecraft:air
fill -4 60 109 15 62 134 minecraft:stone
fill -4 63 109 15 63 134 minecraft:light_gray_concrete
fill 0 64 115 15 79 115 minecraft:light_gray_concrete
fill 0 64 115 0 79 128 minecraft:light_gray_concrete
setblock 1 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "035"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 115 10 79 128 minecraft:light_gray_concrete
setblock 5 64 120 occultism:spirit_fire[color=white]
summon item 5.5 65.5 120.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 121.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
