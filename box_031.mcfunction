# 031 create_brass/arm
#area 265 42 284 67
fill 265 64 42 284 91 67 minecraft:air
fill 265 60 42 284 62 67 minecraft:stone
fill 265 63 42 284 63 67 minecraft:light_gray_concrete
fill 269 64 48 284 79 48 minecraft:light_gray_concrete
fill 269 64 48 269 79 61 minecraft:light_gray_concrete
setblock 270 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "create_brass"}','{"text": "arm"}','{"text": ""}']}}
setblock 271 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mechanical"}','{"text": "arm feeding a"}','{"text": "blaze burner"}','{"text": ""}']}}
fill 279 64 48 279 79 61 minecraft:light_gray_concrete
setblock 272 64 53 create:depot
kw testworld use 272 64 53 up minecraft:coal
setblock 276 64 53 create:blaze_burner[blaze=smouldering]
setblock 274 64 53 create:mechanical_arm[ceiling=false]{InteractionPoints:[{Type:"create:depot",Pos:[I;-2,0,0],Mode:"TAKE"},{Type:"create:blaze_burner",Pos:[I;2,0,0],Mode:"DEPOSIT"}]}
setblock 274 63 53 create:shaft[axis=y]
setblock 274 62 53 create:creative_motor[facing=up]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
