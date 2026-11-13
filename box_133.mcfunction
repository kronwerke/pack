# 133 aether/portal, altar
#area 25 298 53 323
fill 25 64 298 53 91 323 minecraft:air
fill 25 60 298 53 62 323 minecraft:stone
fill 25 63 298 53 63 323 minecraft:light_gray_concrete
fill 29 64 304 53 79 304 minecraft:light_gray_concrete
fill 29 64 304 29 79 317 minecraft:light_gray_concrete
setblock 30 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 304 38 79 317 minecraft:light_gray_concrete
setblock 32 65 309 minecraft:glowstone
setblock 32 66 309 minecraft:glowstone
setblock 32 67 309 minecraft:glowstone
setblock 33 64 309 minecraft:glowstone
setblock 33 68 309 minecraft:glowstone
setblock 34 64 309 minecraft:glowstone
setblock 34 68 309 minecraft:glowstone
setblock 35 65 309 minecraft:glowstone
setblock 35 66 309 minecraft:glowstone
setblock 35 67 309 minecraft:glowstone
fill 33 65 309 34 67 309 aether:aether_portal[axis=x]
execute if block 33 66 309 aether:aether_portal
setblock 39 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "133.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 40 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 304 48 79 317 minecraft:light_gray_concrete
fill 41 63 308 45 63 310 aether:holystone
setblock 41 64 309 aether:altar
setblock 43 64 309 aether:freezer
setblock 45 64 309 aether:incubator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
