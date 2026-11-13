# 058 immersive/dynamo, windmill
#area 66 158 107 185
fill 66 64 158 95 101 185 minecraft:air
fill 96 64 158 107 101 185 minecraft:air
fill 66 60 158 107 62 185 minecraft:stone
fill 66 63 158 107 63 185 minecraft:light_gray_concrete
fill 70 64 164 107 89 164 minecraft:light_gray_concrete
fill 70 64 164 70 89 179 minecraft:light_gray_concrete
setblock 71 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 72 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 73 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 86 64 164 86 89 179 minecraft:light_gray_concrete
fill 78 64 168 78 70 168 immersiveengineering:treated_wood_horizontal
setblock 78 71 168 immersiveengineering:dynamo[facing=south]
kw testworld use 78 71 168 south immersiveengineering:windmill
execute unless block 78 71 169 minecraft:air
setblock 87 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "058.2"}','{"text": "immersive"}','{"text": "windmill"}','{"text": ""}']}}
setblock 88 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz eine"}','{"text": "Windmühle an"}','{"text": "den Dynamo"}','{"text": ""}']}}
fill 102 64 164 102 89 179 minecraft:light_gray_concrete
fill 94 64 168 94 70 168 immersiveengineering:treated_wood_horizontal
setblock 94 71 168 immersiveengineering:dynamo[facing=south]
kw testworld use 94 71 168 south immersiveengineering:windmill
execute unless block 94 71 169 minecraft:air
