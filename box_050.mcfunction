# 050 ars_nouveau/fill_jar
#area 11 88 32 113
fill 11 64 88 32 91 113 minecraft:air
fill 11 60 88 32 62 113 minecraft:stone
fill 11 63 88 32 63 113 minecraft:light_gray_concrete
fill 15 64 94 32 79 94 minecraft:light_gray_concrete
fill 15 64 94 15 79 107 minecraft:light_gray_concrete
setblock 16 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "ars_nouveau"}','{"text": "fill_jar"}','{"text": ""}']}}
setblock 17 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "volcanic"}','{"text": "sourcelink, jar"}','{"text": "and chamber"}','{"text": "within range,"}']}}
setblock 18 64 106 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "logs on the"}','{"text": "ground"}','{"text": ""}','{"text": ""}']}}
fill 27 64 94 27 79 107 minecraft:light_gray_concrete
setblock 18 64 99 ars_nouveau:volcanic_sourcelink
summon item 19.5 64.2 100.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 18.5 64.2 100.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 17.5 64.2 100.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 19.5 64.2 99.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 22 64 99 ars_nouveau:source_jar[fill=5]{source:5000}
setblock 24 64 99 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 24 64 99 south minecraft:amethyst_shard
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
