# 132 ae2/channels
#area -4 286 17 311
fill -4 64 286 17 91 311 minecraft:air
fill -4 60 286 17 62 311 minecraft:stone
fill -4 63 286 17 63 311 minecraft:light_gray_concrete
fill 0 64 292 17 79 292 minecraft:light_gray_concrete
fill 0 64 292 0 79 305 minecraft:light_gray_concrete
setblock 1 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "132"}','{"text": "ae2"}','{"text": "channels"}','{"text": ""}']}}
setblock 2 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "controller with"}','{"text": "dense cables"}','{"text": "branching into"}','{"text": "normal smart"}']}}
setblock 3 64 304 minecraft:oak_sign[rotation=0]{front_text:{messages:['{"text": "cables, channel"}','{"text": "stripes visible"}','{"text": ""}','{"text": ""}']}}
fill 12 64 292 12 79 305 minecraft:light_gray_concrete
setblock 3 63 297 ae2:creative_energy_cell
setblock 3 64 297 ae2:controller
kw testworld use 3 64 297 east ae2:fluix_covered_dense_cable
kw testworld use 3 64 297 east ae2:fluix_covered_dense_cable
kw testworld use 4 64 297 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 297 east ae2:fluix_covered_dense_cable
kw testworld use 6 64 297 east ae2:fluix_covered_dense_cable
kw testworld use 7 64 297 east ae2:fluix_covered_dense_cable
kw testworld use 5 64 297 south ae2:fluix_smart_cable
kw testworld use 5 64 298 south ae2:fluix_smart_cable
setblock 5 64 300 ae2:drive[facing=south,spin=0]
kw testworld use 5 64 297 north ae2:fluix_smart_cable
setblock 5 64 295 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 297 south ae2:fluix_smart_cable
kw testworld use 8 64 298 south ae2:fluix_smart_cable
setblock 8 64 300 ae2:drive[facing=south,spin=0]
kw testworld use 8 64 297 north ae2:fluix_smart_cable
setblock 8 64 295 ae2:drive[facing=south,spin=0]
execute as @e[type=minecraft:item,tag=!kw_shot] run kill @s
