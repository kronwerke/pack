# 014 create/washing
#area 76 40 95 65
fill 76 64 40 95 91 65 minecraft:air
fill 76 60 40 95 62 65 minecraft:stone
fill 76 63 40 95 63 65 minecraft:light_gray_concrete
fill 80 64 46 95 79 46 minecraft:light_gray_concrete
fill 80 64 46 80 79 59 minecraft:light_gray_concrete
setblock 81 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "014"}','{"text": "create"}','{"text": "washing"}','{"text": ""}']}}
setblock 82 64 58 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fan blowing"}','{"text": "through water"}','{"text": "over a belt of"}','{"text": "gravel"}']}}
fill 90 64 46 90 79 59 minecraft:light_gray_concrete
setblock 84 64 49 create:shaft[axis=x]
setblock 84 64 53 create:shaft[axis=x]
kw testworld use 84 64 49 up create:belt_connector
kw testworld use 84 64 53 up create:belt_connector
execute unless block 84 64 51 minecraft:air
setblock 85 64 50 minecraft:glass
setblock 85 64 52 minecraft:glass
setblock 85 64 51 minecraft:water
setblock 86 64 51 create:encased_fan[facing=west]
setblock 87 64 51 create:creative_motor[facing=west]{ScrollValue:64}
setblock 88 64 51 create:andesite_casing
setblock 87 64 52 create:andesite_casing
setblock 87 64 50 create:andesite_casing
setblock 87 65 51 create:andesite_casing
summon item 84.5 65 51.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
