# 126 flux_networks/first_link
#area 73 275 93 300
fill 73 64 275 93 91 300 minecraft:air
fill 73 60 275 93 62 300 minecraft:stone
fill 73 63 275 93 63 300 minecraft:light_gray_concrete
fill 77 64 281 93 79 281 minecraft:light_gray_concrete
fill 77 64 281 77 79 294 minecraft:light_gray_concrete
setblock 78 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "126"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 281 88 79 294 minecraft:light_gray_concrete
setblock 80 64 286 powah:furnator_starter[facing=south]
setblock 80 65 286 fluxnetworks:flux_plug
setblock 85 64 286 mekanism:enrichment_chamber[facing=south]
setblock 85 65 286 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
