# 165 flux_networks/setup_mek, setup_reactor
#area 89 319 119 344
fill 89 64 319 119 91 344 minecraft:air
fill 89 60 319 119 62 344 minecraft:stone
fill 89 63 319 119 63 344 minecraft:light_gray_concrete
fill 93 64 325 119 79 325 minecraft:light_gray_concrete
fill 93 64 325 93 79 338 minecraft:light_gray_concrete
setblock 94 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 95 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 96 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
fill 104 64 325 104 79 338 minecraft:light_gray_concrete
setblock 97 64 330 mekanism:enrichment_chamber[facing=south]
setblock 98 64 330 mekanism:crusher[facing=south]
setblock 99 64 330 mekanism:energized_smelter[facing=south]
setblock 100 64 330 mekanism:metallurgic_infuser[facing=south]
setblock 97 65 330 fluxnetworks:flux_point
setblock 98 65 330 fluxnetworks:flux_point
setblock 99 65 330 fluxnetworks:flux_point
setblock 100 65 330 fluxnetworks:flux_point
setblock 105 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "165.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 106 64 337 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
fill 114 64 325 114 79 338 minecraft:light_gray_concrete
setblock 109 64 330 powah:reactor_starter[core=true]
setblock 109 68 330 fluxnetworks:flux_plug
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
