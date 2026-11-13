# 099 alfheim/open
#area 302 145 323 170
fill 302 64 145 323 91 170 minecraft:air
fill 302 60 145 323 62 170 minecraft:stone
fill 302 63 145 323 63 170 minecraft:light_gray_concrete
fill 306 64 151 323 79 151 minecraft:light_gray_concrete
fill 306 64 151 306 79 164 minecraft:light_gray_concrete
setblock 307 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 308 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 318 64 151 318 79 164 minecraft:light_gray_concrete
setblock 312 64 155 botania:elven_gateway_core
setblock 311 64 155 botania:livingwood_log[axis=x]
setblock 311 68 155 botania:livingwood_log[axis=x]
setblock 313 64 155 botania:livingwood_log[axis=x]
setblock 313 68 155 botania:livingwood_log[axis=x]
setblock 312 68 155 botania:glimmering_livingwood_log[axis=x]
setblock 310 65 155 botania:livingwood_log[axis=y]
setblock 310 66 155 botania:glimmering_livingwood_log[axis=y]
setblock 310 67 155 botania:livingwood_log[axis=y]
setblock 314 65 155 botania:livingwood_log[axis=y]
setblock 314 66 155 botania:glimmering_livingwood_log[axis=y]
setblock 314 67 155 botania:livingwood_log[axis=y]
setblock 308 64 157 botania:mana_pool{mana:1000000}
setblock 308 65 157 botania:natura_pylon
setblock 316 64 157 botania:mana_pool{mana:1000000}
setblock 316 65 157 botania:natura_pylon
kw testworld use 312 64 155 south botania:wand_of_the_forest
execute unless block 312 64 155 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
