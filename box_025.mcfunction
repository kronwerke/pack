# 025 create_brass/crushing_wheel
#area 200 42 221 67
fill 200 64 42 221 91 67 minecraft:air
fill 200 60 42 221 62 67 minecraft:stone
fill 200 63 42 221 63 67 minecraft:light_gray_concrete
fill 204 64 48 221 79 48 minecraft:light_gray_concrete
fill 204 64 48 204 79 61 minecraft:light_gray_concrete
setblock 205 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 206 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 207 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 216 64 48 216 79 61 minecraft:light_gray_concrete
setblock 209 65 53 create:crushing_wheel[axis=z]
setblock 211 65 53 create:crushing_wheel[axis=z]
fill 208 64 52 212 66 52 create:andesite_casing
setblock 209 65 52 create:andesite_encased_shaft[axis=z]
setblock 209 65 51 create:creative_motor[facing=south]{ScrollValue:32}
setblock 211 65 52 create:andesite_encased_shaft[axis=z]
setblock 211 65 51 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 210.5 67 53.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
