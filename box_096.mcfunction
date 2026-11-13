# 096 alfheim/open
#area 285 143 306 168
fill 285 64 143 306 91 168 minecraft:air
fill 285 60 143 306 62 168 minecraft:stone
fill 285 63 143 306 63 168 minecraft:light_gray_concrete
fill 289 64 149 306 79 149 minecraft:light_gray_concrete
fill 289 64 149 289 79 162 minecraft:light_gray_concrete
setblock 290 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "096"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 291 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 301 64 149 301 79 162 minecraft:light_gray_concrete
setblock 295 64 153 botania:elven_gateway_core
setblock 294 64 153 botania:livingwood_log[axis=x]
setblock 294 68 153 botania:livingwood_log[axis=x]
setblock 296 64 153 botania:livingwood_log[axis=x]
setblock 296 68 153 botania:livingwood_log[axis=x]
setblock 295 68 153 botania:glimmering_livingwood_log[axis=x]
setblock 293 65 153 botania:livingwood_log[axis=y]
setblock 293 66 153 botania:glimmering_livingwood_log[axis=y]
setblock 293 67 153 botania:livingwood_log[axis=y]
setblock 297 65 153 botania:livingwood_log[axis=y]
setblock 297 66 153 botania:glimmering_livingwood_log[axis=y]
setblock 297 67 153 botania:livingwood_log[axis=y]
setblock 291 64 155 botania:mana_pool{mana:1000000}
setblock 291 65 155 botania:natura_pylon
setblock 299 64 155 botania:mana_pool{mana:1000000}
setblock 299 65 155 botania:natura_pylon
kw testworld use 295 64 153 south botania:wand_of_the_forest
execute unless block 295 64 153 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
