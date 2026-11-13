# 030 create_brass/crushing_wheel
#area 216 44 237 69
fill 216 64 44 237 91 69 minecraft:air
fill 216 60 44 237 62 69 minecraft:stone
fill 216 63 44 237 63 69 minecraft:light_gray_concrete
fill 220 64 50 237 79 50 minecraft:light_gray_concrete
fill 220 64 50 220 79 63 minecraft:light_gray_concrete
setblock 221 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "030"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 222 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 223 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 232 64 50 232 79 63 minecraft:light_gray_concrete
setblock 225 65 55 create:crushing_wheel[axis=z]
setblock 227 65 55 create:crushing_wheel[axis=z]
fill 224 64 54 228 66 54 create:andesite_casing
setblock 225 65 54 create:andesite_encased_shaft[axis=z]
setblock 225 65 53 create:creative_motor[facing=south]{ScrollValue:32}
setblock 227 65 54 create:andesite_encased_shaft[axis=z]
setblock 227 65 53 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 226.5 67 55.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
