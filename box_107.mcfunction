# 107 list_transport/packages, create_tank, hose_pulley
#area 249 254 288 279
fill 249 64 254 288 91 279 minecraft:air
fill 249 60 254 288 62 279 minecraft:stone
fill 249 63 254 288 63 279 minecraft:light_gray_concrete
fill 253 64 260 288 79 260 minecraft:light_gray_concrete
fill 253 64 260 253 79 273 minecraft:light_gray_concrete
setblock 254 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 255 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 263 64 260 263 79 273 minecraft:light_gray_concrete
setblock 258 64 264 minecraft:barrel[facing=up]
setblock 258 64 265 create:packager[facing=south,linked=false,powered=false]
setblock 256 64 266 create:shaft[axis=z]
setblock 260 64 266 create:shaft[axis=z]
kw testworld use 256 64 266 up create:belt_connector
kw testworld use 260 64 266 up create:belt_connector
execute unless block 258 64 266 minecraft:air
summon item 258.5 65 266.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 259.5 65 266.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 264 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 265 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 273 64 260 273 79 273 minecraft:light_gray_concrete
fill 267 64 264 269 67 266 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 274 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "107.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 275 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 283 64 260 283 79 273 minecraft:light_gray_concrete
fill 277 62 264 279 63 266 minecraft:water
fill 275 64 265 275 66 265 minecraft:spruce_log[axis=y]
fill 281 64 265 281 66 265 minecraft:spruce_log[axis=y]
fill 275 67 265 281 67 265 minecraft:spruce_planks
setblock 278 67 265 create:hose_pulley[facing=east]
setblock 277 67 265 create:creative_motor[facing=east]{ScrollValue:-32}
setblock 276 67 265 create:andesite_casing
setblock 277 67 266 create:andesite_casing
setblock 277 67 264 create:andesite_casing
setblock 277 68 265 create:andesite_casing
setblock 277 66 265 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
