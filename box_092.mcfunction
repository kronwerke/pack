# 092 aether/portal
#area 25 271 43 296
fill 25 64 271 43 91 296 minecraft:air
fill 25 60 271 43 62 296 minecraft:stone
fill 25 63 271 43 63 296 minecraft:light_gray_concrete
fill 29 64 277 43 79 277 minecraft:light_gray_concrete
fill 29 64 277 29 79 290 minecraft:light_gray_concrete
setblock 30 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "092"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 289 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 277 38 79 290 minecraft:light_gray_concrete
setblock 32 65 282 minecraft:glowstone
setblock 32 66 282 minecraft:glowstone
setblock 32 67 282 minecraft:glowstone
setblock 33 64 282 minecraft:glowstone
setblock 33 68 282 minecraft:glowstone
setblock 34 64 282 minecraft:glowstone
setblock 34 68 282 minecraft:glowstone
setblock 35 65 282 minecraft:glowstone
setblock 35 66 282 minecraft:glowstone
setblock 35 67 282 minecraft:glowstone
fill 33 65 282 34 67 282 aether:aether_portal[axis=x]
execute if block 33 66 282 aether:aether_portal
