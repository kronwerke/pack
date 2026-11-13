# 089 flux_networks/first_link
#area 73 254 93 279
fill 73 64 254 93 91 279 minecraft:air
fill 73 60 254 93 62 279 minecraft:stone
fill 73 63 254 93 63 279 minecraft:light_gray_concrete
fill 77 64 260 93 79 260 minecraft:light_gray_concrete
fill 77 64 260 77 79 273 minecraft:light_gray_concrete
setblock 78 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "089"}','{"text": "flux_networks"}','{"text": "first_link"}','{"text": ""}']}}
setblock 79 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a generator"}','{"text": "with a plug and"}','{"text": "a machine with"}','{"text": "a point, no"}']}}
setblock 80 64 272 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables"}','{"text": ""}','{"text": ""}','{"text": ""}']}}
fill 88 64 260 88 79 273 minecraft:light_gray_concrete
setblock 80 64 265 powah:furnator_starter[facing=south]
setblock 80 65 265 fluxnetworks:flux_plug
setblock 85 64 265 mekanism:enrichment_chamber[facing=south]
setblock 85 65 265 fluxnetworks:flux_point
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
