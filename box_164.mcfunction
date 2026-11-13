# 164 flux_networks/first_link
#area 73 319 93 344
fill 73 64 319 93 91 344 minecraft:air
fill 73 60 319 93 62 344 minecraft:stone
fill 73 63 319 93 63 344 minecraft:light_gray_concrete
fill 77 64 325 93 79 325 minecraft:light_gray_concrete
fill 77 64 325 77 79 338 minecraft:light_gray_concrete
setblock 78 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "164"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 325 88 79 338 minecraft:light_gray_concrete
setblock 80 64 330 powah:furnator_starter[facing=south]
setblock 80 65 330 fluxnetworks:flux_plug
setblock 85 64 330 mekanism:enrichment_chamber[facing=south]
setblock 85 65 330 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
