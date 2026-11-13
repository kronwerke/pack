# 059 ars_nouveau/fill_jar
#area 11 118 32 143
fill 11 64 118 32 91 143 minecraft:air
fill 11 60 118 32 62 143 minecraft:stone
fill 11 63 118 32 63 143 minecraft:light_gray_concrete
fill 15 64 124 32 79 124 minecraft:light_gray_concrete
fill 15 64 124 15 79 137 minecraft:light_gray_concrete
setblock 16 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "059"}','{"text": "ars_nouveau"}','{"text": "fill_jar"}','{"text": ""}']}}
setblock 17 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "volcanic"}','{"text": "sourcelink, jar"}','{"text": "and chamber"}','{"text": "within range,"}']}}
setblock 18 64 136 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "logs on the"}','{"text": "ground"}','{"text": ""}','{"text": ""}']}}
fill 27 64 124 27 79 137 minecraft:light_gray_concrete
setblock 18 64 129 ars_nouveau:volcanic_sourcelink
summon item 19.5 64.2 130.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 18.5 64.2 130.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 17.5 64.2 130.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 19.5 64.2 129.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 22 64 129 ars_nouveau:source_jar[fill=5]{source:5000}
setblock 24 64 129 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 24 64 129 south minecraft:amethyst_shard
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
