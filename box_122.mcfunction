# 122 immersive/dynamo, watermill
#area 97 215 136 242
fill 97 64 215 126 101 242 minecraft:air
fill 127 64 215 136 101 242 minecraft:air
fill 97 60 215 136 62 242 minecraft:stone
fill 97 63 215 136 63 242 minecraft:light_gray_concrete
fill 101 64 221 136 89 221 minecraft:light_gray_concrete
fill 101 64 221 101 89 236 minecraft:light_gray_concrete
setblock 102 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 103 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 104 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 117 64 221 117 89 236 minecraft:light_gray_concrete
fill 109 64 225 109 70 225 immersiveengineering:treated_wood_horizontal
setblock 109 71 225 immersiveengineering:dynamo[facing=south]
kw testworld use 109 71 225 south immersiveengineering:windmill
execute unless block 109 71 226 minecraft:air
setblock 118 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 119 64 235 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 131 64 221 131 89 236 minecraft:light_gray_concrete
fill 124 64 224 124 67 224 immersiveengineering:treated_wood_horizontal
setblock 124 68 224 immersiveengineering:dynamo[facing=south]
kw testworld use 124 68 224 south immersiveengineering:watermill
execute unless block 124 68 225 minecraft:air
setblock 119 63 225 minecraft:water
setblock 120 63 225 minecraft:air
setblock 121 63 225 minecraft:air
setblock 122 63 225 minecraft:air
setblock 123 63 225 minecraft:air
setblock 124 63 225 minecraft:air
setblock 125 63 225 minecraft:air
setblock 126 63 225 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
