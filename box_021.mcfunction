# 021 create/frogport
#area 121 42 142 67
fill 121 64 42 142 91 67 minecraft:air
fill 121 60 42 142 62 67 minecraft:stone
fill 121 63 42 142 63 67 minecraft:light_gray_concrete
fill 125 64 48 142 79 48 minecraft:light_gray_concrete
fill 125 64 48 125 79 61 minecraft:light_gray_concrete
setblock 126 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "021"}','{"text": "create"}','{"text": "frogport"}','{"text": ""}']}}
setblock 127 64 60 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chain conveyor"}','{"text": "with a frogport"}','{"text": "carrying a"}','{"text": "package"}']}}
fill 137 64 48 137 79 61 minecraft:light_gray_concrete
setblock 128 66 53 create:chain_conveyor{Connections:[[I;6,0,0]]}
setblock 128 63 53 create:shaft[axis=y]
setblock 128 64 53 create:shaft[axis=y]
setblock 128 65 53 create:shaft[axis=y]
setblock 128 62 53 create:creative_motor[facing=up]{ScrollValue:32}
setblock 134 66 53 create:chain_conveyor{Connections:[[I;-6,0,0]]}
setblock 134 63 53 create:shaft[axis=y]
setblock 134 64 53 create:shaft[axis=y]
setblock 134 65 53 create:shaft[axis=y]
setblock 134 62 53 create:creative_motor[facing=up]{ScrollValue:32}
fill 131 64 54 131 65 54 minecraft:stone_bricks
setblock 131 66 54 create:package_frogport
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
