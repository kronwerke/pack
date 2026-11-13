# 019 create/washing
#area 91 42 110 67
fill 91 64 42 110 91 67 minecraft:air
fill 91 60 42 110 62 67 minecraft:stone
fill 91 63 42 110 63 67 minecraft:light_gray_concrete
fill 95 64 48 110 79 48 minecraft:light_gray_concrete
fill 95 64 48 95 79 61 minecraft:light_gray_concrete
setblock 96 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "019"}','{"text": "create"}','{"text": "washing"}','{"text": ""}']}}
setblock 97 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fan blowing"}','{"text": "through water"}','{"text": "over a belt of"}','{"text": "gravel"}']}}
fill 105 64 48 105 79 61 minecraft:light_gray_concrete
setblock 99 64 51 create:shaft[axis=x]
setblock 99 64 55 create:shaft[axis=x]
kw testworld use 99 64 51 up create:belt_connector
kw testworld use 99 64 55 up create:belt_connector
execute unless block 99 64 53 minecraft:air
setblock 100 64 52 minecraft:glass
setblock 100 64 54 minecraft:glass
setblock 100 64 53 minecraft:water
setblock 101 64 53 create:encased_fan[facing=west]
setblock 102 64 53 create:creative_motor[facing=west]{ScrollValue:64}
setblock 103 64 53 create:andesite_casing
setblock 102 64 54 create:andesite_casing
setblock 102 64 52 create:andesite_casing
setblock 102 65 53 create:andesite_casing
summon item 99.5 65 53.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
