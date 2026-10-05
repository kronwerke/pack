# 042 create_brass/boiler
fill 374 63 48 387 63 63 minecraft:light_gray_concrete
fill 374 64 48 387 71 48 minecraft:light_gray_concrete
fill 374 64 48 374 71 63 minecraft:light_gray_concrete
setblock 375 64 62 minecraft:air
setblock 375 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "042"}','{"text": "create_brass"}','{"text": "boiler"}','{"text": ""}']}}
setblock 376 64 62 minecraft:air
setblock 376 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a four engine"}','{"text": "boiler with the"}','{"text": "goggles boiler"}','{"text": "overlay"}']}}
setblock 377 64 62 minecraft:air
setblock 377 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Brenner unter"}','{"text": "den Tank, vier"}','{"text": "Motoren, Brille"}','{"text": ""}']}}
fill 378 64 52 380 66 54 create:fluid_tank
fill 378 64 51 380 64 51 create:blaze_burner
setblock 379 65 51 create:steam_engine[face=wall,facing=north]
setblock 379 65 50 create:shaft[axis=z]
setblock 379 65 55 create:steam_engine[face=wall,facing=south]
setblock 379 65 56 create:shaft[axis=z]
setblock 385 64 59 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"create:steam_engine",count:1},{Slot:1b,id:"create:steam_engine",count:1},{Slot:2b,id:"create:goggles",count:1},{Slot:3b,id:"create:blaze_cake",count:8}]}
