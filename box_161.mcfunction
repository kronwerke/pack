# 161 list_transport/packages, create_tank, hose_pulley
#area 306 298 345 323
fill 306 64 298 345 91 323 minecraft:air
fill 306 60 298 345 62 323 minecraft:stone
fill 306 63 298 345 63 323 minecraft:light_gray_concrete
fill 310 64 304 345 79 304 minecraft:light_gray_concrete
fill 310 64 304 310 79 317 minecraft:light_gray_concrete
setblock 311 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 312 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 320 64 304 320 79 317 minecraft:light_gray_concrete
setblock 315 64 308 minecraft:barrel[facing=up]
setblock 315 64 309 create:packager[facing=south,linked=false,powered=false]
setblock 313 64 310 create:shaft[axis=z]
setblock 317 64 310 create:shaft[axis=z]
kw testworld use 313 64 310 up create:belt_connector
kw testworld use 317 64 310 up create:belt_connector
execute unless block 315 64 310 minecraft:air
summon item 315.5 65 310.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 316.5 65 310.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 321 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 322 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 330 64 304 330 79 317 minecraft:light_gray_concrete
fill 324 64 308 326 67 310 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 331 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "161.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 332 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 340 64 304 340 79 317 minecraft:light_gray_concrete
fill 334 62 308 336 63 310 minecraft:water
fill 332 64 309 332 66 309 minecraft:spruce_log[axis=y]
fill 338 64 309 338 66 309 minecraft:spruce_log[axis=y]
fill 332 67 309 338 67 309 minecraft:spruce_planks
setblock 335 67 309 create:hose_pulley[facing=south]
setblock 334 67 309 create:creative_motor[facing=east]{ScrollValue:32}
setblock 333 67 309 create:andesite_casing
setblock 334 67 310 create:andesite_casing
setblock 334 67 308 create:andesite_casing
setblock 334 68 309 create:andesite_casing
setblock 334 66 309 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
