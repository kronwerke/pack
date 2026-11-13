# 101 occultism/foliot_crusher
#area 30 180 49 205
fill 30 64 180 49 91 205 minecraft:air
fill 30 60 180 49 62 205 minecraft:stone
fill 30 63 180 49 63 205 minecraft:light_gray_concrete
fill 34 64 186 49 79 186 minecraft:light_gray_concrete
fill 34 64 186 34 79 199 minecraft:light_gray_concrete
setblock 35 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101"}','{"text": "occultism"}','{"text": "foliot_crusher"}','{"text": ""}']}}
setblock 36 64 198 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Foliot crusher"}','{"text": "next to a pile"}','{"text": "of dust"}','{"text": ""}']}}
fill 44 64 186 44 79 199 minecraft:light_gray_concrete
summon occultism:foliot 38.5 64 191.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
summon item 40.5 64.2 191.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 41.5 64.2 192.5 {Item:{id:"occultism:iron_dust",count:16},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
