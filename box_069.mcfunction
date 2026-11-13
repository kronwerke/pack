# 069 ars_nouveau/chamber_auto
#area 28 126 47 151
fill 28 64 126 47 91 151 minecraft:air
fill 28 60 126 47 62 151 minecraft:stone
fill 28 63 126 47 63 151 minecraft:light_gray_concrete
fill 32 64 132 47 79 132 minecraft:light_gray_concrete
fill 32 64 132 32 79 145 minecraft:light_gray_concrete
setblock 33 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069"}','{"text": "ars_nouveau"}','{"text": "chamber_auto"}','{"text": ""}']}}
setblock 34 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "hoppers above"}','{"text": "and below a"}','{"text": "chamber feeding"}','{"text": "a chest"}']}}
fill 42 64 132 42 79 145 minecraft:light_gray_concrete
setblock 37 67 137 minecraft:chest[facing=south]{Items:[{Slot:0b,id:"minecraft:amethyst_shard",count:64}]}
setblock 37 66 137 minecraft:hopper[facing=down]
setblock 37 65 137 ars_nouveau:imbuement_chamber[facing=up]
setblock 37 64 137 minecraft:hopper[facing=east]
setblock 38 64 137 minecraft:chest[facing=south]{Items:[]}
setblock 35 64 137 ars_nouveau:source_jar[fill=11]{source:10000}
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
