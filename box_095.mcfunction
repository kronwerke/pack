# 095 alfheim/frame
#area 268 145 289 170
fill 268 64 145 289 91 170 minecraft:air
fill 268 60 145 289 62 170 minecraft:stone
fill 268 63 145 289 63 170 minecraft:light_gray_concrete
fill 272 64 151 289 79 151 minecraft:light_gray_concrete
fill 272 64 151 272 79 164 minecraft:light_gray_concrete
setblock 273 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 274 64 163 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 284 64 151 284 79 164 minecraft:light_gray_concrete
setblock 278 64 155 botania:elven_gateway_core
setblock 277 64 155 botania:livingwood_log[axis=x]
setblock 277 68 155 botania:livingwood_log[axis=x]
setblock 279 64 155 botania:livingwood_log[axis=x]
setblock 279 68 155 botania:livingwood_log[axis=x]
setblock 278 68 155 botania:glimmering_livingwood_log[axis=x]
setblock 276 65 155 botania:livingwood_log[axis=y]
setblock 276 66 155 botania:glimmering_livingwood_log[axis=y]
setblock 276 67 155 botania:livingwood_log[axis=y]
setblock 280 65 155 botania:livingwood_log[axis=y]
setblock 280 66 155 botania:glimmering_livingwood_log[axis=y]
setblock 280 67 155 botania:livingwood_log[axis=y]
setblock 274 64 157 botania:mana_pool{mana:1000000}
setblock 274 65 157 botania:natura_pylon
setblock 282 64 157 botania:mana_pool{mana:1000000}
setblock 282 65 157 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
