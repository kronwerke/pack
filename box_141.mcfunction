# 141 list_transport/packages, create_tank, hose_pulley
#area 296 290 335 315
fill 296 64 290 335 91 315 minecraft:air
fill 296 60 290 335 62 315 minecraft:stone
fill 296 63 290 335 63 315 minecraft:light_gray_concrete
fill 300 64 296 335 79 296 minecraft:light_gray_concrete
fill 300 64 296 300 79 309 minecraft:light_gray_concrete
setblock 301 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 302 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 310 64 296 310 79 309 minecraft:light_gray_concrete
setblock 305 64 300 minecraft:barrel[facing=up]
setblock 305 64 301 create:packager[facing=south,linked=false,powered=false]
setblock 303 64 302 create:shaft[axis=z]
setblock 307 64 302 create:shaft[axis=z]
kw testworld use 303 64 302 up create:belt_connector
kw testworld use 307 64 302 up create:belt_connector
execute unless block 305 64 302 minecraft:air
summon item 305.5 65 302.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 306.5 65 302.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 311 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 312 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 320 64 296 320 79 309 minecraft:light_gray_concrete
fill 314 64 300 316 67 302 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 321 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "141.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 322 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 330 64 296 330 79 309 minecraft:light_gray_concrete
fill 324 62 300 326 63 302 minecraft:water
fill 322 64 301 322 66 301 minecraft:spruce_log[axis=y]
fill 328 64 301 328 66 301 minecraft:spruce_log[axis=y]
fill 322 67 301 328 67 301 minecraft:spruce_planks
setblock 325 67 301 create:hose_pulley[facing=south]
setblock 324 67 301 create:creative_motor[facing=east]{ScrollValue:32}
setblock 323 67 301 create:andesite_casing
setblock 324 67 302 create:andesite_casing
setblock 324 67 300 create:andesite_casing
setblock 324 68 301 create:andesite_casing
setblock 324 66 301 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
