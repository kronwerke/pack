# 112 list_transport/packages, create_tank, hose_pulley
#area 266 254 305 279
fill 266 64 254 305 91 279 minecraft:air
fill 266 60 254 305 62 279 minecraft:stone
fill 266 63 254 305 63 279 minecraft:light_gray_concrete
fill 270 64 260 305 79 260 minecraft:light_gray_concrete
fill 270 64 260 270 79 273 minecraft:light_gray_concrete
setblock 271 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 272 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 280 64 260 280 79 273 minecraft:light_gray_concrete
setblock 275 64 264 minecraft:barrel[facing=up]
setblock 275 64 265 create:packager[facing=south,linked=false,powered=false]
setblock 273 64 266 create:shaft[axis=z]
setblock 277 64 266 create:shaft[axis=z]
kw testworld use 273 64 266 up create:belt_connector
kw testworld use 277 64 266 up create:belt_connector
execute unless block 275 64 266 minecraft:air
summon item 275.5 65 266.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 276.5 65 266.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 281 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 282 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 290 64 260 290 79 273 minecraft:light_gray_concrete
fill 284 64 264 286 67 266 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 291 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "112.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 292 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 300 64 260 300 79 273 minecraft:light_gray_concrete
fill 294 62 264 296 63 266 minecraft:water
fill 292 64 265 292 66 265 minecraft:spruce_log[axis=y]
fill 298 64 265 298 66 265 minecraft:spruce_log[axis=y]
fill 292 67 265 298 67 265 minecraft:spruce_planks
setblock 295 67 265 create:hose_pulley[facing=south]
setblock 294 67 265 create:creative_motor[facing=east]{ScrollValue:32}
setblock 293 67 265 create:andesite_casing
setblock 294 67 266 create:andesite_casing
setblock 294 67 264 create:andesite_casing
setblock 294 68 265 create:andesite_casing
setblock 294 66 265 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
