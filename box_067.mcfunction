# 067 ars_nouveau/imbuement
#area -4 126 15 151
fill -4 64 126 15 91 151 minecraft:air
fill -4 60 126 15 62 151 minecraft:stone
fill -4 63 126 15 63 151 minecraft:light_gray_concrete
fill 0 64 132 15 79 132 minecraft:light_gray_concrete
fill 0 64 132 0 79 145 minecraft:light_gray_concrete
setblock 1 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "067"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 132 10 79 145 minecraft:light_gray_concrete
setblock 5 64 137 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 137 south minecraft:amethyst_shard
setblock 7 64 137 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
