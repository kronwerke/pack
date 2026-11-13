# 023 create/frogport
#area 106 44 127 69
fill 106 64 44 127 91 69 minecraft:air
fill 106 60 44 127 62 69 minecraft:stone
fill 106 63 44 127 63 69 minecraft:light_gray_concrete
fill 110 64 50 127 79 50 minecraft:light_gray_concrete
fill 110 64 50 110 79 63 minecraft:light_gray_concrete
setblock 111 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "023"}','{"text": "create"}','{"text": "frogport"}','{"text": ""}']}}
setblock 112 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain conveyor"}','{"text": "with a frogport"}','{"text": "carrying a"}','{"text": "package"}']}}
fill 122 64 50 122 79 63 minecraft:light_gray_concrete
setblock 113 66 55 create:chain_conveyor{Connections:[[I;6,0,0]]}
setblock 113 63 55 create:shaft[axis=y]
setblock 113 64 55 create:shaft[axis=y]
setblock 113 65 55 create:shaft[axis=y]
setblock 113 62 55 create:creative_motor[facing=up]{ScrollValue:32}
setblock 119 66 55 create:chain_conveyor{Connections:[[I;-6,0,0]]}
setblock 119 63 55 create:shaft[axis=y]
setblock 119 64 55 create:shaft[axis=y]
setblock 119 65 55 create:shaft[axis=y]
setblock 119 62 55 create:creative_motor[facing=up]{ScrollValue:32}
fill 116 64 56 116 65 56 minecraft:stone_bricks
setblock 116 66 56 create:package_frogport
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
