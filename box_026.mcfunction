# 026 ars_nouveau/chamber_auto
#area 28 67 47 92
fill 28 64 67 47 91 92 minecraft:air
fill 28 60 67 47 62 92 minecraft:stone
fill 28 63 67 47 63 92 minecraft:light_gray_concrete
fill 32 64 73 47 79 73 minecraft:light_gray_concrete
fill 32 64 73 32 79 86 minecraft:light_gray_concrete
setblock 33 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "026"}','{"text": "ars_nouveau"}','{"text": "chamber_auto"}','{"text": ""}']}}
setblock 34 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hoppers above"}','{"text": "and below a"}','{"text": "chamber feeding"}','{"text": "a chest"}']}}
fill 42 64 73 42 79 86 minecraft:light_gray_concrete
setblock 37 67 78 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:64}]}
setblock 37 66 78 minecraft:hopper[facing=down]
setblock 37 65 78 ars_nouveau:imbuement_chamber[facing=up]
setblock 37 64 78 minecraft:hopper[facing=east]
setblock 38 64 78 minecraft:chest[facing=south]{Items:[]}
setblock 35 64 78 ars_nouveau:source_jar[fill=11]{source:10000}
