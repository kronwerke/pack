# 033 create_brass/arm
#area 265 44 284 69
fill 265 64 44 284 91 69 minecraft:air
fill 265 60 44 284 62 69 minecraft:stone
fill 265 63 44 284 63 69 minecraft:light_gray_concrete
fill 269 64 50 284 79 50 minecraft:light_gray_concrete
fill 269 64 50 269 79 63 minecraft:light_gray_concrete
setblock 270 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "create_brass"}','{"text": "arm"}','{"text": ""}']}}
setblock 271 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mechanical"}','{"text": "arm feeding a"}','{"text": "blaze burner"}','{"text": ""}']}}
fill 279 64 50 279 79 63 minecraft:light_gray_concrete
setblock 272 64 55 create:depot
kw testworld use 272 64 55 up minecraft:coal
setblock 276 64 55 create:blaze_burner[blaze=smouldering]
setblock 274 64 55 create:mechanical_arm[ceiling=false]{InteractionPoints:[{Type:"create:depot",Pos:[I;-2,0,0],Mode:"TAKE"},{Type:"create:blaze_burner",Pos:[I;2,0,0],Mode:"DEPOSIT"}]}
setblock 274 63 55 create:shaft[axis=y]
setblock 274 62 55 create:creative_motor[facing=up]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
