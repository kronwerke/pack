# 063 alfheim/open
#area 270 105 291 130
fill 270 64 105 291 91 130 minecraft:air
fill 270 60 105 291 62 130 minecraft:stone
fill 270 63 105 291 63 130 minecraft:light_gray_concrete
fill 274 64 111 291 79 111 minecraft:light_gray_concrete
fill 274 64 111 274 79 124 minecraft:light_gray_concrete
setblock 275 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 276 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 286 64 111 286 79 124 minecraft:light_gray_concrete
setblock 280 64 115 botania:elven_gateway_core
setblock 279 64 115 botania:livingwood_log[axis=x]
setblock 279 68 115 botania:livingwood_log[axis=x]
setblock 281 64 115 botania:livingwood_log[axis=x]
setblock 281 68 115 botania:livingwood_log[axis=x]
setblock 280 68 115 botania:glimmering_livingwood_log[axis=x]
setblock 278 65 115 botania:livingwood_log[axis=y]
setblock 278 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 278 67 115 botania:livingwood_log[axis=y]
setblock 282 65 115 botania:livingwood_log[axis=y]
setblock 282 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 282 67 115 botania:livingwood_log[axis=y]
setblock 276 64 117 botania:mana_pool{mana:1000000}
setblock 276 65 117 botania:natura_pylon
setblock 284 64 117 botania:mana_pool{mana:1000000}
setblock 284 65 117 botania:natura_pylon
kw testworld use 280 64 115 south botania:wand_of_the_forest
execute unless block 280 64 115 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
