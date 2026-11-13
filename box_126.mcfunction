# 126 immersive/dynamo, watermill
#area 122 217 161 244
fill 122 64 217 151 101 244 minecraft:air
fill 152 64 217 161 101 244 minecraft:air
fill 122 60 217 161 62 244 minecraft:stone
fill 122 63 217 161 63 244 minecraft:light_gray_concrete
fill 126 64 223 161 89 223 minecraft:light_gray_concrete
fill 126 64 223 126 89 238 minecraft:light_gray_concrete
setblock 127 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 128 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 129 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 142 64 223 142 89 238 minecraft:light_gray_concrete
fill 134 64 227 134 70 227 immersiveengineering:treated_wood_horizontal
setblock 134 71 227 immersiveengineering:dynamo[facing=south]
kw testworld use 134 71 227 south immersiveengineering:windmill
execute unless block 134 71 228 minecraft:air
setblock 143 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 144 64 237 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 156 64 223 156 89 238 minecraft:light_gray_concrete
fill 149 64 226 149 67 226 immersiveengineering:treated_wood_horizontal
setblock 149 68 226 immersiveengineering:dynamo[facing=south]
kw testworld use 149 68 226 south immersiveengineering:watermill
execute unless block 149 68 227 minecraft:air
setblock 144 63 227 minecraft:water
setblock 145 63 227 minecraft:air
setblock 146 63 227 minecraft:air
setblock 147 63 227 minecraft:air
setblock 148 63 227 minecraft:air
setblock 149 63 227 minecraft:air
setblock 150 63 227 minecraft:air
setblock 151 63 227 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
