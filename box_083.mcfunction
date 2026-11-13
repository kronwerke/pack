# 083 list_transport/belt, create_tank, vault, drawers
#area 59 231 109 256
fill 59 64 231 103 91 256 minecraft:air
fill 104 64 231 109 91 256 minecraft:air
fill 59 60 231 109 62 256 minecraft:stone
fill 59 63 231 109 63 256 minecraft:light_gray_concrete
fill 63 64 237 109 79 237 minecraft:light_gray_concrete
fill 63 64 237 63 79 250 minecraft:light_gray_concrete
setblock 64 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.1"}','{"text": "list_transport"}','{"text": "belt"}','{"text": ""}']}}
setblock 65 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann ein"}','{"text": "Förderband"}','{"text": ""}','{"text": ""}']}}
fill 73 64 237 73 79 250 minecraft:light_gray_concrete
setblock 68 64 240 create:shaft[axis=x]
setblock 68 64 244 create:shaft[axis=x]
kw testworld use 68 64 240 up create:belt_connector
kw testworld use 68 64 244 up create:belt_connector
execute unless block 68 64 242 minecraft:air
summon item 68.5 65 241.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 68.5 65 242.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 68.5 65 243.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 74 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 75 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 83 64 237 83 79 250 minecraft:light_gray_concrete
fill 77 64 241 79 67 243 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 84 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.3"}','{"text": "list_transport"}','{"text": "vault"}','{"text": ""}']}}
setblock 85 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Tresor"}','{"text": ""}','{"text": ""}']}}
fill 94 64 237 94 79 250 minecraft:light_gray_concrete
fill 86 64 241 91 66 243 create:item_vault[axis=x,large=false]
setblock 95 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.4"}','{"text": "list_transport"}','{"text": "drawers"}','{"text": ""}']}}
setblock 96 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Schubladen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 104 64 237 104 79 250 minecraft:light_gray_concrete
fill 98 64 241 100 66 241 minecraft:oak_planks
kw testworld use 98 64 241 south functionalstorage:oak_4
execute unless block 98 64 242 minecraft:air
data merge block 98 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:iron_ingot",count:1},Amount:128},1:{Stack:{id:"minecraft:copper_ingot",count:1},Amount:192},2:{Stack:{id:"minecraft:gold_ingot",count:1},Amount:256},3:{Stack:{id:"minecraft:raw_iron",count:1},Amount:320}}}}
kw testworld use 99 64 241 south functionalstorage:oak_4
execute unless block 99 64 242 minecraft:air
data merge block 99 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:raw_copper",count:1},Amount:128},1:{Stack:{id:"minecraft:raw_gold",count:1},Amount:192},2:{Stack:{id:"minecraft:coal",count:1},Amount:256},3:{Stack:{id:"minecraft:charcoal",count:1},Amount:320}}}}
kw testworld use 100 64 241 south functionalstorage:oak_4
execute unless block 100 64 242 minecraft:air
data merge block 100 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:redstone",count:1},Amount:128},1:{Stack:{id:"minecraft:lapis_lazuli",count:1},Amount:192},2:{Stack:{id:"minecraft:diamond",count:1},Amount:256},3:{Stack:{id:"minecraft:emerald",count:1},Amount:320}}}}
kw testworld use 98 65 241 south functionalstorage:oak_4
execute unless block 98 65 242 minecraft:air
data merge block 98 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:quartz",count:1},Amount:128},1:{Stack:{id:"minecraft:amethyst_shard",count:1},Amount:192},2:{Stack:{id:"minecraft:flint",count:1},Amount:256},3:{Stack:{id:"minecraft:clay_ball",count:1},Amount:320}}}}
kw testworld use 99 65 241 south functionalstorage:oak_4
execute unless block 99 65 242 minecraft:air
data merge block 99 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:bone",count:1},Amount:128},1:{Stack:{id:"minecraft:string",count:1},Amount:192},2:{Stack:{id:"minecraft:gunpowder",count:1},Amount:256},3:{Stack:{id:"minecraft:rotten_flesh",count:1},Amount:320}}}}
kw testworld use 100 65 241 south functionalstorage:oak_4
execute unless block 100 65 242 minecraft:air
data merge block 100 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:leather",count:1},Amount:128},1:{Stack:{id:"minecraft:feather",count:1},Amount:192},2:{Stack:{id:"minecraft:wheat",count:1},Amount:256},3:{Stack:{id:"minecraft:sugar_cane",count:1},Amount:320}}}}
kw testworld use 98 66 241 south functionalstorage:oak_4
execute unless block 98 66 242 minecraft:air
data merge block 98 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:red_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:blue_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:green_dye",count:1},Amount:256},3:{Stack:{id:"minecraft:yellow_dye",count:1},Amount:320}}}}
kw testworld use 99 66 241 south functionalstorage:oak_4
execute unless block 99 66 242 minecraft:air
data merge block 99 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:white_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:black_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:slime_ball",count:1},Amount:256},3:{Stack:{id:"minecraft:ender_pearl",count:1},Amount:320}}}}
kw testworld use 100 66 241 south functionalstorage:oak_4
execute unless block 100 66 242 minecraft:air
data merge block 100 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:blaze_rod",count:1},Amount:128},1:{Stack:{id:"minecraft:glowstone_dust",count:1},Amount:192},2:{Stack:{id:"minecraft:nether_wart",count:1},Amount:256},3:{Stack:{id:"minecraft:paper",count:1},Amount:320}}}}
