# 147 aether/portal, altar
#area 25 330 53 355
fill 25 64 330 53 91 355 minecraft:air
fill 25 60 330 53 62 355 minecraft:stone
fill 25 63 330 53 63 355 minecraft:light_gray_concrete
fill 29 64 336 53 79 336 minecraft:light_gray_concrete
fill 29 64 336 29 79 349 minecraft:light_gray_concrete
setblock 30 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 336 38 79 349 minecraft:light_gray_concrete
setblock 32 65 341 minecraft:glowstone
setblock 32 66 341 minecraft:glowstone
setblock 32 67 341 minecraft:glowstone
setblock 33 64 341 minecraft:glowstone
setblock 33 68 341 minecraft:glowstone
setblock 34 64 341 minecraft:glowstone
setblock 34 68 341 minecraft:glowstone
setblock 35 65 341 minecraft:glowstone
setblock 35 66 341 minecraft:glowstone
setblock 35 67 341 minecraft:glowstone
fill 33 65 341 34 67 341 aether:aether_portal[axis=x]
execute if block 33 66 341 aether:aether_portal
setblock 39 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "147.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 40 64 348 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 336 48 79 349 minecraft:light_gray_concrete
fill 41 63 340 45 63 342 aether:holystone
setblock 41 64 341 aether:altar
setblock 43 64 341 aether:freezer
setblock 45 64 341 aether:incubator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
