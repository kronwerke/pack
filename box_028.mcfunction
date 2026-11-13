# 028 create_brass/crushing_wheel
#area 231 42 252 67
fill 231 64 42 252 91 67 minecraft:air
fill 231 60 42 252 62 67 minecraft:stone
fill 231 63 42 252 63 67 minecraft:light_gray_concrete
fill 235 64 48 252 79 48 minecraft:light_gray_concrete
fill 235 64 48 235 79 61 minecraft:light_gray_concrete
setblock 236 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 237 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 238 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 247 64 48 247 79 61 minecraft:light_gray_concrete
setblock 240 65 53 create:crushing_wheel[axis=z]
setblock 242 65 53 create:crushing_wheel[axis=z]
fill 239 64 52 243 66 52 create:andesite_casing
setblock 240 65 52 create:andesite_encased_shaft[axis=z]
setblock 240 65 51 create:creative_motor[facing=south]{ScrollValue:32}
setblock 242 65 52 create:andesite_encased_shaft[axis=z]
setblock 242 65 51 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 241.5 67 53.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
