# 086 list_transport/packages, create_tank, hose_pulley
#area 228 233 267 258
fill 228 64 233 267 91 258 minecraft:air
fill 228 60 233 267 62 258 minecraft:stone
fill 228 63 233 267 63 258 minecraft:light_gray_concrete
fill 232 64 239 267 79 239 minecraft:light_gray_concrete
fill 232 64 239 232 79 252 minecraft:light_gray_concrete
setblock 233 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 234 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 242 64 239 242 79 252 minecraft:light_gray_concrete
setblock 237 64 243 minecraft:barrel[facing=up]
setblock 237 64 244 create:packager[facing=south,linked=false,powered=false]
setblock 235 64 245 create:shaft[axis=z]
setblock 239 64 245 create:shaft[axis=z]
kw testworld use 235 64 245 up create:belt_connector
kw testworld use 239 64 245 up create:belt_connector
execute unless block 237 64 245 minecraft:air
summon item 237.5 65 245.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 238.5 65 245.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 243 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 244 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 252 64 239 252 79 252 minecraft:light_gray_concrete
fill 246 64 243 248 67 245 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 253 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "086.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 254 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 262 64 239 262 79 252 minecraft:light_gray_concrete
fill 256 62 243 258 63 245 minecraft:water
fill 254 64 244 254 66 244 minecraft:spruce_log[axis=y]
fill 260 64 244 260 66 244 minecraft:spruce_log[axis=y]
fill 254 67 244 260 67 244 minecraft:spruce_planks
setblock 257 67 244 create:hose_pulley[facing=east]
setblock 256 67 244 create:creative_motor[facing=east]{ScrollValue:32}
setblock 255 67 244 create:andesite_casing
setblock 256 67 245 create:andesite_casing
setblock 256 67 243 create:andesite_casing
setblock 256 68 244 create:andesite_casing
setblock 256 66 244 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
