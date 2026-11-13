# 099 occultism/spirit_fire
#area -4 180 15 205
fill -4 64 180 15 91 205 minecraft:air
fill -4 60 180 15 62 205 minecraft:stone
fill -4 63 180 15 63 205 minecraft:light_gray_concrete
fill 0 64 186 15 79 186 minecraft:light_gray_concrete
fill 0 64 186 0 79 199 minecraft:light_gray_concrete
setblock 1 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 186 10 79 199 minecraft:light_gray_concrete
setblock 5 64 191 occultism:spirit_fire[color=white]
summon item 5.5 65.5 191.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 192.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
