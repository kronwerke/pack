# 095 aether/portal, altar
#area 25 277 53 302
fill 25 64 277 53 91 302 minecraft:air
fill 25 60 277 53 62 302 minecraft:stone
fill 25 63 277 53 63 302 minecraft:light_gray_concrete
fill 29 64 283 53 79 283 minecraft:light_gray_concrete
fill 29 64 283 29 79 296 minecraft:light_gray_concrete
setblock 30 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 283 38 79 296 minecraft:light_gray_concrete
setblock 32 65 288 minecraft:glowstone
setblock 32 66 288 minecraft:glowstone
setblock 32 67 288 minecraft:glowstone
setblock 33 64 288 minecraft:glowstone
setblock 33 68 288 minecraft:glowstone
setblock 34 64 288 minecraft:glowstone
setblock 34 68 288 minecraft:glowstone
setblock 35 65 288 minecraft:glowstone
setblock 35 66 288 minecraft:glowstone
setblock 35 67 288 minecraft:glowstone
fill 33 65 288 34 67 288 aether:aether_portal[axis=x]
execute if block 33 66 288 aether:aether_portal
setblock 39 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 40 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 283 48 79 296 minecraft:light_gray_concrete
fill 41 63 287 45 63 289 aether:holystone
setblock 41 64 288 aether:altar
setblock 43 64 288 aether:freezer
setblock 45 64 288 aether:incubator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
