# 083 alfheim/open
#area 270 109 291 134
fill 270 64 109 291 91 134 minecraft:air
fill 270 60 109 291 62 134 minecraft:stone
fill 270 63 109 291 63 134 minecraft:light_gray_concrete
fill 274 64 115 291 79 115 minecraft:light_gray_concrete
fill 274 64 115 274 79 128 minecraft:light_gray_concrete
setblock 275 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "083"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 276 64 127 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 286 64 115 286 79 128 minecraft:light_gray_concrete
setblock 280 64 119 botania:elven_gateway_core
setblock 279 64 119 botania:livingwood_log[axis=x]
setblock 279 68 119 botania:livingwood_log[axis=x]
setblock 281 64 119 botania:livingwood_log[axis=x]
setblock 281 68 119 botania:livingwood_log[axis=x]
setblock 280 68 119 botania:glimmering_livingwood_log[axis=x]
setblock 278 65 119 botania:livingwood_log[axis=y]
setblock 278 66 119 botania:glimmering_livingwood_log[axis=y]
setblock 278 67 119 botania:livingwood_log[axis=y]
setblock 282 65 119 botania:livingwood_log[axis=y]
setblock 282 66 119 botania:glimmering_livingwood_log[axis=y]
setblock 282 67 119 botania:livingwood_log[axis=y]
setblock 276 64 121 botania:mana_pool{mana:1000000}
setblock 276 65 121 botania:natura_pylon
setblock 284 64 121 botania:mana_pool{mana:1000000}
setblock 284 65 121 botania:natura_pylon
kw testworld use 280 64 119 south botania:wand_of_the_forest
execute unless block 280 64 119 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
