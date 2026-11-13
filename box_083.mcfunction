# 083 storage/drawers_4, controller, vault_big
#area 43 231 83 256
fill 43 64 231 83 91 256 minecraft:air
fill 43 60 231 83 62 256 minecraft:stone
fill 43 63 231 83 63 256 minecraft:light_gray_concrete
fill 47 64 237 83 79 237 minecraft:light_gray_concrete
fill 47 64 237 47 79 250 minecraft:light_gray_concrete
setblock 48 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.1"}','{"text": "storage"}','{"text": "drawers_4"}','{"text": ""}']}}
setblock 49 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Schubladenwand"}','{"text": ""}','{"text": ""}']}}
fill 57 64 237 57 79 250 minecraft:light_gray_concrete
setblock 51 64 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 51 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:iron_ingot",count:1},Amount:128},1:{Stack:{id:"minecraft:copper_ingot",count:1},Amount:192},2:{Stack:{id:"minecraft:gold_ingot",count:1},Amount:256},3:{Stack:{id:"minecraft:raw_iron",count:1},Amount:320}}}}
setblock 52 64 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 52 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:raw_copper",count:1},Amount:128},1:{Stack:{id:"minecraft:raw_gold",count:1},Amount:192},2:{Stack:{id:"minecraft:coal",count:1},Amount:256},3:{Stack:{id:"minecraft:charcoal",count:1},Amount:320}}}}
setblock 53 64 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 53 64 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:redstone",count:1},Amount:128},1:{Stack:{id:"minecraft:lapis_lazuli",count:1},Amount:192},2:{Stack:{id:"minecraft:diamond",count:1},Amount:256},3:{Stack:{id:"minecraft:emerald",count:1},Amount:320}}}}
setblock 51 65 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 51 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:quartz",count:1},Amount:128},1:{Stack:{id:"minecraft:amethyst_shard",count:1},Amount:192},2:{Stack:{id:"minecraft:flint",count:1},Amount:256},3:{Stack:{id:"minecraft:clay_ball",count:1},Amount:320}}}}
setblock 52 65 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 52 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:bone",count:1},Amount:128},1:{Stack:{id:"minecraft:string",count:1},Amount:192},2:{Stack:{id:"minecraft:gunpowder",count:1},Amount:256},3:{Stack:{id:"minecraft:rotten_flesh",count:1},Amount:320}}}}
setblock 53 65 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 53 65 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:leather",count:1},Amount:128},1:{Stack:{id:"minecraft:feather",count:1},Amount:192},2:{Stack:{id:"minecraft:wheat",count:1},Amount:256},3:{Stack:{id:"minecraft:sugar_cane",count:1},Amount:320}}}}
setblock 51 66 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 51 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:red_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:blue_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:green_dye",count:1},Amount:256},3:{Stack:{id:"minecraft:yellow_dye",count:1},Amount:320}}}}
setblock 52 66 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 52 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:white_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:black_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:slime_ball",count:1},Amount:256},3:{Stack:{id:"minecraft:ender_pearl",count:1},Amount:320}}}}
setblock 53 66 242 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 53 66 242 {handler:{BigItems:{0:{Stack:{id:"minecraft:blaze_rod",count:1},Amount:128},1:{Stack:{id:"minecraft:glowstone_dust",count:1},Amount:192},2:{Stack:{id:"minecraft:nether_wart",count:1},Amount:256},3:{Stack:{id:"minecraft:paper",count:1},Amount:320}}}}
setblock 58 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.2"}','{"text": "storage"}','{"text": "controller"}','{"text": ""}']}}
setblock 59 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Lagerkern"}','{"text": ""}','{"text": ""}']}}
fill 67 64 237 67 79 250 minecraft:light_gray_concrete
setblock 62 64 242 sophisticatedstorage:controller
setblock 60 64 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 61 64 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 63 64 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 61 65 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 62 65 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 63 65 242 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 68 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083.3"}','{"text": "storage"}','{"text": "vault_big"}','{"text": ""}']}}
setblock 69 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "großen Tresor"}','{"text": ""}','{"text": ""}']}}
fill 78 64 237 78 79 250 minecraft:light_gray_concrete
fill 70 64 241 75 66 243 create:item_vault[axis=x,large=false]
