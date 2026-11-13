# 080 powah/orb, thermo, reactor
#area -4 212 35 237
fill -4 64 212 35 93 237 minecraft:air
fill -4 60 212 35 62 237 minecraft:stone
fill -4 63 212 35 63 237 minecraft:light_gray_concrete
fill 0 64 218 35 81 218 minecraft:light_gray_concrete
fill 0 64 218 0 81 231 minecraft:light_gray_concrete
setblock 1 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 2 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 10 64 218 10 81 231 minecraft:light_gray_concrete
setblock 5 64 223 powah:energizing_orb[facing=down]
setblock 3 64 223 powah:energizing_rod_starter[facing=down]
setblock 7 64 223 powah:energizing_rod_starter[facing=down]
setblock 5 64 221 powah:energizing_rod_starter[facing=down]
setblock 11 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080.2"}','{"text": "powah"}','{"text": "thermo"}','{"text": ""}']}}
setblock 12 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Stell einen"}','{"text": "Thermo"}','{"text": "Generator auf"}','{"text": ""}']}}
fill 20 64 218 20 81 231 minecraft:light_gray_concrete
setblock 15 64 223 minecraft:magma_block
setblock 15 65 223 powah:thermo_generator_starter
setblock 21 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "080.3"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 22 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 30 64 218 30 81 231 minecraft:light_gray_concrete
setblock 25 64 223 powah:reactor_starter[core=true]
