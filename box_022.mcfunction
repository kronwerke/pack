# 022 mekanism_ores/tripling
#area 27 63 47 88
fill 27 64 63 47 91 88 minecraft:air
fill 27 60 63 47 62 88 minecraft:stone
fill 27 63 63 47 63 88 minecraft:light_gray_concrete
fill 31 64 69 47 79 69 minecraft:light_gray_concrete
fill 31 64 69 31 79 82 minecraft:light_gray_concrete
setblock 32 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "022"}','{"text": "mekanism_ores"}','{"text": "tripling"}','{"text": ""}']}}
setblock 33 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "purification"}','{"text": "chamber,"}','{"text": "crusher,"}','{"text": "enrichment"}']}}
setblock 34 64 81 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "chamber,"}','{"text": "smelter with"}','{"text": "separator and"}','{"text": "pump"}']}}
fill 42 64 69 42 79 82 minecraft:light_gray_concrete
setblock 33 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 34 64 75 mekanism:purification_chamber[facing=south,active=false]
setblock 35 64 75 mekanism:crusher[facing=south,active=false]
setblock 36 64 75 mekanism:enrichment_chamber[facing=south,active=false]
setblock 37 64 75 mekanism:energized_smelter[facing=south,active=false]
setblock 38 64 75 minecraft:chest[facing=south]{Items:[]}
setblock 34 64 74 mekanism:basic_pressurized_tube
setblock 34 64 73 mekanism:electrolytic_separator[facing=south]
setblock 35 64 73 mekanism:basic_mechanical_pipe
setblock 36 63 73 minecraft:water
setblock 36 64 73 mekanism:electric_pump[facing=south]
fill 35 64 74 37 64 74 mekanism:basic_universal_cable
setblock 38 64 74 mekanism:basic_energy_cube[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
