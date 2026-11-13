# 095 alfheim/open
#area 270 139 291 164
fill 270 64 139 291 91 164 minecraft:air
fill 270 60 139 291 62 164 minecraft:stone
fill 270 63 139 291 63 164 minecraft:light_gray_concrete
fill 274 64 145 291 79 145 minecraft:light_gray_concrete
fill 274 64 145 274 79 158 minecraft:light_gray_concrete
setblock 275 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 276 64 157 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 286 64 145 286 79 158 minecraft:light_gray_concrete
setblock 280 64 149 botania:elven_gateway_core
setblock 279 64 149 botania:livingwood_log[axis=x]
setblock 279 68 149 botania:livingwood_log[axis=x]
setblock 281 64 149 botania:livingwood_log[axis=x]
setblock 281 68 149 botania:livingwood_log[axis=x]
setblock 280 68 149 botania:glimmering_livingwood_log[axis=x]
setblock 278 65 149 botania:livingwood_log[axis=y]
setblock 278 66 149 botania:glimmering_livingwood_log[axis=y]
setblock 278 67 149 botania:livingwood_log[axis=y]
setblock 282 65 149 botania:livingwood_log[axis=y]
setblock 282 66 149 botania:glimmering_livingwood_log[axis=y]
setblock 282 67 149 botania:livingwood_log[axis=y]
setblock 276 64 151 botania:mana_pool{mana:1000000}
setblock 276 65 151 botania:natura_pylon
setblock 284 64 151 botania:mana_pool{mana:1000000}
setblock 284 65 151 botania:natura_pylon
kw testworld use 280 64 149 south botania:wand_of_the_forest
execute unless block 280 64 149 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
