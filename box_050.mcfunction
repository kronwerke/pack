# 050 mekanism_ores/tripling
#area 75 97 95 122
fill 75 64 97 95 91 122 minecraft:air
fill 75 60 97 95 62 122 minecraft:stone
fill 75 63 97 95 63 122 minecraft:light_gray_concrete
fill 79 64 103 95 79 103 minecraft:light_gray_concrete
fill 79 64 103 79 79 116 minecraft:light_gray_concrete
setblock 80 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "050"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 81 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 82 64 115 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 90 64 103 90 79 116 minecraft:light_gray_concrete
setblock 81 64 109 minecraft:chest[facing=south]{Items:[]}
setblock 82 64 109 mekanism:purification_chamber[facing=south,active=false]
setblock 83 64 109 mekanism:crusher[facing=south,active=false]
setblock 84 64 109 mekanism:enrichment_chamber[facing=south,active=false]
setblock 85 64 109 mekanism:energized_smelter[facing=south,active=false]
setblock 86 64 109 minecraft:chest[facing=south]{Items:[]}
setblock 82 64 108 mekanism:basic_pressurized_tube
setblock 82 64 107 mekanism:electrolytic_separator[facing=south]
setblock 83 64 107 mekanism:basic_mechanical_pipe
setblock 84 63 107 minecraft:water
setblock 84 64 107 mekanism:electric_pump[facing=south]
fill 83 64 108 85 64 108 mekanism:basic_universal_cable
setblock 86 64 108 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
