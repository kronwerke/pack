# 067 aether/portal
#area 10 250 28 275
fill 10 64 250 28 91 275 minecraft:air
fill 10 60 250 28 62 275 minecraft:stone
fill 10 63 250 28 63 275 minecraft:light_gray_concrete
fill 14 64 256 28 79 256 minecraft:light_gray_concrete
fill 14 64 256 14 79 269 minecraft:light_gray_concrete
setblock 15 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 16 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 23 64 256 23 79 269 minecraft:light_gray_concrete
setblock 17 65 261 minecraft:glowstone
setblock 17 66 261 minecraft:glowstone
setblock 17 67 261 minecraft:glowstone
setblock 18 64 261 minecraft:glowstone
setblock 18 68 261 minecraft:glowstone
setblock 19 64 261 minecraft:glowstone
setblock 19 68 261 minecraft:glowstone
setblock 20 65 261 minecraft:glowstone
setblock 20 66 261 minecraft:glowstone
setblock 20 67 261 minecraft:glowstone
fill 18 65 261 19 67 261 aether:aether_portal[axis=x]
execute if block 18 66 261 aether:aether_portal
