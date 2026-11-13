# 072 alfheim/open
#area 270 107 291 132
fill 270 64 107 291 91 132 minecraft:air
fill 270 60 107 291 62 132 minecraft:stone
fill 270 63 107 291 63 132 minecraft:light_gray_concrete
fill 274 64 113 291 79 113 minecraft:light_gray_concrete
fill 274 64 113 274 79 126 minecraft:light_gray_concrete
setblock 275 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "072"}','{"text": "alfheim"}','{"text": "open"}','{"text": ""}']}}
setblock 276 64 125 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the open portal"}','{"text": "with an item"}','{"text": "flying out"}','{"text": ""}']}}
fill 286 64 113 286 79 126 minecraft:light_gray_concrete
setblock 280 64 117 botania:elven_gateway_core
setblock 279 64 117 botania:livingwood_log[axis=x]
setblock 279 68 117 botania:livingwood_log[axis=x]
setblock 281 64 117 botania:livingwood_log[axis=x]
setblock 281 68 117 botania:livingwood_log[axis=x]
setblock 280 68 117 botania:glimmering_livingwood_log[axis=x]
setblock 278 65 117 botania:livingwood_log[axis=y]
setblock 278 66 117 botania:glimmering_livingwood_log[axis=y]
setblock 278 67 117 botania:livingwood_log[axis=y]
setblock 282 65 117 botania:livingwood_log[axis=y]
setblock 282 66 117 botania:glimmering_livingwood_log[axis=y]
setblock 282 67 117 botania:livingwood_log[axis=y]
setblock 276 64 119 botania:mana_pool{mana:1000000}
setblock 276 65 119 botania:natura_pylon
setblock 284 64 119 botania:mana_pool{mana:1000000}
setblock 284 65 119 botania:natura_pylon
kw testworld use 280 64 117 south botania:wand_of_the_forest
execute unless block 280 64 117 botania:elven_gateway_core[state=off]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
