# 031 ars_nouveau/fill_jar
#area 11 67 32 92
fill 11 64 67 32 91 92 minecraft:air
fill 11 60 67 32 62 92 minecraft:stone
fill 11 63 67 32 63 92 minecraft:light_gray_concrete
fill 15 64 73 32 79 73 minecraft:light_gray_concrete
fill 15 64 73 15 79 86 minecraft:light_gray_concrete
setblock 16 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "031"}','{"text": "ars_nouveau"}','{"text": "fill_jar"}','{"text": ""}']}}
setblock 17 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "volcanic"}','{"text": "sourcelink, jar"}','{"text": "and chamber"}','{"text": "within range,"}']}}
setblock 18 64 85 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "logs on the"}','{"text": "ground"}','{"text": ""}','{"text": ""}']}}
fill 27 64 73 27 79 86 minecraft:light_gray_concrete
setblock 18 64 78 ars_nouveau:volcanic_sourcelink
summon item 19.5 64.2 79.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 18.5 64.2 79.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 17.5 64.2 79.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 19.5 64.2 78.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 22 64 78 ars_nouveau:source_jar[fill=5]{source:5000}
setblock 24 64 78 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 24 64 78 south minecraft:amethyst_shard
