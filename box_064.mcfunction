# 064 ars_nouveau/chamber_auto
#area 28 124 47 149
fill 28 64 124 47 91 149 minecraft:air
fill 28 60 124 47 62 149 minecraft:stone
fill 28 63 124 47 63 149 minecraft:light_gray_concrete
fill 32 64 130 47 79 130 minecraft:light_gray_concrete
fill 32 64 130 32 79 143 minecraft:light_gray_concrete
setblock 33 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "064"}','{"text": "ars_nouveau"}','{"text": "chamber_auto"}','{"text": ""}']}}
setblock 34 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hoppers above"}','{"text": "and below a"}','{"text": "chamber feeding"}','{"text": "a chest"}']}}
fill 42 64 130 42 79 143 minecraft:light_gray_concrete
setblock 37 67 135 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:64}]}
setblock 37 66 135 minecraft:hopper[facing=down]
setblock 37 65 135 ars_nouveau:imbuement_chamber[facing=up]
setblock 37 64 135 minecraft:hopper[facing=east]
setblock 38 64 135 minecraft:chest[facing=south]{Items:[]}
setblock 35 64 135 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
