# 020 create/frogport
#area 106 42 127 67
fill 106 64 42 127 91 67 minecraft:air
fill 106 60 42 127 62 67 minecraft:stone
fill 106 63 42 127 63 67 minecraft:light_gray_concrete
fill 110 64 48 127 79 48 minecraft:light_gray_concrete
fill 110 64 48 110 79 61 minecraft:light_gray_concrete
setblock 111 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "020"}','{"text": "create"}','{"text": "frogport"}','{"text": ""}']}}
setblock 112 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain conveyor"}','{"text": "with a frogport"}','{"text": "carrying a"}','{"text": "package"}']}}
fill 122 64 48 122 79 61 minecraft:light_gray_concrete
setblock 113 66 53 create:chain_conveyor{Connections:[[I;6,0,0]]}
setblock 113 63 53 create:shaft[axis=y]
setblock 113 64 53 create:shaft[axis=y]
setblock 113 65 53 create:shaft[axis=y]
setblock 113 62 53 create:creative_motor[facing=up]{ScrollValue:32}
setblock 119 66 53 create:chain_conveyor{Connections:[[I;-6,0,0]]}
setblock 119 63 53 create:shaft[axis=y]
setblock 119 64 53 create:shaft[axis=y]
setblock 119 65 53 create:shaft[axis=y]
setblock 119 62 53 create:creative_motor[facing=up]{ScrollValue:32}
fill 116 64 54 116 65 54 minecraft:stone_bricks
setblock 116 66 54 create:package_frogport
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
