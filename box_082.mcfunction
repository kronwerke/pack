# 082 flux_networks/first_link
#area 47 231 67 256
fill 47 64 231 67 91 256 minecraft:air
fill 47 60 231 67 62 256 minecraft:stone
fill 47 63 231 67 63 256 minecraft:light_gray_concrete
fill 51 64 237 67 79 237 minecraft:light_gray_concrete
fill 51 64 237 51 79 250 minecraft:light_gray_concrete
setblock 52 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "082"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 53 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 54 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 62 64 237 62 79 250 minecraft:light_gray_concrete
setblock 54 64 242 powah:furnator_starter[facing=south]
setblock 54 65 242 fluxnetworks:flux_plug
setblock 59 64 242 mekanism:enrichment_chamber[facing=south]
setblock 59 65 242 fluxnetworks:flux_point
