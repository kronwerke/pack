# 024 create_brass/arm
#area 202 42 221 67
fill 202 64 42 221 91 67 minecraft:air
fill 202 60 42 221 62 67 minecraft:stone
fill 202 63 42 221 63 67 minecraft:light_gray_concrete
fill 206 64 48 221 79 48 minecraft:light_gray_concrete
fill 206 64 48 206 79 61 minecraft:light_gray_concrete
setblock 207 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "024"}','{"text": "create_brass"}','{"text": "arm"}','{"text": ""}']}}
setblock 208 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mechanical"}','{"text": "arm feeding a"}','{"text": "blaze burner"}','{"text": ""}']}}
fill 216 64 48 216 79 61 minecraft:light_gray_concrete
setblock 209 64 53 create:depot
kw testworld use 209 64 53 up minecraft:coal
setblock 213 64 53 create:blaze_burner[blaze=smouldering]
setblock 211 64 53 create:mechanical_arm[ceiling=false]{InteractionPoints:[{Type:"create:depot",Pos:[I;-2,0,0],Mode:"TAKE"},{Type:"create:blaze_burner",Pos:[I;2,0,0],Mode:"DEPOSIT"}]}
setblock 211 63 53 create:shaft[axis=y]
setblock 211 62 53 create:creative_motor[facing=up]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
