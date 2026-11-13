# 135 malum/altar, obelisk, crucible, healing_rite, quickening
#area 196 338 257 367
fill 196 64 338 229 95 367 minecraft:air
fill 230 64 338 257 95 367 minecraft:air
fill 196 60 338 257 62 367 minecraft:stone
fill 196 63 338 257 63 367 minecraft:light_gray_concrete
fill 200 64 344 257 83 344 minecraft:light_gray_concrete
fill 200 64 344 200 83 361 minecraft:light_gray_concrete
setblock 201 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.1"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 202 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 210 64 344 210 83 361 minecraft:light_gray_concrete
setblock 205 64 349 malum:spirit_altar
kw testworld use 205 64 349 south malum:runewood_planks
setblock 203 64 349 malum:runewood_planks
setblock 203 65 349 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 203 65 349 south malum:hallowed_gold_ingot
setblock 207 64 349 malum:runewood_planks
setblock 207 65 349 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 207 65 349 south malum:hallowed_gold_ingot
setblock 211 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.2"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 212 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 222 64 344 222 83 361 minecraft:light_gray_concrete
setblock 216 64 349 malum:spirit_altar
kw testworld use 216 64 349 south malum:runewood_planks
setblock 214 64 349 malum:runewood_planks
setblock 214 65 349 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 214 65 349 south malum:hallowed_gold_ingot
setblock 218 64 349 malum:runewood_planks
setblock 218 65 349 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 218 65 349 south malum:hallowed_gold_ingot
kw testworld use 213 63 347 up malum:runewood_obelisk
execute unless block 213 64 347 minecraft:air
kw testworld use 219 63 347 up malum:runewood_obelisk
execute unless block 219 64 347 minecraft:air
kw testworld use 213 63 351 up malum:runewood_obelisk
execute unless block 213 64 351 minecraft:air
kw testworld use 219 63 351 up malum:runewood_obelisk
execute unless block 219 64 351 minecraft:air
setblock 223 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.3"}','{"text": "malum"}','{"text": "crucible"}','{"text": ""}']}}
setblock 224 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Spirit"}','{"text": "Crucible"}','{"text": ""}','{"text": ""}']}}
fill 232 64 344 232 83 361 minecraft:light_gray_concrete
kw testworld use 227 63 349 up malum:spirit_crucible
setblock 233 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.4"}','{"text": "malum"}','{"text": "healing_rite"}','{"text": ""}']}}
setblock 234 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Healing"}','{"text": ""}','{"text": ""}']}}
fill 242 64 344 242 83 361 minecraft:light_gray_concrete
setblock 237 64 349 malum:runewood_totem_base
setblock 237 65 349 malum:runewood_log[axis=y]
kw testworld use 237 65 349 south malum:arcane_spirit
execute unless block 237 65 349 malum:runewood_log
setblock 237 66 349 malum:runewood_log[axis=y]
kw testworld use 237 66 349 south malum:sacred_spirit
execute unless block 237 66 349 malum:runewood_log
setblock 237 67 349 malum:runewood_log[axis=y]
kw testworld use 237 67 349 south malum:sacred_spirit
execute unless block 237 67 349 malum:runewood_log
setblock 243 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "135.5"}','{"text": "malum"}','{"text": "quickening"}','{"text": ""}']}}
setblock 244 64 360 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Quickening"}','{"text": ""}','{"text": ""}']}}
fill 252 64 344 252 83 361 minecraft:light_gray_concrete
setblock 247 64 348 malum:soulwood_totem_base
setblock 247 65 348 malum:soulwood_log[axis=y]
kw testworld use 247 65 348 south malum:eldritch_spirit
execute unless block 247 65 348 malum:soulwood_log
setblock 247 66 348 malum:soulwood_log[axis=y]
kw testworld use 247 66 348 south malum:arcane_spirit
execute unless block 247 66 348 malum:soulwood_log
setblock 247 67 348 malum:soulwood_log[axis=y]
kw testworld use 247 67 348 south malum:infernal_spirit
execute unless block 247 67 348 malum:soulwood_log
setblock 247 68 348 malum:soulwood_log[axis=y]
kw testworld use 247 68 348 south malum:infernal_spirit
execute unless block 247 68 348 malum:soulwood_log
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
