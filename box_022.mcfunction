# 022 create_brass/crushing_wheel
#area 168 42 189 67
fill 168 64 42 189 91 67 minecraft:air
fill 168 60 42 189 62 67 minecraft:stone
fill 168 63 42 189 63 67 minecraft:light_gray_concrete
fill 172 64 48 189 79 48 minecraft:light_gray_concrete
fill 172 64 48 172 79 61 minecraft:light_gray_concrete
setblock 173 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 174 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 175 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 184 64 48 184 79 61 minecraft:light_gray_concrete
setblock 177 65 53 create:crushing_wheel[axis=z]
setblock 179 65 53 create:crushing_wheel[axis=z]
fill 176 64 52 180 66 52 create:andesite_casing
setblock 177 65 52 create:andesite_encased_shaft[axis=z]
setblock 177 65 51 create:creative_motor[facing=south]{ScrollValue:32}
setblock 179 65 52 create:andesite_encased_shaft[axis=z]
setblock 179 65 51 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 178.5 67 53.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
