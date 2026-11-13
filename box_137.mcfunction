# 137 list_transport/packages, create_tank, hose_pulley
#area 266 286 305 311
fill 266 64 286 305 91 311 minecraft:air
fill 266 60 286 305 62 311 minecraft:stone
fill 266 63 286 305 63 311 minecraft:light_gray_concrete
fill 270 64 292 305 79 292 minecraft:light_gray_concrete
fill 270 64 292 270 79 305 minecraft:light_gray_concrete
setblock 271 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "137.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 272 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 280 64 292 280 79 305 minecraft:light_gray_concrete
setblock 275 64 296 minecraft:barrel[facing=up]
setblock 275 64 297 create:packager[facing=south,linked=false,powered=false]
setblock 273 64 298 create:shaft[axis=z]
setblock 277 64 298 create:shaft[axis=z]
kw testworld use 273 64 298 up create:belt_connector
kw testworld use 277 64 298 up create:belt_connector
execute unless block 275 64 298 minecraft:air
summon item 275.5 65 298.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 276.5 65 298.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 281 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "137.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 282 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 290 64 292 290 79 305 minecraft:light_gray_concrete
fill 284 64 296 286 67 298 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 291 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "137.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 292 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 300 64 292 300 79 305 minecraft:light_gray_concrete
fill 294 62 296 296 63 298 minecraft:water
fill 292 64 297 292 66 297 minecraft:spruce_log[axis=y]
fill 298 64 297 298 66 297 minecraft:spruce_log[axis=y]
fill 292 67 297 298 67 297 minecraft:spruce_planks
setblock 295 67 297 create:hose_pulley[facing=south]
setblock 294 67 297 create:creative_motor[facing=east]{ScrollValue:32}
setblock 293 67 297 create:andesite_casing
setblock 294 67 298 create:andesite_casing
setblock 294 67 296 create:andesite_casing
setblock 294 68 297 create:andesite_casing
setblock 294 66 297 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
