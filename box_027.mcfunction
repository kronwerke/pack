# 027 alfheim/open
#area 81 84 102 109
fill 81 64 84 102 91 109 minecraft:air
fill 81 60 84 102 62 109 minecraft:stone
fill 81 63 84 102 63 109 minecraft:light_gray_concrete
fill 85 64 90 102 79 90 minecraft:light_gray_concrete
fill 85 64 90 85 79 103 minecraft:light_gray_concrete
setblock 86 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "027"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 87 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 97 64 90 97 79 103 minecraft:light_gray_concrete
setblock 91 64 94 botania:elven_gateway_core
setblock 90 64 94 botania:livingwood_log[axis=x]
setblock 90 68 94 botania:livingwood_log[axis=x]
setblock 92 64 94 botania:livingwood_log[axis=x]
setblock 92 68 94 botania:livingwood_log[axis=x]
setblock 91 68 94 botania:glimmering_livingwood_log[axis=x]
setblock 89 65 94 botania:livingwood_log[axis=y]
setblock 89 66 94 botania:glimmering_livingwood_log[axis=y]
setblock 89 67 94 botania:livingwood_log[axis=y]
setblock 93 65 94 botania:livingwood_log[axis=y]
setblock 93 66 94 botania:glimmering_livingwood_log[axis=y]
setblock 93 67 94 botania:livingwood_log[axis=y]
setblock 87 64 96 botania:mana_pool{mana:1000000}
setblock 87 65 96 botania:natura_pylon
setblock 95 64 96 botania:mana_pool{mana:1000000}
setblock 95 65 96 botania:natura_pylon
kw testworld use 91 64 94 south botania:wand_of_the_forest
execute unless block 91 64 94 botania:elven_gateway_core[state=off]
