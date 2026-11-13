# 145 flux_networks/setup_mek, setup_reactor
#area 89 313 119 338
fill 89 64 313 119 91 338 minecraft:air
fill 89 60 313 119 62 338 minecraft:stone
fill 89 63 313 119 63 338 minecraft:light_gray_concrete
fill 93 64 319 119 79 319 minecraft:light_gray_concrete
fill 93 64 319 93 79 332 minecraft:light_gray_concrete
setblock 94 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 95 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 96 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
fill 104 64 319 104 79 332 minecraft:light_gray_concrete
setblock 97 64 324 mekanism:enrichment_chamber[facing=south]
setblock 98 64 324 mekanism:crusher[facing=south]
setblock 99 64 324 mekanism:energized_smelter[facing=south]
setblock 100 64 324 mekanism:metallurgic_infuser[facing=south]
setblock 97 65 324 fluxnetworks:flux_point
setblock 98 65 324 fluxnetworks:flux_point
setblock 99 65 324 fluxnetworks:flux_point
setblock 100 65 324 fluxnetworks:flux_point
setblock 105 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "145.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 106 64 331 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
fill 114 64 319 114 79 332 minecraft:light_gray_concrete
setblock 109 64 324 powah:reactor_starter[core=true]
setblock 109 68 324 fluxnetworks:flux_plug
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
