# 104 immersive/dynamo, watermill
#area 97 179 136 206
fill 97 64 179 126 101 206 minecraft:air
fill 127 64 179 136 101 206 minecraft:air
fill 97 60 179 136 62 206 minecraft:stone
fill 97 63 179 136 63 206 minecraft:light_gray_concrete
fill 101 64 185 136 89 185 minecraft:light_gray_concrete
fill 101 64 185 101 89 200 minecraft:light_gray_concrete
setblock 102 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 103 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 104 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 117 64 185 117 89 200 minecraft:light_gray_concrete
fill 109 64 189 109 70 189 immersiveengineering:treated_wood_horizontal
setblock 109 71 189 immersiveengineering:dynamo[facing=south]
kw testworld use 109 71 189 south immersiveengineering:windmill
execute unless block 109 71 190 minecraft:air
setblock 118 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "104.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 119 64 199 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 131 64 185 131 89 200 minecraft:light_gray_concrete
fill 124 64 188 124 67 188 immersiveengineering:treated_wood_horizontal
setblock 124 68 188 immersiveengineering:dynamo[facing=south]
kw testworld use 124 68 188 south immersiveengineering:watermill
execute unless block 124 68 189 minecraft:air
setblock 119 63 189 minecraft:water
setblock 120 63 189 minecraft:air
setblock 121 63 189 minecraft:air
setblock 122 63 189 minecraft:air
setblock 123 63 189 minecraft:air
setblock 124 63 189 minecraft:air
setblock 125 63 189 minecraft:air
setblock 126 63 189 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
