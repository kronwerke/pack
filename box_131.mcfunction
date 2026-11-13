# 131 flux_networks/setup_mek, setup_reactor
#area 89 277 119 302
fill 89 64 277 119 91 302 minecraft:air
fill 89 60 277 119 62 302 minecraft:stone
fill 89 63 277 119 63 302 minecraft:light_gray_concrete
fill 93 64 283 119 79 283 minecraft:light_gray_concrete
fill 93 64 283 93 79 296 minecraft:light_gray_concrete
setblock 94 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 95 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 96 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
fill 104 64 283 104 79 296 minecraft:light_gray_concrete
setblock 97 64 288 mekanism:enrichment_chamber[facing=south]
setblock 98 64 288 mekanism:crusher[facing=south]
setblock 99 64 288 mekanism:energized_smelter[facing=south]
setblock 100 64 288 mekanism:metallurgic_infuser[facing=south]
setblock 97 65 288 fluxnetworks:flux_point
setblock 98 65 288 fluxnetworks:flux_point
setblock 99 65 288 fluxnetworks:flux_point
setblock 100 65 288 fluxnetworks:flux_point
setblock 105 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "131.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 106 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
fill 114 64 283 114 79 296 minecraft:light_gray_concrete
setblock 109 64 288 powah:reactor_starter[core=true]
setblock 109 68 288 fluxnetworks:flux_plug
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
