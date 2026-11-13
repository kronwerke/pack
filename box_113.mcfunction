# 113 occultism/spirit_fire
#area -4 184 15 209
fill -4 64 184 15 91 209 minecraft:air
fill -4 60 184 15 62 209 minecraft:stone
fill -4 63 184 15 63 209 minecraft:light_gray_concrete
fill 0 64 190 15 79 190 minecraft:light_gray_concrete
fill 0 64 190 0 79 203 minecraft:light_gray_concrete
setblock 1 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "113"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 202 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 190 10 79 203 minecraft:light_gray_concrete
setblock 5 64 195 occultism:spirit_fire[color=white]
summon item 5.5 65.5 195.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 196.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
