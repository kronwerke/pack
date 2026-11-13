# 141 immersive/dynamo, watermill
#area 122 219 161 246
fill 122 64 219 151 101 246 minecraft:air
fill 152 64 219 161 101 246 minecraft:air
fill 122 60 219 161 62 246 minecraft:stone
fill 122 63 219 161 63 246 minecraft:light_gray_concrete
fill 126 64 225 161 89 225 minecraft:light_gray_concrete
fill 126 64 225 126 89 240 minecraft:light_gray_concrete
setblock 127 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.1"}','{"text": "immersive"}','{"text": "dynamo"}','{"text": ""}']}}
setblock 128 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "dynamo with"}','{"text": "windmill, a"}','{"text": "windmill on a"}','{"text": "tower, three"}']}}
setblock 129 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "water wheels on"}','{"text": "one shaft"}','{"text": ""}','{"text": ""}']}}
fill 142 64 225 142 89 240 minecraft:light_gray_concrete
fill 134 64 229 134 70 229 immersiveengineering:treated_wood_horizontal
setblock 134 71 229 immersiveengineering:dynamo[facing=south]
kw testworld use 134 71 229 south immersiveengineering:windmill
execute unless block 134 71 230 minecraft:air
setblock 143 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.2"}','{"text": "immersive"}','{"text": "watermill"}','{"text": ""}']}}
setblock 144 64 239 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Wasserrad"}','{"text": ""}','{"text": ""}']}}
fill 156 64 225 156 89 240 minecraft:light_gray_concrete
fill 149 64 228 149 67 228 immersiveengineering:treated_wood_horizontal
setblock 149 68 228 immersiveengineering:dynamo[facing=south]
kw testworld use 149 68 228 south immersiveengineering:watermill
execute unless block 149 68 229 minecraft:air
setblock 144 63 229 minecraft:water
setblock 145 63 229 minecraft:air
setblock 146 63 229 minecraft:air
setblock 147 63 229 minecraft:air
setblock 148 63 229 minecraft:air
setblock 149 63 229 minecraft:air
setblock 150 63 229 minecraft:air
setblock 151 63 229 minecraft:air
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
