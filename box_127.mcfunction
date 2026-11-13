# 127 flux_networks/setup_mek, setup_reactor
#area 89 275 119 300
fill 89 64 275 119 91 300 minecraft:air
fill 89 60 275 119 62 300 minecraft:stone
fill 89 63 275 119 63 300 minecraft:light_gray_concrete
fill 93 64 281 119 79 281 minecraft:light_gray_concrete
fill 93 64 281 93 79 294 minecraft:light_gray_concrete
setblock 94 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.1"}','{"text": "flux_networks"}','{"text": "setup_mek"}','{"text": ""}']}}
setblock 95 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "a factory row"}','{"text": "with points, a"}','{"text": "Powah reactor"}','{"text": "with a plug, a"}']}}
setblock 96 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "machine hall"}','{"text": "without cables"}','{"text": ""}','{"text": ""}']}}
fill 104 64 281 104 79 294 minecraft:light_gray_concrete
setblock 97 64 286 mekanism:enrichment_chamber[facing=south]
setblock 98 64 286 mekanism:crusher[facing=south]
setblock 99 64 286 mekanism:energized_smelter[facing=south]
setblock 100 64 286 mekanism:metallurgic_infuser[facing=south]
setblock 97 65 286 fluxnetworks:flux_point
setblock 98 65 286 fluxnetworks:flux_point
setblock 99 65 286 fluxnetworks:flux_point
setblock 100 65 286 fluxnetworks:flux_point
setblock 105 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "127.2"}','{"text": "flux_networks"}','{"text": "setup_reactor"}','{"text": ""}']}}
setblock 106 64 293 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Reaktorstrom in"}','{"text": "die Ferne"}','{"text": ""}','{"text": ""}']}}
fill 114 64 281 114 79 294 minecraft:light_gray_concrete
setblock 109 64 286 powah:reactor_starter[core=true]
setblock 109 68 286 fluxnetworks:flux_plug
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
