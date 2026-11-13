# 019 create_brass/crushing_wheel
#area 151 40 172 65
fill 151 64 40 172 91 65 minecraft:air
fill 151 60 40 172 62 65 minecraft:stone
fill 151 63 40 172 63 65 minecraft:light_gray_concrete
fill 155 64 46 172 79 46 minecraft:light_gray_concrete
fill 155 64 46 155 79 59 minecraft:light_gray_concrete
setblock 156 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 157 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 158 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 167 64 46 167 79 59 minecraft:light_gray_concrete
setblock 160 65 51 create:crushing_wheel[axis=z]
setblock 162 65 51 create:crushing_wheel[axis=z]
fill 159 64 50 163 66 50 create:andesite_casing
setblock 160 65 50 create:andesite_encased_shaft[axis=z]
setblock 160 65 49 create:creative_motor[facing=south]{ScrollValue:32}
setblock 162 65 50 create:andesite_encased_shaft[axis=z]
setblock 162 65 49 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 161.5 67 51.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
