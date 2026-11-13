# 015 create_brass/crushing_wheel
#area 151 21 172 46
fill 151 64 21 172 91 46 minecraft:air
fill 151 60 21 172 62 46 minecraft:stone
fill 151 63 21 172 63 46 minecraft:light_gray_concrete
fill 155 64 27 172 79 27 minecraft:light_gray_concrete
fill 155 64 27 155 79 40 minecraft:light_gray_concrete
setblock 156 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "015"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 157 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 158 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 167 64 27 167 79 40 minecraft:light_gray_concrete
setblock 160 65 32 create:crushing_wheel[axis=z]
setblock 162 65 32 create:crushing_wheel[axis=z]
fill 159 64 31 163 66 31 create:andesite_casing
setblock 160 65 31 create:andesite_encased_shaft[axis=z]
setblock 160 65 30 create:creative_motor[facing=south]{ScrollValue:32}
setblock 162 65 31 create:andesite_encased_shaft[axis=z]
setblock 162 65 30 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 161.5 67 32.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
