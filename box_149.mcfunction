# 149 flux_networks/first_link
#area 73 317 93 342
fill 73 64 317 93 91 342 minecraft:air
fill 73 60 317 93 62 342 minecraft:stone
fill 73 63 317 93 63 342 minecraft:light_gray_concrete
fill 77 64 323 93 79 323 minecraft:light_gray_concrete
fill 77 64 323 77 79 336 minecraft:light_gray_concrete
setblock 78 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "149"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 323 88 79 336 minecraft:light_gray_concrete
setblock 80 64 328 powah:furnator_starter[facing=south]
setblock 80 65 328 fluxnetworks:flux_plug
setblock 85 64 328 mekanism:enrichment_chamber[facing=south]
setblock 85 65 328 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
