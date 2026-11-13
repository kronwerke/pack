# 118 immersive/dynamo, watermill
#area 97 211 136 238
fill 97 64 211 126 101 238 minecraft:air
fill 127 64 211 136 101 238 minecraft:air
fill 97 60 211 136 62 238 minecraft:stone
fill 97 63 211 136 63 238 minecraft:light_gray_concrete
fill 101 64 217 136 89 217 minecraft:light_gray_concrete
fill 101 64 217 101 89 232 minecraft:light_gray_concrete
setblock 102 64 231 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 103 64 231 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 104 64 231 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 117 64 217 117 89 232 minecraft:light_gray_concrete
fill 109 64 221 109 70 221 immersiveengineering:treated_wood_horizontal
setblock 109 71 221 immersiveengineering:dynamo[facing=south]
kw testworld use 109 71 221 south immersiveengineering:windmill
execute unless block 109 71 222 minecraft:air
setblock 118 64 231 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 119 64 231 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 131 64 217 131 89 232 minecraft:light_gray_concrete
fill 124 64 220 124 67 220 immersiveengineering:treated_wood_horizontal
setblock 124 68 220 immersiveengineering:dynamo[facing=south]
kw testworld use 124 68 220 south immersiveengineering:watermill
execute unless block 124 68 221 minecraft:air
setblock 119 63 221 minecraft:water
setblock 120 63 221 minecraft:air
setblock 121 63 221 minecraft:air
setblock 122 63 221 minecraft:air
setblock 123 63 221 minecraft:air
setblock 124 63 221 minecraft:air
setblock 125 63 221 minecraft:air
setblock 126 63 221 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
