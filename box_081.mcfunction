# 081 aether/portal
#area 25 250 43 275
fill 25 64 250 43 91 275 minecraft:air
fill 25 60 250 43 62 275 minecraft:stone
fill 25 63 250 43 63 275 minecraft:light_gray_concrete
fill 29 64 256 43 79 256 minecraft:light_gray_concrete
fill 29 64 256 29 79 269 minecraft:light_gray_concrete
setblock 30 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "081"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 256 38 79 269 minecraft:light_gray_concrete
setblock 32 65 261 minecraft:glowstone
setblock 32 66 261 minecraft:glowstone
setblock 32 67 261 minecraft:glowstone
setblock 33 64 261 minecraft:glowstone
setblock 33 68 261 minecraft:glowstone
setblock 34 64 261 minecraft:glowstone
setblock 34 68 261 minecraft:glowstone
setblock 35 65 261 minecraft:glowstone
setblock 35 66 261 minecraft:glowstone
setblock 35 67 261 minecraft:glowstone
fill 33 65 261 34 67 261 aether:aether_portal[axis=x]
execute if block 33 66 261 aether:aether_portal
