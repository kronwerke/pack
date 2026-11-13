# 141 list_transport/packages, create_tank, hose_pulley
#area 296 292 335 317
fill 296 64 292 335 91 317 minecraft:air
fill 296 60 292 335 62 317 minecraft:stone
fill 296 63 292 335 63 317 minecraft:light_gray_concrete
fill 300 64 298 335 79 298 minecraft:light_gray_concrete
fill 300 64 298 300 79 311 minecraft:light_gray_concrete
setblock 301 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 302 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 310 64 298 310 79 311 minecraft:light_gray_concrete
setblock 305 64 302 minecraft:barrel[facing=up]
setblock 305 64 303 create:packager[facing=south,linked=false,powered=false]
setblock 303 64 304 create:shaft[axis=z]
setblock 307 64 304 create:shaft[axis=z]
kw testworld use 303 64 304 up create:belt_connector
kw testworld use 307 64 304 up create:belt_connector
execute unless block 305 64 304 minecraft:air
summon item 305.5 65 304.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 306.5 65 304.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 311 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 312 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 320 64 298 320 79 311 minecraft:light_gray_concrete
fill 314 64 302 316 67 304 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 321 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 322 64 310 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 330 64 298 330 79 311 minecraft:light_gray_concrete
fill 324 62 302 326 63 304 minecraft:water
fill 322 64 303 322 66 303 minecraft:spruce_log[axis=y]
fill 328 64 303 328 66 303 minecraft:spruce_log[axis=y]
fill 322 67 303 328 67 303 minecraft:spruce_planks
setblock 325 67 303 create:hose_pulley[facing=south]
setblock 324 67 303 create:creative_motor[facing=east]{ScrollValue:32}
setblock 323 67 303 create:andesite_casing
setblock 324 67 304 create:andesite_casing
setblock 324 67 302 create:andesite_casing
setblock 324 68 303 create:andesite_casing
setblock 324 66 303 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
