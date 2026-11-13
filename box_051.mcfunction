# 051 aether/portal
#area 10 198 28 223
fill 10 64 198 28 91 223 minecraft:air
fill 10 60 198 28 62 223 minecraft:stone
fill 10 63 198 28 63 223 minecraft:light_gray_concrete
fill 14 64 204 28 79 204 minecraft:light_gray_concrete
fill 14 64 204 14 79 217 minecraft:light_gray_concrete
setblock 15 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "051"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 16 64 216 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 23 64 204 23 79 217 minecraft:light_gray_concrete
setblock 17 65 209 minecraft:glowstone
setblock 17 66 209 minecraft:glowstone
setblock 17 67 209 minecraft:glowstone
setblock 18 64 209 minecraft:glowstone
setblock 18 68 209 minecraft:glowstone
setblock 19 64 209 minecraft:glowstone
setblock 19 68 209 minecraft:glowstone
setblock 20 65 209 minecraft:glowstone
setblock 20 66 209 minecraft:glowstone
setblock 20 67 209 minecraft:glowstone
fill 18 65 209 19 67 209 aether:aether_portal[axis=x]
execute if block 18 66 209 aether:aether_portal
