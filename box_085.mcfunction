# 085 flux_networks/first_link
#area 47 250 67 275
fill 47 64 250 67 91 275 minecraft:air
fill 47 60 250 67 62 275 minecraft:stone
fill 47 63 250 67 63 275 minecraft:light_gray_concrete
fill 51 64 256 67 79 256 minecraft:light_gray_concrete
fill 51 64 256 51 79 269 minecraft:light_gray_concrete
setblock 52 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "085"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 53 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 54 64 268 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 62 64 256 62 79 269 minecraft:light_gray_concrete
setblock 54 64 261 powah:furnator_starter[facing=south]
setblock 54 65 261 fluxnetworks:flux_plug
setblock 59 64 261 mekanism:enrichment_chamber[facing=south]
setblock 59 65 261 fluxnetworks:flux_point
