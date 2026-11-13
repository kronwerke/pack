# 188 malum/spirits, altar, obelisk, crucible, healing_rite, quickening
#area 226 407 297 436
fill 226 64 407 259 95 436 minecraft:air
fill 260 64 407 293 95 436 minecraft:air
fill 294 64 407 297 95 436 minecraft:air
fill 226 60 407 297 62 436 minecraft:stone
fill 226 63 407 297 63 436 minecraft:light_gray_concrete
fill 230 64 413 297 83 413 minecraft:light_gray_concrete
fill 230 64 413 230 83 430 minecraft:light_gray_concrete
setblock 231 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "188.1"}','{"text": "malum"}','{"text": "spirits"}','{"text": ""}']}}
setblock 232 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ernte die"}','{"text": "ersten Arcana"}','{"text": ""}','{"text": ""}']}}
fill 240 64 413 240 83 430 minecraft:light_gray_concrete
setblock 233 64 418 minecraft:smooth_stone_slab
summon item_display 233.5 64.95 418.5 {item:{id:"malum:sacred_spirit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 235 64 418 minecraft:smooth_stone_slab
summon item_display 235.5 64.95 418.5 {item:{id:"malum:wicked_spirit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 237 64 418 minecraft:smooth_stone_slab
summon item_display 237.5 64.95 418.5 {item:{id:"malum:arcane_spirit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 241 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "188.2"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 242 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 250 64 413 250 83 430 minecraft:light_gray_concrete
setblock 245 64 418 malum:spirit_altar
kw testworld use 245 64 418 south malum:runewood_planks
setblock 243 64 418 malum:runewood_planks
setblock 243 65 418 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 243 65 418 south malum:hallowed_gold_ingot
setblock 247 64 418 malum:runewood_planks
setblock 247 65 418 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 247 65 418 south malum:hallowed_gold_ingot
setblock 251 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "188.3"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 252 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 262 64 413 262 83 430 minecraft:light_gray_concrete
setblock 256 64 418 malum:spirit_altar
kw testworld use 256 64 418 south malum:runewood_planks
setblock 254 64 418 malum:runewood_planks
setblock 254 65 418 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 254 65 418 south malum:hallowed_gold_ingot
setblock 258 64 418 malum:runewood_planks
setblock 258 65 418 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 258 65 418 south malum:hallowed_gold_ingot
kw testworld use 253 63 416 up malum:runewood_obelisk
execute unless block 253 64 416 minecraft:air
kw testworld use 259 63 416 up malum:runewood_obelisk
execute unless block 259 64 416 minecraft:air
kw testworld use 253 63 420 up malum:runewood_obelisk
execute unless block 253 64 420 minecraft:air
kw testworld use 259 63 420 up malum:runewood_obelisk
execute unless block 259 64 420 minecraft:air
setblock 263 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "188.4"}','{"text": "malum"}','{"text": "crucible"}','{"text": ""}']}}
setblock 264 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Spirit"}','{"text": "Crucible"}','{"text": ""}','{"text": ""}']}}
fill 272 64 413 272 83 430 minecraft:light_gray_concrete
kw testworld use 267 63 418 up malum:spirit_crucible
setblock 273 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "188.5"}','{"text": "malum"}','{"text": "healing_rite"}','{"text": ""}']}}
setblock 274 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Healing"}','{"text": ""}','{"text": ""}']}}
fill 282 64 413 282 83 430 minecraft:light_gray_concrete
setblock 277 64 418 malum:runewood_totem_base
setblock 277 65 418 malum:runewood_log[axis=y]
kw testworld use 277 65 418 south malum:arcane_spirit
execute unless block 277 65 418 malum:runewood_log
setblock 277 66 418 malum:runewood_log[axis=y]
kw testworld use 277 66 418 south malum:sacred_spirit
execute unless block 277 66 418 malum:runewood_log
setblock 277 67 418 malum:runewood_log[axis=y]
kw testworld use 277 67 418 south malum:sacred_spirit
execute unless block 277 67 418 malum:runewood_log
setblock 283 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "188.6"}','{"text": "malum"}','{"text": "quickening"}','{"text": ""}']}}
setblock 284 64 429 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Quickening"}','{"text": ""}','{"text": ""}']}}
fill 292 64 413 292 83 430 minecraft:light_gray_concrete
setblock 287 64 417 malum:soulwood_totem_base
setblock 287 65 417 malum:soulwood_log[axis=y]
kw testworld use 287 65 417 south malum:eldritch_spirit
execute unless block 287 65 417 malum:soulwood_log
setblock 287 66 417 malum:soulwood_log[axis=y]
kw testworld use 287 66 417 south malum:arcane_spirit
execute unless block 287 66 417 malum:soulwood_log
setblock 287 67 417 malum:soulwood_log[axis=y]
kw testworld use 287 67 417 south malum:infernal_spirit
execute unless block 287 67 417 malum:soulwood_log
setblock 287 68 417 malum:soulwood_log[axis=y]
kw testworld use 287 68 417 south malum:infernal_spirit
execute unless block 287 68 417 malum:soulwood_log
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
