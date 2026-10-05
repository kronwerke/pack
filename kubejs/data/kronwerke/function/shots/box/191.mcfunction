# 191 ae2_advanced/bridge, spatial, reaction, matrix, mega_4m
fill 124 63 337 177 63 350 minecraft:light_gray_concrete
fill 124 64 337 177 71 337 minecraft:light_gray_concrete
fill 124 64 337 124 71 350 minecraft:light_gray_concrete
setblock 125 64 349 minecraft:air
setblock 125 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "191.1"}','{"text": "ae2_advanced"}','{"text": "bridge"}','{"text": ""}']}}
setblock 126 64 349 minecraft:air
setblock 126 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Verbinde zwei"}','{"text": "Orte mit einer"}','{"text": "Quantenbrücke"}','{"text": ""}']}}
setblock 126 64 341 ae2:quantum_ring
setblock 128 64 341 ae2:quantum_link
setblock 130 64 341 minecraft:polished_andesite
summon item_frame 130 64 342 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"ae2:quantum_entangled_singularity",count:1}}
setblock 135 64 349 minecraft:air
setblock 135 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "191.2"}','{"text": "ae2_advanced"}','{"text": "spatial"}','{"text": ""}']}}
setblock 136 64 349 minecraft:air
setblock 136 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell"}','{"text": "Raumpylone auf"}','{"text": ""}','{"text": ""}']}}
fill 137 64 340 143 64 340 ae2:spatial_pylon
fill 137 64 340 137 70 340 ae2:spatial_pylon
fill 137 70 340 143 70 340 ae2:spatial_pylon
setblock 140 64 344 ae2:spatial_io_port
setblock 147 64 349 minecraft:air
setblock 147 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "191.3"}','{"text": "ae2_advanced"}','{"text": "reaction"}','{"text": ""}']}}
setblock 148 64 349 minecraft:air
setblock 148 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau eine"}','{"text": "Reaktionskammer"}','{"text": ""}','{"text": ""}']}}
setblock 148 64 341 advanced_ae:reaction_chamber
setblock 157 64 349 minecraft:air
setblock 157 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "191.4"}','{"text": "ae2_advanced"}','{"text": "matrix"}','{"text": ""}']}}
setblock 158 64 349 minecraft:air
setblock 158 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Assembler-Matrix:"}','{"text": "Hülle, innen"}','{"text": "Muster und"}','{"text": "Kerne"}']}}
fill 159 64 340 163 68 344 extendedae:assembler_matrix_wall
setblock 167 64 349 minecraft:air
setblock 167 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "191.5"}','{"text": "ae2_advanced"}','{"text": "mega_4m"}','{"text": ""}']}}
setblock 168 64 349 minecraft:air
setblock 168 64 349 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Füll das Lager"}','{"text": "des Sternwerks"}','{"text": ""}','{"text": ""}']}}
setblock 168 64 341 minecraft:polished_andesite
summon item_frame 168 64 342 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"megacells:item_storage_cell_4m",count:1}}
setblock 170 64 341 minecraft:polished_andesite
summon item_frame 170 64 342 {Facing:3b,Fixed:1b,Tags:["kw_shot"],Item:{id:"mekanism:elite_control_circuit",count:1}}
