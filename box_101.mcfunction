# 101 powah/orb, furnator, thermo, reactor, ender_cell, transmitter, power_plant
#area 63 233 144 258
fill 63 64 233 104 93 258 minecraft:air
fill 105 64 233 144 93 258 minecraft:air
fill 63 60 233 144 62 258 minecraft:stone
fill 63 63 233 144 63 258 minecraft:light_gray_concrete
fill 67 64 239 144 81 239 minecraft:light_gray_concrete
fill 67 64 239 67 81 252 minecraft:light_gray_concrete
setblock 68 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 69 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 77 64 239 77 81 252 minecraft:light_gray_concrete
setblock 72 64 244 powah:energizing_orb[facing=down]
setblock 70 64 244 powah:energizing_rod_starter[facing=down]
setblock 74 64 244 powah:energizing_rod_starter[facing=down]
setblock 72 64 242 powah:energizing_rod_starter[facing=down]
setblock 78 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.2"}','{"text": "powah"}','{"text": "furnator"}','{"text": ""}']}}
setblock 79 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Furnator"}','{"text": ""}','{"text": ""}']}}
fill 87 64 239 87 81 252 minecraft:light_gray_concrete
setblock 81 64 244 powah:furnator_starter[facing=south]
setblock 82 64 244 powah:energy_cell_starter
setblock 83 64 244 minecraft:trapped_chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:1},{Slot:1b,id:"minecraft:coal",count:1},{Slot:2b,id:"minecraft:coal",count:1}]}
setblock 88 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.3"}','{"text": "powah"}','{"text": "thermo"}','{"text": ""}']}}
setblock 89 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Thermo"}','{"text": "Generator auf"}','{"text": ""}']}}
fill 97 64 239 97 81 252 minecraft:light_gray_concrete
setblock 92 64 244 minecraft:magma_block
setblock 92 65 244 powah:thermo_generator_starter
setblock 98 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.4"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 99 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 107 64 239 107 81 252 minecraft:light_gray_concrete
setblock 102 64 244 powah:reactor_starter[core=true]
setblock 108 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.5"}','{"text": "powah"}','{"text": "ender_cell"}','{"text": ""}']}}
setblock 109 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Teil Strom ohne"}','{"text": "Kabel"}','{"text": ""}','{"text": ""}']}}
fill 119 64 239 119 81 252 minecraft:light_gray_concrete
setblock 110 64 244 powah:furnator_starter[facing=south]
setblock 111 64 244 powah:ender_cell_starter
setblock 115 64 244 powah:ender_cell_starter
setblock 116 64 244 minecraft:redstone_lamp[lit=true]
setblock 120 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.6"}','{"text": "powah"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 121 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lad dein"}','{"text": "Werkzeug"}','{"text": "überall"}','{"text": ""}']}}
fill 129 64 239 129 81 252 minecraft:light_gray_concrete
setblock 124 64 244 powah:energy_cell_starter
setblock 124 65 244 powah:player_transmitter_starter[top=false]
setblock 124 66 244 powah:player_transmitter_starter[top=true]
setblock 130 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "101.7"}','{"text": "powah"}','{"text": "power_plant"}','{"text": ""}']}}
setblock 131 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Blazing-Kraftwerk"}','{"text": ""}','{"text": ""}']}}
fill 139 64 239 139 81 252 minecraft:light_gray_concrete
setblock 133 64 244 powah:furnator_blazing[facing=south]
setblock 134 64 244 powah:energy_cell_blazing
setblock 135 64 244 powah:furnator_blazing[facing=south]
setblock 134 65 244 powah:furnator_blazing[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
