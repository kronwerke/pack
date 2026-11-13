# 020 create_brass/crushing_wheel
#area 168 40 189 65
fill 168 64 40 189 91 65 minecraft:air
fill 168 60 40 189 62 65 minecraft:stone
fill 168 63 40 189 63 65 minecraft:light_gray_concrete
fill 172 64 46 189 79 46 minecraft:light_gray_concrete
fill 172 64 46 172 79 59 minecraft:light_gray_concrete
setblock 173 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 174 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 175 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 184 64 46 184 79 59 minecraft:light_gray_concrete
setblock 177 65 51 create:crushing_wheel[axis=z]
setblock 179 65 51 create:crushing_wheel[axis=z]
fill 176 64 50 180 66 50 create:andesite_casing
setblock 177 65 50 create:andesite_encased_shaft[axis=z]
setblock 177 65 49 create:creative_motor[facing=south]{ScrollValue:32}
setblock 179 65 50 create:andesite_encased_shaft[axis=z]
setblock 179 65 49 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 178.5 67 51.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
