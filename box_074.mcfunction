# 074 ars_master/wilden_ritual
#area 197 122 216 147
fill 197 64 122 216 91 147 minecraft:air
fill 197 60 122 216 62 147 minecraft:stone
fill 197 63 122 216 63 147 minecraft:light_gray_concrete
fill 201 64 128 216 79 128 minecraft:light_gray_concrete
fill 201 64 128 201 79 141 minecraft:light_gray_concrete
setblock 202 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "074"}','{"text": "ars_master"}','{"text": "wilden_ritual"}','{"text": ""}']}}
setblock 203 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "brazier with"}','{"text": "spike, horn and"}','{"text": "wing"}','{"text": ""}']}}
fill 211 64 128 211 79 141 minecraft:light_gray_concrete
setblock 206 64 133 ars_nouveau:ritual_brazier
kw testworld use 206 64 133 up ars_nouveau:ritual_wilden_summon
setblock 204 64 133 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 204 64 133 south ars_nouveau:wilden_spike
setblock 208 64 133 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 208 64 133 south ars_nouveau:wilden_horn
setblock 206 64 131 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 206 64 131 south ars_nouveau:wilden_wing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
