# 073 occultism/spirit_fire
#area -4 144 15 169
fill -4 64 144 15 91 169 minecraft:air
fill -4 60 144 15 62 169 minecraft:stone
fill -4 63 144 15 63 169 minecraft:light_gray_concrete
fill 0 64 150 15 79 150 minecraft:light_gray_concrete
fill 0 64 150 0 79 163 minecraft:light_gray_concrete
setblock 1 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073"}','{"text": "occultism"}','{"text": "spirit_fire"}','{"text": ""}']}}
setblock 2 64 162 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "spirit fire"}','{"text": "turning"}','{"text": "andesite into"}','{"text": "otherstone"}']}}
fill 10 64 150 10 79 163 minecraft:light_gray_concrete
setblock 5 64 155 occultism:spirit_fire[color=white]
summon item 5.5 65.5 155.5 {Item:{id:"minecraft:andesite",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 6.5 64.2 156.5 {Item:{id:"occultism:otherstone",count:4},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
