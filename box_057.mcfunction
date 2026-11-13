# 057 alfheim/open
#area 257 105 278 130
fill 257 64 105 278 91 130 minecraft:air
fill 257 60 105 278 62 130 minecraft:stone
fill 257 63 105 278 63 130 minecraft:light_gray_concrete
fill 261 64 111 278 79 111 minecraft:light_gray_concrete
fill 261 64 111 261 79 124 minecraft:light_gray_concrete
setblock 262 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "057"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 263 64 123 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 273 64 111 273 79 124 minecraft:light_gray_concrete
setblock 267 64 115 botania:elven_gateway_core
setblock 266 64 115 botania:livingwood_log[axis=x]
setblock 266 68 115 botania:livingwood_log[axis=x]
setblock 268 64 115 botania:livingwood_log[axis=x]
setblock 268 68 115 botania:livingwood_log[axis=x]
setblock 267 68 115 botania:glimmering_livingwood_log[axis=x]
setblock 265 65 115 botania:livingwood_log[axis=y]
setblock 265 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 265 67 115 botania:livingwood_log[axis=y]
setblock 269 65 115 botania:livingwood_log[axis=y]
setblock 269 66 115 botania:glimmering_livingwood_log[axis=y]
setblock 269 67 115 botania:livingwood_log[axis=y]
setblock 263 64 117 botania:mana_pool{mana:1000000}
setblock 263 65 117 botania:natura_pylon
setblock 271 64 117 botania:mana_pool{mana:1000000}
setblock 271 65 117 botania:natura_pylon
kw testworld use 267 64 115 south botania:wand_of_the_forest
execute unless block 267 64 115 botania:elven_gateway_core[state=off]
