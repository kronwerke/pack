# 089 occultism/foliot_crusher
#area 30 146 49 171
fill 30 64 146 49 91 171 minecraft:air
fill 30 60 146 49 62 171 minecraft:stone
fill 30 63 146 49 63 171 minecraft:light_gray_concrete
fill 34 64 152 49 79 152 minecraft:light_gray_concrete
fill 34 64 152 34 79 165 minecraft:light_gray_concrete
setblock 35 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "occultism"}','{"text": "foliot_crusher"}','{"text": ""}']}}
setblock 36 64 164 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Foliot crusher"}','{"text": "next to a pile"}','{"text": "of dust"}','{"text": ""}']}}
fill 44 64 152 44 79 165 minecraft:light_gray_concrete
summon occultism:foliot 38.5 64 157.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon item 40.5 64.2 157.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 41.5 64.2 158.5 {Item:{id:"occultism:iron_dust",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
