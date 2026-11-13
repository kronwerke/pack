# 063 deeper_darker/portal
#area 24 250 42 275
fill 24 64 250 42 91 275 minecraft:air
fill 24 60 250 42 62 275 minecraft:stone
fill 24 63 250 42 63 275 minecraft:light_gray_concrete
fill 28 64 256 42 79 256 minecraft:light_gray_concrete
fill 28 64 256 28 79 269 minecraft:light_gray_concrete
setblock 29 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 30 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 37 64 256 37 79 269 minecraft:light_gray_concrete
setblock 31 65 261 minecraft:reinforced_deepslate
setblock 31 66 261 minecraft:reinforced_deepslate
setblock 31 67 261 minecraft:reinforced_deepslate
setblock 32 64 261 minecraft:reinforced_deepslate
setblock 32 68 261 minecraft:reinforced_deepslate
setblock 33 64 261 minecraft:reinforced_deepslate
setblock 33 68 261 minecraft:reinforced_deepslate
setblock 34 65 261 minecraft:reinforced_deepslate
setblock 34 66 261 minecraft:reinforced_deepslate
setblock 34 67 261 minecraft:reinforced_deepslate
fill 32 65 261 33 67 261 deeperdarker:otherside_portal[axis=x]
execute if block 32 66 261 deeperdarker:otherside_portal
