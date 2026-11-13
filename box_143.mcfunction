# 143 flux_networks/first_link
#area 73 307 93 332
fill 73 64 307 93 91 332 minecraft:air
fill 73 60 307 93 62 332 minecraft:stone
fill 73 63 307 93 63 332 minecraft:light_gray_concrete
fill 77 64 313 93 79 313 minecraft:light_gray_concrete
fill 77 64 313 77 79 326 minecraft:light_gray_concrete
setblock 78 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "143"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 313 88 79 326 minecraft:light_gray_concrete
setblock 80 64 318 powah:furnator_starter[facing=south]
setblock 80 65 318 fluxnetworks:flux_plug
setblock 85 64 318 mekanism:enrichment_chamber[facing=south]
setblock 85 65 318 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
