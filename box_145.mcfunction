# 145 flux_networks/setup_mek, setup_reactor
#area 89 311 119 336
fill 89 64 311 119 91 336 minecraft:air
fill 89 60 311 119 62 336 minecraft:stone
fill 89 63 311 119 63 336 minecraft:light_gray_concrete
fill 93 64 317 119 79 317 minecraft:light_gray_concrete
fill 93 64 317 93 79 330 minecraft:light_gray_concrete
setblock 94 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 95 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 96 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
fill 104 64 317 104 79 330 minecraft:light_gray_concrete
setblock 97 64 322 mekanism:enrichment_chamber[facing=south]
setblock 98 64 322 mekanism:crusher[facing=south]
setblock 99 64 322 mekanism:energized_smelter[facing=south]
setblock 100 64 322 mekanism:metallurgic_infuser[facing=south]
setblock 97 65 322 fluxnetworks:flux_point
setblock 98 65 322 fluxnetworks:flux_point
setblock 99 65 322 fluxnetworks:flux_point
setblock 100 65 322 fluxnetworks:flux_point
setblock 105 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 106 64 329 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
fill 114 64 317 114 79 330 minecraft:light_gray_concrete
setblock 109 64 322 powah:reactor_starter[core=true]
setblock 109 68 322 fluxnetworks:flux_plug
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
