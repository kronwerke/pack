# 026 create_brass/arm
#area 219 42 238 67
fill 219 64 42 238 91 67 minecraft:air
fill 219 60 42 238 62 67 minecraft:stone
fill 219 63 42 238 63 67 minecraft:light_gray_concrete
fill 223 64 48 238 79 48 minecraft:light_gray_concrete
fill 223 64 48 223 79 61 minecraft:light_gray_concrete
setblock 224 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "create_brass"}','{"text": "arm"}','{"text": ""}']}}
setblock 225 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a mechanical"}','{"text": "arm feeding a"}','{"text": "blaze burner"}','{"text": ""}']}}
fill 233 64 48 233 79 61 minecraft:light_gray_concrete
setblock 226 64 53 create:depot
kw testworld use 226 64 53 up minecraft:coal
setblock 230 64 53 create:blaze_burner[blaze=smouldering]
setblock 228 64 53 create:mechanical_arm[ceiling=false]{InteractionPoints:[{Type:"create:depot",Pos:[I;-2,0,0],Mode:"TAKE"},{Type:"create:blaze_burner",Pos:[I;2,0,0],Mode:"DEPOSIT"}]}
setblock 228 63 53 create:shaft[axis=y]
setblock 228 62 53 create:creative_motor[facing=up]{ScrollValue:32}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
