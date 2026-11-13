# 089 aether/portal
#area 25 269 43 294
fill 25 64 269 43 91 294 minecraft:air
fill 25 60 269 43 62 294 minecraft:stone
fill 25 63 269 43 63 294 minecraft:light_gray_concrete
fill 29 64 275 43 79 275 minecraft:light_gray_concrete
fill 29 64 275 29 79 288 minecraft:light_gray_concrete
setblock 30 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 287 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 275 38 79 288 minecraft:light_gray_concrete
setblock 32 65 280 minecraft:glowstone
setblock 32 66 280 minecraft:glowstone
setblock 32 67 280 minecraft:glowstone
setblock 33 64 280 minecraft:glowstone
setblock 33 68 280 minecraft:glowstone
setblock 34 64 280 minecraft:glowstone
setblock 34 68 280 minecraft:glowstone
setblock 35 65 280 minecraft:glowstone
setblock 35 66 280 minecraft:glowstone
setblock 35 67 280 minecraft:glowstone
fill 33 65 280 34 67 280 aether:aether_portal[axis=x]
execute if block 33 66 280 aether:aether_portal
