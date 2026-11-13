# 025 ars_nouveau/chamber_auto
#area 11 67 30 92
fill 11 64 67 30 91 92 minecraft:air
fill 11 60 67 30 62 92 minecraft:stone
fill 11 63 67 30 63 92 minecraft:light_gray_concrete
fill 15 64 73 30 79 73 minecraft:light_gray_concrete
fill 15 64 73 15 79 86 minecraft:light_gray_concrete
setblock 16 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "ars_nouveau"}','{"text": "chamber_auto"}','{"text": ""}']}}
setblock 17 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hoppers above"}','{"text": "and below a"}','{"text": "chamber feeding"}','{"text": "a chest"}']}}
fill 25 64 73 25 79 86 minecraft:light_gray_concrete
setblock 20 67 78 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:64}]}
setblock 20 66 78 minecraft:hopper[facing=down]
setblock 20 65 78 ars_nouveau:imbuement_chamber[facing=up]
setblock 20 64 78 minecraft:hopper[facing=east]
setblock 21 64 78 minecraft:chest[facing=south]{Items:[]}
setblock 18 64 78 ars_nouveau:source_jar[fill=11]{source:10000}
