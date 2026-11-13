# 027 create_brass/arm
#area 234 42 253 67
fill 234 64 42 253 91 67 minecraft:air
fill 234 60 42 253 62 67 minecraft:stone
fill 234 63 42 253 63 67 minecraft:light_gray_concrete
fill 238 64 48 253 79 48 minecraft:light_gray_concrete
fill 238 64 48 238 79 61 minecraft:light_gray_concrete
setblock 239 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "create_brass"}','{"text": "arm"}','{"text": ""}']}}
setblock 240 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mechanical"}','{"text": "arm feeding a"}','{"text": "blaze burner"}','{"text": ""}']}}
fill 248 64 48 248 79 61 minecraft:light_gray_concrete
setblock 241 64 53 create:depot
kw testworld use 241 64 53 up minecraft:coal
setblock 245 64 53 create:blaze_burner[blaze=smouldering]
setblock 243 64 53 create:mechanical_arm[ceiling=false]{InteractionPoints:[{Type:"create:depot",Pos:[I;-2,0,0],Mode:"TAKE"},{Type:"create:blaze_burner",Pos:[I;2,0,0],Mode:"DEPOSIT"}]}
setblock 243 63 53 create:shaft[axis=y]
setblock 243 62 53 create:creative_motor[facing=up]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
