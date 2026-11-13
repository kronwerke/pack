# 138 aether/portal, altar
#area 25 300 53 325
fill 25 64 300 53 91 325 minecraft:air
fill 25 60 300 53 62 325 minecraft:stone
fill 25 63 300 53 63 325 minecraft:light_gray_concrete
fill 29 64 306 53 79 306 minecraft:light_gray_concrete
fill 29 64 306 29 79 319 minecraft:light_gray_concrete
setblock 30 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.1"}','{"text": "aether"}','{"text": "portal"}','{"text": ""}']}}
setblock 31 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau das"}','{"text": "Glowstone-Portal"}','{"text": ""}','{"text": ""}']}}
fill 38 64 306 38 79 319 minecraft:light_gray_concrete
setblock 32 65 311 minecraft:glowstone
setblock 32 66 311 minecraft:glowstone
setblock 32 67 311 minecraft:glowstone
setblock 33 64 311 minecraft:glowstone
setblock 33 68 311 minecraft:glowstone
setblock 34 64 311 minecraft:glowstone
setblock 34 68 311 minecraft:glowstone
setblock 35 65 311 minecraft:glowstone
setblock 35 66 311 minecraft:glowstone
setblock 35 67 311 minecraft:glowstone
fill 33 65 311 34 67 311 aether:aether_portal[axis=x]
execute if block 33 66 311 aether:aether_portal
setblock 39 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "138.2"}','{"text": "aether"}','{"text": "altar"}','{"text": ""}']}}
setblock 40 64 318 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen Altar"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 48 64 306 48 79 319 minecraft:light_gray_concrete
fill 41 63 310 45 63 312 aether:holystone
setblock 41 64 311 aether:altar
setblock 43 64 311 aether:freezer
setblock 45 64 311 aether:incubator
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
