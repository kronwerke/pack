# 130 powah/orb, furnator, thermo, reactor, ender_cell, transmitter, power_plant
#area 84 265 165 290
fill 84 64 265 125 93 290 minecraft:air
fill 126 64 265 165 93 290 minecraft:air
fill 84 60 265 165 62 290 minecraft:stone
fill 84 63 265 165 63 290 minecraft:light_gray_concrete
fill 88 64 271 165 81 271 minecraft:light_gray_concrete
fill 88 64 271 88 81 284 minecraft:light_gray_concrete
setblock 89 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 90 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 98 64 271 98 81 284 minecraft:light_gray_concrete
setblock 93 64 276 powah:energizing_orb[facing=down]
setblock 91 64 276 powah:energizing_rod_starter[facing=down]
setblock 95 64 276 powah:energizing_rod_starter[facing=down]
setblock 93 64 274 powah:energizing_rod_starter[facing=down]
setblock 99 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.2"}','{"text": "powah"}','{"text": "furnator"}','{"text": ""}']}}
setblock 100 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Furnator"}','{"text": ""}','{"text": ""}']}}
fill 108 64 271 108 81 284 minecraft:light_gray_concrete
setblock 102 64 276 powah:furnator_starter[facing=south]
setblock 103 64 276 powah:energy_cell_starter
setblock 104 64 276 minecraft:trapped_chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:1},{Slot:1b,id:"minecraft:coal",count:1},{Slot:2b,id:"minecraft:coal",count:1}]}
setblock 109 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.3"}','{"text": "powah"}','{"text": "thermo"}','{"text": ""}']}}
setblock 110 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Thermo"}','{"text": "Generator auf"}','{"text": ""}']}}
fill 118 64 271 118 81 284 minecraft:light_gray_concrete
setblock 113 64 276 minecraft:magma_block
setblock 113 65 276 powah:thermo_generator_starter
setblock 119 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.4"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 120 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 128 64 271 128 81 284 minecraft:light_gray_concrete
setblock 123 64 276 powah:reactor_starter[core=true]
setblock 129 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.5"}','{"text": "powah"}','{"text": "ender_cell"}','{"text": ""}']}}
setblock 130 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Teil Strom ohne"}','{"text": "Kabel"}','{"text": ""}','{"text": ""}']}}
fill 140 64 271 140 81 284 minecraft:light_gray_concrete
setblock 131 64 276 powah:furnator_starter[facing=south]
setblock 132 64 276 powah:ender_cell_starter
setblock 136 64 276 powah:ender_cell_starter
setblock 137 64 276 minecraft:redstone_lamp[lit=true]
setblock 141 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.6"}','{"text": "powah"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 142 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lad dein"}','{"text": "Werkzeug"}','{"text": "überall"}','{"text": ""}']}}
fill 150 64 271 150 81 284 minecraft:light_gray_concrete
setblock 145 64 276 powah:energy_cell_starter
setblock 145 65 276 powah:player_transmitter_starter[top=false]
setblock 145 66 276 powah:player_transmitter_starter[top=true]
setblock 151 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "130.7"}','{"text": "powah"}','{"text": "power_plant"}','{"text": ""}']}}
setblock 152 64 283 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Blazing-Kraftwerk"}','{"text": ""}','{"text": ""}']}}
fill 160 64 271 160 81 284 minecraft:light_gray_concrete
setblock 154 64 276 powah:furnator_blazing[facing=south]
setblock 155 64 276 powah:energy_cell_blazing
setblock 156 64 276 powah:furnator_blazing[facing=south]
setblock 155 65 276 powah:furnator_blazing[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
