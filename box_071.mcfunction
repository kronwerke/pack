# 071 immersive/dynamo, windmill, watermill
#area 66 158 119 185
fill 66 64 158 95 101 185 minecraft:air
fill 96 64 158 119 101 185 minecraft:air
fill 66 60 158 119 62 185 minecraft:stone
fill 66 63 158 119 63 185 minecraft:light_gray_concrete
fill 70 64 164 119 89 164 minecraft:light_gray_concrete
fill 70 64 164 70 89 179 minecraft:light_gray_concrete
setblock 71 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 72 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 73 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 86 64 164 86 89 179 minecraft:light_gray_concrete
fill 78 64 168 78 70 168 immersiveengineering:treated_wood_horizontal
setblock 78 71 168 immersiveengineering:dynamo[facing=south]
kw testworld use 78 71 168 south immersiveengineering:windmill
execute unless block 78 71 169 minecraft:air
setblock 87 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.2"}','{"text": "immersive"}','{"text": "windmill"}','{"text": ""}']}}
setblock 88 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Setz eine"}','{"text": "Windmühle an"}','{"text": "den Dynamo"}','{"text": ""}']}}
fill 102 64 164 102 89 179 minecraft:light_gray_concrete
fill 94 64 168 94 70 168 immersiveengineering:treated_wood_horizontal
setblock 94 71 168 immersiveengineering:dynamo[facing=south]
kw testworld use 94 71 168 south immersiveengineering:windmill
execute unless block 94 71 169 minecraft:air
setblock 103 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "071.3"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 104 64 178 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 114 64 164 114 89 179 minecraft:light_gray_concrete
fill 108 64 167 108 65 167 immersiveengineering:treated_wood_horizontal
setblock 108 66 167 immersiveengineering:dynamo[facing=south]
kw testworld use 108 66 167 south immersiveengineering:watermill
execute unless block 108 66 168 minecraft:air
setblock 104 63 168 minecraft:water
setblock 105 63 168 minecraft:air
setblock 106 63 168 minecraft:air
setblock 107 63 168 minecraft:air
setblock 108 63 168 minecraft:air
setblock 109 63 168 minecraft:air
setblock 110 63 168 minecraft:air
setblock 111 63 168 minecraft:air
