# 099 flux_networks/first_link
#area 73 273 93 298
fill 73 64 273 93 91 298 minecraft:air
fill 73 60 273 93 62 298 minecraft:stone
fill 73 63 273 93 63 298 minecraft:light_gray_concrete
fill 77 64 279 93 79 279 minecraft:light_gray_concrete
fill 77 64 279 77 79 292 minecraft:light_gray_concrete
setblock 78 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "099"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 291 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 279 88 79 292 minecraft:light_gray_concrete
setblock 80 64 284 powah:furnator_starter[facing=south]
setblock 80 65 284 fluxnetworks:flux_plug
setblock 85 64 284 mekanism:enrichment_chamber[facing=south]
setblock 85 65 284 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
