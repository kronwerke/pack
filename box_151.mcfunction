# 151 aether/portal, altar
#area 25 334 53 359
fill 25 64 334 53 91 359 minecraft:air
fill 25 60 334 53 62 359 minecraft:stone
fill 25 63 334 53 63 359 minecraft:light_gray_concrete
fill 29 64 340 53 79 340 minecraft:light_gray_concrete
fill 29 64 340 29 79 353 minecraft:light_gray_concrete
setblock 30 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 340 38 79 353 minecraft:light_gray_concrete
setblock 32 65 345 minecraft:glowstone
setblock 32 66 345 minecraft:glowstone
setblock 32 67 345 minecraft:glowstone
setblock 33 64 345 minecraft:glowstone
setblock 33 68 345 minecraft:glowstone
setblock 34 64 345 minecraft:glowstone
setblock 34 68 345 minecraft:glowstone
setblock 35 65 345 minecraft:glowstone
setblock 35 66 345 minecraft:glowstone
setblock 35 67 345 minecraft:glowstone
fill 33 65 345 34 67 345 aether:aether_portal[axis=x]
execute if block 33 66 345 aether:aether_portal
setblock 39 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "151.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 40 64 352 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 340 48 79 353 minecraft:light_gray_concrete
fill 41 63 344 45 63 346 aether:holystone
setblock 41 64 345 aether:altar
setblock 43 64 345 aether:freezer
setblock 45 64 345 aether:incubator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
