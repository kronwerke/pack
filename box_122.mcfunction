# 122 immersive/dynamo, watermill
#area 97 217 136 244
fill 97 64 217 126 101 244 minecraft:air
fill 127 64 217 136 101 244 minecraft:air
fill 97 60 217 136 62 244 minecraft:stone
fill 97 63 217 136 63 244 minecraft:light_gray_concrete
fill 101 64 223 136 89 223 minecraft:light_gray_concrete
fill 101 64 223 101 89 238 minecraft:light_gray_concrete
setblock 102 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 103 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 104 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 117 64 223 117 89 238 minecraft:light_gray_concrete
fill 109 64 227 109 70 227 immersiveengineering:treated_wood_horizontal
setblock 109 71 227 immersiveengineering:dynamo[facing=south]
kw testworld use 109 71 227 south immersiveengineering:windmill
execute unless block 109 71 228 minecraft:air
setblock 118 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "122.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 119 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 131 64 223 131 89 238 minecraft:light_gray_concrete
fill 124 64 226 124 67 226 immersiveengineering:treated_wood_horizontal
setblock 124 68 226 immersiveengineering:dynamo[facing=south]
kw testworld use 124 68 226 south immersiveengineering:watermill
execute unless block 124 68 227 minecraft:air
setblock 119 63 227 minecraft:water
setblock 120 63 227 minecraft:air
setblock 121 63 227 minecraft:air
setblock 122 63 227 minecraft:air
setblock 123 63 227 minecraft:air
setblock 124 63 227 minecraft:air
setblock 125 63 227 minecraft:air
setblock 126 63 227 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
