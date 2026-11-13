# 025 mekanism_ores/tripling
#area 42 63 62 88
fill 42 64 63 62 91 88 minecraft:air
fill 42 60 63 62 62 88 minecraft:stone
fill 42 63 63 62 63 88 minecraft:light_gray_concrete
fill 46 64 69 62 79 69 minecraft:light_gray_concrete
fill 46 64 69 46 79 82 minecraft:light_gray_concrete
setblock 47 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "025"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 48 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 49 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 57 64 69 57 79 82 minecraft:light_gray_concrete
setblock 48 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 75 mekanism:purification_chamber[facing=south,active=false]
setblock 50 64 75 mekanism:crusher[facing=south,active=false]
setblock 51 64 75 mekanism:enrichment_chamber[facing=south,active=false]
setblock 52 64 75 mekanism:energized_smelter[facing=south,active=false]
setblock 53 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 49 64 74 mekanism:basic_pressurized_tube
setblock 49 64 73 mekanism:electrolytic_separator[facing=south]
setblock 50 64 73 mekanism:basic_mechanical_pipe
setblock 51 63 73 minecraft:water
setblock 51 64 73 mekanism:electric_pump[facing=south]
fill 50 64 74 52 64 74 mekanism:basic_universal_cable
setblock 53 64 74 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
