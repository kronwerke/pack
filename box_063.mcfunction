# 063 ars_nouveau/fill_jar
#area 11 124 32 149
fill 11 64 124 32 91 149 minecraft:air
fill 11 60 124 32 62 149 minecraft:stone
fill 11 63 124 32 63 149 minecraft:light_gray_concrete
fill 15 64 130 32 79 130 minecraft:light_gray_concrete
fill 15 64 130 15 79 143 minecraft:light_gray_concrete
setblock 16 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "063"}','{"text": "ars_nouveau"}','{"text": "fill_jar"}','{"text": ""}']}}
setblock 17 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "volcanic"}','{"text": "sourcelink, jar"}','{"text": "and chamber"}','{"text": "within range,"}']}}
setblock 18 64 142 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "logs on the"}','{"text": "ground"}','{"text": ""}','{"text": ""}']}}
fill 27 64 130 27 79 143 minecraft:light_gray_concrete
setblock 18 64 135 ars_nouveau:volcanic_sourcelink
summon item 19.5 64.2 136.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 18.5 64.2 136.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 17.5 64.2 136.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
summon item 19.5 64.2 135.5 {Item:{id:"minecraft:oak_log",count:64},PickupDelay:32767,Age:-32768,Tags:["kw_shot"]}
setblock 22 64 135 ars_nouveau:source_jar[fill=5]{source:5000}
setblock 24 64 135 ars_nouveau:imbuement_chamber[facing=up]
kw testworld use 24 64 135 south minecraft:amethyst_shard
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
