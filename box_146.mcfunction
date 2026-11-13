# 146 list_transport/packages, create_tank, hose_pulley
#area 296 296 335 321
fill 296 64 296 335 91 321 minecraft:air
fill 296 60 296 335 62 321 minecraft:stone
fill 296 63 296 335 63 321 minecraft:light_gray_concrete
fill 300 64 302 335 79 302 minecraft:light_gray_concrete
fill 300 64 302 300 79 315 minecraft:light_gray_concrete
setblock 301 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 302 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 310 64 302 310 79 315 minecraft:light_gray_concrete
setblock 305 64 306 minecraft:barrel[facing=up]
setblock 305 64 307 create:packager[facing=south,linked=false,powered=false]
setblock 303 64 308 create:shaft[axis=z]
setblock 307 64 308 create:shaft[axis=z]
kw testworld use 303 64 308 up create:belt_connector
kw testworld use 307 64 308 up create:belt_connector
execute unless block 305 64 308 minecraft:air
summon item 305.5 65 308.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 306.5 65 308.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 311 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 312 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 320 64 302 320 79 315 minecraft:light_gray_concrete
fill 314 64 306 316 67 308 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 321 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "146.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 322 64 314 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 330 64 302 330 79 315 minecraft:light_gray_concrete
fill 324 62 306 326 63 308 minecraft:water
fill 322 64 307 322 66 307 minecraft:spruce_log[axis=y]
fill 328 64 307 328 66 307 minecraft:spruce_log[axis=y]
fill 322 67 307 328 67 307 minecraft:spruce_planks
setblock 325 67 307 create:hose_pulley[facing=south]
setblock 324 67 307 create:creative_motor[facing=east]{ScrollValue:32}
setblock 323 67 307 create:andesite_casing
setblock 324 67 308 create:andesite_casing
setblock 324 67 306 create:andesite_casing
setblock 324 68 307 create:andesite_casing
setblock 324 66 307 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
