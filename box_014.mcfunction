# 014 create_brass/crushing_wheel
#area 136 21 157 46
fill 136 64 21 157 91 46 minecraft:air
fill 136 60 21 157 62 46 minecraft:stone
fill 136 63 21 157 63 46 minecraft:light_gray_concrete
fill 140 64 27 157 79 27 minecraft:light_gray_concrete
fill 140 64 27 140 79 40 minecraft:light_gray_concrete
setblock 141 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "create_brass"}','{"text": "crushing_wheel"}','{"text": ""}']}}
setblock 142 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a pair of"}','{"text": "crushing"}','{"text": "wheels, goggles"}','{"text": "showing the"}']}}
setblock 143 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "stress"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 152 64 27 152 79 40 minecraft:light_gray_concrete
setblock 145 65 32 create:crushing_wheel[axis=z]
setblock 147 65 32 create:crushing_wheel[axis=z]
fill 144 64 31 148 66 31 create:andesite_casing
setblock 145 65 31 create:andesite_encased_shaft[axis=z]
setblock 145 65 30 create:creative_motor[facing=south]{ScrollValue:32}
setblock 147 65 31 create:andesite_encased_shaft[axis=z]
setblock 147 65 30 create:creative_motor[facing=south]{ScrollValue:-32}
summon item 146.5 67 32.5 {Item:{id:"minecraft:raw_iron",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
