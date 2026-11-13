# 061 ars_nouveau/imbuement
#area -4 122 15 147
fill -4 64 122 15 91 147 minecraft:air
fill -4 60 122 15 62 147 minecraft:stone
fill -4 63 122 15 63 147 minecraft:light_gray_concrete
fill 0 64 128 15 79 128 minecraft:light_gray_concrete
fill 0 64 128 0 79 141 minecraft:light_gray_concrete
setblock 1 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "061"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 140 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 128 10 79 141 minecraft:light_gray_concrete
setblock 5 64 133 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 133 south minecraft:amethyst_shard
setblock 7 64 133 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
