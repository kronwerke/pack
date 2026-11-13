# 096 list_transport/packages, create_tank, hose_pulley
#area 228 252 267 277
fill 228 64 252 267 91 277 minecraft:air
fill 228 60 252 267 62 277 minecraft:stone
fill 228 63 252 267 63 277 minecraft:light_gray_concrete
fill 232 64 258 267 79 258 minecraft:light_gray_concrete
fill 232 64 258 232 79 271 minecraft:light_gray_concrete
setblock 233 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.1"}','{"text": "list_transport"}','{"text": "packages"}','{"text": ""}']}}
setblock 234 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verschick ein"}','{"text": "Paket"}','{"text": ""}','{"text": ""}']}}
fill 242 64 258 242 79 271 minecraft:light_gray_concrete
setblock 237 64 262 minecraft:barrel[facing=up]
setblock 237 64 263 create:packager[facing=south,linked=false,powered=false]
setblock 235 64 264 create:shaft[axis=z]
setblock 239 64 264 create:shaft[axis=z]
kw testworld use 235 64 264 up create:belt_connector
kw testworld use 239 64 264 up create:belt_connector
execute unless block 237 64 264 minecraft:air
summon item 237.5 65 264.5 {Item:{id:"create:cardboard_package_10x12",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 238.5 65 264.5 {Item:{id:"create:cardboard_package_10x8",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 243 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 244 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 252 64 258 252 79 271 minecraft:light_gray_concrete
fill 246 64 262 248 67 264 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 253 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096.3"}','{"text": "list_transport"}','{"text": "hose_pulley"}','{"text": ""}']}}
setblock 254 64 270 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Häng einen"}','{"text": "Schlauchaufzug"}','{"text": "über den See"}','{"text": ""}']}}
fill 262 64 258 262 79 271 minecraft:light_gray_concrete
fill 256 62 262 258 63 264 minecraft:water
fill 254 64 263 254 66 263 minecraft:spruce_log[axis=y]
fill 260 64 263 260 66 263 minecraft:spruce_log[axis=y]
fill 254 67 263 260 67 263 minecraft:spruce_planks
setblock 257 67 263 create:hose_pulley[facing=east]
setblock 256 67 263 create:creative_motor[facing=east]{ScrollValue:32}
setblock 255 67 263 create:andesite_casing
setblock 256 67 264 create:andesite_casing
setblock 256 67 262 create:andesite_casing
setblock 256 68 263 create:andesite_casing
setblock 256 66 263 create:andesite_casing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
