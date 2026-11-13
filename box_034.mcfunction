# 034 alfheim/open
#area 156 84 177 109
fill 156 64 84 177 91 109 minecraft:air
fill 156 60 84 177 62 109 minecraft:stone
fill 156 63 84 177 63 109 minecraft:light_gray_concrete
fill 160 64 90 177 79 90 minecraft:light_gray_concrete
fill 160 64 90 160 79 103 minecraft:light_gray_concrete
setblock 161 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 162 64 102 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 172 64 90 172 79 103 minecraft:light_gray_concrete
setblock 166 64 94 botania:elven_gateway_core
setblock 165 64 94 botania:livingwood_log[axis=x]
setblock 165 68 94 botania:livingwood_log[axis=x]
setblock 167 64 94 botania:livingwood_log[axis=x]
setblock 167 68 94 botania:livingwood_log[axis=x]
setblock 166 68 94 botania:glimmering_livingwood_log[axis=x]
setblock 164 65 94 botania:livingwood_log[axis=y]
setblock 164 66 94 botania:glimmering_livingwood_log[axis=y]
setblock 164 67 94 botania:livingwood_log[axis=y]
setblock 168 65 94 botania:livingwood_log[axis=y]
setblock 168 66 94 botania:glimmering_livingwood_log[axis=y]
setblock 168 67 94 botania:livingwood_log[axis=y]
setblock 162 64 96 botania:mana_pool{mana:1000000}
setblock 162 65 96 botania:natura_pylon
setblock 170 64 96 botania:mana_pool{mana:1000000}
setblock 170 65 96 botania:natura_pylon
kw testworld use 166 64 94 south botania:wand_of_the_forest
execute unless block 166 64 94 botania:elven_gateway_core[state=off]
