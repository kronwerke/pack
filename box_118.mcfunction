# 118 powah/orb, furnator, thermo, reactor, ender_cell, transmitter, power_plant
#area 84 233 165 258
fill 84 64 233 125 93 258 minecraft:air
fill 126 64 233 165 93 258 minecraft:air
fill 84 60 233 165 62 258 minecraft:stone
fill 84 63 233 165 63 258 minecraft:light_gray_concrete
fill 88 64 239 165 81 239 minecraft:light_gray_concrete
fill 88 64 239 88 81 252 minecraft:light_gray_concrete
setblock 89 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 90 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 98 64 239 98 81 252 minecraft:light_gray_concrete
setblock 93 64 244 powah:energizing_orb[facing=down]
setblock 91 64 244 powah:energizing_rod_starter[facing=down]
setblock 95 64 244 powah:energizing_rod_starter[facing=down]
setblock 93 64 242 powah:energizing_rod_starter[facing=down]
setblock 99 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.2"}','{"text": "powah"}','{"text": "furnator"}','{"text": ""}']}}
setblock 100 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Furnator"}','{"text": ""}','{"text": ""}']}}
fill 108 64 239 108 81 252 minecraft:light_gray_concrete
setblock 102 64 244 powah:furnator_starter[facing=south]
setblock 103 64 244 powah:energy_cell_starter
setblock 104 64 244 minecraft:trapped_chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:1},{Slot:1b,id:"minecraft:coal",count:1},{Slot:2b,id:"minecraft:coal",count:1}]}
setblock 109 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.3"}','{"text": "powah"}','{"text": "thermo"}','{"text": ""}']}}
setblock 110 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Thermo"}','{"text": "Generator auf"}','{"text": ""}']}}
fill 118 64 239 118 81 252 minecraft:light_gray_concrete
setblock 113 64 244 minecraft:magma_block
setblock 113 65 244 powah:thermo_generator_starter
setblock 119 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.4"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 120 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 128 64 239 128 81 252 minecraft:light_gray_concrete
setblock 123 64 244 powah:reactor_starter[core=true]
setblock 129 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.5"}','{"text": "powah"}','{"text": "ender_cell"}','{"text": ""}']}}
setblock 130 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Teil Strom ohne"}','{"text": "Kabel"}','{"text": ""}','{"text": ""}']}}
fill 140 64 239 140 81 252 minecraft:light_gray_concrete
setblock 131 64 244 powah:furnator_starter[facing=south]
setblock 132 64 244 powah:ender_cell_starter
setblock 136 64 244 powah:ender_cell_starter
setblock 137 64 244 minecraft:redstone_lamp[lit=true]
setblock 141 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.6"}','{"text": "powah"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 142 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lad dein"}','{"text": "Werkzeug"}','{"text": "überall"}','{"text": ""}']}}
fill 150 64 239 150 81 252 minecraft:light_gray_concrete
setblock 145 64 244 powah:energy_cell_starter
setblock 145 65 244 powah:player_transmitter_starter[top=false]
setblock 145 66 244 powah:player_transmitter_starter[top=true]
setblock 151 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "118.7"}','{"text": "powah"}','{"text": "power_plant"}','{"text": ""}']}}
setblock 152 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Blazing-Kraftwerk"}','{"text": ""}','{"text": ""}']}}
fill 160 64 239 160 81 252 minecraft:light_gray_concrete
setblock 154 64 244 powah:furnator_blazing[facing=south]
setblock 155 64 244 powah:energy_cell_blazing
setblock 156 64 244 powah:furnator_blazing[facing=south]
setblock 155 65 244 powah:furnator_blazing[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
