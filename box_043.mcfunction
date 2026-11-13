# 043 alfheim/open
#area 208 86 229 111
fill 208 64 86 229 91 111 minecraft:air
fill 208 60 86 229 62 111 minecraft:stone
fill 208 63 86 229 63 111 minecraft:light_gray_concrete
fill 212 64 92 229 79 92 minecraft:light_gray_concrete
fill 212 64 92 212 79 105 minecraft:light_gray_concrete
setblock 213 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "043"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 214 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 224 64 92 224 79 105 minecraft:light_gray_concrete
setblock 218 64 96 botania:elven_gateway_core
setblock 217 64 96 botania:livingwood_log[axis=x]
setblock 217 68 96 botania:livingwood_log[axis=x]
setblock 219 64 96 botania:livingwood_log[axis=x]
setblock 219 68 96 botania:livingwood_log[axis=x]
setblock 218 68 96 botania:glimmering_livingwood_log[axis=x]
setblock 216 65 96 botania:livingwood_log[axis=y]
setblock 216 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 216 67 96 botania:livingwood_log[axis=y]
setblock 220 65 96 botania:livingwood_log[axis=y]
setblock 220 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 220 67 96 botania:livingwood_log[axis=y]
setblock 214 64 98 botania:mana_pool{mana:1000000}
setblock 214 65 98 botania:natura_pylon
setblock 222 64 98 botania:mana_pool{mana:1000000}
setblock 222 65 98 botania:natura_pylon
kw testworld use 218 64 96 south botania:wand_of_the_forest
execute unless block 218 64 96 botania:elven_gateway_core[state=off]
