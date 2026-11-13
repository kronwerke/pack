# 084 list_transport/belt, create_tank, ie_wire, mek_transporter, vault, drawers
#area 79 231 152 256
fill 79 64 231 123 91 256 minecraft:air
fill 124 64 231 152 91 256 minecraft:air
fill 79 60 231 152 62 256 minecraft:stone
fill 79 63 231 152 63 256 minecraft:light_gray_concrete
fill 83 64 237 152 79 237 minecraft:light_gray_concrete
fill 83 64 237 83 79 250 minecraft:light_gray_concrete
setblock 84 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.1"}','{"text": "list_transport"}','{"text": "belt"}','{"text": ""}']}}
setblock 85 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Spann ein"}','{"text": "Förderband"}','{"text": ""}','{"text": ""}']}}
fill 93 64 237 93 79 250 minecraft:light_gray_concrete
setblock 88 64 240 create:shaft[axis=x]
setblock 88 64 244 create:shaft[axis=x]
kw testworld use 88 64 240 up create:belt_connector
kw testworld use 88 64 244 up create:belt_connector
execute unless block 88 64 242 minecraft:air
summon item 88.5 65 241.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 88.5 65 242.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 88.5 65 243.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 94 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.2"}','{"text": "list_transport"}','{"text": "create_tank"}','{"text": ""}']}}
setblock 95 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Flüssigkeitstank"}','{"text": ""}','{"text": ""}']}}
fill 103 64 237 103 79 250 minecraft:light_gray_concrete
fill 97 64 241 99 67 243 create:fluid_tank[bottom=false,shape=window,top=false]
setblock 104 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.3"}','{"text": "list_transport"}','{"text": "ie_wire"}','{"text": ""}']}}
setblock 105 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lies: IE-Drähte"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 115 64 237 115 79 250 minecraft:light_gray_concrete
setblock 106 64 242 immersiveengineering:capacitor_lv
setblock 112 64 242 immersiveengineering:capacitor_lv
fill 109 64 242 109 66 242 immersiveengineering:treated_fence
kw testworld use 106 64 242 up immersiveengineering:connector_lv
kw testworld use 112 64 242 up immersiveengineering:connector_lv
kw testworld use 109 66 242 up immersiveengineering:connector_lv_relay
kw testworld use 106 65 242 south immersiveengineering:wirecoil_copper
kw testworld use 109 67 242 south immersiveengineering:wirecoil_copper
kw testworld use 109 67 242 south immersiveengineering:wirecoil_copper
kw testworld use 112 65 242 south immersiveengineering:wirecoil_copper
setblock 116 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.4"}','{"text": "list_transport"}','{"text": "mek_transporter"}','{"text": ""}']}}
setblock 117 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lies:"}','{"text": "Logistiktransporter"}','{"text": ""}','{"text": ""}']}}
fill 126 64 237 126 79 250 minecraft:light_gray_concrete
setblock 117 64 242 minecraft:chest[facing=south]{Items:[]}
setblock 119 64 242 mekanism:enrichment_chamber[facing=south,active=false]
setblock 121 64 242 mekanism:energized_smelter[facing=south,active=false]
setblock 123 64 242 minecraft:chest[facing=south]{Items:[]}
setblock 118 64 242 mekanism:basic_logistical_transporter
setblock 120 64 242 mekanism:basic_logistical_transporter
setblock 122 64 242 mekanism:basic_logistical_transporter
fill 119 64 241 122 64 241 mekanism:basic_universal_cable
setblock 123 64 241 mekanism:basic_energy_cube[facing=south]
setblock 127 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.5"}','{"text": "list_transport"}','{"text": "vault"}','{"text": ""}']}}
setblock 128 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Tresor"}','{"text": ""}','{"text": ""}']}}
fill 137 64 237 137 79 250 minecraft:light_gray_concrete
fill 129 64 241 134 66 243 create:item_vault[axis=x,large=false]
setblock 138 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "084.6"}','{"text": "list_transport"}','{"text": "drawers"}','{"text": ""}']}}
setblock 139 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau Schubladen"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 147 64 237 147 79 250 minecraft:light_gray_concrete
fill 141 64 241 143 66 241 minecraft:oak_planks
kw testworld use 141 64 241 south functionalstorage:oak_4
execute unless block 141 64 242 minecraft:air
data merge block 141 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:iron_ingot",count:1},Amount:128},1:{Stack:{id:"minecraft:copper_ingot",count:1},Amount:192},2:{Stack:{id:"minecraft:gold_ingot",count:1},Amount:256},3:{Stack:{id:"minecraft:raw_iron",count:1},Amount:320}}}}
kw testworld use 142 64 241 south functionalstorage:oak_4
execute unless block 142 64 242 minecraft:air
data merge block 142 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:raw_copper",count:1},Amount:128},1:{Stack:{id:"minecraft:raw_gold",count:1},Amount:192},2:{Stack:{id:"minecraft:coal",count:1},Amount:256},3:{Stack:{id:"minecraft:charcoal",count:1},Amount:320}}}}
kw testworld use 143 64 241 south functionalstorage:oak_4
execute unless block 143 64 242 minecraft:air
data merge block 143 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:redstone",count:1},Amount:128},1:{Stack:{id:"minecraft:lapis_lazuli",count:1},Amount:192},2:{Stack:{id:"minecraft:diamond",count:1},Amount:256},3:{Stack:{id:"minecraft:emerald",count:1},Amount:320}}}}
kw testworld use 141 65 241 south functionalstorage:oak_4
execute unless block 141 65 242 minecraft:air
data merge block 141 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:quartz",count:1},Amount:128},1:{Stack:{id:"minecraft:amethyst_shard",count:1},Amount:192},2:{Stack:{id:"minecraft:flint",count:1},Amount:256},3:{Stack:{id:"minecraft:clay_ball",count:1},Amount:320}}}}
kw testworld use 142 65 241 south functionalstorage:oak_4
execute unless block 142 65 242 minecraft:air
data merge block 142 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:bone",count:1},Amount:128},1:{Stack:{id:"minecraft:string",count:1},Amount:192},2:{Stack:{id:"minecraft:gunpowder",count:1},Amount:256},3:{Stack:{id:"minecraft:rotten_flesh",count:1},Amount:320}}}}
kw testworld use 143 65 241 south functionalstorage:oak_4
execute unless block 143 65 242 minecraft:air
data merge block 143 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:leather",count:1},Amount:128},1:{Stack:{id:"minecraft:feather",count:1},Amount:192},2:{Stack:{id:"minecraft:wheat",count:1},Amount:256},3:{Stack:{id:"minecraft:sugar_cane",count:1},Amount:320}}}}
kw testworld use 141 66 241 south functionalstorage:oak_4
execute unless block 141 66 242 minecraft:air
data merge block 141 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:red_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:blue_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:green_dye",count:1},Amount:256},3:{Stack:{id:"minecraft:yellow_dye",count:1},Amount:320}}}}
kw testworld use 142 66 241 south functionalstorage:oak_4
execute unless block 142 66 242 minecraft:air
data merge block 142 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:white_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:black_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:slime_ball",count:1},Amount:256},3:{Stack:{id:"minecraft:ender_pearl",count:1},Amount:320}}}}
kw testworld use 143 66 241 south functionalstorage:oak_4
execute unless block 143 66 242 minecraft:air
data merge block 143 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:blaze_rod",count:1},Amount:128},1:{Stack:{id:"minecraft:glowstone_dust",count:1},Amount:192},2:{Stack:{id:"minecraft:nether_wart",count:1},Amount:256},3:{Stack:{id:"minecraft:paper",count:1},Amount:320}}}}
