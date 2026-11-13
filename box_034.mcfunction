# 034 mekanism_ores/tripling
#area 60 65 80 90
fill 60 64 65 80 91 90 minecraft:air
fill 60 60 65 80 62 90 minecraft:stone
fill 60 63 65 80 63 90 minecraft:light_gray_concrete
fill 64 64 71 80 79 71 minecraft:light_gray_concrete
fill 64 64 71 64 79 84 minecraft:light_gray_concrete
setblock 65 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "034"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 66 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 67 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 75 64 71 75 79 84 minecraft:light_gray_concrete
setblock 66 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 67 64 77 mekanism:purification_chamber[facing=south,active=false]
setblock 68 64 77 mekanism:crusher[facing=south,active=false]
setblock 69 64 77 mekanism:enrichment_chamber[facing=south,active=false]
setblock 70 64 77 mekanism:energized_smelter[facing=south,active=false]
setblock 71 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 67 64 76 mekanism:basic_pressurized_tube
setblock 67 64 75 mekanism:electrolytic_separator[facing=south]
setblock 68 64 75 mekanism:basic_mechanical_pipe
setblock 69 63 75 minecraft:water
setblock 69 64 75 mekanism:electric_pump[facing=south]
fill 68 64 76 70 64 76 mekanism:basic_universal_cable
setblock 71 64 76 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
