# 045 create_brass/alternator
fill 45 63 69 58 63 82 minecraft:light_gray_concrete
fill 45 64 69 58 71 69 minecraft:light_gray_concrete
fill 45 64 69 45 71 82 minecraft:light_gray_concrete
setblock 46 64 81 minecraft:air
setblock 46 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "045"}','{"text": "create_brass"}','{"text": "alternator"}','{"text": ""}']}}
setblock 47 64 81 minecraft:air
setblock 47 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "steam engine"}','{"text": "driving an"}','{"text": "alternator with"}','{"text": "connectors"}']}}
setblock 48 64 74 create:steam_engine[face=floor,facing=east]
fill 49 64 74 50 64 74 create:shaft[axis=x]
setblock 51 64 74 createaddition:alternator[facing=west]
setblock 51 65 74 createaddition:connector
