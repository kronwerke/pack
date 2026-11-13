# 033 ars_nouveau/imbuement
#area -4 86 15 111
fill -4 64 86 15 91 111 minecraft:air
fill -4 60 86 15 62 111 minecraft:stone
fill -4 63 86 15 63 111 minecraft:light_gray_concrete
fill 0 64 92 15 79 92 minecraft:light_gray_concrete
fill 0 64 92 0 79 105 minecraft:light_gray_concrete
setblock 1 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "033"}','{"text": "ars_nouveau"}','{"text": "imbuement"}','{"text": ""}']}}
setblock 2 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "the chamber"}','{"text": "with an"}','{"text": "amethyst shard,"}','{"text": "then with a"}']}}
setblock 3 64 104 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "finished gem"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 10 64 92 10 79 105 minecraft:light_gray_concrete
setblock 5 64 97 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 5 64 97 south minecraft:amethyst_shard
setblock 7 64 97 ars_nouveau:source_jar[fill=11]{source:10000}
