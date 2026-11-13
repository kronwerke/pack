# 069 powah/orb, reactor
#area -4 193 25 218
fill -4 64 193 25 93 218 minecraft:air
fill -4 60 193 25 62 218 minecraft:stone
fill -4 63 193 25 63 218 minecraft:light_gray_concrete
fill 0 64 199 25 81 199 minecraft:light_gray_concrete
fill 0 64 199 0 81 212 minecraft:light_gray_concrete
setblock 1 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069.1"}','{"text": "powah"}','{"text": "orb"}','{"text": ""}']}}
setblock 2 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau die"}','{"text": "Energizing Orb"}','{"text": ""}','{"text": ""}']}}
fill 10 64 199 10 81 212 minecraft:light_gray_concrete
setblock 5 64 204 powah:energizing_orb[facing=down]
setblock 3 64 204 powah:energizing_rod_starter[facing=down]
setblock 7 64 204 powah:energizing_rod_starter[facing=down]
setblock 5 64 202 powah:energizing_rod_starter[facing=down]
setblock 11 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "069.2"}','{"text": "powah"}','{"text": "reactor"}','{"text": ""}']}}
setblock 12 64 211 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "Reaktor"}','{"text": ""}','{"text": ""}']}}
fill 20 64 199 20 81 212 minecraft:light_gray_concrete
setblock 15 64 204 powah:reactor_starter[core=true]
