# 096 alfheim/open
#area 285 145 306 170
fill 285 64 145 306 91 170 minecraft:air
fill 285 60 145 306 62 170 minecraft:stone
fill 285 63 145 306 63 170 minecraft:light_gray_concrete
fill 289 64 151 306 79 151 minecraft:light_gray_concrete
fill 289 64 151 289 79 164 minecraft:light_gray_concrete
setblock 290 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 291 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 301 64 151 301 79 164 minecraft:light_gray_concrete
setblock 295 64 155 botania:elven_gateway_core
setblock 294 64 155 botania:livingwood_log[axis=x]
setblock 294 68 155 botania:livingwood_log[axis=x]
setblock 296 64 155 botania:livingwood_log[axis=x]
setblock 296 68 155 botania:livingwood_log[axis=x]
setblock 295 68 155 botania:glimmering_livingwood_log[axis=x]
setblock 293 65 155 botania:livingwood_log[axis=y]
setblock 293 66 155 botania:glimmering_livingwood_log[axis=y]
setblock 293 67 155 botania:livingwood_log[axis=y]
setblock 297 65 155 botania:livingwood_log[axis=y]
setblock 297 66 155 botania:glimmering_livingwood_log[axis=y]
setblock 297 67 155 botania:livingwood_log[axis=y]
setblock 291 64 157 botania:mana_pool{mana:1000000}
setblock 291 65 157 botania:natura_pylon
setblock 299 64 157 botania:mana_pool{mana:1000000}
setblock 299 65 157 botania:natura_pylon
kw testworld use 295 64 155 south botania:wand_of_the_forest
execute unless block 295 64 155 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
