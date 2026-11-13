# 031 create_brass/arm
#area 280 42 299 67
fill 280 64 42 299 91 67 minecraft:air
fill 280 60 42 299 62 67 minecraft:stone
fill 280 63 42 299 63 67 minecraft:light_gray_concrete
fill 284 64 48 299 79 48 minecraft:light_gray_concrete
fill 284 64 48 284 79 61 minecraft:light_gray_concrete
setblock 285 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "create_brass"}','{"text": "arm"}','{"text": ""}']}}
setblock 286 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mechanical"}','{"text": "arm feeding a"}','{"text": "blaze burner"}','{"text": ""}']}}
fill 294 64 48 294 79 61 minecraft:light_gray_concrete
setblock 287 64 53 create:depot
kw testworld use 287 64 53 up minecraft:coal
setblock 291 64 53 create:blaze_burner[blaze=smouldering]
setblock 289 64 53 create:mechanical_arm[ceiling=false]{InteractionPoints:[{Type:"create:depot",Pos:[I;-2,0,0],Mode:"TAKE"},{Type:"create:blaze_burner",Pos:[I;2,0,0],Mode:"DEPOSIT"}]}
setblock 289 63 53 create:shaft[axis=y]
setblock 289 62 53 create:creative_motor[facing=up]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
