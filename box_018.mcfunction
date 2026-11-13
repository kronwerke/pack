# 018 mekanism_ores/tripling
#area 27 44 47 69
fill 27 64 44 47 91 69 minecraft:air
fill 27 60 44 47 62 69 minecraft:stone
fill 27 63 44 47 63 69 minecraft:light_gray_concrete
fill 31 64 50 47 79 50 minecraft:light_gray_concrete
fill 31 64 50 31 79 63 minecraft:light_gray_concrete
setblock 32 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "018"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 33 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 34 64 62 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 42 64 50 42 79 63 minecraft:light_gray_concrete
setblock 33 64 56 minecraft:chest[facing=south]{Items:[]}
setblock 34 64 56 mekanism:purification_chamber[facing=south,active=false]
setblock 35 64 56 mekanism:crusher[facing=south,active=false]
setblock 36 64 56 mekanism:enrichment_chamber[facing=south,active=false]
setblock 37 64 56 mekanism:energized_smelter[facing=south,active=false]
setblock 38 64 56 minecraft:chest[facing=south]{Items:[]}
setblock 34 64 55 mekanism:basic_pressurized_tube
setblock 34 64 54 mekanism:electrolytic_separator[facing=south]
setblock 35 64 54 mekanism:basic_mechanical_pipe
setblock 36 63 54 minecraft:water
setblock 36 64 54 mekanism:electric_pump[facing=south]
fill 35 64 55 37 64 55 mekanism:basic_universal_cable
setblock 38 64 55 mekanism:basic_energy_cube[facing=south]
