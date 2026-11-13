# 073 immersive/dynamo, watermill
#area 66 177 105 204
fill 66 64 177 95 101 204 minecraft:air
fill 96 64 177 105 101 204 minecraft:air
fill 66 60 177 105 62 204 minecraft:stone
fill 66 63 177 105 63 204 minecraft:light_gray_concrete
fill 70 64 183 105 89 183 minecraft:light_gray_concrete
fill 70 64 183 70 89 198 minecraft:light_gray_concrete
setblock 71 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 72 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 73 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 86 64 183 86 89 198 minecraft:light_gray_concrete
fill 78 64 187 78 70 187 immersiveengineering:treated_wood_horizontal
setblock 78 71 187 immersiveengineering:dynamo[facing=south]
kw testworld use 78 71 187 south immersiveengineering:windmill
execute unless block 78 71 188 minecraft:air
setblock 87 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "073.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 88 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 100 64 183 100 89 198 minecraft:light_gray_concrete
fill 93 64 186 93 67 186 immersiveengineering:treated_wood_horizontal
setblock 93 68 186 immersiveengineering:dynamo[facing=south]
kw testworld use 93 68 186 south immersiveengineering:watermill
execute unless block 93 68 187 minecraft:air
setblock 88 63 187 minecraft:water
setblock 89 63 187 minecraft:air
setblock 90 63 187 minecraft:air
setblock 91 63 187 minecraft:air
setblock 92 63 187 minecraft:air
setblock 93 63 187 minecraft:air
setblock 94 63 187 minecraft:air
setblock 95 63 187 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
