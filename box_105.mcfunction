# 105 aether/portal, altar
#area 25 296 53 321
fill 25 64 296 53 91 321 minecraft:air
fill 25 60 296 53 62 321 minecraft:stone
fill 25 63 296 53 63 321 minecraft:light_gray_concrete
fill 29 64 302 53 79 302 minecraft:light_gray_concrete
fill 29 64 302 29 79 315 minecraft:light_gray_concrete
setblock 30 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 302 38 79 315 minecraft:light_gray_concrete
setblock 32 65 307 minecraft:glowstone
setblock 32 66 307 minecraft:glowstone
setblock 32 67 307 minecraft:glowstone
setblock 33 64 307 minecraft:glowstone
setblock 33 68 307 minecraft:glowstone
setblock 34 64 307 minecraft:glowstone
setblock 34 68 307 minecraft:glowstone
setblock 35 65 307 minecraft:glowstone
setblock 35 66 307 minecraft:glowstone
setblock 35 67 307 minecraft:glowstone
fill 33 65 307 34 67 307 aether:aether_portal[axis=x]
execute if block 33 66 307 aether:aether_portal
setblock 39 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "105.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 40 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 302 48 79 315 minecraft:light_gray_concrete
fill 41 63 306 45 63 308 aether:holystone
setblock 41 64 307 aether:altar
setblock 43 64 307 aether:freezer
setblock 45 64 307 aether:incubator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
