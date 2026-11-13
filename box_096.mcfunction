# 096 gaia/fight
#area 235 145 256 172
fill 235 64 145 256 91 172 minecraft:air
fill 235 60 145 256 62 172 minecraft:stone
fill 235 63 145 256 63 172 minecraft:light_gray_concrete
fill 239 64 151 256 79 151 minecraft:light_gray_concrete
fill 239 64 151 239 79 166 minecraft:light_gray_concrete
setblock 240 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "gaia"}','{"text": "fight"}','{"text": ""}']}}
setblock 241 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the guardian"}','{"text": "with the purple"}','{"text": "traps"}','{"text": ""}']}}
fill 251 64 151 251 79 166 minecraft:light_gray_concrete
summon botania:gaia_guardian 245.5 64 157.5 {NoAI:1b,PersistenceRequired:1b,Silent:1b,Tags:["kw_shot"],Rotation:[0f,0f]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
