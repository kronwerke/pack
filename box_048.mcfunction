# 048 mekanism_ores/tripling
#area 75 95 95 120
fill 75 64 95 95 91 120 minecraft:air
fill 75 60 95 95 62 120 minecraft:stone
fill 75 63 95 95 63 120 minecraft:light_gray_concrete
fill 79 64 101 95 79 101 minecraft:light_gray_concrete
fill 79 64 101 79 79 114 minecraft:light_gray_concrete
setblock 80 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "048"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 81 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 82 64 113 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 90 64 101 90 79 114 minecraft:light_gray_concrete
setblock 81 64 107 minecraft:chest[facing=south]{Items:[]}
setblock 82 64 107 mekanism:purification_chamber[facing=south,active=false]
setblock 83 64 107 mekanism:crusher[facing=south,active=false]
setblock 84 64 107 mekanism:enrichment_chamber[facing=south,active=false]
setblock 85 64 107 mekanism:energized_smelter[facing=south,active=false]
setblock 86 64 107 minecraft:chest[facing=south]{Items:[]}
setblock 82 64 106 mekanism:basic_pressurized_tube
setblock 82 64 105 mekanism:electrolytic_separator[facing=south]
setblock 83 64 105 mekanism:basic_mechanical_pipe
setblock 84 63 105 minecraft:water
setblock 84 64 105 mekanism:electric_pump[facing=south]
fill 83 64 106 85 64 106 mekanism:basic_universal_cable
setblock 86 64 106 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
