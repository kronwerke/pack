# 095 alfheim/frame
#area 268 143 289 168
fill 268 64 143 289 91 168 minecraft:air
fill 268 60 143 289 62 168 minecraft:stone
fill 268 63 143 289 63 168 minecraft:light_gray_concrete
fill 272 64 149 289 79 149 minecraft:light_gray_concrete
fill 272 64 149 272 79 162 minecraft:light_gray_concrete
setblock 273 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "095"}','{"text": "alfheim"}','{"text": "frame"}','{"text": ""}']}}
setblock 274 64 161 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the finished"}','{"text": "gateway with"}','{"text": "two pools and"}','{"text": "natura pylons"}']}}
fill 284 64 149 284 79 162 minecraft:light_gray_concrete
setblock 278 64 153 botania:elven_gateway_core
setblock 277 64 153 botania:livingwood_log[axis=x]
setblock 277 68 153 botania:livingwood_log[axis=x]
setblock 279 64 153 botania:livingwood_log[axis=x]
setblock 279 68 153 botania:livingwood_log[axis=x]
setblock 278 68 153 botania:glimmering_livingwood_log[axis=x]
setblock 276 65 153 botania:livingwood_log[axis=y]
setblock 276 66 153 botania:glimmering_livingwood_log[axis=y]
setblock 276 67 153 botania:livingwood_log[axis=y]
setblock 280 65 153 botania:livingwood_log[axis=y]
setblock 280 66 153 botania:glimmering_livingwood_log[axis=y]
setblock 280 67 153 botania:livingwood_log[axis=y]
setblock 274 64 155 botania:mana_pool{mana:1000000}
setblock 274 65 155 botania:natura_pylon
setblock 282 64 155 botania:mana_pool{mana:1000000}
setblock 282 65 155 botania:natura_pylon
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
