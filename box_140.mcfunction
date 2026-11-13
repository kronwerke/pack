# 140 storage/welcome, drawers_4, config_tool, copper_tier, controller, vault_big, trash
#area 220 290 300 315
fill 220 64 290 264 91 315 minecraft:air
fill 265 64 290 300 91 315 minecraft:air
fill 220 60 290 300 62 315 minecraft:stone
fill 220 63 290 300 63 315 minecraft:light_gray_concrete
fill 224 64 296 300 79 296 minecraft:light_gray_concrete
fill 224 64 296 224 79 309 minecraft:light_gray_concrete
setblock 225 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.1"}','{"text": "storage"}','{"text": "welcome"}','{"text": ""}']}}
setblock 226 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Näh einen"}','{"text": "Rucksack"}','{"text": ""}','{"text": ""}']}}
fill 234 64 296 234 79 309 minecraft:light_gray_concrete
setblock 229 64 301 sophisticatedbackpacks:backpack[facing=south]
setblock 235 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.2"}','{"text": "storage"}','{"text": "drawers_4"}','{"text": ""}']}}
setblock 236 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Schubladenwand"}','{"text": ""}','{"text": ""}']}}
fill 244 64 296 244 79 309 minecraft:light_gray_concrete
setblock 238 64 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 238 64 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:iron_ingot",count:1},Amount:128},1:{Stack:{id:"minecraft:copper_ingot",count:1},Amount:192},2:{Stack:{id:"minecraft:gold_ingot",count:1},Amount:256},3:{Stack:{id:"minecraft:raw_iron",count:1},Amount:320}}}}
setblock 239 64 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 239 64 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:raw_copper",count:1},Amount:128},1:{Stack:{id:"minecraft:raw_gold",count:1},Amount:192},2:{Stack:{id:"minecraft:coal",count:1},Amount:256},3:{Stack:{id:"minecraft:charcoal",count:1},Amount:320}}}}
setblock 240 64 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 240 64 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:redstone",count:1},Amount:128},1:{Stack:{id:"minecraft:lapis_lazuli",count:1},Amount:192},2:{Stack:{id:"minecraft:diamond",count:1},Amount:256},3:{Stack:{id:"minecraft:emerald",count:1},Amount:320}}}}
setblock 238 65 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 238 65 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:quartz",count:1},Amount:128},1:{Stack:{id:"minecraft:amethyst_shard",count:1},Amount:192},2:{Stack:{id:"minecraft:flint",count:1},Amount:256},3:{Stack:{id:"minecraft:clay_ball",count:1},Amount:320}}}}
setblock 239 65 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 239 65 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:bone",count:1},Amount:128},1:{Stack:{id:"minecraft:string",count:1},Amount:192},2:{Stack:{id:"minecraft:gunpowder",count:1},Amount:256},3:{Stack:{id:"minecraft:rotten_flesh",count:1},Amount:320}}}}
setblock 240 65 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 240 65 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:leather",count:1},Amount:128},1:{Stack:{id:"minecraft:feather",count:1},Amount:192},2:{Stack:{id:"minecraft:wheat",count:1},Amount:256},3:{Stack:{id:"minecraft:sugar_cane",count:1},Amount:320}}}}
setblock 238 66 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 238 66 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:red_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:blue_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:green_dye",count:1},Amount:256},3:{Stack:{id:"minecraft:yellow_dye",count:1},Amount:320}}}}
setblock 239 66 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 239 66 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:white_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:black_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:slime_ball",count:1},Amount:256},3:{Stack:{id:"minecraft:ender_pearl",count:1},Amount:320}}}}
setblock 240 66 301 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 240 66 301 {handler:{BigItems:{0:{Stack:{id:"minecraft:blaze_rod",count:1},Amount:128},1:{Stack:{id:"minecraft:glowstone_dust",count:1},Amount:192},2:{Stack:{id:"minecraft:nether_wart",count:1},Amount:256},3:{Stack:{id:"minecraft:paper",count:1},Amount:320}}}}
setblock 245 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.3"}','{"text": "storage"}','{"text": "config_tool"}','{"text": ""}']}}
setblock 246 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Sperr eine"}','{"text": "Schublade"}','{"text": ""}','{"text": ""}']}}
fill 254 64 296 254 79 309 minecraft:light_gray_concrete
setblock 248 64 301 functionalstorage:oak_1[facing=down,subfacing=south]
setblock 250 64 301 minecraft:smooth_stone_slab
summon item_display 250.5 64.95 301.5 {item:{id:"functionalstorage:configuration_tool",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 255 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.4"}','{"text": "storage"}','{"text": "copper_tier"}','{"text": ""}']}}
setblock 256 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Werte auf"}','{"text": "Kupfer auf"}','{"text": ""}','{"text": ""}']}}
fill 264 64 296 264 79 309 minecraft:light_gray_concrete
setblock 258 64 301 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 260 64 301 sophisticatedstorage:copper_barrel[facing=south,flat_top=false]
setblock 265 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.5"}','{"text": "storage"}','{"text": "controller"}','{"text": ""}']}}
setblock 266 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Lagerkern"}','{"text": ""}','{"text": ""}']}}
fill 274 64 296 274 79 309 minecraft:light_gray_concrete
setblock 269 64 301 sophisticatedstorage:controller
setblock 267 64 301 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 268 64 301 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 270 64 301 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 268 65 301 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 269 65 301 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 270 65 301 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 275 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.6"}','{"text": "storage"}','{"text": "vault_big"}','{"text": ""}']}}
setblock 276 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "großen Tresor"}','{"text": ""}','{"text": ""}']}}
fill 285 64 296 285 79 309 minecraft:light_gray_concrete
fill 277 64 300 282 66 302 create:item_vault[axis=x,large=false]
setblock 286 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "140.7"}','{"text": "storage"}','{"text": "trash"}','{"text": ""}']}}
setblock 287 64 308 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Mülleimer"}','{"text": ""}','{"text": ""}']}}
fill 295 64 296 295 79 309 minecraft:light_gray_concrete
setblock 290 64 301 trashcans:item_trash_can
setblock 290 65 301 minecraft:hopper[facing=down]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
