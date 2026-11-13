# 131 flux_networks/first_link
#area 73 277 93 302
fill 73 64 277 93 91 302 minecraft:air
fill 73 60 277 93 62 302 minecraft:stone
fill 73 63 277 93 63 302 minecraft:light_gray_concrete
fill 77 64 283 93 79 283 minecraft:light_gray_concrete
fill 77 64 283 77 79 296 minecraft:light_gray_concrete
setblock 78 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 283 88 79 296 minecraft:light_gray_concrete
setblock 80 64 288 powah:furnator_starter[facing=south]
setblock 80 65 288 fluxnetworks:flux_plug
setblock 85 64 288 mekanism:enrichment_chamber[facing=south]
setblock 85 65 288 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
