# 144 flux_networks/setup_mek, setup_reactor
#area 89 307 119 332
fill 89 64 307 119 91 332 minecraft:air
fill 89 60 307 119 62 332 minecraft:stone
fill 89 63 307 119 63 332 minecraft:light_gray_concrete
fill 93 64 313 119 79 313 minecraft:light_gray_concrete
fill 93 64 313 93 79 326 minecraft:light_gray_concrete
setblock 94 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 95 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 96 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
fill 104 64 313 104 79 326 minecraft:light_gray_concrete
setblock 97 64 318 mekanism:enrichment_chamber[facing=south]
setblock 98 64 318 mekanism:crusher[facing=south]
setblock 99 64 318 mekanism:energized_smelter[facing=south]
setblock 100 64 318 mekanism:metallurgic_infuser[facing=south]
setblock 97 65 318 fluxnetworks:flux_point
setblock 98 65 318 fluxnetworks:flux_point
setblock 99 65 318 fluxnetworks:flux_point
setblock 100 65 318 fluxnetworks:flux_point
setblock 105 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "144.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 106 64 325 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
fill 114 64 313 114 79 326 minecraft:light_gray_concrete
setblock 109 64 318 powah:reactor_starter[core=true]
setblock 109 68 318 fluxnetworks:flux_plug
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
