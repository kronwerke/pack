# 074 immersive/dynamo, windmill, watermill
#area 66 177 121 204
fill 66 64 177 95 101 204 minecraft:air
fill 96 64 177 121 101 204 minecraft:air
fill 66 60 177 121 62 204 minecraft:stone
fill 66 63 177 121 63 204 minecraft:light_gray_concrete
fill 70 64 183 121 89 183 minecraft:light_gray_concrete
fill 70 64 183 70 89 198 minecraft:light_gray_concrete
setblock 71 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 72 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 73 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 86 64 183 86 89 198 minecraft:light_gray_concrete
fill 78 64 187 78 70 187 immersiveengineering:treated_wood_horizontal
setblock 78 71 187 immersiveengineering:dynamo[facing=south]
kw testworld use 78 71 187 south immersiveengineering:windmill
execute unless block 78 71 188 minecraft:air
setblock 87 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.2"}','{"text": "immersive"}','{"text": "windmill"}','{"text": ""}']}}
setblock 88 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz eine"}','{"text": "Windmühle an"}','{"text": "den Dynamo"}','{"text": ""}']}}
fill 102 64 183 102 89 198 minecraft:light_gray_concrete
fill 94 64 187 94 70 187 immersiveengineering:treated_wood_horizontal
setblock 94 71 187 immersiveengineering:dynamo[facing=south]
kw testworld use 94 71 187 south immersiveengineering:windmill
execute unless block 94 71 188 minecraft:air
setblock 103 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074.3"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 104 64 197 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 116 64 183 116 89 198 minecraft:light_gray_concrete
fill 109 64 186 109 67 186 immersiveengineering:treated_wood_horizontal
setblock 109 68 186 immersiveengineering:dynamo[facing=south]
kw testworld use 109 68 186 south immersiveengineering:watermill
execute unless block 109 68 187 minecraft:air
setblock 104 63 187 minecraft:water
setblock 105 63 187 minecraft:air
setblock 106 63 187 minecraft:air
setblock 107 63 187 minecraft:air
setblock 108 63 187 minecraft:air
setblock 109 63 187 minecraft:air
setblock 110 63 187 minecraft:air
setblock 111 63 187 minecraft:air
