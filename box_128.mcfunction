# 128 list_transport/packages, create_tank, hose_pulley
#area 266 256 305 281
fill 266 64 256 305 91 281 minecraft:air
fill 266 60 256 305 62 281 minecraft:stone
fill 266 63 256 305 63 281 minecraft:light_gray_concrete
fill 270 64 262 305 79 262 minecraft:light_gray_concrete
fill 270 64 262 270 79 275 minecraft:light_gray_concrete
setblock 271 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 272 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 280 64 262 280 79 275 minecraft:light_gray_concrete
setblock 275 64 266 minecraft:barrel[facing=up]
setblock 275 64 267 create:packager[facing=south,linked=false,powered=false]
setblock 273 64 268 create:shaft[axis=z]
setblock 277 64 268 create:shaft[axis=z]
kw testworld use 273 64 268 up create:belt_connector
kw testworld use 277 64 268 up create:belt_connector
execute unless block 275 64 268 minecraft:air
summon item 275.5 65 268.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 276.5 65 268.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 281 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 282 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 290 64 262 290 79 275 minecraft:light_gray_concrete
fill 284 64 266 286 67 268 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 291 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "128.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 292 64 274 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 300 64 262 300 79 275 minecraft:light_gray_concrete
fill 294 62 266 296 63 268 minecraft:water
fill 292 64 267 292 66 267 minecraft:spruce_log[axis=y]
fill 298 64 267 298 66 267 minecraft:spruce_log[axis=y]
fill 292 67 267 298 67 267 minecraft:spruce_planks
setblock 295 67 267 create:hose_pulley[facing=south]
setblock 294 67 267 create:creative_motor[facing=east]{ScrollValue:32}
setblock 293 67 267 create:andesite_casing
setblock 294 67 268 create:andesite_casing
setblock 294 67 266 create:andesite_casing
setblock 294 68 267 create:andesite_casing
setblock 294 66 267 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
