# 111 immersive/dynamo, watermill
#area 97 181 136 208
fill 97 64 181 126 101 208 minecraft:air
fill 127 64 181 136 101 208 minecraft:air
fill 97 60 181 136 62 208 minecraft:stone
fill 97 63 181 136 63 208 minecraft:light_gray_concrete
fill 101 64 187 136 89 187 minecraft:light_gray_concrete
fill 101 64 187 101 89 202 minecraft:light_gray_concrete
setblock 102 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 103 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 104 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 117 64 187 117 89 202 minecraft:light_gray_concrete
fill 109 64 191 109 70 191 immersiveengineering:treated_wood_horizontal
setblock 109 71 191 immersiveengineering:dynamo[facing=south]
kw testworld use 109 71 191 south immersiveengineering:windmill
execute unless block 109 71 192 minecraft:air
setblock 118 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "111.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 119 64 201 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 131 64 187 131 89 202 minecraft:light_gray_concrete
fill 124 64 190 124 67 190 immersiveengineering:treated_wood_horizontal
setblock 124 68 190 immersiveengineering:dynamo[facing=south]
kw testworld use 124 68 190 south immersiveengineering:watermill
execute unless block 124 68 191 minecraft:air
setblock 119 63 191 minecraft:water
setblock 120 63 191 minecraft:air
setblock 121 63 191 minecraft:air
setblock 122 63 191 minecraft:air
setblock 123 63 191 minecraft:air
setblock 124 63 191 minecraft:air
setblock 125 63 191 minecraft:air
setblock 126 63 191 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
