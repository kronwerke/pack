# 091 deeper_darker/portal
#area 39 269 57 294
fill 39 64 269 57 91 294 minecraft:air
fill 39 60 269 57 62 294 minecraft:stone
fill 39 63 269 57 63 294 minecraft:light_gray_concrete
fill 43 64 275 57 79 275 minecraft:light_gray_concrete
fill 43 64 275 43 79 288 minecraft:light_gray_concrete
setblock 44 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "091"}','{"text": "deeper_darker"}','{"text": "portal"}','{"text": ""}']}}
setblock 45 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das Portal"}','{"text": "zur Anderwelt"}','{"text": ""}','{"text": ""}']}}
fill 52 64 275 52 79 288 minecraft:light_gray_concrete
setblock 46 65 280 minecraft:reinforced_deepslate
setblock 46 66 280 minecraft:reinforced_deepslate
setblock 46 67 280 minecraft:reinforced_deepslate
setblock 47 64 280 minecraft:reinforced_deepslate
setblock 47 68 280 minecraft:reinforced_deepslate
setblock 48 64 280 minecraft:reinforced_deepslate
setblock 48 68 280 minecraft:reinforced_deepslate
setblock 49 65 280 minecraft:reinforced_deepslate
setblock 49 66 280 minecraft:reinforced_deepslate
setblock 49 67 280 minecraft:reinforced_deepslate
fill 47 65 280 48 67 280 deeperdarker:otherside_portal[axis=x]
execute if block 47 66 280 deeperdarker:otherside_portal
