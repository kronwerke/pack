# 060 ars_master/wilden_ritual
#area 195 88 214 113
fill 195 64 88 214 91 113 minecraft:air
fill 195 60 88 214 62 113 minecraft:stone
fill 195 63 88 214 63 113 minecraft:light_gray_concrete
fill 199 64 94 214 79 94 minecraft:light_gray_concrete
fill 199 64 94 199 79 107 minecraft:light_gray_concrete
setblock 200 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "060"}','{"text": "ars_master"}','{"text": "wilden_ritual"}','{"text": ""}']}}
setblock 201 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "brazier with"}','{"text": "spike, horn and"}','{"text": "wing"}','{"text": ""}']}}
fill 209 64 94 209 79 107 minecraft:light_gray_concrete
setblock 204 64 99 ars_nouveau:ritual_brazier
kw testworld use 204 64 99 up ars_nouveau:ritual_wilden_summon
setblock 202 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 202 64 99 south ars_nouveau:wilden_spike
setblock 206 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 206 64 99 south ars_nouveau:wilden_horn
setblock 204 64 97 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 204 64 97 south ars_nouveau:wilden_wing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
