# 160 storage/welcome, drawers_4, config_tool, copper_tier, controller, vault_big, trash
#area 230 298 310 323
fill 230 64 298 274 91 323 minecraft:air
fill 275 64 298 310 91 323 minecraft:air
fill 230 60 298 310 62 323 minecraft:stone
fill 230 63 298 310 63 323 minecraft:light_gray_concrete
fill 234 64 304 310 79 304 minecraft:light_gray_concrete
fill 234 64 304 234 79 317 minecraft:light_gray_concrete
setblock 235 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.1"}','{"text": "storage"}','{"text": "welcome"}','{"text": ""}']}}
setblock 236 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Näh einen"}','{"text": "Rucksack"}','{"text": ""}','{"text": ""}']}}
fill 244 64 304 244 79 317 minecraft:light_gray_concrete
setblock 239 64 309 sophisticatedbackpacks:backpack[facing=south]
setblock 245 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.2"}','{"text": "storage"}','{"text": "drawers_4"}','{"text": ""}']}}
setblock 246 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Schubladenwand"}','{"text": ""}','{"text": ""}']}}
fill 254 64 304 254 79 317 minecraft:light_gray_concrete
setblock 248 64 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 248 64 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:iron_ingot",count:1},Amount:128},1:{Stack:{id:"minecraft:copper_ingot",count:1},Amount:192},2:{Stack:{id:"minecraft:gold_ingot",count:1},Amount:256},3:{Stack:{id:"minecraft:raw_iron",count:1},Amount:320}}}}
setblock 249 64 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 249 64 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:raw_copper",count:1},Amount:128},1:{Stack:{id:"minecraft:raw_gold",count:1},Amount:192},2:{Stack:{id:"minecraft:coal",count:1},Amount:256},3:{Stack:{id:"minecraft:charcoal",count:1},Amount:320}}}}
setblock 250 64 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 250 64 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:redstone",count:1},Amount:128},1:{Stack:{id:"minecraft:lapis_lazuli",count:1},Amount:192},2:{Stack:{id:"minecraft:diamond",count:1},Amount:256},3:{Stack:{id:"minecraft:emerald",count:1},Amount:320}}}}
setblock 248 65 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 248 65 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:quartz",count:1},Amount:128},1:{Stack:{id:"minecraft:amethyst_shard",count:1},Amount:192},2:{Stack:{id:"minecraft:flint",count:1},Amount:256},3:{Stack:{id:"minecraft:clay_ball",count:1},Amount:320}}}}
setblock 249 65 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 249 65 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:bone",count:1},Amount:128},1:{Stack:{id:"minecraft:string",count:1},Amount:192},2:{Stack:{id:"minecraft:gunpowder",count:1},Amount:256},3:{Stack:{id:"minecraft:rotten_flesh",count:1},Amount:320}}}}
setblock 250 65 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 250 65 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:leather",count:1},Amount:128},1:{Stack:{id:"minecraft:feather",count:1},Amount:192},2:{Stack:{id:"minecraft:wheat",count:1},Amount:256},3:{Stack:{id:"minecraft:sugar_cane",count:1},Amount:320}}}}
setblock 248 66 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 248 66 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:red_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:blue_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:green_dye",count:1},Amount:256},3:{Stack:{id:"minecraft:yellow_dye",count:1},Amount:320}}}}
setblock 249 66 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 249 66 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:white_dye",count:1},Amount:128},1:{Stack:{id:"minecraft:black_dye",count:1},Amount:192},2:{Stack:{id:"minecraft:slime_ball",count:1},Amount:256},3:{Stack:{id:"minecraft:ender_pearl",count:1},Amount:320}}}}
setblock 250 66 309 functionalstorage:oak_4[facing=down,subfacing=south]
data merge block 250 66 309 {handler:{BigItems:{0:{Stack:{id:"minecraft:blaze_rod",count:1},Amount:128},1:{Stack:{id:"minecraft:glowstone_dust",count:1},Amount:192},2:{Stack:{id:"minecraft:nether_wart",count:1},Amount:256},3:{Stack:{id:"minecraft:paper",count:1},Amount:320}}}}
setblock 255 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.3"}','{"text": "storage"}','{"text": "config_tool"}','{"text": ""}']}}
setblock 256 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Sperr eine"}','{"text": "Schublade"}','{"text": ""}','{"text": ""}']}}
fill 264 64 304 264 79 317 minecraft:light_gray_concrete
setblock 258 64 309 functionalstorage:oak_1[facing=down,subfacing=south]
setblock 260 64 309 minecraft:smooth_stone_slab
summon item_display 260.5 64.95 309.5 {item:{id:"functionalstorage:configuration_tool",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 265 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.4"}','{"text": "storage"}','{"text": "copper_tier"}','{"text": ""}']}}
setblock 266 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Werte auf"}','{"text": "Kupfer auf"}','{"text": ""}','{"text": ""}']}}
fill 274 64 304 274 79 317 minecraft:light_gray_concrete
setblock 268 64 309 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 270 64 309 sophisticatedstorage:copper_barrel[facing=south,flat_top=false]
setblock 275 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.5"}','{"text": "storage"}','{"text": "controller"}','{"text": ""}']}}
setblock 276 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Lagerkern"}','{"text": ""}','{"text": ""}']}}
fill 284 64 304 284 79 317 minecraft:light_gray_concrete
setblock 279 64 309 sophisticatedstorage:controller
setblock 277 64 309 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 278 64 309 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 280 64 309 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 278 65 309 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 279 65 309 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 280 65 309 sophisticatedstorage:barrel[facing=south,flat_top=false]
setblock 285 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.6"}','{"text": "storage"}','{"text": "vault_big"}','{"text": ""}']}}
setblock 286 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "großen Tresor"}','{"text": ""}','{"text": ""}']}}
fill 295 64 304 295 79 317 minecraft:light_gray_concrete
fill 287 64 308 292 66 310 create:item_vault[axis=x,large=false]
setblock 296 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "160.7"}','{"text": "storage"}','{"text": "trash"}','{"text": ""}']}}
setblock 297 64 316 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Mülleimer"}','{"text": ""}','{"text": ""}']}}
fill 305 64 304 305 79 317 minecraft:light_gray_concrete
setblock 300 64 309 trashcans:item_trash_can
setblock 300 65 309 minecraft:hopper[facing=down]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
