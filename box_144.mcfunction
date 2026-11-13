# 144 flux_networks/first_link
#area 73 311 93 336
fill 73 64 311 93 91 336 minecraft:air
fill 73 60 311 93 62 336 minecraft:stone
fill 73 63 311 93 63 336 minecraft:light_gray_concrete
fill 77 64 317 93 79 317 minecraft:light_gray_concrete
fill 77 64 317 77 79 330 minecraft:light_gray_concrete
setblock 78 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 317 88 79 330 minecraft:light_gray_concrete
setblock 80 64 322 powah:furnator_starter[facing=south]
setblock 80 65 322 fluxnetworks:flux_plug
setblock 85 64 322 mekanism:enrichment_chamber[facing=south]
setblock 85 65 322 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
