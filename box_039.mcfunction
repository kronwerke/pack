# 039 alfheim/open
#area 189 86 210 111
fill 189 64 86 210 91 111 minecraft:air
fill 189 60 86 210 62 111 minecraft:stone
fill 189 63 86 210 63 111 minecraft:light_gray_concrete
fill 193 64 92 210 79 92 minecraft:light_gray_concrete
fill 193 64 92 193 79 105 minecraft:light_gray_concrete
setblock 194 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "039"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 195 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 205 64 92 205 79 105 minecraft:light_gray_concrete
setblock 199 64 96 botania:elven_gateway_core
setblock 198 64 96 botania:livingwood_log[axis=x]
setblock 198 68 96 botania:livingwood_log[axis=x]
setblock 200 64 96 botania:livingwood_log[axis=x]
setblock 200 68 96 botania:livingwood_log[axis=x]
setblock 199 68 96 botania:glimmering_livingwood_log[axis=x]
setblock 197 65 96 botania:livingwood_log[axis=y]
setblock 197 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 197 67 96 botania:livingwood_log[axis=y]
setblock 201 65 96 botania:livingwood_log[axis=y]
setblock 201 66 96 botania:glimmering_livingwood_log[axis=y]
setblock 201 67 96 botania:livingwood_log[axis=y]
setblock 195 64 98 botania:mana_pool{mana:1000000}
setblock 195 65 98 botania:natura_pylon
setblock 203 64 98 botania:mana_pool{mana:1000000}
setblock 203 65 98 botania:natura_pylon
kw testworld use 199 64 96 south botania:wand_of_the_forest
execute unless block 199 64 96 botania:elven_gateway_core[state=off]
