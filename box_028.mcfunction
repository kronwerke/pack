# 028 create_brass/crushing_wheel
#area 216 42 237 67
fill 216 64 42 237 91 67 minecraft:air
fill 216 60 42 237 62 67 minecraft:stone
fill 216 63 42 237 63 67 minecraft:light_gray_concrete
fill 220 64 48 237 79 48 minecraft:light_gray_concrete
fill 220 64 48 220 79 61 minecraft:light_gray_concrete
setblock 221 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 222 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 223 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 232 64 48 232 79 61 minecraft:light_gray_concrete
setblock 225 65 53 create:crushing_wheel[axis=z]
setblock 227 65 53 create:crushing_wheel[axis=z]
fill 224 64 52 228 66 52 create:andesite_casing
setblock 225 65 52 create:andesite_encased_shaft[axis=z]
setblock 225 65 51 create:creative_motor[facing=south]{ScrollValue:32}
setblock 227 65 52 create:andesite_encased_shaft[axis=z]
setblock 227 65 51 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 226.5 67 53.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
