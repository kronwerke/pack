# 150 flux_networks/setup_mek, setup_reactor
#area 89 317 119 342
fill 89 64 317 119 91 342 minecraft:air
fill 89 60 317 119 62 342 minecraft:stone
fill 89 63 317 119 63 342 minecraft:light_gray_concrete
fill 93 64 323 119 79 323 minecraft:light_gray_concrete
fill 93 64 323 93 79 336 minecraft:light_gray_concrete
setblock 94 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 95 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 96 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
fill 104 64 323 104 79 336 minecraft:light_gray_concrete
setblock 97 64 328 mekanism:enrichment_chamber[facing=south]
setblock 98 64 328 mekanism:crusher[facing=south]
setblock 99 64 328 mekanism:energized_smelter[facing=south]
setblock 100 64 328 mekanism:metallurgic_infuser[facing=south]
setblock 97 65 328 fluxnetworks:flux_point
setblock 98 65 328 fluxnetworks:flux_point
setblock 99 65 328 fluxnetworks:flux_point
setblock 100 65 328 fluxnetworks:flux_point
setblock 105 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "150.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 106 64 335 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
fill 114 64 323 114 79 336 minecraft:light_gray_concrete
setblock 109 64 328 powah:reactor_starter[core=true]
setblock 109 68 328 fluxnetworks:flux_plug
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
