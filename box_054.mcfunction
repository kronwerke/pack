# 054 alfheim/open
#area 257 86 278 111
fill 257 64 86 278 91 111 minecraft:air
fill 257 60 86 278 62 111 minecraft:stone
fill 257 63 86 278 63 111 minecraft:light_gray_concrete
fill 261 64 92 278 79 92 minecraft:light_gray_concrete
fill 261 64 92 261 79 105 minecraft:light_gray_concrete
setblock 262 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "054"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 263 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 273 64 92 273 79 105 minecraft:light_gray_concrete
setblock 267 64 96 botania:elven_gateway_core
setblock 266 64 96 botania:livingwood_log[axis=x]
setblock 266 68 96 botania:livingwood_log[axis=x]
setblock 268 64 96 botania:livingwood_log[axis=x]
setblock 268 68 96 botania:livingwood_log[axis=x]
setblock 267 68 96 botania:glimmering_livingwood_log[axis=x]
setblock 265 65 96 botania:livingwood_log[axis=y]
setblock 265 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 265 67 96 botania:livingwood_log[axis=y]
setblock 269 65 96 botania:livingwood_log[axis=y]
setblock 269 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 269 67 96 botania:livingwood_log[axis=y]
setblock 263 64 98 botania:mana_pool{mana:1000000}
setblock 263 65 98 botania:natura_pylon
setblock 271 64 98 botania:mana_pool{mana:1000000}
setblock 271 65 98 botania:natura_pylon
kw testworld use 267 64 96 south botania:wand_of_the_forest
execute unless block 267 64 96 botania:elven_gateway_core[state=off]
