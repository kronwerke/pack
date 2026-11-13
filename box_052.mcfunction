# 052 deeper_darker/portal
#area 24 198 42 223
fill 24 64 198 42 91 223 minecraft:air
fill 24 60 198 42 62 223 minecraft:stone
fill 24 63 198 42 63 223 minecraft:light_gray_concrete
fill 28 64 204 42 79 204 minecraft:light_gray_concrete
fill 28 64 204 28 79 217 minecraft:light_gray_concrete
setblock 29 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 30 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 37 64 204 37 79 217 minecraft:light_gray_concrete
setblock 31 65 209 minecraft:reinforced_deepslate
setblock 31 66 209 minecraft:reinforced_deepslate
setblock 31 67 209 minecraft:reinforced_deepslate
setblock 32 64 209 minecraft:reinforced_deepslate
setblock 32 68 209 minecraft:reinforced_deepslate
setblock 33 64 209 minecraft:reinforced_deepslate
setblock 33 68 209 minecraft:reinforced_deepslate
setblock 34 65 209 minecraft:reinforced_deepslate
setblock 34 66 209 minecraft:reinforced_deepslate
setblock 34 67 209 minecraft:reinforced_deepslate
fill 32 65 209 33 67 209 deeperdarker:otherside_portal[axis=x]
execute if block 32 66 209 deeperdarker:otherside_portal
