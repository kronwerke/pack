# 076 list_transport/belt, create_tank, vault, drawers
#area 59 212 109 237
fill 59 64 212 103 91 237 minecraft:air
fill 104 64 212 109 91 237 minecraft:air
fill 59 60 212 109 62 237 minecraft:stone
fill 59 63 212 109 63 237 minecraft:light_gray_concrete
fill 63 64 218 109 79 218 minecraft:light_gray_concrete
fill 63 64 218 63 79 231 minecraft:light_gray_concrete
setblock 64 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076.1"}','{"text": "list_transport"}','{"text": "belt"}','{"text": ""}']}}
setblock 65 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann ein"}','{"text": "Förderband"}','{"text": ""}','{"text": ""}']}}
fill 73 64 218 73 79 231 minecraft:light_gray_concrete
setblock 68 64 221 create:shaft[axis=x]
setblock 68 64 225 create:shaft[axis=x]
kw testworld use 68 64 221 up create:belt_connector
kw testworld use 68 64 225 up create:belt_connector
execute unless block 68 64 223 minecraft:air
summon item 68.5 65 222.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 68.5 65 223.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 68.5 65 224.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 74 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 75 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 83 64 218 83 79 231 minecraft:light_gray_concrete
fill 77 64 222 79 67 224 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 84 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076.3"}','{"text": "list_transport"}','{"text": "vault"}','{"text": ""}']}}
setblock 85 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Tresor"}','{"text": ""}','{"text": ""}']}}
fill 94 64 218 94 79 231 minecraft:light_gray_concrete
fill 86 64 222 91 66 224 create:item_vault[axis=x,large=false]
setblock 95 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "076.4"}','{"text": "list_transport"}','{"text": "drawers"}','{"text": ""}']}}
setblock 96 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Schubladen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 104 64 218 104 79 231 minecraft:light_gray_concrete
fill 98 64 222 100 66 222 minecraft:oak_planks
kw testworld use 98 64 222 south functionalstorage:oak_4
execute unless block 98 64 223 minecraft:air
kw testworld use 98 64 223 south minecraft:iron_ingot
kw testworld use 99 64 222 south functionalstorage:oak_4
execute unless block 99 64 223 minecraft:air
kw testworld use 99 64 223 south minecraft:copper_ingot
kw testworld use 100 64 222 south functionalstorage:oak_4
execute unless block 100 64 223 minecraft:air
kw testworld use 100 64 223 south minecraft:gold_ingot
kw testworld use 98 65 222 south functionalstorage:oak_4
execute unless block 98 65 223 minecraft:air
kw testworld use 98 65 223 south minecraft:redstone
kw testworld use 99 65 222 south functionalstorage:oak_4
execute unless block 99 65 223 minecraft:air
kw testworld use 99 65 223 south minecraft:coal
kw testworld use 100 65 222 south functionalstorage:oak_4
execute unless block 100 65 223 minecraft:air
kw testworld use 100 65 223 south minecraft:lapis_lazuli
kw testworld use 98 66 222 south functionalstorage:oak_4
execute unless block 98 66 223 minecraft:air
kw testworld use 98 66 223 south minecraft:diamond
kw testworld use 99 66 222 south functionalstorage:oak_4
execute unless block 99 66 223 minecraft:air
kw testworld use 99 66 223 south minecraft:quartz
kw testworld use 100 66 222 south functionalstorage:oak_4
execute unless block 100 66 223 minecraft:air
kw testworld use 100 66 223 south minecraft:bone
