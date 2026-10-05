# 142 occultism/foliot_crusher
fill 30 63 224 41 63 237 minecraft:light_gray_concrete
fill 30 64 224 41 71 224 minecraft:light_gray_concrete
fill 30 64 224 30 71 237 minecraft:light_gray_concrete
setblock 31 64 236 minecraft:air
setblock 31 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "142"}','{"text": "occultism"}','{"text": "foliot_crusher"}','{"text": ""}']}}
setblock 32 64 236 minecraft:air
setblock 32 64 236 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Foliot crusher"}','{"text": "next to a pile"}','{"text": "of dust"}','{"text": ""}']}}
setblock 39 64 233 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"occultism:iron_dust",count:32}]}
summon occultism:foliot 33.5 64 231.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[180f,0f]}
