# 063 ars_nouveau/chamber_auto
#area 28 118 47 143
fill 28 64 118 47 91 143 minecraft:air
fill 28 60 118 47 62 143 minecraft:stone
fill 28 63 118 47 63 143 minecraft:light_gray_concrete
fill 32 64 124 47 79 124 minecraft:light_gray_concrete
fill 32 64 124 32 79 137 minecraft:light_gray_concrete
setblock 33 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "ars_nouveau"}','{"text": "chamber_auto"}','{"text": ""}']}}
setblock 34 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hoppers above"}','{"text": "and below a"}','{"text": "chamber feeding"}','{"text": "a chest"}']}}
fill 42 64 124 42 79 137 minecraft:light_gray_concrete
setblock 37 67 129 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:64}]}
setblock 37 66 129 minecraft:hopper[facing=down]
setblock 37 65 129 ars_nouveau:imbuement_chamber[facing=up]
setblock 37 64 129 minecraft:hopper[facing=east]
setblock 38 64 129 minecraft:chest[facing=south]{Items:[]}
setblock 35 64 129 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
