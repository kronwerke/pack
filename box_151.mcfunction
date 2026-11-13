# 151 aether/portal, altar
#area 25 336 53 361
fill 25 64 336 53 91 361 minecraft:air
fill 25 60 336 53 62 361 minecraft:stone
fill 25 63 336 53 63 361 minecraft:light_gray_concrete
fill 29 64 342 53 79 342 minecraft:light_gray_concrete
fill 29 64 342 29 79 355 minecraft:light_gray_concrete
setblock 30 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 342 38 79 355 minecraft:light_gray_concrete
setblock 32 65 347 minecraft:glowstone
setblock 32 66 347 minecraft:glowstone
setblock 32 67 347 minecraft:glowstone
setblock 33 64 347 minecraft:glowstone
setblock 33 68 347 minecraft:glowstone
setblock 34 64 347 minecraft:glowstone
setblock 34 68 347 minecraft:glowstone
setblock 35 65 347 minecraft:glowstone
setblock 35 66 347 minecraft:glowstone
setblock 35 67 347 minecraft:glowstone
fill 33 65 347 34 67 347 aether:aether_portal[axis=x]
execute if block 33 66 347 aether:aether_portal
setblock 39 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 40 64 354 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 342 48 79 355 minecraft:light_gray_concrete
fill 41 63 346 45 63 348 aether:holystone
setblock 41 64 347 aether:altar
setblock 43 64 347 aether:freezer
setblock 45 64 347 aether:incubator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
