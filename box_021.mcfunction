# 021 create/washing
#area 76 44 95 69
fill 76 64 44 95 91 69 minecraft:air
fill 76 60 44 95 62 69 minecraft:stone
fill 76 63 44 95 63 69 minecraft:light_gray_concrete
fill 80 64 50 95 79 50 minecraft:light_gray_concrete
fill 80 64 50 80 79 63 minecraft:light_gray_concrete
setblock 81 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "021"}','{"text": "create"}','{"text": "washing"}','{"text": ""}']}}
setblock 82 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fan blowing"}','{"text": "through water"}','{"text": "over a belt of"}','{"text": "gravel"}']}}
fill 90 64 50 90 79 63 minecraft:light_gray_concrete
setblock 84 64 53 create:shaft[axis=x]
setblock 84 64 57 create:shaft[axis=x]
kw testworld use 84 64 53 up create:belt_connector
kw testworld use 84 64 57 up create:belt_connector
execute unless block 84 64 55 minecraft:air
setblock 85 64 54 minecraft:glass
setblock 85 64 56 minecraft:glass
setblock 85 64 55 minecraft:water
setblock 86 64 55 create:encased_fan[facing=west]
setblock 87 64 55 create:creative_motor[facing=west]{ScrollValue:64}
setblock 88 64 55 create:andesite_casing
setblock 87 64 56 create:andesite_casing
setblock 87 64 54 create:andesite_casing
setblock 87 65 55 create:andesite_casing
summon item 84.5 65 55.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
