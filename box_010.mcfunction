# 010 create/washing
#area 76 21 95 46
fill 76 64 21 95 91 46 minecraft:air
fill 76 60 21 95 62 46 minecraft:stone
fill 76 63 21 95 63 46 minecraft:light_gray_concrete
fill 80 64 27 95 79 27 minecraft:light_gray_concrete
fill 80 64 27 80 79 40 minecraft:light_gray_concrete
setblock 81 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "010"}','{"text": "create"}','{"text": "washing"}','{"text": ""}']}}
setblock 82 64 39 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "fan blowing"}','{"text": "through water"}','{"text": "over a belt of"}','{"text": "gravel"}']}}
fill 90 64 27 90 79 40 minecraft:light_gray_concrete
setblock 84 64 30 create:shaft[axis=x]
setblock 84 64 34 create:shaft[axis=x]
kw testworld use 84 64 30 up create:belt_connector
kw testworld use 84 64 34 up create:belt_connector
execute unless block 84 64 32 minecraft:air
setblock 85 64 31 minecraft:glass
setblock 85 64 33 minecraft:glass
setblock 85 64 32 minecraft:water
setblock 86 64 32 create:encased_fan[facing=west]
setblock 87 64 32 create:creative_motor[facing=west]{ScrollValue:64}
setblock 88 64 32 create:andesite_casing
setblock 87 64 33 create:andesite_casing
setblock 87 64 31 create:andesite_casing
setblock 87 65 32 create:andesite_casing
summon item 84.5 65 32.5 {Item:{id:"minecraft:gravel",count:8},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
