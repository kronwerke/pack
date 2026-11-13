# 024 create_brass/crushing_wheel
#area 185 42 206 67
fill 185 64 42 206 91 67 minecraft:air
fill 185 60 42 206 62 67 minecraft:stone
fill 185 63 42 206 63 67 minecraft:light_gray_concrete
fill 189 64 48 206 79 48 minecraft:light_gray_concrete
fill 189 64 48 189 79 61 minecraft:light_gray_concrete
setblock 190 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 191 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 192 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 201 64 48 201 79 61 minecraft:light_gray_concrete
setblock 194 65 53 create:crushing_wheel[axis=z]
setblock 196 65 53 create:crushing_wheel[axis=z]
fill 193 64 52 197 66 52 create:andesite_casing
setblock 194 65 52 create:andesite_encased_shaft[axis=z]
setblock 194 65 51 create:creative_motor[facing=south]{ScrollValue:32}
setblock 196 65 52 create:andesite_encased_shaft[axis=z]
setblock 196 65 51 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 195.5 67 53.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
