# 055 ars_master/wilden_ritual
#area 165 88 184 113
fill 165 64 88 184 91 113 minecraft:air
fill 165 60 88 184 62 113 minecraft:stone
fill 165 63 88 184 63 113 minecraft:light_gray_concrete
fill 169 64 94 184 79 94 minecraft:light_gray_concrete
fill 169 64 94 169 79 107 minecraft:light_gray_concrete
setblock 170 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "055"}','{"text": "ars_master"}','{"text": "wilden_ritual"}','{"text": ""}']}}
setblock 171 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "brazier with"}','{"text": "spike, horn and"}','{"text": "wing"}','{"text": ""}']}}
fill 179 64 94 179 79 107 minecraft:light_gray_concrete
setblock 174 64 99 ars_nouveau:ritual_brazier
kw testworld use 174 64 99 up ars_nouveau:ritual_wilden_summon
setblock 172 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 172 64 99 south ars_nouveau:wilden_spike
setblock 176 64 99 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 176 64 99 south ars_nouveau:wilden_horn
setblock 174 64 97 ars_nouveau:arcane_pedestal[facing=up]
kw testworld use 174 64 97 south ars_nouveau:wilden_wing
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
