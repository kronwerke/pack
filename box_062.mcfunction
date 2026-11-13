# 062 ars_nouveau/imbuement
#area -4 124 15 149
fill -4 64 124 15 91 149 minecraft:air
fill -4 60 124 15 62 149 minecraft:stone
fill -4 63 124 15 63 149 minecraft:light_gray_concrete
fill 0 64 130 15 79 130 minecraft:light_gray_concrete
fill 0 64 130 0 79 143 minecraft:light_gray_concrete
setblock 1 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "062"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 130 10 79 143 minecraft:light_gray_concrete
setblock 5 64 135 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 135 south minecraft:amethyst_shard
setblock 7 64 135 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
