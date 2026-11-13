# 090 powah/orb, furnator, thermo, reactor, ender_cell, transmitter, power_plant
#area 63 231 144 256
fill 63 64 231 104 93 256 minecraft:air
fill 105 64 231 144 93 256 minecraft:air
fill 63 60 231 144 62 256 minecraft:stone
fill 63 63 231 144 63 256 minecraft:light_gray_concrete
fill 67 64 237 144 81 237 minecraft:light_gray_concrete
fill 67 64 237 67 81 250 minecraft:light_gray_concrete
setblock 68 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 69 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 77 64 237 77 81 250 minecraft:light_gray_concrete
setblock 72 64 242 powah:energizing_orb[facing=down]
setblock 70 64 242 powah:energizing_rod_starter[facing=down]
setblock 74 64 242 powah:energizing_rod_starter[facing=down]
setblock 72 64 240 powah:energizing_rod_starter[facing=down]
setblock 78 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.2"}','{"text": "powah"}','{"text": "furnator"}','{"text": ""}']}}
setblock 79 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Furnator"}','{"text": ""}','{"text": ""}']}}
fill 87 64 237 87 81 250 minecraft:light_gray_concrete
setblock 81 64 242 powah:furnator_starter[facing=south]
setblock 82 64 242 powah:energy_cell_starter
setblock 83 64 242 minecraft:trapped_chest[facing=south]{Items:[{Slot:0b,id:"minecraft:coal",count:1},{Slot:1b,id:"minecraft:coal",count:1},{Slot:2b,id:"minecraft:coal",count:1}]}
setblock 88 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.3"}','{"text": "powah"}','{"text": "thermo"}','{"text": ""}']}}
setblock 89 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Thermo"}','{"text": "Generator auf"}','{"text": ""}']}}
fill 97 64 237 97 81 250 minecraft:light_gray_concrete
setblock 92 64 242 minecraft:magma_block
setblock 92 65 242 powah:thermo_generator_starter
setblock 98 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.4"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 99 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 107 64 237 107 81 250 minecraft:light_gray_concrete
setblock 102 64 242 powah:reactor_starter[core=true]
setblock 108 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.5"}','{"text": "powah"}','{"text": "ender_cell"}','{"text": ""}']}}
setblock 109 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Teil Strom ohne"}','{"text": "Kabel"}','{"text": ""}','{"text": ""}']}}
fill 119 64 237 119 81 250 minecraft:light_gray_concrete
setblock 110 64 242 powah:furnator_starter[facing=south]
setblock 111 64 242 powah:ender_cell_starter
setblock 115 64 242 powah:ender_cell_starter
setblock 116 64 242 minecraft:redstone_lamp[lit=true]
setblock 120 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.6"}','{"text": "powah"}','{"text": "transmitter"}','{"text": ""}']}}
setblock 121 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Lad dein"}','{"text": "Werkzeug"}','{"text": "überall"}','{"text": ""}']}}
fill 129 64 237 129 81 250 minecraft:light_gray_concrete
setblock 124 64 242 powah:energy_cell_starter
setblock 124 65 242 powah:player_transmitter_starter[top=false]
setblock 124 66 242 powah:player_transmitter_starter[top=true]
setblock 130 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "090.7"}','{"text": "powah"}','{"text": "power_plant"}','{"text": ""}']}}
setblock 131 64 249 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau ein"}','{"text": "Blazing-Kraftwerk"}','{"text": ""}','{"text": ""}']}}
fill 139 64 237 139 81 250 minecraft:light_gray_concrete
setblock 133 64 242 powah:furnator_blazing[facing=south]
setblock 134 64 242 powah:energy_cell_blazing
setblock 135 64 242 powah:furnator_blazing[facing=south]
setblock 134 65 242 powah:furnator_blazing[facing=south]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
