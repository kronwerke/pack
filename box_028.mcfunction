# 028 mekanism_ores/tripling
#area 42 65 62 90
fill 42 64 65 62 91 90 minecraft:air
fill 42 60 65 62 62 90 minecraft:stone
fill 42 63 65 62 63 90 minecraft:light_gray_concrete
fill 46 64 71 62 79 71 minecraft:light_gray_concrete
fill 46 64 71 46 79 84 minecraft:light_gray_concrete
setblock 47 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "028"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 48 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 49 64 83 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 57 64 71 57 79 84 minecraft:light_gray_concrete
setblock 48 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 77 mekanism:purification_chamber[facing=south,active=false]
setblock 50 64 77 mekanism:crusher[facing=south,active=false]
setblock 51 64 77 mekanism:enrichment_chamber[facing=south,active=false]
setblock 52 64 77 mekanism:energized_smelter[facing=south,active=false]
setblock 53 64 77 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 76 mekanism:basic_pressurized_tube
setblock 49 64 75 mekanism:electrolytic_separator[facing=south]
setblock 50 64 75 mekanism:basic_mechanical_pipe
setblock 51 63 75 minecraft:water
setblock 51 64 75 mekanism:electric_pump[facing=south]
fill 50 64 76 52 64 76 mekanism:basic_universal_cable
setblock 53 64 76 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
