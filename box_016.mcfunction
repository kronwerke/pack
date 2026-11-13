# 016 create/washing
#area 76 42 95 67
fill 76 64 42 95 91 67 minecraft:air
fill 76 60 42 95 62 67 minecraft:stone
fill 76 63 42 95 63 67 minecraft:light_gray_concrete
fill 80 64 48 95 79 48 minecraft:light_gray_concrete
fill 80 64 48 80 79 61 minecraft:light_gray_concrete
setblock 81 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "016"}','{"text": "create"}','{"text": "washing"}','{"text": ""}']}}
setblock 82 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fan blowing"}','{"text": "through water"}','{"text": "over a belt of"}','{"text": "gravel"}']}}
fill 90 64 48 90 79 61 minecraft:light_gray_concrete
setblock 84 64 51 create:shaft[axis=x]
setblock 84 64 55 create:shaft[axis=x]
kw testworld use 84 64 51 up create:belt_connector
kw testworld use 84 64 55 up create:belt_connector
execute unless block 84 64 53 minecraft:air
setblock 85 64 52 minecraft:glass
setblock 85 64 54 minecraft:glass
setblock 85 64 53 minecraft:water
setblock 86 64 53 create:encased_fan[facing=west]
setblock 87 64 53 create:creative_motor[facing=west]{ScrollValue:64}
setblock 88 64 53 create:andesite_casing
setblock 87 64 54 create:andesite_casing
setblock 87 64 52 create:andesite_casing
setblock 87 65 53 create:andesite_casing
summon item 84.5 65 53.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
