# 078 ae2/network, controller
#area -4 212 27 237
fill -4 64 212 27 91 237 minecraft:air
fill -4 60 212 27 62 237 minecraft:stone
fill -4 63 212 27 63 237 minecraft:light_gray_concrete
fill 0 64 218 27 79 218 minecraft:light_gray_concrete
fill 0 64 218 0 79 231 minecraft:light_gray_concrete
setblock 1 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078.1"}','{"text": "ae2"}','{"text": "network"}','{"text": ""}']}}
setblock 2 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Schließ dein"}','{"text": "erstes Netz an"}','{"text": ""}','{"text": ""}']}}
fill 11 64 218 11 79 231 minecraft:light_gray_concrete
setblock 3 63 223 ae2:creative_energy_cell
setblock 3 64 223 ae2:energy_acceptor
kw testworld use 3 64 223 east ae2:fluix_glass_cable
kw testworld use 4 64 223 east ae2:fluix_glass_cable
kw testworld use 5 64 223 east ae2:fluix_glass_cable
execute unless block 6 64 223 minecraft:air
setblock 7 64 223 ae2:drive[facing=south,spin=0]
kw testworld use 5 64 223 south ae2:terminal
setblock 12 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "078.2"}','{"text": "ae2"}','{"text": "controller"}','{"text": ""}']}}
setblock 13 64 230 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "Bau einen"}','{"text": "ME-Controller"}','{"text": ""}','{"text": ""}']}}
fill 22 64 218 22 79 231 minecraft:light_gray_concrete
setblock 15 63 223 ae2:creative_energy_cell
fill 15 64 223 15 66 223 ae2:controller
kw testworld use 15 64 223 east ae2:fluix_smart_cable
kw testworld use 16 64 223 east ae2:fluix_smart_cable
kw testworld use 17 64 223 east ae2:fluix_smart_cable
execute unless block 18 64 223 minecraft:air
setblock 19 64 223 ae2:drive[facing=south,spin=0]
setblock 18 65 223 ae2:drive[facing=south,spin=0]
kw testworld use 16 64 223 south ae2:terminal
