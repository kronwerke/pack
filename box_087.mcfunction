# 087 flux_networks/first_link
#area 80 250 100 275
fill 80 64 250 100 91 275 minecraft:air
fill 80 60 250 100 62 275 minecraft:stone
fill 80 63 250 100 63 275 minecraft:light_gray_concrete
fill 84 64 256 100 79 256 minecraft:light_gray_concrete
fill 84 64 256 84 79 269 minecraft:light_gray_concrete
setblock 85 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "087"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 86 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 87 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 95 64 256 95 79 269 minecraft:light_gray_concrete
setblock 87 64 261 powah:furnator_starter[facing=south]
setblock 87 65 261 fluxnetworks:flux_plug
setblock 92 64 261 mekanism:enrichment_chamber[facing=south]
setblock 92 65 261 fluxnetworks:flux_point
