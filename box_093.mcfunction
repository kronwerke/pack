# 093 deeper_darker/portal
#area 39 271 57 296
fill 39 64 271 57 91 296 minecraft:air
fill 39 60 271 57 62 296 minecraft:stone
fill 39 63 271 57 63 296 minecraft:light_gray_concrete
fill 43 64 277 57 79 277 minecraft:light_gray_concrete
fill 43 64 277 43 79 290 minecraft:light_gray_concrete
setblock 44 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "093"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 45 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 52 64 277 52 79 290 minecraft:light_gray_concrete
setblock 46 65 282 minecraft:reinforced_deepslate
setblock 46 66 282 minecraft:reinforced_deepslate
setblock 46 67 282 minecraft:reinforced_deepslate
setblock 47 64 282 minecraft:reinforced_deepslate
setblock 47 68 282 minecraft:reinforced_deepslate
setblock 48 64 282 minecraft:reinforced_deepslate
setblock 48 68 282 minecraft:reinforced_deepslate
setblock 49 65 282 minecraft:reinforced_deepslate
setblock 49 66 282 minecraft:reinforced_deepslate
setblock 49 67 282 minecraft:reinforced_deepslate
fill 47 65 282 48 67 282 deeperdarker:otherside_portal[axis=x]
execute if block 47 66 282 deeperdarker:otherside_portal
