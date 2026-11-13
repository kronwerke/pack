# 108 alfheim/open
#area 315 147 336 172
fill 315 64 147 336 91 172 minecraft:air
fill 315 60 147 336 62 172 minecraft:stone
fill 315 63 147 336 63 172 minecraft:light_gray_concrete
fill 319 64 153 336 79 153 minecraft:light_gray_concrete
fill 319 64 153 319 79 166 minecraft:light_gray_concrete
setblock 320 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "108"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 321 64 165 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 331 64 153 331 79 166 minecraft:light_gray_concrete
setblock 325 64 157 botania:elven_gateway_core
setblock 324 64 157 botania:livingwood_log[axis=x]
setblock 324 68 157 botania:livingwood_log[axis=x]
setblock 326 64 157 botania:livingwood_log[axis=x]
setblock 326 68 157 botania:livingwood_log[axis=x]
setblock 325 68 157 botania:glimmering_livingwood_log[axis=x]
setblock 323 65 157 botania:livingwood_log[axis=y]
setblock 323 66 157 botania:glimmering_livingwood_log[axis=y]
setblock 323 67 157 botania:livingwood_log[axis=y]
setblock 327 65 157 botania:livingwood_log[axis=y]
setblock 327 66 157 botania:glimmering_livingwood_log[axis=y]
setblock 327 67 157 botania:livingwood_log[axis=y]
setblock 321 64 159 botania:mana_pool{mana:1000000}
setblock 321 65 159 botania:natura_pylon
setblock 329 64 159 botania:mana_pool{mana:1000000}
setblock 329 65 159 botania:natura_pylon
kw testworld use 325 64 157 south botania:wand_of_the_forest
execute unless block 325 64 157 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
