# 116 powah/orb, furnator, thermo, reactor, ender_cell, transmitter, power_plant
#area 73 233 154 258
fill 73 64 233 114 93 258 minecraft:air
fill 115 64 233 154 93 258 minecraft:air
fill 73 60 233 154 62 258 minecraft:stone
fill 73 63 233 154 63 258 minecraft:light_gray_concrete
fill 77 64 239 154 81 239 minecraft:light_gray_concrete
fill 77 64 239 77 81 252 minecraft:light_gray_concrete
setblock 78 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 79 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 87 64 239 87 81 252 minecraft:light_gray_concrete
setblock 82 64 244 powah:energizing_orb[facing=down]
setblock 80 64 244 powah:energizing_rod_starter[facing=down]
setblock 84 64 244 powah:energizing_rod_starter[facing=down]
setblock 82 64 242 powah:energizing_rod_starter[facing=down]
setblock 88 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.2"}','{"text": "powah"}','{"text": "furnator"}','{"text": ""}']}}
setblock 89 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Furnator"}','{"text": ""}','{"text": ""}']}}
fill 97 64 239 97 81 252 minecraft:light_gray_concrete
setblock 91 64 244 powah:furnator_starter[facing=south]
setblock 92 64 244 powah:energy_cell_starter
setblock 93 64 244 minecraft:trapped_chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:1},{Slot:1b,id:"minecraft:coal",count:1},{Slot:2b,id:"minecraft:coal",count:1}]}
setblock 98 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.3"}','{"text": "powah"}','{"text": "thermo"}','{"text": ""}']}}
setblock 99 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Thermo"}','{"text": "Generator auf"}','{"text": ""}']}}
fill 107 64 239 107 81 252 minecraft:light_gray_concrete
setblock 102 64 244 minecraft:magma_block
setblock 102 65 244 powah:thermo_generator_starter
setblock 108 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.4"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 109 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 117 64 239 117 81 252 minecraft:light_gray_concrete
setblock 112 64 244 powah:reactor_starter[core=true]
setblock 118 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.5"}','{"text": "powah"}','{"text": "ender_cell"}','{"text": ""}']}}
setblock 119 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Teil Strom ohne"}','{"text": "Kabel"}','{"text": ""}','{"text": ""}']}}
fill 129 64 239 129 81 252 minecraft:light_gray_concrete
setblock 120 64 244 powah:furnator_starter[facing=south]
setblock 121 64 244 powah:ender_cell_starter
setblock 125 64 244 powah:ender_cell_starter
setblock 126 64 244 minecraft:redstone_lamp[lit=true]
setblock 130 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.6"}','{"text": "powah"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 131 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lad dein"}','{"text": "Werkzeug"}','{"text": "überall"}','{"text": ""}']}}
fill 139 64 239 139 81 252 minecraft:light_gray_concrete
setblock 134 64 244 powah:energy_cell_starter
setblock 134 65 244 powah:player_transmitter_starter[top=false]
setblock 134 66 244 powah:player_transmitter_starter[top=true]
setblock 140 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "116.7"}','{"text": "powah"}','{"text": "power_plant"}','{"text": ""}']}}
setblock 141 64 251 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Blazing-Kraftwerk"}','{"text": ""}','{"text": ""}']}}
fill 149 64 239 149 81 252 minecraft:light_gray_concrete
setblock 143 64 244 powah:furnator_blazing[facing=south]
setblock 144 64 244 powah:energy_cell_blazing
setblock 145 64 244 powah:furnator_blazing[facing=south]
setblock 144 65 244 powah:furnator_blazing[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
