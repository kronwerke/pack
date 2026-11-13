# 154 powah/orb, furnator, thermo, reactor, ender_cell, transmitter, power_plant
#area 134 277 215 302
fill 134 64 277 175 93 302 minecraft:air
fill 176 64 277 215 93 302 minecraft:air
fill 134 60 277 215 62 302 minecraft:stone
fill 134 63 277 215 63 302 minecraft:light_gray_concrete
fill 138 64 283 215 81 283 minecraft:light_gray_concrete
fill 138 64 283 138 81 296 minecraft:light_gray_concrete
setblock 139 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 140 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 148 64 283 148 81 296 minecraft:light_gray_concrete
setblock 143 64 288 powah:energizing_orb[facing=down]
setblock 141 64 288 powah:energizing_rod_starter[facing=down]
setblock 145 64 288 powah:energizing_rod_starter[facing=down]
setblock 143 64 286 powah:energizing_rod_starter[facing=down]
setblock 149 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.2"}','{"text": "powah"}','{"text": "furnator"}','{"text": ""}']}}
setblock 150 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Furnator"}','{"text": ""}','{"text": ""}']}}
fill 158 64 283 158 81 296 minecraft:light_gray_concrete
setblock 152 64 288 powah:furnator_starter[facing=south]
setblock 153 64 288 powah:energy_cell_starter
setblock 154 64 288 minecraft:trapped_chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:1},{Slot:1b,id:"minecraft:coal",count:1},{Slot:2b,id:"minecraft:coal",count:1}]}
setblock 159 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.3"}','{"text": "powah"}','{"text": "thermo"}','{"text": ""}']}}
setblock 160 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Thermo"}','{"text": "Generator auf"}','{"text": ""}']}}
fill 168 64 283 168 81 296 minecraft:light_gray_concrete
setblock 163 64 288 minecraft:magma_block
setblock 163 65 288 powah:thermo_generator_starter
setblock 169 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.4"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 170 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 178 64 283 178 81 296 minecraft:light_gray_concrete
setblock 173 64 288 powah:reactor_starter[core=true]
setblock 179 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.5"}','{"text": "powah"}','{"text": "ender_cell"}','{"text": ""}']}}
setblock 180 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Teil Strom ohne"}','{"text": "Kabel"}','{"text": ""}','{"text": ""}']}}
fill 190 64 283 190 81 296 minecraft:light_gray_concrete
setblock 181 64 288 powah:furnator_starter[facing=south]
setblock 182 64 288 powah:ender_cell_starter
setblock 186 64 288 powah:ender_cell_starter
setblock 187 64 288 minecraft:redstone_lamp[lit=true]
setblock 191 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.6"}','{"text": "powah"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 192 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lad dein"}','{"text": "Werkzeug"}','{"text": "überall"}','{"text": ""}']}}
fill 200 64 283 200 81 296 minecraft:light_gray_concrete
setblock 195 64 288 powah:energy_cell_starter
setblock 195 65 288 powah:player_transmitter_starter[top=false]
setblock 195 66 288 powah:player_transmitter_starter[top=true]
setblock 201 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "154.7"}','{"text": "powah"}','{"text": "power_plant"}','{"text": ""}']}}
setblock 202 64 295 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Blazing-Kraftwerk"}','{"text": ""}','{"text": ""}']}}
fill 210 64 283 210 81 296 minecraft:light_gray_concrete
setblock 204 64 288 powah:furnator_blazing[facing=south]
setblock 205 64 288 powah:energy_cell_blazing
setblock 206 64 288 powah:furnator_blazing[facing=south]
setblock 205 65 288 powah:furnator_blazing[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
