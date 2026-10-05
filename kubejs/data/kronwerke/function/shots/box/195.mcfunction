# 195 list_transport/belt, packages, create_tank, hose_pulley, ie_wire, mek_transporter, vault, drawers
fill 336 63 337 417 63 350 minecraft:light_gray_concrete
fill 336 64 337 417 71 337 minecraft:light_gray_concrete
fill 336 64 337 336 71 350 minecraft:light_gray_concrete
setblock 337 64 349 minecraft:air
setblock 337 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.1"}','{"text": "list_transport"}','{"text": "belt"}','{"text": ""}']}}
setblock 338 64 349 minecraft:air
setblock 338 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann ein"}','{"text": "Förderband"}','{"text": ""}','{"text": ""}']}}
setblock 338 64 341 minecraft:polished_andesite
summon item_frame 338 64 342 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"create:belt_connector",count:1}}
setblock 347 64 349 minecraft:air
setblock 347 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.2"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 348 64 349 minecraft:air
setblock 348 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
setblock 348 64 341 create:packager
setblock 357 64 349 minecraft:air
setblock 357 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.3"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 358 64 349 minecraft:air
setblock 358 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
setblock 358 64 341 create:fluid_tank
setblock 367 64 349 minecraft:air
setblock 367 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.4"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 368 64 349 minecraft:air
setblock 368 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
setblock 368 64 341 create:hose_pulley
setblock 377 64 349 minecraft:air
setblock 377 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.5"}','{"text": "list_transport"}','{"text": "ie_wire"}','{"text": ""}']}}
setblock 378 64 349 minecraft:air
setblock 378 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lies: IE-Drähte"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 378 64 341 minecraft:polished_andesite
summon item_frame 378 64 342 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:copper_ingot",count:1}}
setblock 387 64 349 minecraft:air
setblock 387 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.6"}','{"text": "list_transport"}','{"text": "mek_transporter"}','{"text": ""}']}}
setblock 388 64 349 minecraft:air
setblock 388 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lies:"}','{"text": "Logistiktransporter"}','{"text": ""}','{"text": ""}']}}
setblock 388 64 341 minecraft:polished_andesite
summon item_frame 388 64 342 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"minecraft:iron_ingot",count:1}}
setblock 397 64 349 minecraft:air
setblock 397 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.7"}','{"text": "list_transport"}','{"text": "vault"}','{"text": ""}']}}
setblock 398 64 349 minecraft:air
setblock 398 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Tresor"}','{"text": ""}','{"text": ""}']}}
setblock 398 64 341 create:item_vault
setblock 407 64 349 minecraft:air
setblock 407 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "195.8"}','{"text": "list_transport"}','{"text": "drawers"}','{"text": ""}']}}
setblock 408 64 349 minecraft:air
setblock 408 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Schubladen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
setblock 408 64 341 functionalstorage:oak_1
