# 068 ars_nouveau/fill_jar
#area 11 126 32 151
fill 11 64 126 32 91 151 minecraft:air
fill 11 60 126 32 62 151 minecraft:stone
fill 11 63 126 32 63 151 minecraft:light_gray_concrete
fill 15 64 132 32 79 132 minecraft:light_gray_concrete
fill 15 64 132 15 79 145 minecraft:light_gray_concrete
setblock 16 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "068"}','{"text": "ars_nouveau"}','{"text": "fill_jar"}','{"text": ""}']}}
setblock 17 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "volcanic"}','{"text": "sourcelink, jar"}','{"text": "and chamber"}','{"text": "within range,"}']}}
setblock 18 64 144 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "logs on the"}','{"text": "ground"}','{"text": ""}','{"text": ""}']}}
fill 27 64 132 27 79 145 minecraft:light_gray_concrete
setblock 18 64 137 ars_nouveau:volcanic_sourcelink
summon item 19.5 64.2 138.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 18.5 64.2 138.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 17.5 64.2 138.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 19.5 64.2 137.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 22 64 137 ars_nouveau:source_jar[fill=5]{source:5000}
setblock 24 64 137 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 24 64 137 south minecraft:amethyst_shard
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
