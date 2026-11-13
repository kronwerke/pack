# 049 alfheim/open
#area 242 86 263 111
fill 242 64 86 263 91 111 minecraft:air
fill 242 60 86 263 62 111 minecraft:stone
fill 242 63 86 263 63 111 minecraft:light_gray_concrete
fill 246 64 92 263 79 92 minecraft:light_gray_concrete
fill 246 64 92 246 79 105 minecraft:light_gray_concrete
setblock 247 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "049"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 248 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 258 64 92 258 79 105 minecraft:light_gray_concrete
setblock 252 64 96 botania:elven_gateway_core
setblock 251 64 96 botania:livingwood_log[axis=x]
setblock 251 68 96 botania:livingwood_log[axis=x]
setblock 253 64 96 botania:livingwood_log[axis=x]
setblock 253 68 96 botania:livingwood_log[axis=x]
setblock 252 68 96 botania:glimmering_livingwood_log[axis=x]
setblock 250 65 96 botania:livingwood_log[axis=y]
setblock 250 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 250 67 96 botania:livingwood_log[axis=y]
setblock 254 65 96 botania:livingwood_log[axis=y]
setblock 254 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 254 67 96 botania:livingwood_log[axis=y]
setblock 248 64 98 botania:mana_pool{mana:1000000}
setblock 248 65 98 botania:natura_pylon
setblock 256 64 98 botania:mana_pool{mana:1000000}
setblock 256 65 98 botania:natura_pylon
kw testworld use 252 64 96 south botania:wand_of_the_forest
execute unless block 252 64 96 botania:elven_gateway_core[state=off]
