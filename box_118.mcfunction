# 118 malum/altar, obelisk, crucible, healing_rite, quickening
#area 196 336 257 365
fill 196 64 336 229 95 365 minecraft:air
fill 230 64 336 257 95 365 minecraft:air
fill 196 60 336 257 62 365 minecraft:stone
fill 196 63 336 257 63 365 minecraft:light_gray_concrete
fill 200 64 342 257 83 342 minecraft:light_gray_concrete
fill 200 64 342 200 83 359 minecraft:light_gray_concrete
setblock 201 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.1"}','{"text": "malum"}','{"text": "altar"}','{"text": ""}']}}
setblock 202 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Spirit Altar"}','{"text": ""}','{"text": ""}']}}
fill 210 64 342 210 83 359 minecraft:light_gray_concrete
setblock 205 64 347 malum:spirit_altar
kw testworld use 205 64 347 south malum:runewood_planks
setblock 203 64 347 malum:runewood_planks
setblock 203 65 347 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 203 65 347 south malum:hallowed_gold_ingot
setblock 207 64 347 malum:runewood_planks
setblock 207 65 347 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 207 65 347 south malum:hallowed_gold_ingot
setblock 211 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.2"}','{"text": "malum"}','{"text": "obelisk"}','{"text": ""}']}}
setblock 212 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Runewood-Obelisken"}','{"text": "auf"}','{"text": ""}']}}
fill 222 64 342 222 83 359 minecraft:light_gray_concrete
setblock 216 64 347 malum:spirit_altar
kw testworld use 216 64 347 south malum:runewood_planks
setblock 214 64 347 malum:runewood_planks
setblock 214 65 347 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 214 65 347 south malum:hallowed_gold_ingot
setblock 218 64 347 malum:runewood_planks
setblock 218 65 347 malum:runewood_item_stand[facing=up,waterlogged=false]
kw testworld use 218 65 347 south malum:hallowed_gold_ingot
kw testworld use 213 63 345 up malum:runewood_obelisk
execute unless block 213 64 345 minecraft:air
kw testworld use 219 63 345 up malum:runewood_obelisk
execute unless block 219 64 345 minecraft:air
kw testworld use 213 63 349 up malum:runewood_obelisk
execute unless block 213 64 349 minecraft:air
kw testworld use 219 63 349 up malum:runewood_obelisk
execute unless block 219 64 349 minecraft:air
setblock 223 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.3"}','{"text": "malum"}','{"text": "crucible"}','{"text": ""}']}}
setblock 224 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau den Spirit"}','{"text": "Crucible"}','{"text": ""}','{"text": ""}']}}
fill 232 64 342 232 83 359 minecraft:light_gray_concrete
kw testworld use 227 63 347 up malum:spirit_crucible
setblock 233 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.4"}','{"text": "malum"}','{"text": "healing_rite"}','{"text": ""}']}}
setblock 234 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Healing"}','{"text": ""}','{"text": ""}']}}
fill 242 64 342 242 83 359 minecraft:light_gray_concrete
setblock 237 64 347 malum:runewood_totem_base
setblock 237 65 347 malum:runewood_log[axis=y]
kw testworld use 237 65 347 south malum:arcane_spirit
execute unless block 237 65 347 malum:runewood_log
setblock 237 66 347 malum:runewood_log[axis=y]
kw testworld use 237 66 347 south malum:sacred_spirit
execute unless block 237 66 347 malum:runewood_log
setblock 237 67 347 malum:runewood_log[axis=y]
kw testworld use 237 67 347 south malum:sacred_spirit
execute unless block 237 67 347 malum:runewood_log
setblock 243 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.5"}','{"text": "malum"}','{"text": "quickening"}','{"text": ""}']}}
setblock 244 64 358 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Zünde den Rite"}','{"text": "of Quickening"}','{"text": ""}','{"text": ""}']}}
fill 252 64 342 252 83 359 minecraft:light_gray_concrete
setblock 247 64 346 malum:soulwood_totem_base
setblock 247 65 346 malum:soulwood_log[axis=y]
kw testworld use 247 65 346 south malum:eldritch_spirit
execute unless block 247 65 346 malum:soulwood_log
setblock 247 66 346 malum:soulwood_log[axis=y]
kw testworld use 247 66 346 south malum:arcane_spirit
execute unless block 247 66 346 malum:soulwood_log
setblock 247 67 346 malum:soulwood_log[axis=y]
kw testworld use 247 67 346 south malum:infernal_spirit
execute unless block 247 67 346 malum:soulwood_log
setblock 247 68 346 malum:soulwood_log[axis=y]
kw testworld use 247 68 346 south malum:infernal_spirit
execute unless block 247 68 346 malum:soulwood_log
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
