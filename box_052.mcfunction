# 052 ars_nouveau/chamber_auto
#area 28 88 47 113
fill 28 64 88 47 91 113 minecraft:air
fill 28 60 88 47 62 113 minecraft:stone
fill 28 63 88 47 63 113 minecraft:light_gray_concrete
fill 32 64 94 47 79 94 minecraft:light_gray_concrete
fill 32 64 94 32 79 107 minecraft:light_gray_concrete
setblock 33 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "052"}','{"text": "ars_nouveau"}','{"text": "chamber_auto"}','{"text": ""}']}}
setblock 34 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hoppers above"}','{"text": "and below a"}','{"text": "chamber feeding"}','{"text": "a chest"}']}}
fill 42 64 94 42 79 107 minecraft:light_gray_concrete
setblock 37 67 99 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:64}]}
setblock 37 66 99 minecraft:hopper[facing=down]
setblock 37 65 99 ars_nouveau:imbuement_chamber[facing=up]
setblock 37 64 99 minecraft:hopper[facing=east]
setblock 38 64 99 minecraft:chest[facing=south]{Items:[]}
setblock 35 64 99 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
