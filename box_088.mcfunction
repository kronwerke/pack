# 088 deeper_darker/portal
#area 39 250 57 275
fill 39 64 250 57 91 275 minecraft:air
fill 39 60 250 57 62 275 minecraft:stone
fill 39 63 250 57 63 275 minecraft:light_gray_concrete
fill 43 64 256 57 79 256 minecraft:light_gray_concrete
fill 43 64 256 43 79 269 minecraft:light_gray_concrete
setblock 44 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "088"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 45 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 52 64 256 52 79 269 minecraft:light_gray_concrete
setblock 46 65 261 minecraft:reinforced_deepslate
setblock 46 66 261 minecraft:reinforced_deepslate
setblock 46 67 261 minecraft:reinforced_deepslate
setblock 47 64 261 minecraft:reinforced_deepslate
setblock 47 68 261 minecraft:reinforced_deepslate
setblock 48 64 261 minecraft:reinforced_deepslate
setblock 48 68 261 minecraft:reinforced_deepslate
setblock 49 65 261 minecraft:reinforced_deepslate
setblock 49 66 261 minecraft:reinforced_deepslate
setblock 49 67 261 minecraft:reinforced_deepslate
fill 47 65 261 48 67 261 deeperdarker:otherside_portal[axis=x]
execute if block 47 66 261 deeperdarker:otherside_portal
