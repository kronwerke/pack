# 164 malum/spirits, altar, obelisk, crucible, healing_rite, quickening
#area 216 374 287 403
fill 216 64 374 249 95 403 minecraft:air
fill 250 64 374 283 95 403 minecraft:air
fill 284 64 374 287 95 403 minecraft:air
fill 216 60 374 287 62 403 minecraft:stone
fill 216 63 374 287 63 403 minecraft:light_gray_concrete
fill 220 64 380 287 83 380 minecraft:light_gray_concrete
fill 220 64 380 220 83 397 minecraft:light_gray_concrete
setblock 221 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.1"}','{"text": "malum"}','{"text": "spirits"}','{"text": ""}']}}
setblock 222 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Ernte die"}','{"text": "ersten Arcana"}','{"text": ""}','{"text": ""}']}}
fill 230 64 380 230 83 397 minecraft:light_gray_concrete
setblock 223 64 385 minecraft:smooth_stone_slab
summon item_display 223.5 64.95 385.5 {item:{id:"malum:sacred_spirit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 225 64 385 minecraft:smooth_stone_slab
summon item_display 225.5 64.95 385.5 {item:{id:"malum:wicked_spirit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 227 64 385 minecraft:smooth_stone_slab
summon item_display 227.5 64.95 385.5 {item:{id:"malum:arcane_spirit",count:1},item_display:"fixed",billboard:"vertical",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.0f,1.0f,1.0f]},brightness:{sky:15,block:15},Tags:["kw_shot"]}
setblock 231 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.2"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 232 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 240 64 380 240 83 397 minecraft:light_gray_concrete
setblock 235 64 385 malum:spirit_altar
kw testworld use 235 64 385 south malum:runewood_planks
setblock 233 64 385 malum:runewood_planks
setblock 233 65 385 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 233 65 385 south malum:hallowed_gold_ingot
setblock 237 64 385 malum:runewood_planks
setblock 237 65 385 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 237 65 385 south malum:hallowed_gold_ingot
setblock 241 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.3"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 242 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 252 64 380 252 83 397 minecraft:light_gray_concrete
setblock 246 64 385 malum:spirit_altar
kw testworld use 246 64 385 south malum:runewood_planks
setblock 244 64 385 malum:runewood_planks
setblock 244 65 385 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 244 65 385 south malum:hallowed_gold_ingot
setblock 248 64 385 malum:runewood_planks
setblock 248 65 385 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 248 65 385 south malum:hallowed_gold_ingot
kw testworld use 243 63 383 up malum:runewood_obelisk
execute unless block 243 64 383 minecraft:air
kw testworld use 249 63 383 up malum:runewood_obelisk
execute unless block 249 64 383 minecraft:air
kw testworld use 243 63 387 up malum:runewood_obelisk
execute unless block 243 64 387 minecraft:air
kw testworld use 249 63 387 up malum:runewood_obelisk
execute unless block 249 64 387 minecraft:air
setblock 253 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.4"}','{"text": "malum"}','{"text": "crucible"}','{"text": ""}']}}
setblock 254 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Spirit"}','{"text": "Crucible"}','{"text": ""}','{"text": ""}']}}
fill 262 64 380 262 83 397 minecraft:light_gray_concrete
kw testworld use 257 63 385 up malum:spirit_crucible
setblock 263 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.5"}','{"text": "malum"}','{"text": "healing_rite"}','{"text": ""}']}}
setblock 264 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Healing"}','{"text": ""}','{"text": ""}']}}
fill 272 64 380 272 83 397 minecraft:light_gray_concrete
setblock 267 64 385 malum:runewood_totem_base
setblock 267 65 385 malum:runewood_log[axis=y]
kw testworld use 267 65 385 south malum:arcane_spirit
execute unless block 267 65 385 malum:runewood_log
setblock 267 66 385 malum:runewood_log[axis=y]
kw testworld use 267 66 385 south malum:sacred_spirit
execute unless block 267 66 385 malum:runewood_log
setblock 267 67 385 malum:runewood_log[axis=y]
kw testworld use 267 67 385 south malum:sacred_spirit
execute unless block 267 67 385 malum:runewood_log
setblock 273 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164.6"}','{"text": "malum"}','{"text": "quickening"}','{"text": ""}']}}
setblock 274 64 396 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Quickening"}','{"text": ""}','{"text": ""}']}}
fill 282 64 380 282 83 397 minecraft:light_gray_concrete
setblock 277 64 384 malum:soulwood_totem_base
setblock 277 65 384 malum:soulwood_log[axis=y]
kw testworld use 277 65 384 south malum:eldritch_spirit
execute unless block 277 65 384 malum:soulwood_log
setblock 277 66 384 malum:soulwood_log[axis=y]
kw testworld use 277 66 384 south malum:arcane_spirit
execute unless block 277 66 384 malum:soulwood_log
setblock 277 67 384 malum:soulwood_log[axis=y]
kw testworld use 277 67 384 south malum:infernal_spirit
execute unless block 277 67 384 malum:soulwood_log
setblock 277 68 384 malum:soulwood_log[axis=y]
kw testworld use 277 68 384 south malum:infernal_spirit
execute unless block 277 68 384 malum:soulwood_log
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
