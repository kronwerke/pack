# 037 mekanism_ores/tripling
#area 75 65 95 90
fill 75 64 65 95 91 90 minecraft:air
fill 75 60 65 95 62 90 minecraft:stone
fill 75 63 65 95 63 90 minecraft:light_gray_concrete
fill 79 64 71 95 79 71 minecraft:light_gray_concrete
fill 79 64 71 79 79 84 minecraft:light_gray_concrete
setblock 80 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "037"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 81 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 82 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 90 64 71 90 79 84 minecraft:light_gray_concrete
setblock 81 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 82 64 77 mekanism:purification_chamber[facing=south,active=false]
setblock 83 64 77 mekanism:crusher[facing=south,active=false]
setblock 84 64 77 mekanism:enrichment_chamber[facing=south,active=false]
setblock 85 64 77 mekanism:energized_smelter[facing=south,active=false]
setblock 86 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 82 64 76 mekanism:basic_pressurized_tube
setblock 82 64 75 mekanism:electrolytic_separator[facing=south]
setblock 83 64 75 mekanism:basic_mechanical_pipe
setblock 84 63 75 minecraft:water
setblock 84 64 75 mekanism:electric_pump[facing=south]
fill 83 64 76 85 64 76 mekanism:basic_universal_cable
setblock 86 64 76 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
