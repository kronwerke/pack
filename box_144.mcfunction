# 144 flux_networks/first_link
#area 73 313 93 338
fill 73 64 313 93 91 338 minecraft:air
fill 73 60 313 93 62 338 minecraft:stone
fill 73 63 313 93 63 338 minecraft:light_gray_concrete
fill 77 64 319 93 79 319 minecraft:light_gray_concrete
fill 77 64 319 77 79 332 minecraft:light_gray_concrete
setblock 78 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 319 88 79 332 minecraft:light_gray_concrete
setblock 80 64 324 powah:furnator_starter[facing=south]
setblock 80 65 324 fluxnetworks:flux_plug
setblock 85 64 324 mekanism:enrichment_chamber[facing=south]
setblock 85 65 324 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
